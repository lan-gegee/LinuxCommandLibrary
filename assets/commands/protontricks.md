# TAGLINE

为 Proton Steam 游戏运行 Winetricks

# TLDR

运行 **GUI**

```protontricks --gui```

为**特定游戏**运行 Winetricks

```protontricks [appid] [winetricks_args]```

在游戏目录中运行**命令**

```protontricks -c "[command]" [appid]```

**列出**已安装的游戏

```protontricks -l```

**搜索**游戏名称

```protontricks -s [game_name]```

在 Proton 环境中**启动**可执行文件

```protontricks-launch --appid [appid] [path/to/file.exe]```

# SYNOPSIS

**protontricks** [**--gui**] [**-l**|**--list**] [**-s** _name_] [**-c** _cmd_] [_appid_] [_args_...]

# PARAMETERS

**--gui**
> 启动图形界面

**-l, --list**
> 列出已安装的 Steam 游戏

**-s, --search _name_**
> 按名称搜索游戏 App ID

**-c, --command _cmd_**
> 在游戏的 Wine prefix 中运行命令

**--no-bwrap**
> 禁用 bubblewrap 沙箱

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**protontricks** 为启用 Proton 的 Steam 游戏运行 Winetricks 命令。它允许向游戏 prefix 安装 Windows 组件、字体和库，以解决兼容性问题。

该工具会自动定位游戏 prefix 并设置正确的 Proton 环境。它适用于通过 Steam 使用 Proton 兼容层安装的游戏。

# CAVEATS

需要 Steam 和 Proton。游戏必须至少运行过一次才会创建 prefix。某些 winetricks 动词可能不适用于所有 Proton 版本。

# HISTORY

**protontricks** 由 **Matoking** 创建，用于衔接 Winetricks 与 Proton，满足在 Proton 游戏 prefix 中安装 Windows 依赖的常见需求。

# INSTALL

```dnf: sudo dnf install protontricks```

```pacman: sudo pacman -S protontricks```

```zypper: sudo zypper install protontricks```

```nix: nix profile install nixpkgs#protontricks```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[winetricks](/man/winetricks)(1), [wine](/man/wine)(1), [steam](/man/steam)(1)
