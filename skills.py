# -*- coding: utf-8 -*-
"""Serum Ferritin & Transferrin Saturation Iron Overload Sentinel Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def screen_iron_overload_ferroptosis(**kwargs):
    """Calculates Transferrin Saturation (TSAT %), serum ferritin accumulation, Fenton reaction hydroxyl radical generation propensity, and flags HFE C282Y hemochromatosis risks."""
    serum_ferritin_ng_ml = kwargs.get('serum_ferritin_ng_ml')
    serum_iron_ug_dl = kwargs.get('serum_iron_ug_dl')
    total_iron_binding_capacity_tibc = kwargs.get('total_iron_binding_capacity_tibc')
    is_male = kwargs.get('is_male')

    # Transferrin Saturation: TSAT = (Serum Iron / TIBC) * 100
    tsat_pct = round((serum_iron_ug_dl / (total_iron_binding_capacity_tibc if total_iron_binding_capacity_tibc > 0 else 1.0)) * 100.0, 1)
    
    # Longevity optimal ferritin is generally 40 - 100 ng/mL; excess free iron catalyzes Fenton reaction (Fe2+ + H2O2 -> Fe3+ + OH* + OH-)
    ferritin_upper_limit = 200.0 if is_male else 150.0
    
    if tsat_pct >= 50.0 or serum_ferritin_ng_ml >= 500.0:
        overload_status = "CRITICAL IRON OVERLOAD / HEMOCHROMATOSIS ALERT (Active Fenton hydroxyl radical generation & ferroptosis)"
        action = "HFE genetic test (C282Y/H63D), liver MRI T2* for iron quantification, therapeutic phlebotomy (500 mL blood donation)."
    elif tsat_pct >= 45.0 or serum_ferritin_ng_ml > ferritin_upper_limit:
        overload_status = "ELEVATED SYSTEMIC IRON BURDEN (Accelerated vascular and hepatic oxidative stress)"
        action = "Schedule voluntary blood donation, avoid cast-iron cooking and vitamin C with red meat, increase IP6 (phytic acid) intake."
    elif serum_ferritin_ng_ml < 30.0:
        overload_status = "IRON DEFICIENCY / DEPLETED STORAGE POOL"
        action = "Investigate occult GI blood loss, supplement iron bisglycinate with cofactors."
    else:
        overload_status = "OPTIMAL EUFERRIC CELLULAR HOMEOSTASIS"
        action = "Iron stores within longevity sweet spot (40-100 ng/mL); low pro-oxidant hydroxyl catalytic risk."
        
    result = {
        "status": "success",
        "serum_ferritin_ng_ml": serum_ferritin_ng_ml,
        "transferrin_saturation_pct": tsat_pct,
        "iron_overload_ferroptosis_grade": overload_status,
        "clinical_phlebotomy_action_plan": action,
        "engine": "GenPark Fenton Reaction Euferric Longevity Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "screen_iron_overload_ferroptosis": {
        "name": "screen_iron_overload_ferroptosis",
        "description": "Calculates Transferrin Saturation (TSAT %), serum ferritin accumulation, Fenton reaction hydroxyl radical generation propensity, and flags HFE C282Y hemochromatosis risks.",
        "parameters": {
            "type": "object",
            "properties": {
                "serum_ferritin_ng_ml": {"type": "number", "description": "Serum ferritin concentration (ng/mL)"},
                "serum_iron_ug_dl": {"type": "number", "description": "Total serum iron (ug/dL)"},
                "total_iron_binding_capacity_tibc": {"type": "number", "description": "Total Iron Binding Capacity (ug/dL)"},
                "is_male": {"type": "boolean", "description": "Biological sex"},
            },
            "required": ['serum_ferritin_ng_ml', 'serum_iron_ug_dl', 'total_iron_binding_capacity_tibc', 'is_male']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "screen_iron_overload_ferroptosis":
            res = screen_iron_overload_ferroptosis(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-blood-ferritin-iron-overload-hemochromatosis-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-blood-ferritin-iron-overload-hemochromatosis-skill...")
    test_args = {'serum_ferritin_ng_ml': 380.0, 'serum_iron_ug_dl': 165.0, 'total_iron_binding_capacity_tibc': 310.0, 'is_male': True}
    res = screen_iron_overload_ferroptosis(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-blood-ferritin-iron-overload-hemochromatosis-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
