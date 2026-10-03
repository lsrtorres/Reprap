# Projeto RepRap — Redesenho para 200×200×200

Projeto colaborativo de atualização/redesenho de uma impressora 3D RepRap existente (estilo Ultimaker, gantry de eixos cruzados) para um volume de impressão de **200×200×200 mm**, reaproveitando **todos os componentes atuais** (motores, fusos, guias, eletrônica, fontes, mesa, etc.).

## Objetivos

1. Volume de impressão final: **200 × 200 × 200 mm**
2. Reaproveitar todos os componentes existentes (ver [inventário](Docs/01-inventario-componentes.md))
3. Modelagem completa em **Fusion 360**, com exportação de STEP/F3D versionados neste repositório
4. Estrutura em perfil de alumínio (temos perfis de 380 mm e 630 mm; podemos comprar mais)

## Estrutura do repositório

| Pasta | Conteúdo |
|---|---|
| `Docs/` | Documentação: inventário, análise da máquina atual, requisitos e registro de decisões |
| `Fotos/` | Fotos da impressora atual (originais `.heic` + convertidas em `Fotos/jpg/`) |
| `CAD/` | Modelos do Fusion 360 exportados (`.f3d`, `.step`) e STEPs de componentes de terceiros |
| `Firmware/` | Configuração de firmware (Marlin para MKS TinyBee) quando chegarmos nessa fase |

## Documentos principais

- [01 — Inventário de componentes](Docs/01-inventario-componentes.md)
- [02 — Análise da máquina atual](Docs/02-analise-maquina-atual.md)
- [03 — Requisitos e registro de decisões](Docs/03-requisitos-e-decisoes.md)

## Fluxo de trabalho de CAD

O Fusion 360 salva os projetos na nuvem da Autodesk. Para manter o repositório como fonte de verdade colaborativa:

1. Modelar no Fusion 360 normalmente;
2. Ao fechar uma etapa, exportar `.f3d` (com histórico paramétrico) e `.step` (neutro) para `CAD/`;
3. Commitar com mensagem descrevendo a mudança;
4. STEPs de componentes comprados (motores NEMA17, perfis, trilhos MGN, etc.) ficam em `CAD/componentes/`.
