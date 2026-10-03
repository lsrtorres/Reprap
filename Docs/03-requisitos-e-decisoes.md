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
| 2026-10-03 | **Guias Y = 2 barras Ø8×400 existentes** com LM8UU | Reuso direto; 400 mm dão curso de sobra; pode migrar p/ MGN no futuro sem mudar o quadro | ✅ Ativa |
| 2026-10-03 | Divisão de energia: fonte **360 W → mesa + hotend + motores/placa**; fonte **120 W → ventoinhas/iluminação/aux** (detalhar na fase de eletrônica) | Mesa MK3 12 V puxa ~10–11 A sozinha; 30 A comportam o sistema todo com margem | ✅ Ativa |
| — | Tamanho do anel XY: proposta = comprar perfis 20×20 de **440 mm** (anel superior; vão interno 400 mm) | Vão de 400 mm recebe as barras Y de 400 mm **sem corte** (parede a parede) e comporta 200 mm de curso com folga; ver dimensional em 04 | 🔶 Proposta |

## Próximos passos

1. **[Leandro]** Confirmar quantidade/comprimento dos trilhos MGN e das barras Ø8 (itens 1–2 do inventário)
2. **[Leandro]** Validar o anel XY de 440 mm (proposta aberta acima) antes de comprar perfis
3. **[Claude]** Lista de corte definitiva + lista de compras final (depende dos itens acima)
4. **[Claude]** Levantar STEPs de componentes padrão (NEMA17, perfil 20×20, MGN9/12, GT2, TinyBee, mesa MK3) para `CAD/componentes/`
5. Modelagem do esqueleto no Fusion 360 (quadro + posições de motores/polias)
