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

## Registro de decisões

| Data | Decisão | Justificativa | Status |
|---|---|---|---|
| 2026-10-03 | Repositório git como fonte de verdade do projeto (docs + CAD exportado + fotos) | Projeto colaborativo; Fusion 360 fica na nuvem Autodesk, mas exportações F3D/STEP são versionadas | ✅ Ativa |
| 2026-10-03 | Fotos originais `.heic` mantidas + conversões `.jpg` (1600 px) para visualização no GitHub | GitHub não renderiza HEIC; JPGs facilitam a colaboração | ✅ Ativa |
| — | Cinemática do redesenho: manter estilo Ultimaker (XY cruzado no topo + mesa descendo em Z) vs migrar p/ CoreXY | A discutir — ambos reaproveitam os mesmos motores/correias; CoreXY simplifica o gantry mas muda as polias/correias | 🔶 Aberta |
| — | Tamanho do quadro XY: manter perfis 380 mm (vão ~340 mm) vs comprar perfis maiores | Depende da medição do gantry atual (largura dos blocos + carro central) — ver pendências do inventário | 🔶 Aberta |
| — | Fusos Z: manter os atuais vs upgrade TR8×8 | Depende de confirmar o que são os atuais (inventário, item 5) | 🔶 Aberta |

## Próximos passos

1. **[Leandro]** Medições pendentes do inventário ([01-inventario-componentes.md](01-inventario-componentes.md), seção final) — paquímetro na mão 🙂
2. **[Claude]** Esboço dimensional do novo quadro (cálculo de cursos vs vãos) assim que as medições chegarem
3. **[Claude]** Levantar STEPs de componentes padrão (NEMA17, perfil 20×20, MGN12, GT2, TinyBee) para `CAD/componentes/`
4. Definir cinemática (decisão aberta acima)
5. Modelagem do quadro no Fusion 360
