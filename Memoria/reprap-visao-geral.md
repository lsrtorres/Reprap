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

**A memória real do projeto vive no repositório** (requisito do Leandro: tudo commitável): `Docs/01-inventario-componentes.md` (inventário + medições pendentes), `Docs/02-analise-maquina-atual.md`, `Docs/03-requisitos-e-decisoes.md` (registro de decisões), `Docs/04-conceito-novo-gantry.md`. Decidido em 2026-10-03: **CoreXY aprovado**; anel XY 440 mm aprovado p/ compra; guias Y = 2× MGN9×300 nos perfis laterais; viga X = perfil 20×20 + MGN9 na face frontal; 4º trilho e barras Ø8×400 de reserva. Lista de compras pronta em `Docs/05-lista-de-compras.md`. Próximo: esqueleto CAD p/ Fusion 360. Sempre ler esses docs no início da sessão e registrar decisões novas lá, com commit.

CAD: Fusion 360 (nuvem Autodesk); exportar .f3d + .step para `CAD/`. Fotos HEIC convertidas para JPG em `Fotos/jpg/` (ImageMagick instalado via winget; HEIC não é legível diretamente). [[leandro-perfil]]
