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
| 2026-10-03 | **Cinemática do novo gantry: CoreXY** — correias ancoram direto no carro do toolhead, motores fixos no quadro — ver [04-conceito-novo-gantry.md](04-conceito-novo-gantry.md) | Atende R8; elimina eixos rotativos e correias perimetrais do estilo Ultimaker; reusa os 2 motores XY e polias; Marlin `COREXY` nativo na TinyBee. **Aprovado pelo Leandro** | ✅ Ativa |
| 2026-10-03 | **Viga X = perfil 20×20 + trilho MGN montado nele**; toolhead corre no MGN | Pedido do Leandro (robustez); perfil dá rigidez torcional que barras não dão | ✅ Ativa |
| 2026-10-03 | Trilho MGN na **face frontal** da viga X (não no topo), estilo Voron | Sugestão do Leandro: placa do toolhead plana, CG do cabeçote perto do trilho (menos momento), topo livre p/ esteira — detalhes em [04](04-conceito-novo-gantry.md) | ✅ Ativa |
| 2026-10-03 | ~~Guias Y = 2 barras Ø8×400 com LM8UU~~ | Substituída no mesmo dia ao confirmar que existem 4 trilhos MGN9 | ♻️ Substituída |
| 2026-10-03 | **Guias Y = 2× trilho MGN9 300 mm** parafusados nos perfis laterais; viga X usa o 3º trilho; 4º fica de reserva; barras Ø8×400 viram reserva p/ futuro | Confirmados 4× MGN9×300: trilho direto no perfil é mais rígido que barra em bloco impresso, carros Y viram placas simples e dispensa comprar LM8UU | ✅ Ativa |
| 2026-10-03 | Divisão de energia: fonte **360 W → mesa + hotend + motores/placa**; fonte **120 W → ventoinhas/iluminação/aux** (detalhar na fase de eletrônica) | Mesa MK3 12 V puxa ~10–11 A sozinha; 30 A comportam o sistema todo com margem | ✅ Ativa |
| 2026-10-03 | Anel XY com perfis 20×20 de **440 mm** (vão interno 400 mm) — **aprovado para compra** | Comporta 200 mm de curso com folga nos dois eixos; dimensional em [04](04-conceito-novo-gantry.md); lista de compras em [05](05-lista-de-compras.md). **OK do Leandro** | ✅ Ativa |

## Próximos passos

1. **[Leandro]** Fazer o pedido da [lista de compras](05-lista-de-compras.md)
2. **[Claude]** Esqueleto dimensional do gantry (quadro 440, trilhos, blocos de canto, viga X) — gerar STEP de referência para importar no Fusion 360
3. **[Claude]** Levantar STEPs de componentes padrão (NEMA17, perfil 20×20, MGN9, GT2, TinyBee, mesa MK3) para `CAD/componentes/`
4. **[Leandro]** Medições da fase Z/eletrônica ([inventário](01-inventario-componentes.md), seção final) — sem pressa, não bloqueiam o gantry
5. Modelagem das peças impressas (blocos de motor, cantos, carros Y, carro do toolhead) no Fusion 360
