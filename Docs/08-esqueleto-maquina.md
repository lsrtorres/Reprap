# 08 — Esqueleto dimensional da máquina completa

Gerado por [`CAD/scripts/esqueleto_maquina.py`](../CAD/scripts/esqueleto_maquina.py), que importa o gantry do script anterior e adiciona o frame vertical e o Z Trident. Saída: **`CAD/11-esqueleto-maquina_v1.step`** (abre direto no Fusion 360). Mesmo sistema de coordenadas do [Docs/07](07-esqueleto-gantry.md) (origem no centro do anel superior, z=0 no topo do anel).

## Arquitetura vertical (de cima para baixo)

| z (mm) | Elemento |
|---|---|
| −20 … 0 | **Anel superior** (2× 440 laterais sobre as colunas + 2× 400 frente/trás) + gantry CoreXY |
| −55 | Ponta do bico (V6 Volcano, estimado) = topo do vidro com a mesa em **home** |
| −50 … −350 | **Trilhos Z** MGN9×300: 2 nas colunas frontais (face interna) + 1 na coluna central traseira |
| −67 … −267 | Topo dos braços da mesa ao longo do curso de **200 mm** |
| −55 … −455 | **Fusos TR8×8 × 400** (3×): sobra +12 mm acima da castanha em home, +168 mm na base |
| −460 … −480 | **Deck** (4× perfil 400 entre colunas): mancais KP08/KFL08 em cima, motores Z pendurados embaixo |
| −480 … −630 | **Baia da eletrônica**: 150 mm internos p/ SKIPR, 2 fontes, MOSFET, WAGOs |
| −630 … −650 | **Anel da base** (4× perfil 400 entre colunas), no chão |
| −650 | Piso |

- **Colunas**: 4× perfil **630 inteiro** nos cantos (do piso até sob o anel superior — estoque confirmado: exatamente 4) + 1 coluna central traseira de **440** (comprada — mesma medida das laterais do anel), do deck ao anel — carrega o 3º trilho Z
- **Mesa**: rígida em 3 pontos (**sem molas** — `z_tilt` + `bed_mesh` substituem o nivelamento manual); vidro 3 + MK3 3 + espaçador 6 + braço 8
- Posições dos fusos: frontais (±180, −195), traseiro (0, +195) — coordenadas que depois alimentam o `[z_tilt]` do Klipper

## Verificações automáticas (o script falha se alguma quebrar)

| Checagem | Resultado |
|---|---|
| Curso XY do bico ≥ 200 | 261,5 mm ✓ (folga +30,8/lado) |
| Fuso cobre a castanha em todo o curso Z | ✓ (+12 topo / +168 base) |
| Carrinho Z dentro do trilho em todo o curso | ✓ (−71…−271 dentro de −69,2…−330,8) |
| Baia ≥ 90 mm p/ fontes | ✓ 150 mm |
| Mesa não colide com colunas | ✓ |

## Lista de corte consolidada (perfis 20×20)

| Origem | Peças |
|---|---|
| **Comprar** | 3× **440** + 11× **400** |
| **Estoque (630)** | 4× inteiros (colunas dos cantos) — sem corte |
| **Estoque (380)** | livres p/ travessas da baia (suportes de fonte/SKIPR) e reforços |

> Único corte de perfil do projeto: a viga X (400 → 340).

## Fluxo com o Fusion 360

O STEP é o formato neutro que o Fusion abre nativamente — **todo o trabalho de modelagem continua no Fusion 360**; os scripts só produzem a referência dimensional:

1. *File → Open* (ou *Insert → Insert CAD*) no `11-esqueleto-maquina_v1.step` — a árvore vem com os componentes **nomeados** (perfis, trilhos, fusos, motores…)
2. `Ground` nos perfis; modelar cada peça impressa como componente novo **referenciando as faces do esqueleto**
3. O STEP não traz histórico paramétrico nem juntas (é geometria estática) — se uma dimensão de conceito mudar, eu altero [`parametros.py`](../CAD/scripts/parametros.py), regenero, e re-importamos a nova versão
4. Peças modeladas voltam ao repositório como F3D + STEP em `CAD/`

## Próximas peças a modelar (Fusion 360)

1. Juntas XY com polias encapsuladas (2×, espelhadas)
2. Carro do toolhead (ranhuras GT2 + V6 Volcano + BLTouch + extrusora vermelha)
3. Blocos dos motores A/B e das polias dianteiras
4. Braços da mesa (3×) com alojamento de castanha e interface MGN9
5. Suportes de mancal/motor Z no deck; suportes da SKIPR/fontes na baia
6. Cantoneiras/uniões dos perfis (padrão M5 + porca T)
