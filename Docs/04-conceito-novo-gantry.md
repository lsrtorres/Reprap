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
- **Reuso**: 2× NEMA17 XY, 2 polias motoras GT2 20T, 2 barras Ø8×400 (guias Y), trilho MGN existente (viga X)
- **Comprar**: ~5 m de correia GT2 6 mm, ~8 polias desviadoras (idlers lisos Ø5 mm, ou rolamentos F695 empilhados), parafusos
- Motores ficam **fixos no quadro** (cantos traseiros) → menos massa móvel que qualquer alternativa
- Tensionamento simples: parafuso tensor na ancoragem do carro (estilo Voron)

> **Status: APROVADA pelo Leandro em 2026-10-03** (registro em [03-requisitos-e-decisoes.md](03-requisitos-e-decisoes.md)).

### Opção B — Cartesiano "Prusa de teto" / Markforged (H-Bot)

H-Bot usa 1 correia só, mas aplica momento de giro na viga X — exige trilhos lineares rígidos nos dois lados, senão trava/racking. Markforged complica os desvios. Sem vantagem real sobre CoreXY aqui. ❌

### Opção C — Ultimaker melhorado

Manter cinemática e só limpar o roteamento. Não resolve a insatisfação (as correias continuam chegando indiretamente ao toolhead) e continua consumindo ~160 mm de vão. ❌

## Arquitetura das guias (decidida 2026-10-03)

- **Y (2×)**: barras **Ø8×400 existentes**, uma em cada lateral, com rolamentos LM8UU nos carros Y (blocos impressos)
- **X (viga)**: **perfil 20×20 + trilho MGN (~300 mm) montado sobre ele** — pedido do Leandro: o perfil dá rigidez à viga, o trilho guia o toolhead. O carro do toolhead parafusa no carrinho do MGN; as correias ancoram nele

## Dimensional (CoreXY, curso 200×200, números reais)

O quadro é dimensionado **a partir das barras Y de 400 mm, usadas sem corte** (cortar barra retificada é ruim): vão interno = 400 mm → perfil do anel externo = 400 + 2×20 = **440 mm**.

| Elemento | Valor | Observação |
|---|---|---|
| Anel XY (externo) | **440 × 440 mm** | Perfil 20×20 a comprar |
| Vão interno | 400 × 400 mm | Barras Y Ø8×400 de parede a parede, presas nos blocos de canto |
| Carro Y (cada lado) | ~55 mm (ao longo de Y) | 2× LM8UU + ancoragens |
| Viga X | perfil 20×20 × **~340–360 mm** + MGN 300 centrado | Comprimento exato no CAD |
| Curso X | ~260 mm disponíveis | Limitado pelo trilho de 300 mm − carrinho − folgas; **precisa de 200** ✓ folga ~60 |
| Curso Y | ~275 mm disponíveis | 400 − bloco motor (45) − polias frontais (25) − carro Y (55); **precisa de 200** ✓ folga ~75 |
| Mesa 220×220 | cabe no vão de 400 | Torres Z posicionadas fora do caminho da mesa — CAD |

> As folgas de 60–75 mm absorvem o offset do bico, esteira porta-cabos e tensores sem aperto de projeto.
>
> Os perfis de **380 mm atuais ficam para travessas internas e a caixa da eletrônica**; os **630 mm continuam como colunas verticais** (torres Z + estrutura). Lista de corte definitiva sai do CAD.

## Z (sem mudança de conceito)

Mantém as 2 torres com fuso TR8 + 2 barras lisas cada, motores em cima, mesa MK3 220×220 com vidro e 4 molas. Curso alvo 200 mm — folga de sobra com colunas de 630 mm. Melhorias pontuais a avaliar no CAD: mancal na ponta inferior do fuso e acoplamento flexível, se já não houver.

## Lista de compras (rascunho — fechar após OK e CAD)

| Item | Qtde | Obs |
|---|---|---|
| Perfil 20×20 T-slot, 440 mm | 8 | 4× anel XY superior + 4× anel da base (cortes exatos saem do CAD) |
| Perfil 20×20 T-slot, ~360 mm | 1 | Viga X (pode sair da sobra de um perfil maior) |
| Correia GT2 6 mm | 5 m | Dois loops CoreXY (~2,1 m cada) + sobra |
| Idler GT2 liso 20T furo 5 mm (ou F695ZZ aos pares) | 6–8 | Desvios dos cantos e dos motores |
| Idler GT2 dentado 20T furo 5 mm | 2–4 | Onde o lado dentado toca a polia |
| Parafusos M5/M3 + porcas T | — | Estoque |
| LM8UU | 4 | 2 por carro Y (verificar reuso dos atuais antes de comprar) |

## Perguntas em aberto

1. ~~Aprovação da Opção A (CoreXY)~~ ✅ aprovada 2026-10-03
2. ~~Fontes~~ ✅ 360 W + 120 W confirmadas
3. Quantos trilhos MGN existem e largura exata (provável MGN9)? — precisamos de **1** para a viga X; se houver 2+, sobram para upgrades futuros
4. Validar compra dos perfis de 440 mm (proposta em [03](03-requisitos-e-decisoes.md)) antes do pedido
