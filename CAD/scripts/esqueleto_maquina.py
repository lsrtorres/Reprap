"""Esqueleto dimensional da MÁQUINA COMPLETA: gantry CoreXY (importado de
esqueleto_gantry) + colunas, anel da base, deck da eletrônica e eixo Z
estilo Voron Trident (3 trilhos MGN9 + 3 fusos TR8x8 400).

Verifica: cobertura dos fusos e trilhos no curso Z de 200 mm, folgas da
mesa, altura da baia da eletrônica. Imprime o stack-up e a lista de corte.

Uso (de CAD/scripts/):
    ..\\..\\.venv\\Scripts\\python.exe esqueleto_maquina.py

Saída: CAD/11-esqueleto-maquina_v1.step
"""
import os

import cadquery as cq

import parametros as P
import componentes as C
from esqueleto_gantry import montar as montar_gantry, verificar_cursos, ROT_X, ROT_Y, ROT_Z

AQUI = os.path.dirname(os.path.abspath(__file__))
DIR_CAD = os.path.normpath(os.path.join(AQUI, ".."))


# ---------------------------------------------------------------- verificação
def verificar_z():
    print("=== Verificação do eixo Z (curso requerido: %.0f mm) ===" % P.Z_TRAVEL)
    braco_top_min = P.BRACO_TOP_HOME - P.Z_TRAVEL            # -267
    fuso_topo = P.FUSO_Z0 + P.FUSO_L                         # -55
    sobra_fuso_topo = fuso_topo - P.BRACO_TOP_HOME           # acima da castanha em home
    engate_min = braco_top_min - P.CASTANHA_H                # fundo da castanha embaixo
    sobra_fuso_base = engate_min - (P.FUSO_Z0 + 5.0)

    # carrinho MGN no braço: centro acompanha o braço
    bloco_c_home = P.BRACO_TOP_HOME - P.BRACO_T / 2          # -71
    bloco_c_min = bloco_c_home - P.Z_TRAVEL                  # -271
    lim_sup = P.RAIL_Z_TOPO - P.MGN9_BLOCO_L / 2
    lim_inf = P.RAIL_Z_BASE + P.MGN9_BLOCO_L / 2

    print(f"Mesa (vidro) em home : z = {P.BICO_TIP_Z:+.1f} (ponta do bico)")
    print(f"Braços da mesa       : topo {P.BRACO_TOP_HOME:+.1f} (home) .. {braco_top_min:+.1f} (baixo)")
    print(f"Fuso TR8x8 400       : z {P.FUSO_Z0:+.1f} .. {fuso_topo:+.1f} | sobra topo {sobra_fuso_topo:+.1f}, base {sobra_fuso_base:+.1f}")
    print(f"Carrinho Z (centro)  : {bloco_c_min:+.1f} .. {bloco_c_home:+.1f} | trilho permite {lim_inf:+.1f} .. {lim_sup:+.1f}")
    print(f"Baia da eletrônica   : {P.BAIA_ALTURA:.0f} mm internos (deck {P.DECK_Z[0]:+.0f} / base {P.BASE_Z[1]:+.0f})")
    assert sobra_fuso_topo >= 5, "Fuso termina antes da castanha em home!"
    assert sobra_fuso_base >= 5, "Castanha bate no mancal no fim do curso!"
    assert bloco_c_home <= lim_sup + 1e-6, "Carrinho Z sai do trilho no topo!"
    assert bloco_c_min >= lim_inf - 1e-6, "Carrinho Z sai do trilho embaixo!"
    assert P.BAIA_ALTURA >= 90, "Baia da eletrônica baixa demais p/ as fontes!"
    # folgas da mesa em planta
    assert P.MESA_LADO / 2 + abs(P.MESA_CENTRO_Y) < P.RAIL_Y_X - P.PERFIL / 2, \
        "Mesa colide com a coluna traseira!"
    print("OK: Z de 200 mm fecha com fuso de 400 e trilho de 300.\n")

    print("=== Lista de corte (perfis 20x20) ===")
    print(f"Colunas: 4x {P.COLUNA_L:.0f} (estoque, inteiras) + 1x {P.COL_TRAS_L:.0f} comprada (coluna Z traseira)")
    print(f"Anel superior: 2x 440 + 2x 400 | Deck: 4x 400 | Base: 4x 400 | Viga X: 1x {P.VIGA_X_L:.0f} (de um 400)")
    print("Compra: 3x 440 + 11x 400 | Estoque: 4x 630 inteiros (unico corte do projeto: viga X 400->340)\n")


