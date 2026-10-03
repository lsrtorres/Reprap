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

## Acionamento — a restrição da TinyBee

A MKS TinyBee tem **5 slots de driver: X, Y, Z, E0, E1**. Com CoreXY usando X+Y e a extrusora em E0, sobram **2 slots para o Z** (Z e E1). Um Trident "completo" (3 fusos com motores independentes + `G34`/`Z_STEPPER_AUTO_ALIGN` de 3 pontos) precisaria de 3 slots — **não cabe** sem placa de expansão.

| Opção | Descrição | Prós | Contras |
|---|---|---|---|
| **A (recomendada)** | **2 fusos TR8 frontais** (motores e fusos existentes, um em cada slot: Z e E1) + ponto traseiro **seguidor passivo** no MGN | Zero compra de motor/fuso/driver; `G34` de 2 pontos nivela a **rolagem** automaticamente (com sonda); o pitch fica fixado pela rigidez dos carrinhos frontais + seguidor | Pitch não é ajustável por software (ajuste mecânico único na montagem do braço traseiro) |
| B | 3 fusos TR8, **sincronizados por correia** na base, 1 motor só (libera 1 NEMA17!) | Plano da mesa travado mecanicamente — nunca desnivela; 1 driver só | Comprar 1 TR8 + 3 polias + correia fechada longa; tram mecânico (soltar correia) em vez de automático |
| C | 3 fusos com 3 motores (Trident real) | Auto-tram 3 pontos | Precisa de expansor/placa nova — viola o reuso da TinyBee ❌ |

**✅ Opção A confirmada (2026-10-03)** — o Leandro especificou o hardware correspondente:

- **Fusos novos: TR8 × 400 mm com passo de 8 mm** (TR8×8, 4 entradas) + **castanhas de bronze** — os TR8 atuais viram reserva. Com passo 8: 1 volta = 8 mm → Z rápido no posicionamento; com 2 fusos e castanhas novas, sem descida espontânea em repouso na prática
- **Mancais KP08 ou KFL08 (Ø8)** na base, um por fuso — motor embaixo (estilo Trident), acoplador 5×8 entre motor e fuso, mancal logo acima do acoplador, ponta superior do fuso livre
- **Sonda: BLTouch** (a TinyBee tem porta 3D-Touch dedicada) — habilita `G34` (auto-alinhamento dos 2 fusos) e malha `G29` sobre o vidro

> Passos/mm do Z com TR8×8 e motor 1,8°: 16 microsteps → **400 steps/mm**.

## O que é liberado dos componentes atuais

| Componente | Destino |
|---|---|
| 4× barra Ø8×~400 (torres) | Reserva |
| 8× LM8UU (ou similares das torres) | Reserva |
| 2× fuso TR8 atual | Reserva (substituídos por TR8×8 400 mm novos) |
| Hotend atual (envolto em fita) | Reserva (substituído por V6 Volcano 12 V) |
| Perfis das torres | Voltam ao estoque (380/630) |

## Pendências desta fase

1. ~~Confirmar acionamento~~ ✅ Opção A com TR8×8 400 + KP08/KFL08 + BLTouch
2. CAD: braços da mesa, suportes de fuso/motor, posição exata da coluna traseira, altura da zona Z (dimensionar com o curso de 200 + espessuras da mesa)
