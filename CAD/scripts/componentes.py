"""Geradores de sólidos simplificados dos componentes padrão.

Modelos de ENVELOPE dimensional (não cosméticos): seções, furos e
interfaces corretos para posicionamento no Fusion 360.
Todos retornam cadquery.Workplane com origem documentada em cada função.
"""
import cadquery as cq

import parametros as P


def perfil_2020(comprimento: float) -> cq.Workplane:
    """Perfil 20x20 T-slot simplificado. Eixo do comprimento = Z,
    base em z=0, seção centrada em XY."""
    s = (
        cq.Workplane("XY")
        .rect(P.PERFIL, P.PERFIL)
        .extrude(comprimento)
        .faces(">Z")
        .workplane()
        .hole(4.2)  # furo central (rosca M5)
    )
    # canais T simplificados (6 mm de boca, 5 de profundidade) nas 4 faces
    canal = (
        cq.Workplane("XZ", origin=(0, -P.PERFIL / 2, comprimento / 2))
        .rect(6.0, comprimento)
        .extrude(-5.0)
    )
    for ang in (0, 90, 180, 270):
        s = s.cut(canal.rotate((0, 0, 0), (0, 0, 1), ang))
    return s


def mgn9_trilho(comprimento: float) -> cq.Workplane:
    """Trilho MGN9. Comprimento em X, base em z=0, centrado em X e Y."""
    furos_n = int((comprimento - 2 * P.MGN9_FURO_BORDA) // P.MGN9_FURO_PASSO) + 1
    x0 = -(furos_n - 1) * P.MGN9_FURO_PASSO / 2
    pts = [(x0 + i * P.MGN9_FURO_PASSO, 0) for i in range(furos_n)]
    return (
        cq.Workplane("XY")
        .box(comprimento, P.MGN9_RAIL_W, P.MGN9_RAIL_H, centered=(True, True, False))
        .faces(">Z")
        .workplane()
        .pushPoints(pts)
        .hole(3.5, P.MGN9_RAIL_H)
    )


def mgn9_carrinho() -> cq.Workplane:
    """Carrinho MGN9C. Deslocamento em X; topo em z=MGN9_BLOCO_H,
    posicionado como se o trilho estivesse com base em z=0."""
    z_base = 1.5  # folga sob o carrinho
    bloco = (
        cq.Workplane("XY", origin=(0, 0, z_base))
        .box(P.MGN9_BLOCO_L, P.MGN9_BLOCO_W, P.MGN9_BLOCO_H - z_base,
             centered=(True, True, False))
        # rasgo por onde passa o trilho
        .cut(
            cq.Workplane("XY")
            .box(P.MGN9_BLOCO_L + 1, P.MGN9_RAIL_W + 0.6, P.MGN9_RAIL_H + 0.3,
                 centered=(True, True, False))
        )
    )
    furos = [
        (sx * P.MGN9_FUROS_C / 2, sy * P.MGN9_FUROS_B / 2)
        for sx in (-1, 1) for sy in (-1, 1)
    ]
    return (
        bloco.faces(">Z").workplane().pushPoints(furos).hole(3.0, 4.0)
    )


def nema17() -> cq.Workplane:
    """NEMA17. Corpo com base em z=0, eixo para CIMA (+Z), centrado em XY."""
    furos = [
        (sx * P.NEMA17_FUROS / 2, sy * P.NEMA17_FUROS / 2)
        for sx in (-1, 1) for sy in (-1, 1)
    ]
    corpo = (
        cq.Workplane("XY")
        .box(P.NEMA17_LADO, P.NEMA17_LADO, P.NEMA17_COMPR, centered=(True, True, False))
        .edges("|Z")
        .chamfer(5.0)
        .faces(">Z")
        .workplane()
        .pushPoints(furos)
        .hole(3.0, 5.0)
    )
    boss = (
        cq.Workplane("XY", origin=(0, 0, P.NEMA17_COMPR))
        .circle(P.NEMA17_BOSS_D / 2)
        .extrude(2.0)
    )
    eixo = (
        cq.Workplane("XY", origin=(0, 0, P.NEMA17_COMPR))
        .circle(P.NEMA17_EIXO_D / 2)
        .extrude(24.0)
    )
    return corpo.union(boss).union(eixo)


def polia_gt2_20t() -> cq.Workplane:
    """Polia GT2 20T furo 5. Base em z=0, altura 14 (flanges + corpo)."""
    return (
        cq.Workplane("XY")
        .circle(16.0 / 2).extrude(1.0)                       # flange inferior
        .faces(">Z").workplane().circle(P.POLIA_20T_DP / 2).extrude(8.0)
        .faces(">Z").workplane().circle(16.0 / 2).extrude(1.0)  # flange superior
        .faces(">Z").workplane().circle(7.0 / 2).extrude(4.0)   # cubo do grub
        .faces(">Z").workplane().hole(5.0)
    )


def idler_20t(h: float = 10.0) -> cq.Workplane:
    """Polia desviadora lisa c/ flanges, furo 5. Base em z=0."""
    return (
        cq.Workplane("XY")
        .circle(18.0 / 2).extrude(1.0)
        .faces(">Z").workplane().circle(12.0 / 2).extrude(h - 2.0)
        .faces(">Z").workplane().circle(18.0 / 2).extrude(1.0)
        .faces(">Z").workplane().hole(5.0)
    )


def fuso_tr8(comprimento: float) -> cq.Workplane:
    """Fuso TR8 simplificado (cilindro Ø8 com chanfros nas pontas) — a rosca
    trapezoidal não é modelada (desnecessária p/ montagem/simulação).
    Eixo em Z, base em z=0."""
    return (
        cq.Workplane("XY")
        .circle(P.FUSO_D / 2)
        .extrude(comprimento)
        .faces(">Z").chamfer(0.8)
        .faces("<Z").chamfer(0.8)
    )


def mesa_mk3() -> cq.Workplane:
    """Mesa MK3 220x220x3 + vidro 3 mm. Base do alumínio em z=0, centrada."""
    mk3 = (
        cq.Workplane("XY")
        .box(P.MESA_LADO, P.MESA_LADO, P.MESA_ESP, centered=(True, True, False))
        .faces(">Z").workplane()
        .pushPoints([(sx * 104.5, sy * 104.5) for sx in (-1, 1) for sy in (-1, 1)])
        .hole(3.5, P.MESA_ESP)
    )
    vidro = (
        cq.Workplane("XY", origin=(0, 0, P.MESA_ESP))
        .box(P.MESA_LADO, P.MESA_LADO, P.VIDRO_ESP, centered=(True, True, False))
    )
    return mk3.union(vidro)
