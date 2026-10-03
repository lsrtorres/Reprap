# Firmware — Klipper

Decisão de 2026-10-03 ([registro](../Docs/03-requisitos-e-decisoes.md)): a impressora roda **Klipper**, com a **MKS Monster8 V2** como MCU. O Leandro já opera outra RepRap com Klipper. Host ainda em decisão (2ª instância no host existente / Raspberry Pi / MKS SKIPR).

Esta pasta vai receber o **`printer.cfg`** (versionado — toda mudança de configuração entra por commit) e macros.

## Sementes do printer.cfg (valores já decididos)

| Parâmetro | Valor | Origem |
|---|---|---|
| `kinematics` | `corexy` | [Docs/04](../Docs/04-conceito-novo-gantry.md) |
| `rotation_distance` X/Y | **40** (GT2 2 mm × polia 20T) | polias existentes |
| `rotation_distance` Z (×3) | **8** (TR8×8) | [Docs/06](../Docs/06-conceito-z-voron.md) |
| Steppers | `stepper_x`, `stepper_y`, `stepper_z`, `stepper_z1`, `stepper_z2`, `extruder` | Monster8: 6 de 8 slots |
| `[probe]`/`[bltouch]` | BLTouch | lista de compras item 11 |
| `[z_tilt]` | 3 pontos (2 frontais + 1 central traseiro) — coordenadas sairão do CAD | [Docs/06](../Docs/06-conceito-z-voron.md) |
| `[bed_mesh]` | janela 200×200 centrada em (0, −35) do sistema do anel — mapear p/ coords da mesa | [Docs/07](../Docs/07-esqueleto-gantry.md) |
| Mesa | MK3 12 V via MOSFET externo, termistor 100k | inventário |
| Hotend | V6 Volcano 12 V, 40 W | lista de compras item 16 |
| Extrusora | direct-drive vermelha atual — `rotation_distance` a calibrar | inventário (modelo pendente) |

## Pendências

1. Escolha do host (decide se compramos Pi, usamos o host existente ou SKIPR)
2. Modelo dos drivers atuais (corrente de referência / jumpers de microstep na Monster8)
3. Posições exatas dos 3 fusos para o `[z_tilt]` (sai do CAD do Z)
4. ADXL345 (opcional) para input shaper
