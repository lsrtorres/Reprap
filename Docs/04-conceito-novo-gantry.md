# 04 — Conceito do novo gantry XY (roteamento de correias)

**Motivação (R8):** no gantry atual, estilo Ultimaker, as correias não chegam diretamente ao toolhead: os motores acionam eixos rotativos, que acionam 4 correias perimetrais, que movem blocos deslizantes, que movem as barras cruzadas, que finalmente movem o toolhead. São muitos elementos em série (folgas se somam), tensionamento difícil e manutenção chata. O Leandro pediu explicitamente para mudar como as correias chegam ao toolhead e ao gantry.

## Opções avaliadas

### Opção A — CoreXY (recomendada ✅)

Duas correias contínuas em dois planos empilhados (~10 mm de distância vertical). **As duas correias ancoram diretamente no carro do toolhead** — sem eixos intermediários, sem blocos acionados por correia.

```
  motor A ◼──────────────◼ motor B      (traseira)
         │╲              ╱│
         │ ╲            ╱ │
  guia Y │  ╲__________╱  │ guia Y
         │  [ toolhead ]──┼── correias ancoram aqui
         │  ╱  viga X  ╲  │
         │ ╱            ╲ │
         ○╱              ╲○             (polias frontais)
```

- ΔA = ΔX + ΔY ; ΔB = ΔX − ΔY (Marlin: `COREXY`, suportado nativamente pela MKS TinyBee)
- **Reuso**: 2× NEMA17 XY, 2 polias motoras GT2 20T, barras Ø8×300 (guias Y e X) e/ou trilho MGN existente na viga X
- **Comprar**: ~5 m de correia GT2 6 mm, ~8 polias desviadoras (idlers lisos Ø5 mm, ou rolamentos F695 empilhados), parafusos
- Motores ficam **fixos no quadro** (cantos traseiros) → menos massa móvel que qualquer alternativa
- Tensionamento simples: parafuso tensor na ancoragem do carro (estilo Voron)

### Opção B — Cartesiano "Prusa de teto" / Markforged (H-Bot)

H-Bot usa 1 correia só, mas aplica momento de giro na viga X — exige trilhos lineares rígidos nos dois lados, senão trava/racking. Markforged complica os desvios. Sem vantagem real sobre CoreXY aqui. ❌

### Opção C — Ultimaker melhorado

Manter cinemática e só limpar o roteamento. Não resolve a insatisfação (as correias continuam chegando indiretamente ao toolhead) e continua consumindo ~160 mm de vão. ❌

## Dimensional preliminar (CoreXY, curso 200×200)

Trabalhando com perfil 20×20 e blocos impressos:

| Elemento | Estimativa |
|---|---|
| Largura do carro do toolhead | ~50 mm |
| Carros/extremidades da viga X | ~40 mm cada |
| Viga X (comprimento total) | 200 + 50 + 2×40 ≈ **330 mm** ✓ (barras de 300 mm servem se o carro for ~45 mm e as pontas ~30 mm — a fechar no CAD) |
| Blocos traseiros (motor A/B) | ~45 mm de profundidade |
| Polias dianteiras | ~25 mm de profundidade |
| Vão interno necessário (X) | ~355–365 mm |
| Vão interno necessário (Y) | ~360–370 mm |
| **Perfil do anel XY** | **~420 mm externo** (vão interno 380 mm) → folga de 15–25 mm |

> Os perfis de **380 mm atuais ficam para o anel inferior/base da eletrônica ou travessas**; os **630 mm continuam como colunas verticais** (torres Z + estrutura). Lista de corte definitiva sai do CAD.

### Guias XY — decisão interna à opção A

1. **Y (2×)**: barras Ø8×300 com rolamentos LM8UU nos carros laterais, ou trilhos MGN12 se houver 2 disponíveis — ❓ depende do inventário (quantos MGN existem?)
2. **X (viga)**: trilho MGN12 já existente sobre tubo/perfil leve, ou 2 barras Ø8×300 com LM8UU no carro

Critério: menor massa móvel na viga X → preferir 1 MGN12 sobre perfil 20×20 leve, se o trilho existente tiver ≥300 mm.

## Z (sem mudança de conceito)

Mantém as 2 torres com fuso TR8 + 2 barras lisas cada, motores em cima, mesa MK3 220×220 com vidro e 4 molas. Curso alvo 200 mm — folga de sobra com colunas de 630 mm. Melhorias pontuais a avaliar no CAD: mancal na ponta inferior do fuso e acoplamento flexível, se já não houver.

## Lista de compras (rascunho — fechar após OK e CAD)

| Item | Qtde | Obs |
|---|---|---|
| Perfil 20×20 T-slot, 420 mm | 8 | Anel XY superior + anel correspondente (cortes exatos saem do CAD) |
| Correia GT2 6 mm | 5 m | Dois loops CoreXY (~2,3 m cada) + sobra |
| Idler GT2 liso 20T furo 5 mm (ou F695ZZ aos pares) | 8 | Desvios dos cantos e dos motores |
| Idler GT2 dentado 20T furo 5 mm | 2–4 | Onde o lado dentado toca a polia |
| Parafusos M5/M3 + porcas T | — | Estoque |
| LM8UU | 4–8 | Se optarmos por barras Ø8 nas guias (verificar reuso dos atuais) |

## Perguntas em aberto

1. **Aprovação da Opção A (CoreXY)** — trava o conceito e libera a modelagem
2. Quantos trilhos MGN existem e qual o comprimento? (define a decisão de guias)
3. Re-checagem das fontes (10 A vs 30 A) — define se a mesa 12 V (~11 A) fica numa fonte dedicada
