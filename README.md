# Serum Ferritin & Transferrin Saturation Iron Overload Sentinel Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `screen_iron_overload_ferroptosis`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Calculates Transferrin Saturation (TSAT %), serum ferritin accumulation, Fenton reaction hydroxyl radical generation propensity, and flags HFE C282Y hemochromatosis risks.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Fenton Reaction & Ferroptosis)`

## MCP Tool Specification
### `screen_iron_overload_ferroptosis`
Parameters:
- `serum_ferritin_ng_ml` (float): Serum ferritin concentration (ng/mL)
- `serum_iron_ug_dl` (float): Total serum iron (ug/dL)
- `total_iron_binding_capacity_tibc` (float): Total Iron Binding Capacity (ug/dL)
- `is_male` (bool): Biological sex

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-blood-ferritin-iron-overload-hemochromatosis-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-blood-ferritin-iron-overload-hemochromatosis-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
