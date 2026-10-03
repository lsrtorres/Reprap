"""Gera o esqueleto dimensional do gantry CoreXY (STEP) + STEPs dos
componentes padrão, e VERIFICA os cursos contra o requisito de 200x200.

Uso (a partir de CAD/scripts/):
    ..\\..\\.venv\\Scripts\\python.exe esqueleto_gantry.py

Saídas:
    CAD/10-esqueleto-gantry_v1.step   (montagem de referência p/ Fusion 360)
    CAD/componentes/*.step            (componentes individuais)
"""
import os

import cadquery as cq

import parametros as P
import componentes as C

AQUI = os.path.dirname(os.path.abspath(__file__))
DIR_CAD = os.path.normpath(os.path.join(AQUI, ".."))
DIR_COMP = os.path.join(DIR_CAD, "componentes")

ROT_X = lambda s, a: s.rotate((0, 0, 0), (1, 0, 0), a)
ROT_Y = lambda s, a: s.rotate((0, 0, 0), (0, 1, 0), a)
ROT_Z = lambda s, a: s.rotate((0, 0, 0), (0, 0, 1), a)


# ---------------------------------------------------------------- verificação
def verificar_cursos():
    meia_viagem = P.TRILHO_XY_L / 2 - P.MGN9_BLOCO_L / 2   # carrinho no trilho 300
    curso_x = 2 * meia_viagem
    curso_y = 2 * meia_viagem
    bico_y_min = -meia_viagem + P.BICO_OFFSET_Y
    bico_y_max = +meia_viagem + P.BICO_OFFSET_Y

    print("=== Verificação de cursos (requisito: %.0f mm) ===" % P.CURSO_REQ)
    print(f"Curso X do bico : {curso_x:6.1f} mm  (±{meia_viagem:.1f})")
    print(f"Curso Y do bico : {curso_y:6.1f} mm  ({bico_y_min:+.1f} .. {bico_y_max:+.1f})")
    print(f"Centro útil da mesa em Y: {P.MESA_CENTRO_Y:+.1f} mm (offset do bico)")
    folga_x = (curso_x - P.CURSO_REQ) / 2
    folga_y = (curso_y - P.CURSO_REQ) / 2
    print(f"Folga por lado  : X {folga_x:+.1f} mm | Y {folga_y:+.1f} mm")
    assert curso_x >= P.CURSO_REQ, "Curso X insuficiente!"
    assert curso_y >= P.CURSO_REQ, "Curso Y insuficiente!"
    # janela 200x200 centrada em (0, MESA_CENTRO_Y) precisa caber no alcance do bico
    assert bico_y_min <= P.MESA_CENTRO_Y - P.CURSO_REQ / 2, "Mesa fora do alcance (frente)!"
    assert bico_y_max >= P.MESA_CENTRO_Y + P.CURSO_REQ / 2, "Mesa fora do alcance (trás)!"
    print("OK: janela de 200x200 coberta.\n")

    # estimativa de correia por loop CoreXY (ida/volta nas 2 laterais + travessas)
    lado = P.MOTOR_POS[1] - P.IDLER_POS_FRENTE[1]
    estim = 2 * lado + 2 * (2 * P.MOTOR_POS[0]) + 2 * (2 * P.JUNTA_X_IN)
    print(f"Estimativa de correia por loop: ~{estim / 1000:.2f} m "
          f"(2 loops ≈ {2 * estim / 1000:.2f} m; rolo de 5 m OK)\n")


