# TAGLINE

验证 HPLIP 的安装和依赖

# TLDR

**检查 HPLIP 状态**

```hp-check```

**自动安装缺失组件**

```hp-check -a```

**修复运行时问题**

```hp-check -r```

**检查特定依赖**

```hp-check -t```

# SYNOPSIS

**hp-check** [_options_]

# PARAMETERS

**-a**, **--auto**
> 自动安装模式。

**-r**, **--runtime**
> 仅检查运行时。

**-t**
> 检查依赖项。

**-f**
> 强制执行所有检查。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hp-check** 验证 HPLIP 的安装和依赖。它检查缺失的软件包、配置问题以及打印机连接状况。

该工具可以在受支持的发行版上自动安装缺失的组件。它有助于诊断和修复打印问题。

# CAVEATS

属于 HPLIP 软件包。修复操作可能需要 root 权限。行为因发行版而异。

# HISTORY

hp-check 是 **HPLIP**（HP Linux Imaging and Printing）的一部分，为 HP 打印机设置提供诊断能力。

# INSTALL

```apt: sudo apt install hplip```

```dnf: sudo dnf install hplip```

```pacman: sudo pacman -S hplip```

```zypper: sudo zypper install hplip```

```nix: nix profile install nixpkgs#hplip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hp-setup](/man/hp-setup)(1), [hp-info](/man/hp-info)(1)
