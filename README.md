# Theme Manager

A modular theme manager for Linux desktop environments.

Currently focused on Sway, with plans to support other window managers in the future.

This project applies a selected theme system-wide by synchronizing colors, wallpapers, and configuration files across multiple applications.

---

## Features

- Theme switching based on palettes (TOML) and assets  
- Animated wallpapers (GIF) via swww  
- Waybar color integration via generated `colors.css`  
- Kitty terminal color synchronization  
- Modular architecture (each application is handled by its own module)  
- Automatic user directory setup  

---

## How it works

1. The user selects a theme  
2. Theme data (palette and assets) is copied into user directories  
3. The palette is parsed  
4. Application modules are executed  
5. Each application reloads its configuration and applies new colors  

---

## Project structure

```text
theme-manager/
├── assets/
│   └── themes/          # Theme definitions (wallpapers + palettes)
│
├── modules/             # Application-specific logic
│   ├── sway.py
│   ├── waybar.py
│   ├── kitty.py
│   ├── fastfetch.py
│   ├── cava.py
│   └── wallpaper.py
│
├── utils/               # Helper utilities
│   ├── path.py          # Path constants
│   ├── files.py         # File and directory helpers
│   └── theme.py         # Theme orchestration logic
│
├── main.py              # Entry point
├── pyproject.toml
└── README.md