# ---------------------------------------------------------------- montagem
def montar_maquina() -> cq.Assembly:
    asm = montar_gantry()
    cinza = cq.Color(0.75, 0.75, 0.78)
    verde = cq.Color(0.2, 0.6, 0.3)
    preto = cq.Color(0.2, 0.2, 0.2)
    aco = cq.Color(0.55, 0.55, 0.6)
    bronze = cq.Color(0.72, 0.5, 0.2)
    branco = cq.Color(0.92, 0.92, 0.92)

    # --- colunas dos cantos (630 inteiras) ---
    col = C.perfil_2020(P.COLUNA_L)
    for i, (cx, cy) in enumerate(P.COL_POS):
        asm.add(col.translate((cx, cy, P.Z_PISO)),
                name=f"coluna-{i}", color=cinza)
    # coluna central traseira (cortada), do deck ao anel
    asm.add(C.perfil_2020(P.COL_TRAS_L).translate(
        (P.COL_TRAS_POS[0], P.COL_TRAS_POS[1], P.DECK_Z[1])),
        name="coluna-z-tras", color=cinza)

    # --- anéis da base e do deck (4x 400 entre colunas) ---
    for nome, z0 in (("base", P.BASE_Z[0]), ("deck", P.DECK_Z[0])):
        perfil = C.perfil_2020(P.LADO_400)
        for sx in (-1, 1):  # laterais (ao longo de Y)
            asm.add(ROT_X(perfil, -90).translate(
                (sx * P.RAIL_Y_X, -P.LADO_400 / 2, z0 + P.PERFIL / 2)),
                name=f"{nome}-lateral-{'esq' if sx < 0 else 'dir'}", color=cinza)
        for sy in (-1, 1):  # frente/trás (ao longo de X)
            asm.add(ROT_Y(perfil, 90).translate(
                (-P.LADO_400 / 2, sy * P.RAIL_Y_X, z0 + P.PERFIL / 2)),
                name=f"{nome}-{'frente' if sy < 0 else 'tras'}", color=cinza)

    # --- trilhos Z (verticais) + carrinhos nos braços ---
    trilho_v = ROT_Z(ROT_Y(C.mgn9_trilho(P.RAIL_Z_L), 90), 90)   # comprimento em -Z, base p/ +Y
    carr_v = ROT_Z(ROT_Y(C.mgn9_carrinho(), 90), 90)
    z_bloco_home = P.BRACO_TOP_HOME - P.BRACO_T / 2
    for sx, nome in ((-1, "z-esq"), (1, "z-dir")):
        pos = (sx * P.RAIL_Y_X, -P.RAIL_Y_X + P.PERFIL / 2, P.RAIL_Z_TOPO)
        asm.add(trilho_v.translate(pos), name=f"trilho-{nome}", color=verde)
        asm.add(carr_v.translate((pos[0], pos[1], z_bloco_home)),
                name=f"carrinho-{nome}", color=preto)
    pos_tras = (0.0, P.RAIL_Y_X - P.PERFIL / 2, P.RAIL_Z_TOPO)
    trilho_tras = ROT_Z(ROT_Y(C.mgn9_trilho(P.RAIL_Z_L), 90), -90)  # base p/ -Y
    carr_tras = ROT_Z(ROT_Y(C.mgn9_carrinho(), 90), -90)
    asm.add(trilho_tras.translate(pos_tras), name="trilho-z-tras", color=verde)
    asm.add(carr_tras.translate((0.0, pos_tras[1], z_bloco_home)),
            name="carrinho-z-tras", color=preto)

    # --- fusos TR8 + castanhas + mancais + motores ---
    for i, (fx, fy) in enumerate(P.FUSO_POS):
        fuso = cq.Workplane("XY").circle(P.FUSO_D / 2).extrude(P.FUSO_L)
        asm.add(fuso.translate((fx, fy, P.FUSO_Z0)), name=f"fuso-z{i}", color=aco)
        cast = cq.Workplane("XY").circle(P.CASTANHA_D / 2).extrude(-P.CASTANHA_H)
        asm.add(cast.translate((fx, fy, P.BRACO_TOP_HOME)),
                name=f"castanha-z{i}", color=bronze)
        mancal = (cq.Workplane("XY").box(50, 32, 12, centered=(True, True, False))
                  .union(cq.Workplane("XY", origin=(0, 0, 12)).circle(11).extrude(8)))
        asm.add(mancal.translate((fx, fy, P.DECK_Z[1])),
                name=f"mancal-kp08-z{i}", color=preto)
        asm.add(C.nema17().translate((fx, fy, P.DECK_Z[0] - 4 - P.NEMA17_COMPR)),
                name=f"motor-z{i}", color=preto)

    # --- braços da mesa (placeholders) + mesa em home ---
    z_braco = P.BRACO_TOP_HOME - P.BRACO_T
    for sx, nome in ((-1, "braco-esq"), (1, "braco-dir")):
        braco = cq.Workplane("XY").box(100, 85, P.BRACO_T, centered=(False, True, False))
        asm.add(braco.translate((min(sx * 205, sx * 205 - (100 if sx < 0 else 0)),
                                 -157.5, z_braco)),
                name=nome, color=branco)
    braco_t = cq.Workplane("XY").box(70, 85, P.BRACO_T, centered=(True, False, False))
    asm.add(braco_t.translate((0, 112.5, z_braco)), name="braco-tras", color=branco)

    mesa = C.mesa_mk3().translate(
        (0, P.MESA_CENTRO_Y, P.BICO_TIP_Z - P.VIDRO_ESP - P.MESA_ESP))
    asm.add(mesa, name="mesa-mk3-home", color=cq.Color(0.25, 0.25, 0.3))

    return asm


if __name__ == "__main__":
    verificar_cursos()
    verificar_z()
    print("Montando esqueleto da máquina...")
    asm = montar_maquina()
    destino = os.path.join(DIR_CAD, "11-esqueleto-maquina_v1.step")
    asm.export(destino)
    print("Esqueleto salvo em:", destino)
