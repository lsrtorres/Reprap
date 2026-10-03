# 09 — Montagem peça a peça no Fusion 360 (juntas + simulação)

Objetivo: montar a impressora no Fusion com componentes reais, **juntas rígidas + sliders**, e testar os movimentos (cursos, colisões) antes de comprar/imprimir qualquer peça.

Sistema de coordenadas: o mesmo de todo o projeto ([07](07-esqueleto-gantry.md)/[08](08-esqueleto-maquina.md)) — origem no centro do anel superior, z=0 no topo do anel, X+ direita, Y+ trás.

## Fluxo de incorporação (upload → inserir, um a um)

1. **Upload**: no Data Panel do Fusion, subir cada `.step` de `CAD/componentes/` (e os de fabricante) para a pasta do projeto — cada um vira um **componente na nuvem com versionamento próprio**;
2. **Inserir**: na montagem, botão direito no item → *Insert into Current Design* — o componente entra **vinculado (X-ref)**;
3. **Posicionar** com *Move/Align* usando a tabela de posições abaixo — ou inserir o `11-esqueleto-maquina_v1.step` como gabarito temporário, dar `Ground`, encaixar as peças nele e depois ocultá-lo/removê-lo;
4. **Atualização**: quando um STEP for regenerado pelos scripts (dimensão de conceito mudou), fazer upload **como nova versão do mesmo item** (mesmo nome, mesma pasta) — o Fusion marca o link como desatualizado na montagem e atualiza com um clique. Por isso os nomes de arquivo são estáveis;
5. Manter o nome do arquivo como nome do componente, para a árvore da montagem bater com os documentos.

## Divisão dos STEPs

### Gerados por script (já em `CAD/componentes/`)

| Arquivo | Peça | Usos |
|---|---|---|
| `perfil-2020-630.step` | coluna | 4× cantos |
| `perfil-2020-440.step` | lateral do anel / coluna Z traseira | 2× + 1× |
| `perfil-2020-400.step` | membro de anel | 10× (2 anel sup. + 4 deck + 4 base) |
| `perfil-2020-340-viga-x.step` | viga X | 1× |
| `mgn9-trilho-300.step` | trilho MGN9 (a "régua", sem carrinho) | 6× (2 Y, 1 X, 3 Z) |
| `fuso-tr8x8-400.step` | fuso TR8×8 (cilindro liso — rosca não modelada) | 3× |
| `nema17.step`, `polia-gt2-20t.step`, `idler-20t.step`, `mesa-mk3-220.step` | placeholders dimensionais | — |

### Você traz do fabricante (STEP comercial)

| Peça | Qtde | Onde achar |
|---|---|---|
| **Carrinho MGN9C** (patins) | 6 | Site da HIWIN (CAD download), TraceParts, GrabCAD |
| **Mancal KP08** (ou KFL08) | 3 | GrabCAD, TraceParts, 3DContentCentral |
| **Castanha T8 flangeada** (bronze) | 3 | GrabCAD ("T8 brass nut") |
| Opcionais p/ realismo: NEMA17, V6 Volcano, BLTouch, SKIPR | — | GrabCAD; a MKS publica desenhos no GitHub (makerbase-mks) |

> Dica: confira se o MGN9C baixado tem **38,5 mm de comprimento × 20 de largura × altura 10 da base do trilho** — é o que o esqueleto assume.

## Posições das peças de fabricante (máquina em **home**)

| Peça | Instâncias | Posição do centro (x, y, z) | Orientação |
|---|---|---|---|
| MGN9C nos trilhos Y | 2 | (−210, 0, topo a z=10) e (+210, 0, idem) | desliza em **Y** |
| MGN9C no trilho X | 1 | (0, −15, 25) | desliza em **X**, montado na face frontal da viga |
| MGN9C nos trilhos Z frontais | 2 | (−210, −195, −71) e (+210, −195, −71) | desliza em **Z**, face p/ trás |
| MGN9C no trilho Z traseiro | 1 | (0, +195, −71) | desliza em **Z**, face p/ frente |
| Castanha T8 | 3 | (−180, −195), (+180, −195), (0, +195) — flange no topo do braço, z = **−67** | eixo vertical |
| Mancal KP08 | 3 | mesmos (x, y) das castanhas, base sobre o deck em z = **−460** | eixo vertical |
| Fuso TR8×8×400 | 3 | mesmos (x, y), de z −455 a −55 | vertical |
| NEMA17 do Z | 3 | mesmos (x, y), corpo de z −524 a −484, eixo p/ cima | na baia, sob o deck |
| NEMA17 A/B | 2 | (−185, +182) e (+185, +182), corpo de z 40 a 80, eixo p/ baixo | cantos traseiros |

## Receita de juntas no Fusion

1. **Rigid Group "frame"**: todos os perfis + trilhos + mancais + motores (tudo que não se move)
2. **Rigid Group "leito"**: mesa + 3 braços + 3 castanhas + 3 carrinhos Z
3. **Sliders** (*Joint → Slider*, usar *As-Built Joint* com a peça já posicionada):
   | Junta | Entre | Eixo | Limites |
   |---|---|---|---|
   | Y-esq / Y-dir | carrinho MGN9C ↔ trilho Y | Y | **±130,75 mm** |
   | X | carrinho MGN9C ↔ trilho X | X | **±130,75 mm** |
   | Z | grupo "leito" ↔ trilho Z (1 slider basta; os outros 2 carrinhos já vão juntos pelo grupo) | Z | **0 a −200** (do home) |
4. **Viga X**: rigid entre viga + juntas XY + os 2 carrinhos Y (ela acompanha o Y e carrega o trilho X)
5. **Fusos (opcional, bonito na simulação)**: *Revolute* fuso↔mancal + **Motion Link** revolute↔slider Z com **8 mm por volta** (passo do TR8×8)
6. **Colisões**: *Assemble → Enable Contact Sets* nos pares críticos (mesa × colunas, juntas XY × cantos) e arrastar as juntas pelos limites

> **Nota CoreXY**: a cinemática real (ΔA=ΔX+ΔY etc.) vem das correias, que não são modeláveis como junta no Fusion. Para validar cursos e colisões, os dois sliders independentes (X e Y) são exatamente equivalentes — o que a correia muda é *quem* gira, não *onde* o carro chega.

## Checagens que a simulação deve confirmar

- [ ] Bico varre 200×200 centrado em (0, −35) sem a junta XY tocar os cantos
- [ ] Mesa desce 200 sem tocar deck/mancais (fim de curso do braço em z −267; mancal a −460 ✓ folga ~190)
- [ ] Esteira porta-cabos e cabos do toolhead (quando modelados) não interferem no curso Y
- [ ] Castanha nunca alcança a ponta do fuso (+12 mm de sobra no topo em home)
