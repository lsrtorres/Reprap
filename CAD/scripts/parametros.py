"""Parâmetros dimensionais do projeto RepRap 200x200x200.

Sistema de coordenadas (igual ao Docs/07-esqueleto-gantry.md):
  - Origem: centro do anel XY superior em planta
  - Z = 0 no TOPO do anel superior; Z+ para cima
  - X+ para a direita; Y+ para trás (traseira da máquina)
Unidades: mm.
"""

# ---- Perfil estrutural ----
PERFIL = 20.0                 # seção do perfil 20x20
ANEL_EXT = 440.0              # lado externo do anel XY
ANEL_INT = ANEL_EXT - 2 * PERFIL   # vão interno = 400
LADO_440 = 440.0              # perfis laterais (esq/dir), comprimento total
LADO_400 = ANEL_INT           # perfis frente/trás, encaixam entre os laterais

# ---- MGN9 (dimensões de catálogo, simplificadas) ----
MGN9_RAIL_W = 9.0
MGN9_RAIL_H = 6.5
MGN9_FURO_PASSO = 20.0        # passo dos furos M3 do trilho
MGN9_FURO_BORDA = 10.0        # 1º furo a 10 mm da ponta
MGN9_BLOCO_W = 20.0           # largura do carrinho (atravessa o trilho)
MGN9_BLOCO_L = 38.5           # comprimento do carrinho (com tampas)
MGN9_BLOCO_H = 10.0           # altura do topo do carrinho desde a BASE do trilho
MGN9_FUROS_B = 15.0           # espaçamento transversal dos furos M3 do carrinho
MGN9_FUROS_C = 10.0           # espaçamento longitudinal
TRILHO_XY_L = 300.0           # trilhos existentes (4x)

# ---- Gantry ----
# Trilhos Y em cima dos perfis laterais, centrados em y=0
RAIL_Y_X = ANEL_EXT / 2 - PERFIL / 2        # ±210 (centro do perfil lateral)
# Junta XY (placeholder Voron-style: polias encapsuladas)
JUNTA_X_IN = 175.0            # face interna da junta (|x|)
JUNTA_X_OUT = 230.0           # face externa
JUNTA_W = JUNTA_X_OUT - JUNTA_X_IN   # 55
JUNTA_L = 60.0                # extensão em Y
JUNTA_H = 38.0                # altura total do bloco (z 10..48)
JUNTA_Z0 = MGN9_BLOCO_H       # base da junta apoiada no carrinho Y (z=10)
# Viga X: perfil 20x20 entre as faces internas das juntas (folga 5mm/lado)
VIGA_X_Z0 = 15.0              # base da viga (z)
VIGA_X_L = 2 * (JUNTA_X_IN - 5.0)    # 340
# Trilho X na face FRONTAL da viga (y-)
TOOLHEAD_PLACA_W = 60.0
TOOLHEAD_PLACA_H = 70.0
TOOLHEAD_PLACA_T = 4.0
BICO_OFFSET_Y = -35.0         # offset do bico à frente do centro da viga (estimado)
BICO_COMPR = 39.0             # marcador do bico até a ponta (V6 Volcano: ~55 abaixo da viga)
BICO_TIP_Z = -55.0            # ponta do bico (z) — mesa em home encosta aqui

# ---- Planos de correia (CoreXY empilhado) ----
CORREIA_H = 6.0
PLANO_B_Z = (17.0, 23.0)      # correia inferior
PLANO_A_Z = (27.0, 33.0)      # correia superior

# ---- Motores A/B (NEMA17) ----
NEMA17_LADO = 42.3
NEMA17_COMPR = 40.0
NEMA17_FUROS = 31.0           # M3, quadrado
NEMA17_BOSS_D = 22.0
NEMA17_EIXO_D = 5.0
MOTOR_POS = (185.0, 182.0)    # |x|, y do eixo dos motores (cantos traseiros)
MOTOR_CORPO_Z0 = 40.0         # base do corpo do motor (eixo p/ baixo)

# ---- Polias ----
POLIA_20T_DP = 12.73          # diâmetro primitivo GT2 20T
IDLER_POS_FRENTE = (185.0, -185.0)   # |x|, y dos postes de polia dianteiros

# ---- Mesa ----
MESA_LADO = 220.0
MESA_ESP = 3.0
VIDRO_ESP = 3.0
AREA_UTIL = 200.0
MESA_CENTRO_Y = BICO_OFFSET_Y  # mesa centrada no alcance real do bico

# ---- Cursos exigidos ----
CURSO_REQ = 200.0

# ============================ FRAME VERTICAL / Z ============================
# Colunas 20x20 nos 4 cantos (perfis de 630 existentes, inteiros) + 1 coluna
# central traseira (cortada) para o 3o trilho Z (estilo Voron Trident).
COLUNA_L = 630.0
Z_TOPO_COLUNA = -PERFIL                      # colunas encostam sob o anel (-20)
Z_PISO = Z_TOPO_COLUNA - COLUNA_L            # -650
COL_POS = [(sx * RAIL_Y_X, sy * RAIL_Y_X) for sx in (-1, 1) for sy in (-1, 1)]

# Anel da base (4x perfil 400 entre as colunas, no chão)
BASE_Z = (Z_PISO, Z_PISO + PERFIL)           # -650 .. -630

# Deck intermediário (4x perfil 400): piso dos mancais/motores do Z;
# abaixo dele fica a baia da eletrônica (SKIPR, fontes, MOSFET)
DECK_Z = (-480.0, -460.0)
BAIA_ALTURA = DECK_Z[0] - BASE_Z[1]          # 150 interno

# Coluna central traseira: do deck ao anel superior (cortar de um 630)
COL_TRAS_POS = (0.0, RAIL_Y_X)
COL_TRAS_L = Z_TOPO_COLUNA - DECK_Z[1]       # 440

# Trilhos Z: MGN9x300 verticais — 2 nas colunas frontais (face +Y) e
# 1 na coluna central traseira (face -Y)
RAIL_Z_L = 300.0
RAIL_Z_TOPO = -50.0
RAIL_Z_BASE = RAIL_Z_TOPO - RAIL_Z_L         # -350

# Fusos TR8x8 x 400 + castanha; mancal KP08/KFL08 sobre o deck; motor na baia
FUSO_L = 400.0
FUSO_D = 8.0
FUSO_Z0 = DECK_Z[1] + 5.0                    # -455 (acima do mancal)
FUSO_POS = [(-180.0, -195.0), (180.0, -195.0), (0.0, 195.0)]
CASTANHA_D = 22.0
CASTANHA_H = 15.0

# Mesa rígida em 3 pontos (SEM molas — z_tilt + bed_mesh substituem):
# vidro 3 + MK3 3 + espaçador 6 + braço 8
ESPACADOR_H = 6.0
BRACO_T = 8.0
BRACO_TOP_HOME = BICO_TIP_Z - VIDRO_ESP - MESA_ESP - ESPACADOR_H   # -67
Z_TRAVEL = 200.0
