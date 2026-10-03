# 10 — Roteiro Fusion, Fase 1: o frame (16 perfis)

Companheiro do [09](09-montagem-fusion.md). Método: usar o **esqueleto como gabarito** e encaixar cada componente nele com *Point to Point* — zero digitação de coordenada, precisão total.

## Fase 0 — Projeto e uploads

1. Data Panel → **New Project**: `Reprap`; dentro dele, pasta `componentes`
2. Upload para `componentes/`: `perfil-2020-630.step`, `perfil-2020-440.step`, `perfil-2020-400.step` (os 3 bastam p/ a Fase 1)
3. Upload na raiz do projeto: `11-esqueleto-maquina_v1.step` (o gabarito)
4. Aguardar o processamento de cada upload terminar (ícone pára de girar)

## Fase 1 — Montagem do frame

### Preparação

1. **New Design**, salvar como `montagem-reprap` (unidades: mm — padrão)
2. Inserir o gabarito: botão direito em `11-esqueleto-maquina_v1` → *Insert into Current Design* → **OK sem mover nada**
3. Botão direito no gabarito na árvore → **Ground**. Renomear para `GABARITO`

### Encaixe de cada perfil (receita de 2 passos)

Para cada linha da tabela abaixo:

1. *Insert into Current Design* no perfil indicado → OK (ele cai na origem)
2. **Se a tabela pedir rotação**: `M` (Move/Copy) → *Components* → girar **90° no eixo indicado** (o pivô não importa — o passo 3 corrige a posição)
3. `M` → *Move Type: **Point to Point*** → clicar num **vértice de canto** do perfil inserido → clicar no **vértice correspondente** do membro homônimo do GABARITO. Pronto: encaixado com exatidão
4. Renomear a instância na árvore com o nome da tabela

| Ordem | Componente | Instância (nome) | Rotação | Onde encaixa (membro do gabarito) |
|---|---|---|---|---|
| 1–4 | `perfil-2020-630` | `coluna-0..3` | nenhuma (já é vertical) | 4 colunas dos cantos |
| 5–6 | `perfil-2020-400` | `base-lateral-esq/dir` | **90° em X** | anel da base, laterais |
| 7–8 | `perfil-2020-400` | `base-frente/tras` | **90° em Y** | anel da base, frente e trás |
| 9–10 | `perfil-2020-400` | `deck-lateral-esq/dir` | **90° em X** | deck, laterais |
| 11–12 | `perfil-2020-400` | `deck-frente/tras` | **90° em Y** | deck, frente e trás |
| 13–14 | `perfil-2020-440` | `perfil-esq/dir` | **90° em X** | anel superior, laterais (sobre as colunas) |
| 15–16 | `perfil-2020-400` | `perfil-frente/tras` | **90° em Y** | anel superior, frente e trás |
| 17 | `perfil-2020-440` | `coluna-z-tras` | nenhuma | coluna central traseira (do deck ao anel) |

> Regra de bolso da rotação: membro que corre na direção **Y** (laterais) → girar em **X**; membro que corre em **X** (frente/trás) → girar em **Y**. O perfil é simétrico, o sinal do giro não importa.

### Espans de referência (conferência, se quiser medir)

| Grupo | Ocupação |
|---|---|
| Colunas | (x, y) = (±210 ± 10), z −650 … −20 |
| Anel base | z −650 … −630 |
| Deck | z −480 … −460 |
| Anel superior | z −20 … 0 (laterais de 440 cobrem y −220 … +220) |
| Coluna Z traseira | (0 ± 10, 210 ± 10), z −460 … −20 |

### Fechamento da fase

1. Selecionar os 17 componentes (não o GABARITO) → botão direito → **Rigid Group** → nomear `frame`
2. **Ground** num deles (o grupo todo trava)
3. Ocultar o `GABARITO` (olhinho na árvore) — **não apagar**: ele guia as fases 2 (trilhos + gantry) e 3 (Z + mesa)
4. Conferir com *Inspect → Measure*: externo 440 × 440, altura total 650 do piso ao topo do anel

### Resultado esperado

Frame completo: 4 colunas + 3 anéis (base, deck, superior) + coluna Z traseira — idêntico ao gabarito, mas com cada perfil sendo um componente X-ref independente, pronto para receber trilhos e juntas na Fase 2.
