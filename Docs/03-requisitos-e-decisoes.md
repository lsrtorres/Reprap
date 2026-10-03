# 03 — Requisitos e registro de decisões

Este documento é a memória viva do projeto. Toda decisão relevante entra na tabela de decisões com data e justificativa. Alterações via commit — o histórico do git é o registro oficial.

## Requisitos

| # | Requisito | Tipo |
|---|---|---|
| R1 | Volume de impressão de 200 × 200 × 200 mm | Obrigatório |
| R2 | Reaproveitar todos os componentes atuais (motores, fusos, guias, eletrônica, fontes, mesa, display, extrusora/hotend) | Obrigatório |
| R3 | Estrutura em perfil de alumínio; estoque atual: 380 mm e 630 mm; compra de perfis adicionais é permitida | Obrigatório |
| R4 | Fixação dos perfis com cantoneiras externas, parafuso M5 + porca T (padrão atual) — pode evoluir se justificado | Desejável |
| R5 | Modelagem completa em Fusion 360, com F3D/STEP versionados no repositório | Obrigatório |
| R6 | Projeto colaborativo: tudo (docs, CAD, decisões, memória) versionado no git | Obrigatório |
| R7 | Peças impressas em 3D fabricáveis na própria máquina atual (bootstrap) | Desejável |
| R8 | Novo roteamento de correias: chegada limpa e direta das correias ao toolhead e ao gantry XY (insatisfação com o esquema atual estilo Ultimaker) | Obrigatório |

## Registro de decisões

| Data | Decisão | Justificativa | Status |
|---|---|---|---|
| 2026-10-03 | Repositório git como fonte de verdade do projeto (docs + CAD exportado + fotos) | Projeto colaborativo; Fusion 360 fica na nuvem Autodesk, mas exportações F3D/STEP são versionadas | ✅ Ativa |
| 2026-10-03 | Fotos originais `.heic` mantidas + conversões `.jpg` (1600 px) para visualização no GitHub | GitHub não renderiza HEIC; JPGs facilitam a colaboração | ✅ Ativa |
| 2026-10-03 | Perfis adicionais podem ser comprados (20×20, mesmo padrão) | Necessário: quadro atual (380 mm) só entrega ~180 mm de curso | ✅ Ativa |
| 2026-10-03 | Fusos Z: **manter os TR8 atuais** | Confirmado que já são trapezoidais TR8 — sem motivo para troca | ✅ Ativa |
| — | Cinemática do novo gantry: **proposta = CoreXY** (atende R8: correias ancoram direto no carro do toolhead, motores fixos) — ver [04-conceito-novo-gantry.md](04-conceito-novo-gantry.md) | Elimina os eixos rotativos e as 8 correias do estilo Ultimaker; reusa os 2 motores XY e polias; aguardando OK do Leandro | 🔶 Proposta |
| — | Tamanho do anel XY: proposta = comprar 8× perfil 20×20 de **~420 mm** (anel superior + anel da base) | Vão interno 380 mm comporta 200 mm de curso CoreXY com folga; números em 04 | 🔶 Proposta |

## Próximos passos

1. **[Leandro]** Decidir: aprova CoreXY conforme [04-conceito-novo-gantry.md](04-conceito-novo-gantry.md)?
2. **[Leandro]** Medições que ainda faltam ([01-inventario-componentes.md](01-inventario-componentes.md), seção final) — em especial a re-checagem da fonte e os trilhos MGN
3. **[Claude]** Com o OK, fechar o dimensional do quadro e a lista de compras definitiva
4. **[Claude]** Levantar STEPs de componentes padrão (NEMA17, perfil 20×20, MGN12, GT2, TinyBee, mesa MK3) para `CAD/componentes/`
5. Modelagem do quadro no Fusion 360
