# 01 — Inventário de componentes (a reaproveitar)

Levantamento feito a partir das fotos de 2026-10-03 (`Fotos/jpg/`) + medições do Leandro (2026-10-03). Itens marcados com ❓ precisam ser confirmados/medidos na máquina física.

## Eletrônica

| Item | Identificação | Status |
|---|---|---|
| Placa controladora | **MKS TinyBee V1.0** (Makerbase, ESP32 com WiFi, 5 slots de driver) — será substituída pela **MKS Monster8 V2** (8 slots) e vira reserva ([decisão](03-requisitos-e-decisoes.md)) | Confirmado (IMG_0322) |
| Drivers de passo | Módulos removíveis com dissipador azul — ❓ modelo (A4988 / DRV8825 / TMC2209?) | A confirmar |
| Fonte 1 | **ST-120-12** — **12 V 10 A (120 W)**, fab. 2021 | Confirmado (IMG_0322 + Leandro) |
| Fonte 2 | Fonte chaveada prata maior — **12 V 30 A (360 W)** | Confirmado (Leandro) |
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
| Trilho linear | **4× trilho MGN9 (9 mm) × 300 mm** com carrinho (tampas verdes) | Confirmado (Leandro) |
| Eixos lisos (torres Z) | Barras retificadas **Ø8 mm × ~400 mm**, 2 por torre (4 no total) — únicos eixos em barra da máquina; o gantry XY é todo em MGN9 | Confirmado (Leandro) |
| Fusos Z | 2 fusos **trapezoidais TR8** verticais (torres esq./dir.), acionados por cima, porca de bronze — ❓ passo/avanço (TR8×8? ×2?) e comprimento | Confirmado (Leandro) |
| Curso XY atual | **~180 mm** em X e Y (limite do quadro atual de 380 mm) | Confirmado (Leandro) |
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
| Mesa aquecida | **MK3 de alumínio, 220 × 220 mm**, alimentação 12 V, conector de bloco + LED indicador | Confirmado (Mesa.heic + Leandro) |
| Suporte | Plataforma impressa branca com molas de nivelamento (4 pontos) | Confirmado (IMG_0317/0325) |

## Estrutura

| Item | Identificação | Status |
|---|---|---|
| Perfis de alumínio | **20×20 mm**, ranhura p/ porca T M5 — comprimentos disponíveis: **380 mm** e **630 mm**; compra de perfis adicionais aprovada | Confirmado (Leandro) |
| Fixação | Cantoneiras/placas impressas externas, parafusos M5 + porca T | Confirmado (IMG_0317/0318) |
| Painéis | Chapas perfuradas brancas na base (compartimento da eletrônica) | Confirmado (IMG_0321/0322) |

## Medições pendentes (fazer na máquina)

Nenhuma pendência bloqueia o gantry XY. As restantes são para as fases Z e eletrônica:

1. Modelo dos drivers de passo (tirar um do slot e fotografar)
2. Modelo/corrente dos motores NEMA 17 (etiqueta lateral)
3. Modelo do display
4. Modelo da extrusora vermelha (o hotend será substituído por V6 Volcano — [decisão](03-requisitos-e-decisoes.md); fusos TR8 atuais viram reserva, substituídos por TR8×8 novos)
