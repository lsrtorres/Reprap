---
name: reprap-visao-geral
description: "Projeto RepRap 200x200x200 - repo, convencoes e onde esta a memoria real do projeto"
metadata:
  node_type: memory
  type: project
  originSessionId: 7e4093a0-5cda-47a9-a74d-79533ce589c3
  modified: 2026-10-03T14:39:08.445Z
---

Redesenho de impressora RepRap (estilo Ultimaker: XY cruzado no topo, mesa desce no Z) para volume 200×200×200 mm, reaproveitando todos os componentes. Repo local `C:\Reprap` → `https://github.com/lsrtorres/Reprap.git` (branch main, identidade git local: lsrtorres / lsrtorred@gmail.com).

**A memória real do projeto vive no repositório** (requisito do Leandro: tudo commitável): `Docs/01-inventario-componentes.md` (inventário + medições pendentes), `Docs/02-analise-maquina-atual.md`, `Docs/03-requisitos-e-decisoes.md` (registro de decisões), `Docs/04-conceito-novo-gantry.md`. Decidido em 2026-10-03: **CoreXY aprovado** (anel 440 mm; guias Y = MGN9×300 nos laterais; viga X = perfil 20×20 + MGN9 na face frontal; juntas XY estilo Voron com polias encapsuladas; correias ancoram por ranhuras atrás do toolhead). **Z estilo Voron Trident**: 3 guias MGN (2 frontais + 1 central traseira); acionamento proposto = 2 TR8 frontais + seguidor (TinyBee só tem 5 slots de driver — detalhes em `Docs/06`). Z confirmado: **Trident completo** — nova placa **MKS Monster8 V2** (TinyBee vira reserva; exceção ao reuso aprovada), 3× fuso TR8×8×400 + castanhas bronze com 3 motores independentes (G34 3 pontos), mancais KP08/KFL08, motores embaixo, BLTouch; +1 NEMA17 e +1 driver a comprar; hotend novo V6 Volcano 12 V (extrusora vermelha continua). Esqueleto CAD paramétrico em `CAD/scripts/` (CadQuery; venv em `C:\Reprap\.venv`, Python 3.12) gera `CAD/10-esqueleto-gantry_v1.step` com verificação de cursos. Sistema de coordenadas e stack-up em `Docs/07-esqueleto-gantry.md`. Barras Ø8 eram guias do Z atual; serão aposentadas. Sempre ler esses docs no início da sessão e registrar decisões novas lá, com commit.

CAD: Fusion 360 (nuvem Autodesk); exportar .f3d + .step para `CAD/`. Fotos HEIC convertidas para JPG em `Fotos/jpg/` (ImageMagick instalado via winget; HEIC não é legível diretamente). [[leandro-perfil]]
