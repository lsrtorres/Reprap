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
- **Reuso**: 2× NEMA17 XY, 2 polias motoras GT2 20T, 3 dos 4 trilhos MGN9×300 (2 guias Y + 1 viga X)
- **Comprar**: ~5 m de correia GT2 6 mm, ~8 polias desviadoras (idlers lisos Ø5 mm, ou rolamentos F695 empilhados), parafusos
- Motores ficam **fixos no quadro** (cantos traseiros) → menos massa móvel que qualquer alternativa
- Tensionamento simples: parafuso tensor na ancoragem do carro (estilo Voron)

> **Status: APROVADA pelo Leandro em 2026-10-03** (registro em [03-requisitos-e-decisoes.md](03-requisitos-e-decisoes.md)).

### Opção B — Cartesiano "Prusa de teto" / Markforged (H-Bot)

H-Bot usa 1 correia só, mas aplica momento de giro na viga X — exige trilhos lineares rígidos nos dois lados, senão trava/racking. Markforged complica os desvios. Sem vantagem real sobre CoreXY aqui. ❌

### Opção C — Ultimaker melhorado

Manter cinemática e só limpar o roteamento. Não resolve a insatisfação (as correias continuam chegando indiretamente ao toolhead) e continua consumindo ~160 mm de vão. ❌

## Arquitetura das guias (decidida 2026-10-03, revisada após confirmação dos 4× MGN9)

- **Y (2×)**: **trilhos MGN9×300 parafusados no topo dos perfis laterais** do anel XY. Os carros Y viram placas simples parafusadas nos carrinhos — mais rígido que barra Ø8 em bloco impresso, sem blocos de canto para barras, sem LM8UU. As barras Ø8×400 ficam de **reserva** (candidatas naturais ao Z no futuro)
- **X (viga)**: **perfil 20×20 + trilho MGN (~300 mm) montado na face frontal** (estilo Voron/RatRig) — o perfil dá rigidez à viga, o trilho guia o toolhead. Montagem frontal (e não no topo) porque: placa do toolhead fica plana e parafusa direto no carrinho (sem "L" contornando a viga), o trilho fica mais perto do centro de massa do cabeçote (menos momento nas acelerações) e o topo da viga fica livre para esteira porta-cabos e endstop. Trilho fixado com parafusos M3 + porcas T no canal do perfil. As correias ancoram no carro do toolhead

```
             topo livre (esteira)
            ┌──────────┐
   carrinho │  perfil  │
   MGN  ┌─┐ │  20×20   │
  ══════│█│▌│          │
 trilho └─┘ │          │
        │   └──────────┘
  placa │
  plana ├── extrusora/hotend (CG perto do trilho)
        │
```

## Dimensional (CoreXY, curso 200×200, números reais)

Anel de **440 mm externo** (vão interno 400 mm) — aprovado para compra em 2026-10-03. Com os trilhos MGN9×300 nos perfis laterais, o curso é limitado pelos trilhos, e 440 mm dão o espaço necessário para trilho + blocos de motor/polias nos cantos.

| Elemento | Valor | Observação |
|---|---|---|
| Anel XY (externo) | **440 × 440 mm** | Perfil 20×20 a comprar |
| Vão interno | 400 × 400 mm | Blocos de motor (traseira) e polias (frente) nos cantos |
| Guias Y | 2× MGN9×300 no topo dos perfis laterais | Trilho centrado: sobra 70 mm em cada ponta p/ os blocos de canto |
| Carro Y (cada lado) | placa ~45 mm sobre o carrinho MGN9 | Leva as polias de desvio das correias |
| Viga X | perfil 20×20 × **~360–400 mm** + MGN9×300 na face frontal | Comprimento exato no CAD; pontas parafusam nos carros Y |
| Curso X | ~255 mm disponíveis | Trilho 300 − carrinho (~29) − placa do toolhead; **precisa de 200** ✓ folga ~55 |
| Curso Y | ~250 mm disponíveis | Trilho 300 − placa do carro Y (~45); **precisa de 200** ✓ folga ~50 |
| Mesa 220×220 | cabe no vão de 400 | Torres Z posicionadas fora do caminho da mesa — CAD |

> As folgas de 50–55 mm absorvem o offset do bico, esteira porta-cabos e tensores sem aperto de projeto.
>
> Os perfis de **380 mm atuais ficam para travessas internas e a caixa da eletrônica**; os **630 mm continuam como colunas verticais** (torres Z + estrutura). Lista de corte definitiva sai do CAD.

## Z (sem mudança de conceito)

Mantém as 2 torres com fuso TR8 + 2 barras lisas cada, motores em cima, mesa MK3 220×220 com vidro e 4 molas. Curso alvo 200 mm — folga de sobra com colunas de 630 mm. Melhorias pontuais a avaliar no CAD: mancal na ponta inferior do fuso e acoplamento flexível, se já não houver.

## Lista de compras

Consolidada e pronta para pedido em [05-lista-de-compras.md](05-lista-de-compras.md).

## Perguntas em aberto

1. ~~Aprovação da Opção A (CoreXY)~~ ✅ aprovada 2026-10-03
2. ~~Fontes~~ ✅ 360 W + 120 W confirmadas
3. ~~Trilhos MGN~~ ✅ 4× MGN9×300 — 2 p/ Y, 1 p/ viga X, 1 reserva
4. ~~Perfis de 440 mm~~ ✅ compra aprovada 2026-10-03

Nenhuma pendência de conceito — próxima etapa é a modelagem do esqueleto no Fusion 360.
