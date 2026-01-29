import json
from utils.path import FASTFETCH_CONFIG


def apply_fastfetch_palette(palette: dict) -> bool:
    if not FASTFETCH_CONFIG.exists():
        print("Default way of fastfetch config not found!")
        return False

    with FASTFETCH_CONFIG.open("r") as f:
        config_fastfetch = json.load(f)

    ff = palette["fastfetch"]

    # logo
    config_fastfetch["logo"]["color"]["1"] = ff["logo"]["primary"]
    config_fastfetch["logo"]["color"]["2"] = ff["logo"]["secondary"]

    # percent
    config_fastfetch["percent"]["color"]["green"] = ff["percent"]["green"]
    config_fastfetch["percent"]["color"]["yellow"] = ff["percent"]["yellow"]
    config_fastfetch["percent"]["color"]["red"] = ff["percent"]["red"]

    # modules
    for module in config_fastfetch["modules"]:
        module_type = module.get("type")
        if module_type in ff['key']:
            module["keyColor"] = ff["key"][module_type]
        if module_type == "custom":
            module["outputColor"] = ff["separator"]["line"]

    with FASTFETCH_CONFIG.open("w") as f:
        json.dump(config_fastfetch, f, indent=2, ensure_ascii=False)
    return True
