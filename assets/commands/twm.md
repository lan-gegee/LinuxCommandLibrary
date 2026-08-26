# TAGLINE

经典的 X11 Tab 窗口管理器

# TLDR

**启动窗口管理器**

```twm```

**指定显示器**

```twm -display [localhost:0]```

**详细模式**

```twm -v```

**单屏幕模式**

```twm -s```

# SYNOPSIS

**twm** [_-display dpy_] [_-v_] [_-s_] [_options_]

# PARAMETERS

**-display** _DPY_
> 要使用的 X display。

**-v**
> 详细模式。

**-s**
> 单屏幕模式。

**-f** _FILE_
> 配置文件。

# DESCRIPTION

**twm**（Tab Window Manager）是 X Window System 的一个极简窗口管理器。它提供基本的窗口管理功能，包括标题栏、边框、窗口大小调整和图标化，同时内存占用很小。

该窗口管理器可通过 **~/.twmrc** 配置文件高度定制，其中定义了按键绑定、菜单、标题栏按钮和窗口外观。它支持虚拟屏幕来组织工作区。

作为标准 X.Org 发行版的一部分，twm 在没有配置其他窗口管理器时充当后备选择。它的极简特性使其适合资源受限的环境，也可作为理解 X11 窗口管理的基础。

# CONFIGURATION

**~/.twmrc**
> 主配置文件，定义按键绑定、菜单、标题栏按钮、颜色和窗口行为。

# CAVEATS

非常简陋。没有现代功能。属于传统 X11 组件。

# HISTORY

**twm**（Tab Window Manager）曾是 X11 的默认窗口管理器，由 Tom LaStrange 于 1987 年创建。

# INSTALL

```apt: sudo apt install twm```

```apk: sudo apk add twm```

```zypper: sudo zypper install twm```

```brew: brew install twm```

```nix: nix profile install nixpkgs#twm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fvwm](/man/fvwm)(1), [i3](/man/i3)(1), [openbox](/man/openbox)(1)
