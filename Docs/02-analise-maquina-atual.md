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

- O gantry estilo Ultimaker exige largura interna ≈ curso + blocos deslizantes + folgas. Com perfis de **380 mm** o vão interno fica ~340 mm (perfil 20×20), o que é **apertado porém factível** para 200 mm de curso (o Ultimaker Original tinha ~342 mm externo para 210 de curso, mas com painéis de madeira finos, não perfis + cantoneiras externas).
- Decisão chave pendente: **manter os perfis de 380 mm** e otimizar os blocos do gantry, ou **comprar perfis um pouco maiores** (ex.: 420–450 mm) para folga de projeto.
- Curso Z de 200 mm é tranquilo com as torres atuais (perfis de 630 mm dão espaço de sobra para fuso + mesa + base).
- A caixa de eletrônica na base pode ser mantida conceitualmente igual, só redimensionada.
