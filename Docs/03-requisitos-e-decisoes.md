# 03 — Requisitos e registro de decisões

Este documento é a memória viva do projeto. Toda decisão relevante entra na tabela de decisões com data e justificativa. Alterações via commit — o histórico do git é o registro oficial.

## Requisitos

| # | Requisito | Tipo |
|---|---|---|
| R1 | Volume de impressão de 200 × 200 × 200 mm | Obrigatório |
| R2 | Reaproveitar todos os componentes atuais (motores, fusos, guias, eletrônica, fontes, mesa, display, extrusora/hotend) | Obrigatório |
| R3 | Estrutura em perfil de alumínio; estoque atual: 380 mm e 630 mm; compra de perfis adicionais é permitida | Obrigatório |
| R4 | Fixação dos perfis com cantoneiras externas, parafuso M5 + porca T (padrão atual) — pode evoluir se justificado | Desejável |
| R5 | Modelagem completa em Fusion 360, com F3D/STEP versionados no repositório | Obrigatório |
| R6 | Projeto colaborativo: tudo (docs, CAD, decisões, memória) versionado no git | Obrigatório |
| R7 | Peças impressas em 3D fabricáveis na própria máquina atual (bootstrap) | Desejável |
| R8 | Novo roteamento de correias: chegada limpa e direta das correias ao toolhead e ao gantry XY (insatisfação com o esquema atual estilo Ultimaker) | Obrigatório |

## Registro de decisões

