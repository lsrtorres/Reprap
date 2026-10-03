# 06 — Conceito do eixo Z (estilo Voron Trident)

**Decisão do Leandro (2026-10-03):** o Z passa a ser ancorado em **guias MGN verticais — duas na frente e uma no centro traseiro** —, com a mesa suportada em 3 pontos, no estilo Voron Trident. As torres atuais (fuso + 2 barras Ø8 cada) são aposentadas; as barras Ø8×~400 viram reserva.

## Arquitetura

```
   vista de cima (anel da base)          vista frontal
   ┌─────────[MGN]─────────┐          ║ col.    col. ║
   │          trás          │          ║ MGN     MGN ║
   │                        │          ║ │         │ ║
   │      mesa 220×220      │          ║ ├─ mesa ──┤ ║
   │     (3 braços p/       │          ║ │  braços │ ║
   │      os carrinhos)     │          ║ TR8     TR8 ║
 [MGN]                   [MGN]         ║ (fusos)     ║
   └──frente────────────────┘          ╚═════════════╝
```

- **Guias**: 3× trilho MGN9×300 vertical — 2 parafusados nas faces internas das colunas frontais + 1 numa coluna central traseira (perfil 20×20 adicionado ao quadro). Curso útil ≈ 300 − carrinho (39) − margens ≈ **~250 mm** → atende os 200 mm com folga
- **Mesa**: MK3 220×220 + vidro sobre 3 braços (frente-esq., frente-dir., centro-trás) parafusados nos carrinhos — suporte em 3 pontos, o único que não empena a mesa por definição
- **Trilhos**: temos 1 MGN9×300 de reserva; **comprar 2** (já estão na [lista de compras](05-lista-de-compras.md))
- **Colunas**: perfis de 630 mm existentes; a coluna central traseira pode sair do estoque de 380 mm se a altura da zona Z permitir (fechar no CAD)

## Acionamento — Trident completo com MKS Monster8 V2

A TinyBee tem só 5 slots de driver (X, Y, Z, E0, E1) — com CoreXY + extrusora sobrariam 2 para o Z. **Decisão (2026-10-03): comprar uma MKS Monster8 V2** (8 slots removíveis, entrada 12–24 V, Marlin 2.x oficial) e fazer o **Trident completo**:

- **3 fusos TR8 × 400 mm, passo 8 mm** (TR8×8, 4 entradas) + **castanhas de bronze** — frontal-esq., frontal-dir. e central traseiro; os TR8 atuais viram reserva
- **3 motores NEMA17 independentes** (2 existentes + **1 a comprar**), cada um no seu slot → `G34`/`Z_STEPPER_AUTO_ALIGN` de **3 pontos** com a BLTouch: auto-tram verdadeiro de rolagem **e** inclinação
- **Mancais KP08 ou KFL08 (Ø8)** na base, um por fuso — motor embaixo, acoplador 5×8, mancal logo acima, ponta superior do fuso livre
- **Sonda: BLTouch** — `G34` + malha `G29` sobre o vidro
- Slots da Monster8: X, Y, E0 + 3× Z (Z/E1/E2 conforme o mapeamento do Marlin) = 6 usados, 2 de folga
- **Drivers**: reaproveitam-se os 5 atuais + 1 igual a comprar (identificar o modelo — pendência do inventário); upgrade opcional futuro: jogo de TMC2209
- **WiFi**: módulo MKS WiFi (ESP12S) opcional na Monster8 repõe o WiFi embutido da TinyBee
- **TinyBee**: vira reserva (exceção ao requisito R2 aprovada pelo Leandro)

> Passos/mm do Z com TR8×8 e motor 1,8°: 16 microsteps → **400 steps/mm**.

Alternativas descartadas: manter TinyBee com 2 fusos + seguidor passivo (pitch não ajustável por software); 3 fusos sincronizados por correia (tram mecânico); MKS SKIPR (excelente, mas muda tudo para Klipper de uma vez — fica como caminho futuro, a Monster8 também roda Klipper).

## O que é liberado dos componentes atuais

| Componente | Destino |
|---|---|
| 4× barra Ø8×~400 (torres) | Reserva |
| 8× LM8UU (ou similares das torres) | Reserva |
| 2× fuso TR8 atual | Reserva (substituídos por 3× TR8×8 400 mm novos) |
| Hotend atual (envolto em fita) | Reserva (substituído por V6 Volcano 12 V) |
| **MKS TinyBee V1.0** | Reserva (substituída pela Monster8 V2 — exceção ao R2 aprovada) |
| Perfis das torres | Voltam ao estoque (380/630) |

## Pendências desta fase

1. ~~Confirmar acionamento~~ ✅ Opção A com TR8×8 400 + KP08/KFL08 + BLTouch
2. CAD: braços da mesa, suportes de fuso/motor, posição exata da coluna traseira, altura da zona Z (dimensionar com o curso de 200 + espessuras da mesa)
