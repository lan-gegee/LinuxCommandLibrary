# TAGLINE

用于管理 X 下多显示器布局的 POSIX 兼容 shell 脚本

# TLDR

只启用**主显示器**

```mons -o```

只启用**副显示器**

```mons -s```

将主显示器**复制**到副显示器（主显示器分辨率）

```mons -d```

将主显示器**镜像**到副显示器（副显示器分辨率）

```mons -m```

向右**扩展**主显示器

```mons -e right```

**列出**已连接的显示器

```mons```

按 ID 启用**特定显示器**

```mons -O [id]```

# SYNOPSIS

**mons** [**-o**] [**-s**] [**-d**] [**-m**] [**-e** _side_] [**-O** _id_] [**-S** _id1,id2:pos_] [**--dpi** _value_]

# PARAMETERS

**-o**
> 只启用主显示器

**-s**
> 只启用副显示器

**-d**
> 将主显示器的输出复制到副显示器

**-m**
> 将主显示器的画面镜像到副显示器

**-e _side_**
> 扩展主显示器；side：top、left、right、bottom

**-n _side_**
> 依次循环切换显示模式

**-O _id_**
> 按标识符启用特定显示器

**-S _id1,id2:pos_**
> 启用两个特定显示器；pos：R（右侧）、T（顶部）

**-a**
> 守护进程模式；显示器变化时自动启用屏幕

**-x _script_**
> 显示器数量变化时执行自定义脚本

**--dpi _value_**
> 设置显示 DPI（范围 0-27432）

**--primary _name_**
> 指定主输出显示器

**-h**
> 显示帮助

**-v**
> 显示版本

# DESCRIPTION

**mons** 是一个 POSIX 兼容的 shell 脚本，用于管理 X Window System 上的多显示器布局。它无需大量依赖即可简化显示配置之间的切换。

该工具封装了 xrandr，为常见的双显示器设置提供直观的命令：仅主屏、仅副屏、复制、镜像和扩展模式。它支持守护进程模式，在显示器接入或断开时自动管理显示配置。

# CAVEATS

需要 X Window System 和 xrandr。不适用于 Wayland 合成器。仅限于 xrandr 支持的配置。副显示器由连接顺序决定；使用多显示器时请用 -O 或 -S 显式控制。

# HISTORY

**mons** 由 **Thomas� Venturini**（Ventto）开发，是图形化显示配置工具之外的轻量选择。它为常见的多显示器操作提供了极简、可脚本化的接口。

# INSTALL

```nix: nix profile install nixpkgs#mons```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xrandr](/man/xrandr)(1), [autorandr](/man/autorandr)(1), [arandr](/man/arandr)(1)
