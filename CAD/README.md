# CAD

Modelos do projeto.

- Raiz: montagens e peças (`.f3d` com histórico paramétrico do Fusion 360 + `.step` neutro)
- `componentes/`: STEPs de componentes comprados/padrão (gerados por script — envelopes dimensionais)
- `scripts/`: scripts Python/CadQuery que **geram** o esqueleto e os componentes — ver [Docs/07](../Docs/07-esqueleto-gantry.md) para o sistema de coordenadas e instruções de regeneração

Convenção de nomes: `NN-nome-da-peca_vX.step` (ex.: `10-esqueleto-gantry_v1.step`). O `.f3d` correspondente acompanha a mesma numeração.

Regra de ouro: dimensões "mestras" vivem em [`scripts/parametros.py`](scripts/parametros.py) e no registro de decisões — se mudar uma dimensão de conceito, mudar lá e regenerar.