| Data | Decisão | Justificativa | Status |
|---|---|---|---|
| 2026-10-03 | Repositório git como fonte de verdade do projeto (docs + CAD exportado + fotos) | Projeto colaborativo; Fusion 360 fica na nuvem Autodesk, mas exportações F3D/STEP são versionadas | ✅ Ativa |
| 2026-10-03 | Fotos originais `.heic` mantidas + conversões `.jpg` (1600 px) para visualização no GitHub | GitHub não renderiza HEIC; JPGs facilitam a colaboração | ✅ Ativa |
| 2026-10-03 | Perfis adicionais podem ser comprados (20×20, mesmo padrão) | Necessário: quadro atual (380 mm) só entrega ~180 mm de curso | ✅ Ativa |
| 2026-10-03 | Fusos Z: **manter os TR8 atuais** | Confirmado que já são trapezoidais TR8 — sem motivo para troca | ✅ Ativa |
| 2026-10-03 | **Cinemática do novo gantry: CoreXY** — correias ancoram direto no carro do toolhead, motores fixos no quadro — ver [04-conceito-novo-gantry.md](04-conceito-novo-gantry.md) | Atende R8; elimina eixos rotativos e correias perimetrais do estilo Ultimaker; reusa os 2 motores XY e polias; Marlin `COREXY` nativo na TinyBee. **Aprovado pelo Leandro** | ✅ Ativa |
| 2026-10-03 | **Viga X = perfil 20×20 + trilho MGN montado nele**; toolhead corre no MGN | Pedido do Leandro (robustez); perfil dá rigidez torcional que barras não dão | ✅ Ativa |
| 2026-10-03 | Trilho MGN na **face frontal** da viga X (não no topo), estilo Voron | Sugestão do Leandro: placa do toolhead plana, CG do cabeçote perto do trilho (menos momento), topo livre p/ esteira — detalhes em [04](04-conceito-novo-gantry.md) | ✅ Ativa |
| 2026-10-03 | ~~Guias Y = 2 barras Ø8×400 com LM8UU~~ | Substituída no mesmo dia ao confirmar que existem 4 trilhos MGN9 | ♻️ Substituída |
| 2026-10-03 | **Guias Y = 2× trilho MGN9 300 mm** parafusados nos perfis laterais; viga X usa o 3º trilho; 4º fica de reserva | **Mantém a solução da máquina atual** (o Y já corre em 1 MGN9 de cada lado; barras lisas só existem no Z); carros Y viram placas simples e dispensa LM8UU | ✅ Ativa |
| 2026-10-03 | **Juntas XY estilo Voron**: polias desviadoras **encapsuladas** dentro das peças que unem a viga X aos carrinhos Y (não expostas no topo) | Pedido do Leandro; protege as polias, alinha os dois planos de correia por construção e enrijece a junta | ✅ Ativa |
| 2026-10-03 | **Ancoragem das correias por ranhuras** na traseira do carro do toolhead (dente da GT2 morde a ranhura impressa), uma por plano de correia | Pedido do Leandro; elimina a peça única "de dois andares", facilita troca de correia e tensionamento | ✅ Ativa |
| 2026-10-03 | **Z estilo Voron Trident nas guias**: 3 guias MGN verticais (2 colunas frontais + 1 central traseira), mesa em 3 pontos; torres atuais com barras Ø8 aposentadas | Pedido do Leandro; conceito detalhado em [06-conceito-z-voron.md](06-conceito-z-voron.md) | ✅ Ativa |
| 2026-10-03 | ~~Acionamento do Z (Opção A): 2 fusos frontais + seguidor passivo~~ | Substituída no mesmo dia: Leandro decidiu comprar placa com mais slots para viabilizar o Trident completo | ♻️ Substituída |
| 2026-10-03 | ~~Nova placa: MKS Monster8 V2~~ | Substituída no mesmo dia: com o firmware fechado em Klipper, o Leandro escolheu a placa com host embutido | ♻️ Substituída |
| 2026-10-03 | **Nova placa: MKS SKIPR** (SoC quad-core com Klipper host embutido + MCU STM32, **7 slots de driver**, entrada 12–24 V); TinyBee vira reserva. **Exceção aprovada ao R2** (reuso total) | Decisão do Leandro; elimina host externo (sem Pi, sem buck 5 V), reusa os 5 drivers atuais; 6 slots usados (X, Y, 3×Z, E) + 1 folga; rede via Ethernet ou dongle WiFi USB | ✅ Ativa |
| 2026-10-03 | **Acionamento do Z: Trident completo — 3 fusos TR8×8×400 com 3 motores independentes** (`G34`/`Z_STEPPER_AUTO_ALIGN` de 3 pontos com BLTouch) | Com a Monster8 há slots de sobra; auto-tram verdadeiro (rolagem + inclinação); requer +1 NEMA17, +1 fuso/castanha/mancal/acoplador e +1 driver | ✅ Ativa |
| 2026-10-03 | **Fusos Z novos: 3× TR8×8 (passo 8) × 400 mm + castanhas de bronze**; apoio em **mancal KP08/KFL08** na base, motor embaixo; TR8 atuais viram reserva | Especificação do Leandro (qtde atualizada de 2→3 com o Trident completo); passo 8 dá Z rápido (400 steps/mm @ 16 µsteps) | ✅ Ativa |
| 2026-10-03 | **Firmware: Klipper** (TinyBee/ESP32 nem roda Klipper). Nivelamento: `Z_TILT_ADJUST` 3 pontos + `BED_MESH_CALIBRATE` com BLTouch. Display MKS TFT atual → reserva (UI = Mainsail/Fluidd no navegador) | Decisão do Leandro — já opera outra RepRap com Klipper; CoreXY + input shaper é o ponto forte do Klipper | ✅ Ativa |
| 2026-10-03 | **Host do Klipper: embutido na MKS SKIPR** | Decisão do Leandro — resolve a decisão aberta de host junto com a placa | ✅ Ativa |
| 2026-10-03 | **Sonda BLTouch** no toolhead | Especificação do Leandro; vidro exige sonda de pino; TinyBee tem porta 3D-Touch; habilita `G34` + `G29` | ✅ Ativa |
| 2026-10-03 | **Hotend novo: V6 com bloco Volcano, 12 V** (cartucho 40 W + termistor) | Especificação do Leandro; substitui o hotend atual; extrusora vermelha direct-drive continua | ✅ Ativa |
| 2026-10-03 | Divisão de energia: fonte **360 W → mesa + hotend + motores/placa**; fonte **120 W → ventoinhas/iluminação/aux** (detalhar na fase de eletrônica) | Mesa MK3 12 V puxa ~10–11 A sozinha; 30 A comportam o sistema todo com margem | ✅ Ativa |
| 2026-10-03 | Anel XY com perfis 20×20 de **440 mm** (vão interno 400 mm) — **aprovado para compra** | Comporta 200 mm de curso com folga nos dois eixos; dimensional em [04](04-conceito-novo-gantry.md); lista de compras em [05](05-lista-de-compras.md). **OK do Leandro** | ✅ Ativa |

## Próximos passos

1. **[Leandro]** Fazer o pedido da [lista de compras](05-lista-de-compras.md) (perfis: **3× 440 + 11× 400** — estoque de 630 confirmado em 4, usados inteiros)
2. **[Leandro]** Abrir `CAD/11-esqueleto-maquina_v1.step` no Fusion 360 e validar ([08](08-esqueleto-maquina.md))
3. Modelagem das peças impressas no Fusion 360, na ordem do [08](08-esqueleto-maquina.md): juntas XY, carro do toolhead (Volcano+BLTouch), blocos de motor, braços da mesa, suportes do deck/baia
4. **[Leandro]** Pendências leves do inventário: etiqueta dos motores, modelo da extrusora, contagem dos perfis 380
