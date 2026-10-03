# 01 — Inventário de componentes (a reaproveitar)

Levantamento inicial feito a partir das fotos de 2026-10-03 (`Fotos/jpg/`). Itens marcados com ❓ precisam ser confirmados/medidos na máquina física.

## Eletrônica

| Item | Identificação | Status |
|---|---|---|
| Placa controladora | **MKS TinyBee V1.0** (Makerbase, ESP32 com WiFi, 5 slots de driver) | Confirmado (IMG_0322) |
| Drivers de passo | Módulos removíveis com dissipador azul — ❓ modelo (A4988 / DRV8825 / TMC2209?) | A confirmar |
| Fonte 1 | **ST-120-12** — 110/220 V → **12 V 10 A (120 W)**, fab. 2021 | Confirmado (IMG_0322) |
| Fonte 2 | Fonte chaveada prata maior — ❓ tensão/corrente (etiqueta) | A confirmar (IMG_0321/0322) |
| MOSFET externo | Módulo preto para mesa aquecida, com borne parafusado | Confirmado (IMG_0321/0322) |
| Distribuição | Conectores WAGO tipo 221 (5 vias) ×2 | Confirmado (IMG_0321) |
| Display | Tela em caixa impressa branca no meio da torre — ❓ modelo (MKS TFT? 12864?) | A confirmar (IMG_0317) |
| Ventoinhas | 2× fans (~40–50 mm) no painel da base | Confirmado (IMG_0323) |
| Endstops | Pelo menos 1 endstop em PCB (suporte verde no Z) — ❓ quantidade/tipo | A confirmar (IMG_0325) |

## Motores

| Item | Qtde | Observação |
|---|---|---|
| NEMA 17 | **5** (X, Y, 2× Z, extrusora) — um deles etiquetado "5" | ❓ confirmar modelo/corrente (etiqueta dos motores) |

## Movimento

| Item | Identificação | Status |
|---|---|---|
| Gantry XY | Estilo Ultimaker: eixos cruzados com correias GT2 no perímetro, blocos deslizantes impressos | Confirmado (IMG_0320/0325/0326/0328) |
| Trilho linear | Pelo menos 1 trilho MGN (tampas verdes) usado no gantry — ❓ tamanho (MGN12?) e quantidade | A confirmar (IMG_0320/0326) |
| Eixos lisos | Barras retificadas — ❓ diâmetro (6 ou 8 mm?) e comprimentos | A confirmar |
| Fusos Z | 2 fusos verticais (torres esq./dir.), acionados por cima, porca de bronze — ❓ tipo (barra roscada M8 ou trapezoidal TR8?) | A confirmar (IMG_0323/0324/0325) |
| Guias Z | 2 barras lisas por torre (4 no total) | Confirmado (IMG_0323/0324) |
| Correias | GT2 6 mm com polias e esticadores | Confirmado (IMG_0320/0328) |
| Esteira porta-cabos | Esteira impressa branca para o cabeçote | Confirmado (IMG_0318/0328) |

## Cabeçote / Extrusão

| Item | Identificação | Status |
|---|---|---|
| Extrusora | Direct-drive com corpo vermelho sobre o carro central | Confirmado (IMG_0317) — ❓ modelo |
| Hotend | Montado sob o carro, envolto em fita preta — ❓ modelo (E3D V5/V6 clone? MK8?) | A confirmar (IMG_0326) |

## Mesa de impressão

| Item | Identificação | Status |
|---|---|---|
| Superfície | Vidro com clipes | Confirmado (IMG_0317) |
| Mesa aquecida | ❓ existe PCB aquecedor sob o vidro? Modelo/tamanho (MK2b 214×214?) e tensão (12 V?) | A confirmar |
| Suporte | Plataforma impressa branca com molas de nivelamento (4 pontos) | Confirmado (IMG_0317/0325) |

## Estrutura

| Item | Identificação | Status |
|---|---|---|
| Perfis de alumínio | ❓ série (20×20? há peças que parecem 20×40) — comprimentos disponíveis: **380 mm** e **630 mm** | A confirmar |
| Fixação | Cantoneiras/placas impressas externas, parafusos M5 + porca T | Confirmado (IMG_0317/0318) |
| Painéis | Chapas perfuradas brancas na base (compartimento da eletrônica) | Confirmado (IMG_0321/0322) |

## Medições pendentes (fazer na máquina)

1. Etiqueta da fonte 2 (tensão/corrente)
2. Modelo dos drivers de passo (tirar um do slot e fotografar)
3. Modelo/corrente dos motores NEMA 17 (etiqueta lateral)
4. Diâmetro das barras lisas (paquímetro: 6 vs 8 mm) e comprimentos
5. Fusos Z: diâmetro, passo e tipo de rosca (M8 ×1,25 vs TR8×8?)
6. Perfil de alumínio: medir seção (20×20?) e ranhura (canal ~6 mm?)
7. Mesa: dimensões do vidro, existência e modelo do aquecedor, tensão
8. Trilho(s) MGN: largura do trilho e comprimento; quantos existem
9. Curso XY e Z atuais da máquina
10. Modelo do display
11. Modelo do hotend e da extrusora
