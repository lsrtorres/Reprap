# 07 — Esqueleto dimensional do gantry (CAD de referência)

Gerado programaticamente por [`CAD/scripts/esqueleto_gantry.py`](../CAD/scripts/esqueleto_gantry.py) (CadQuery/Python — paramétrico e versionado). Saídas:

- **`CAD/10-esqueleto-gantry_v1.step`** — montagem de referência do gantry CoreXY
- **`CAD/componentes/*.step`** — componentes padrão individuais (perfis, MGN9, NEMA17, polias, mesa MK3)

Os modelos são **envelopes dimensionais** (seções, cursos e interfaces corretos), não cosméticos. Servem de referência de posição para modelar as peças impressas por cima, no Fusion 360.

## Sistema de coordenadas (adotar o mesmo no Fusion!)

- **Origem**: centro do anel XY superior, em planta
- **Z = 0** no **topo** do anel superior; Z+ para cima
- **X+** para a direita; **Y+** para trás

## Empilhamento vertical (stack-up)

| z (mm) | O que está lá |
|---|---|
| −20 … 0 | Anel superior (perfis 20×20: laterais 440, frente/trás 400) |
| 0 … 6,5 | Trilhos MGN9×300 do Y (sobre os perfis laterais, centrados em y=0) |
| 0 … 10 | Carrinhos MGN9 do Y (topo em z=10) |
| 10 … 48 | **Juntas XY** (caixa âmbar translúcida no STEP — as polias desviadoras ficam **dentro** delas) |
| 15 … 35 | Viga X (perfil 20×20 × **340 mm**, entre as faces internas das juntas em x=±175, folga 5 mm/lado) |
| 17 … 23 | **Plano de correia B** (inferior) |
| 27 … 33 | **Plano de correia A** (superior) |
| — | Trilho MGN9×300 do X na **face frontal** da viga (y −10 … −16,5); carrinho até y=−20; placa do toolhead y −20 … −24 |

## Posições-chave (em planta)

| Elemento | Posição |
|---|---|
| Centros dos perfis laterais / trilhos Y | x = ±210 |
| Motores A (esq.) e B (dir.) | (±185, +182), corpo acima, eixo p/ baixo, polia 20T no plano da sua correia |
| Polias desviadoras dianteiras | (±185, −185), uma por plano em cada canto |
| Faces internas das juntas XY | x = ±175 |
| **Bico** (marcador vermelho) | offset de **−35 mm em Y** do centro da viga |
| **Centro útil da mesa** | **(0, −35)** — a mesa fica deslocada 35 mm para a frente do centro do anel |

## Verificação de cursos (impressa pelo script a cada execução)

| Grandeza | Valor | Requisito |
|---|---|---|
| Curso X do bico | **261,5 mm** (±130,8) | 200 ✓ (folga +30,8/lado) |
| Curso Y do bico | **261,5 mm** (−165,8 … +95,8) | 200 ✓ (folga +30,8/lado) |
| Janela 200×200 centrada em (0, −35) | coberta | ✓ |
| Correia por loop | ~2,17 m (2 loops ≈ 4,35 m) | rolo de 5 m ✓ |

> O offset de −35 do bico é **estimado** (espessura da placa + corpo do hotend). Quando o toolhead real for modelado, atualizar `BICO_OFFSET_Y` em [`parametros.py`](../CAD/scripts/parametros.py) e rodar o script de novo — as asserções garantem que os 200×200 continuam cobertos.

## Como regenerar / usar

```powershell
# uma vez por máquina:
py -3.12 -m venv C:\Reprap\.venv
C:\Reprap\.venv\Scripts\pip install -r C:\Reprap\CAD\scripts\requirements.txt

# gerar (de dentro de CAD/scripts/):
C:\Reprap\.venv\Scripts\python.exe esqueleto_gantry.py
```

**No Fusion 360**: `File → Open → selecionar o .step` (ou *Insert → Insert CAD*). Fixar (`Ground`) os perfis do anel e modelar as peças impressas referenciando as faces do esqueleto. Exportar os resultados (F3D+STEP) de volta para `CAD/`.

## O que o esqueleto ainda NÃO contém (próximas iterações)

1. Colunas verticais, anel da base e coluna central traseira do Z (depende da aprovação da Opção A de acionamento — [06](06-conceito-z-voron.md))
2. Polias internas das juntas XY e trajeto fino das correias (fase de detalhamento das peças impressas)
3. Toolhead real (extrusora vermelha + hotend) — falta identificar os modelos ([inventário](01-inventario-componentes.md))