# ---------------------------------------------------------------- montagem
def montar() -> cq.Assembly:
    asm = cq.Assembly(name="esqueleto-gantry-corexy")
    cinza = cq.Color(0.75, 0.75, 0.78)
    preto = cq.Color(0.2, 0.2, 0.2)
    verde = cq.Color(0.2, 0.6, 0.3)
    azul = cq.Color(0.25, 0.45, 0.8)
    verm = cq.Color(0.85, 0.25, 0.2)
    ambar = cq.Color(0.95, 0.65, 0.1, 0.55)

    # --- anel superior (topo em z=0) ---
    lat = C.perfil_2020(P.LADO_440)
    for sx, nome in ((-1, "perfil-esq"), (1, "perfil-dir")):
        p = ROT_X(lat, -90).translate((sx * P.RAIL_Y_X, -P.LADO_440 / 2, -P.PERFIL / 2))
        asm.add(p, name=nome, color=cinza)
    tra = C.perfil_2020(P.LADO_400)
    for sy, nome in ((-1, "perfil-frente"), (1, "perfil-tras")):
        p = ROT_Y(tra, 90).translate((-P.LADO_400 / 2, sy * P.RAIL_Y_X, -P.PERFIL / 2))
        asm.add(p, name=nome, color=cinza)

    # --- trilhos Y + carrinhos (gantry em y=0, home no centro) ---
    trilho = C.mgn9_trilho(P.TRILHO_XY_L)
    carr = C.mgn9_carrinho()
    for sx, lado_nome in ((-1, "esq"), (1, "dir")):
        asm.add(ROT_Z(trilho, 90).translate((sx * P.RAIL_Y_X, 0, 0)),
                name=f"trilho-y-{lado_nome}", color=verde)
        asm.add(ROT_Z(carr, 90).translate((sx * P.RAIL_Y_X, 0, 0)),
                name=f"carrinho-y-{lado_nome}", color=preto)
        # junta XY (placeholder translúcido: polias ficam DENTRO dela)
        junta = cq.Workplane("XY").box(
            P.JUNTA_W, P.JUNTA_L, P.JUNTA_H, centered=(False, True, False)
        ).translate((P.JUNTA_X_IN if sx > 0 else -P.JUNTA_X_OUT, 0, P.JUNTA_Z0))
        asm.add(junta, name=f"junta-xy-{lado_nome}", color=ambar)

    # --- viga X + trilho X + toolhead (home no centro) ---
    viga = ROT_Y(C.perfil_2020(P.VIGA_X_L), 90).translate(
        (-P.VIGA_X_L / 2, 0, P.VIGA_X_Z0 + P.PERFIL / 2))
    asm.add(viga, name="viga-x", color=cinza)
    z_viga_c = P.VIGA_X_Z0 + P.PERFIL / 2
    trilho_x = ROT_X(C.mgn9_trilho(P.TRILHO_XY_L), 90).translate((0, -10.0, z_viga_c))
    asm.add(trilho_x, name="trilho-x", color=verde)
    carr_x = ROT_X(C.mgn9_carrinho(), 90).translate((0, -10.0, z_viga_c))
    asm.add(carr_x, name="carrinho-x", color=preto)
    placa = cq.Workplane("XY").box(
        P.TOOLHEAD_PLACA_W, P.TOOLHEAD_PLACA_T, P.TOOLHEAD_PLACA_H,
        centered=(True, False, True)
    ).translate((0, -24.0, z_viga_c))
    asm.add(placa, name="toolhead-placa", color=verm)
    bico = (
        cq.Workplane("XY", origin=(0, P.BICO_OFFSET_Y, z_viga_c - 35))
        .circle(4).extrude(-P.BICO_COMPR)
        .faces("<Z").workplane().circle(4).workplane(offset=-6).circle(0.4)
        .loft(combine=True)
    )
    asm.add(bico, name="bico-marcador", color=verm)

    # --- motores A/B + polias (traseira) ---
    motor = ROT_X(C.nema17(), 180)
    polia = C.polia_gt2_20t()
    for sx, nome, zp in ((-1, "motor-a", P.PLANO_A_Z[0] - 1),
                         (1, "motor-b", P.PLANO_B_Z[0] - 1)):
        asm.add(motor.translate((sx * P.MOTOR_POS[0], P.MOTOR_POS[1],
                                 P.MOTOR_CORPO_Z0 + P.NEMA17_COMPR)),
                name=nome, color=preto)
        asm.add(polia.translate((sx * P.MOTOR_POS[0], P.MOTOR_POS[1], zp)),
                name=f"polia-{nome}", color=azul)

    # --- polias desviadoras dianteiras (2 planos por canto) ---
    idler = C.idler_20t()
    for sx, lado_nome in ((-1, "esq"), (1, "dir")):
        for plano, z in (("a", P.PLANO_A_Z[0] - 1), ("b", P.PLANO_B_Z[0] - 1)):
            asm.add(idler.translate((sx * P.IDLER_POS_FRENTE[0],
                                     P.IDLER_POS_FRENTE[1], z)),
                    name=f"idler-frente-{lado_nome}-{plano}", color=azul)

    # --- mesa (referência de posição em planta; altura ilustrativa) ---
    mesa = C.mesa_mk3().translate((0, P.MESA_CENTRO_Y, -86))
    asm.add(mesa, name="mesa-mk3-referencia", color=cq.Color(0.3, 0.3, 0.35, 0.6))

    return asm


# ---------------------------------------------------------------- exportação
def exportar_componentes():
    os.makedirs(DIR_COMP, exist_ok=True)
    itens = {
        "perfil-2020-630": C.perfil_2020(P.COLUNA_L),
        "perfil-2020-440": C.perfil_2020(440),
        "perfil-2020-400": C.perfil_2020(400),
        "perfil-2020-340-viga-x": C.perfil_2020(P.VIGA_X_L),
        "mgn9-trilho-300": C.mgn9_trilho(300),
        "mgn9-carrinho": C.mgn9_carrinho(),
        "fuso-tr8x8-400": C.fuso_tr8(P.FUSO_L),
        "nema17": C.nema17(),
        "polia-gt2-20t": C.polia_gt2_20t(),
        "idler-20t": C.idler_20t(),
        "mesa-mk3-220": C.mesa_mk3(),
    }
    for nome, solido in itens.items():
        destino = os.path.join(DIR_COMP, nome + ".step")
        cq.exporters.export(solido, destino)
        print("  componente:", os.path.relpath(destino, DIR_CAD))


if __name__ == "__main__":
    verificar_cursos()
    print("Exportando componentes...")
    exportar_componentes()
    print("Montando esqueleto...")
    asm = montar()
    destino = os.path.join(DIR_CAD, "10-esqueleto-gantry_v1.step")
    asm.export(destino)
    print("Esqueleto salvo em:", destino)
