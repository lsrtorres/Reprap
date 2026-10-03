# 05 — Lista de compras (gantry CoreXY + Z)

Consolidada em 2026-10-03 após aprovação dos conceitos ([04](04-conceito-novo-gantry.md), [06](06-conceito-z-voron.md)) e do anel de 440 mm.

> ⚠️ **Correção 2026-10-03**: a versão anterior listava 8× perfil de 440 mm. Um anel de 440×440 com cantoneiras leva **2× 440 + 2× 400** (frente/trás encaixam entre os laterais). Quantidades corrigidas abaixo.

## Pedido principal

| # | Item | Especificação | Qtde | Uso |
|---|---|---|---|---|
| 1 | Perfil alumínio 20×20 T-slot (canal 6) | **440 mm** | **4** | Laterais dos anéis XY superior e da base (2 por anel) |
| 2 | Perfil alumínio 20×20 T-slot (canal 6) | **400 mm** | **5** | Frente/trás dos 2 anéis (4) + viga X (1, ajuste fino por corte conforme CAD) |
| 3 | Correia GT2 largura 6 mm (aberta) | **5 m** | 1 rolo | 2 loops CoreXY (~2,1 m cada) + sobra |
| 4 | Polia idler GT2 **lisa** 20 dentes equiv., furo 5 mm, p/ correia 6 mm | — | **6** | Desvios onde o **dorso** da correia toca |
| 5 | Polia idler GT2 **dentada** 20T, furo 5 mm, p/ correia 6 mm | — | **4** | Desvios onde o **lado dentado** toca |
| 6 | Porca T (martelo) M3, canal 6, perfil 20×20 | — | **60** | Fixação dos 3 trilhos MGN9 (15 furos/trilho, passo 20 mm) + reserva |
| 7 | Parafuso M3×8 cabeça cilíndrica (allen) | — | **50** | Trilhos MGN9 nos perfis |
| 8 | Parafuso M3×10/12 + M3 porca | — | **~20** | Carrinhos MGN9 → placas dos carros (conferir comprimento no CAD) |
| 9 | Parafuso M5×25/30 (eixo das polias idler) | — | **10** | Postes das polias nas juntas XY e blocos de motor |

## Fase Z (conceito [06](06-conceito-z-voron.md))

| # | Item | Especificação | Qtde | Uso |
|---|---|---|---|---|
| 10 | Trilho linear **MGN9 × 300 mm com carrinho** | padrão (ex.: MGN9C) | **2** | Guias Z frontais (a traseira usa o 4º trilho do estoque) |
| 11 | **BLTouch** (original ou clone 3DTouch) | sonda de pino (vidro exige pino; indutiva não serve) | **1** | `G34` (auto-alinhamento dos 2 fusos) + malha `G29`; a TinyBee tem porta 3D-Touch |
| 12 | Porca T M3 + parafuso M3×8 | adicionais aos do item 6/7 | **+40** | Fixação dos 3 trilhos Z nas colunas |
| 13 | Acoplador flexível 5×8 mm | se os atuais não forem reaproveitáveis | 1–3 | Motor → fuso TR8 (conferir estoque; precisamos de 3) |
| 14 | **Fuso TR8 × 400 mm, passo 8 mm** (TR8×8, 4 entradas) **+ castanha de bronze** | kit fuso+castanha | **3** | Trident completo: frontal-esq., frontal-dir. e central traseiro |
| 15 | **Mancal KP08 ou KFL08** (eixo Ø8) | com rolamento | **3** | Apoio dos fusos na base (motor embaixo, estilo Trident) |
| 16 | **Hotend V6 com bloco Volcano** | ⚠️ versão **12 V** (cartucho 40 W 12 V + termistor) — muitos kits vêm 24 V | **1** | Novo cabeçote; substitui o hotend atual envolto em fita |
| 17 | **Placa MKS Monster8 V2** | 8 slots de driver, entrada 12–24 V (MCU do **Klipper**) | **1** | Substitui a TinyBee (vira reserva); viabiliza 3× Z independente |
| 18 | **Motor NEMA17** | similar aos atuais (~40 mm, 1,5–1,7 A; confirmar etiqueta dos existentes) | **1** | 3º fuso Z |
| 19 | **Driver de passo** | 1× igual aos 5 atuais (identificar modelo — pendência do inventário); Klipper aceita qualquer step/dir | **1** | 6º slot da Monster8; upgrade opcional futuro: 8× TMC2209 UART |
| 20 | ~~Módulo MKS WiFi~~ | **cancelado** — com Klipper o host já provê rede/interface (Mainsail/Fluidd) | 0 | — |

## Fase Klipper (host — aguardando decisão do caminho)

| # | Item | Especificação | Qtde | Uso |
|---|---|---|---|---|
| 21 | Host Klipper | **(a)** 2ª instância no host da outra impressora (custo zero) · **(b)** Raspberry Pi (Zero 2 W já serve; 3/4 melhor) · **(c)** trocar o item 17 por **MKS SKIPR** (host embutido) | — | Roda o Klipper; placa vira só MCU |
| 22 | Conversor buck 12→5 V ≥3 A | só no caminho (b) | 0–1 | Alimentar o Pi pela fonte de 12 V |
| 23 | Acelerômetro **ADXL345** (opcional) | com cabo | 0–1 | Calibração do input shaper — onde o Klipper brilha no CoreXY |

## Conferir no estoque antes de comprar (já devem existir)

- Parafusos M5×8/10 + porcas T M5 (cantoneiras do quadro) — padrão atual da máquina
- Cantoneiras externas — serão substituídas/complementadas por peças impressas novas
- Polias motoras GT2 20T furo 5 mm — **reuso das 2 atuais**
- LM8UU — ~~não são mais necessários para o gantry~~ (guias Y agora usam MGN9)

## Observações de compra

- **Perfis**: pedir já cortados no tamanho (fornecedores de perfil estrutural cortam sob medida). Tolerância de corte ±0,5 mm é suficiente; o esquadro vem das peças impressas de canto.
- **Idlers**: alternativa aos itens 4–5 são rolamentos F695ZZ aos pares (mais baratos, montagem em parafuso M5), mas as polias prontas com flange alinham melhor a correia de 6 mm.
- **Correia**: preferir GT2 com reforço de fibra de vidro; evitar as com alma de aço (raio mínimo de curvatura maior).
