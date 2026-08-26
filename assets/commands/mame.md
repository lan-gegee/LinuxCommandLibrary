# TAGLINE

模拟街机游戏硬件

# TLDR

**运行街机 ROM**

```mame [romname]```

**列出可用的游戏**

```mame -listfull```

**以全屏运行**

```mame -window 0 [romname]```

**校验 ROM 集合**

```mame -verifyroms [romname]```

**显示游戏的控制配置**

```mame -listctrl [romname]```

**配置控制**

```mame [romname] -ui_active```

# SYNOPSIS

**mame** [_options_] [_system_] [_media_...]

# PARAMETERS

**-window**
> 以窗口模式（1）或全屏模式（0）运行。

**-listfull**
> 列出所有支持的系统。

**-verifyroms**
> 校验 ROM 完整性。

**-rompath** _path_
> ROM 目录。

**-listctrl**
> 显示控制配置。

**-ui_active**
> 在模拟过程中激活 UI。

**-createconfig**
> 创建默认配置。

# DESCRIPTION

**MAME**（Multiple Arcade Machine Emulator）用于模拟街机游戏硬件。它通过记录和模拟街机来保护游戏历史，让原始软件能够在现代计算机上运行。

MAME 支持数千种街机系统以及部分家用游戏机。

# DIRECTORY STRUCTURE

```
~/.mame/
├── roms/      # Game ROMs
├── cfg/       # Configurations
├── nvram/     # Saved data
└── snap/      # Screenshots
```

# CAVEATS

ROM 必须合法获得。ROM 集合在不同版本之间会有变化。某些游戏需要 CHD 文件。性能因被模拟的系统而异。

# HISTORY

MAME 由 **Nicola Salmoria** 于 **1997 年**发起。2015 年它与 MESS 合并，成为一个同时保护街机和家用系统的通用模拟项目。

# INSTALL

```dnf: sudo dnf install mame```

```pacman: sudo pacman -S mame```

```zypper: sudo zypper install mame```

```brew: brew install mame```

```nix: nix profile install nixpkgs#mame```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[retroarch](/man/retroarch)(1), [dosbox](/man/dosbox)(1)
