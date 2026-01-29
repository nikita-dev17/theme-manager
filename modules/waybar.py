import subprocess
from utils.path import COLOR_CSS


def apply_waybar_palette(palette: dict) -> bool:
    if not COLOR_CSS.exists():
        print("Default way of color.css not found!")
        return False

    wb = palette["waybar"]

    generate_block = f"""\
@define-color window_bg         {wb["base"]["window_bg"]};
@define-color module_bg         {wb["base"]["module_bg"]};
@define-color module_border     {wb["base"]["module_border"]};

@define-color module_fg         {wb["text"]["module_fg"]};
@define-color muted_fg          {wb["text"]["muted_fg"]};

@define-color wspace_btn_fg     {wb["workspace"]["wspace_btn_fg"]};
@define-color wspace_btn_f_bg   {wb["workspace"]["wspace_btn_f_bg"]};
@define-color wspace_btn_f_fg   {wb["workspace"]["wspace_btn_f_fg"]};
@define-color wspace_btn_hvr_bg {wb["workspace"]["wspace_btn_hvr_bg"]};
@define-color wspace_btn_hvr_fg {wb["workspace"]["wspace_btn_hvr_fg"]};

@define-color module_hvr        {wb["accent"]["module_hvr"]};"""

    with COLOR_CSS.open("w") as f:
        f.write(generate_block)

    cmd = (
        "pkill waybar; "
        "waybar -c ~/.config/waybar/sway/config.json "
        "-s ~/.config/waybar/sway/style.css "
        "> /dev/null 2>&1 & disown"
    )

    subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
    )
    return True
