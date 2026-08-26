# TAGLINE

开源游戏引擎与编辑器

# TLDR

**启动 Godot 编辑器**

```godot```

**打开项目**

```godot --path [project-dir]```

**运行项目**

```godot --path [project-dir] --main-pack [game.pck]```

**导出项目**

```godot --headless --export-release "[preset]" [output]```

**运行脚本**

```godot --script [script.gd]```

# SYNOPSIS

**godot** [_options_] [_scene_]

# PARAMETERS

_SCENE_
> 要打开的场景文件。

**--path** _DIR_
> 项目目录。

**--editor**, **-e**
> 以编辑器模式启动。

**--headless**
> 无窗口模式。

**--export-release** _PRESET_
> 使用指定预设导出。

**--script** _SCRIPT_
> 运行脚本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Godot** 是 Godot 游戏引擎的编辑器与运行时。它提供完整的游戏开发环境，涵盖 2D/3D 渲染、物理、脚本和导出能力。

游戏逻辑可以使用 GDScript、C# 或 C++ 编写，并支持导出到桌面、移动和 Web 平台。无头（headless）模式适用于 CI/CD 流水线的自动化构建与测试。

# CAVEATS

3D 方面对资源消耗较大。GDScript 有一定的学习曲线。面向各平台导出需要相应的导出模板。

# HISTORY

Godot 由 **Juan Linietsky** 与 **Ariel Manzur** 创建，**2014 年**开源，如今已成为广受欢迎的免费游戏引擎。

# INSTALL

```dnf: sudo dnf install godot```

```pacman: sudo pacman -S godot```

```zypper: sudo zypper install godot```

```nix: nix profile install nixpkgs#godot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blender](/man/blender)(1)
