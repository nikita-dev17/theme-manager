import re
import subprocess
from utils.path import SWAY_CONFIG


def apply_sway_palette(palette: dict) -> bool:
    if not SWAY_CONFIG.exists():
        print("Default way of sway config not found!")
        return False

    with SWAY_CONFIG.open("r") as f:
        config_sway = f.read()

    sw = palette["sway"]

    client_block = {
        "client.focused": "focused",
        "client.focused_inactive": "focused_inactive",
        "client.unfocused": "unfocused",
        "client.urgent": "urgent"
    }

    for client_name, palette_key in client_block.items():
        colors = sw[palette_key]

        new_line = f"{client_name}    {colors['border']} {colors['background']} {colors['text']} {colors['indicator']} {colors['child_border']}"
        pattern = re.compile(rf"^{re.escape(client_name)}\s+.*$", re.MULTILINE)
        config_sway = pattern.sub(new_line, config_sway)

    with SWAY_CONFIG.open("w") as f:
        f.write(config_sway)

    subprocess.run(["swaymsg", "reload"])
    return True
