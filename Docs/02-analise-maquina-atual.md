# 02 — Análise da máquina atual

Baseada nas fotos de 2026-10-03 (`Fotos/jpg/IMG_0317...0328`). A máquina está montada e **funcional**.

## Arquitetura geral

Impressora de pórtico superior **estilo Ultimaker**:

- **XY no topo**: dois eixos cruzados (barras lisas) com o cabeçote na interseção; blocos deslizantes impressos correm em barras no perímetro do quadro superior, acionados por correias GT2. Motores X/Y fixados por baixo dos perfis superiores, nos cantos traseiros (IMG_0328). Há pelo menos um trilho linear MGN complementando o guiamento (IMG_0320/0326).
- **Z**: a mesa desce durante a impressão. Duas torres laterais, cada uma com 1 fuso central + 2 barras lisas; os fusos são acionados por motores no **topo** das torres (IMG_0317). Porcas de bronze nas plataformas (IMG_0325).
- **Cabeçote**: extrusora direct-drive (corpo vermelho) sobre o carro central, hotend para baixo (IMG_0317/0326). Cabos levados por esteira porta-cabos impressa em branco.
- **Mesa**: vidro com clipes sobre plataforma impressa com 4 molas de nivelamento (IMG_0317/0325).
- **Base**: caixa inferior em perfis + chapas perfuradas brancas abrigando as 2 fontes, a MKS TinyBee, o MOSFET da mesa e a distribuição WAGO; 2 ventoinhas no painel frontal (IMG_0321/0322/0323).
- **Estrutura**: perfis de alumínio unidos por placas/cantoneiras impressas externas com M5 + porca T. Display no meio da coluna frontal.

## Pontos fortes (a preservar)

1. **Arquitetura estável**: cabeçote leve no XY, massa da mesa só no Z — bom para velocidade.
2. **Eletrônica moderna**: MKS TinyBee (ESP32) roda Marlin 2.x com WiFi — ótima base.
3. **Caixa de eletrônica separada** na base, com ventilação própria.
4. **Distribuição elétrica organizada** com WAGO e MOSFET externo para a mesa.
5. Estrutura em perfil de alumínio — fácil de redimensionar e expandir.

## Fragilidades observadas (candidatas a melhoria no redesenho)

1. **Peças impressas estruturais grandes** (plataformas do Z, blocos do gantry) — algumas aparentam desgaste/folga; redesenhar com reforço ou substituir por conjuntos mais rígidos.
2. **Fusos Z aparentam ser barra roscada comum** com sinais de oxidação/sujeira (IMG_0323/0324) — se confirmado, considerar limpeza/lubrificação ou upgrade para TR8 (mantendo se o objetivo for custo zero).
3. **Acionamento Z por cima** com fuso longo em balanço embaixo — alinhamento crítico; avaliar mancal inferior.
4. **Cabeamento** parcialmente solto na caixa da base — refazer com canaletas já existentes e identificação.
5. **Hotend envolto em fita** (IMG_0326) — avaliar estado térmico real, silicone sock ou reisolamento.
6. **Tensionamento de correia por esticador simples** — prever tensionadores ajustáveis no redesenho.
7. **Fonte 1 de 120 W (12 V 10 A)**: se a mesa aquecida for 12 V ~10–12 A, a soma com hotend+motores exige as duas fontes bem separadas por função — documentar a divisão atual antes de mexer.

## Implicações para o redesenho 200×200×200

- **O quadro atual não entrega 200 mm**: perfis de 380 mm (20×20) dão vão interno de ~340 mm, e o curso real medido é **~180 mm** — os blocos deslizantes e o carro central do gantry Ultimaker consomem ~160 mm de vão. Para 200 mm de curso será preciso **comprar perfis maiores para o anel XY** e/ou mudar para uma cinemática que consuma menos vão (CoreXY).
- O Leandro quer **mudar o roteamento das correias** (como chegam ao toolhead e ao próprio gantry) — ver [04-conceito-novo-gantry.md](04-conceito-novo-gantry.md).
- Curso Z de 200 mm é tranquilo com as torres atuais (perfis de 630 mm dão espaço de sobra para fuso + mesa + base).
- Mesa MK3 220×220 comporta os 200×200 úteis com margem de 10 mm por lado.
- A caixa de eletrônica na base pode ser mantida conceitualmente igual, só redimensionada.
