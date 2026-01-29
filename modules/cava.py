import re
from utils.path import CAVA_CONFIG


def apply_cava_palette(palette: dict) -> bool:
    if not CAVA_CONFIG.exists():
        print("Default way of cava config not found!")
        return False

    with CAVA_CONFIG.open("r") as f:
        config_cava = f.read()

    cv = palette["cava"]["color"]
    color_block = f"""\
[color]
background = default
foreground = '{cv["foreground"]}'
gradient = 1
gradient_color_1 = '{cv["gradient_color_1"]}'
gradient_color_2 = '{cv["gradient_color_2"]}'
gradient_color_3 = '{cv["gradient_color_3"]}'
gradient_color_4 = '{cv["gradient_color_4"]}'\n\n"""

    COLOR_BLOCK = re.compile(r"\[color\][\s\S]*?(?=\n\[|\Z)")
    config_cava = COLOR_BLOCK.sub(color_block, config_cava)

    with CAVA_CONFIG.open("w") as f:
        f.write(config_cava)
    return True
