# TAGLINE

模式化的键盘驱动虚拟指针

# TLDR

在后台启动 warpd **守护进程**

```warpd```

以前台方式启动便于调试

```warpd -f```

以 **hint** 模式运行（为屏幕位置加标签）

```warpd --hint```

以 **grid** 模式运行（将屏幕划分为象限）

```warpd --grid```

以 **normal** 模式运行（类似 vi 的光标移动）

```warpd --normal```

以 hint 模式运行并在选择后**退出**（oneshot）

```warpd --hint --oneshot```

**列出**所有可配置选项

```warpd --list-options```

使用自定义**配置**文件

```warpd -c [path/to/config]```

# SYNOPSIS

**warpd** [_OPTIONS_]

# PARAMETERS

**-f**, **--foreground**
> 以前台方式运行（便于调试）。

**-l**, **--list-keys**
> 打印可用作配置值的合法按键列表。

**--list-options**
> 打印所有可配置选项。

**-v**, **--version**
> 显示版本信息。

**-c**, **--config** _file_
> 使用指定的配置文件（用 - 表示 stdin）。

**--hint**
> 以无守护进程的 hint 模式运行。

**--hint2**
> 以两阶段 hint 模式运行。

**--grid**
> 以 grid 模式运行（将屏幕划分为象限进行选择）。

**--normal**
> 以 normal 模式运行（类似 vi 的光标移动）。

**--history**
> 以 history hint 模式运行（在之前选中的目标上显示提示标签）。

**--screen**
> 以屏幕选择模式运行（用于多显示器环境）。

**--oneshot**
> 模式完成后退出，而不是进入 normal 模式。

**--click** _button_
> 发送一次鼠标点击并退出。

**--move** _'x y'_
> 将指针定位到指定坐标。

# KEY BINDINGS

**h**, **j**, **k**, **l**
> 向左、下、上、右移动光标（normal 模式）。

**H**, **M**, **L**
> 跳到屏幕左边缘、中间、右边缘。

**e**, **y**
> 向下滚动、向上滚动。

**m**
> 鼠标左键点击。

**,**
> 鼠标中键点击。

**.**
> 鼠标右键点击。

**n**
> 在 normal 模式中激活 hint 模式。

# DESCRIPTION

**warpd** 是一个模式化的键盘驱动指针操控程序。它提供三种主要模式，让你无需物理鼠标即可移动鼠标光标，交互模型借鉴了 vi。

**Normal 模式**（默认通过 A-M-c 激活）提供类 vi 的 hjkl 光标移动，并支持数字倍数来控制移动距离。**Hint 模式**（A-M-x）在屏幕各位置叠加带标签的提示，键入对应标签即可快速移动指针。**Grid 模式**（A-M-g）将屏幕划分为 2x2 网格，每次选择后递归细分以缩小目标位置范围。

其他模式包括在之前选中目标上显示提示的 **history 模式**，以及在多显示器之间切换的 **screen 模式**。配置通过 `~/.config/warpd/config` 完成。

# CAVEATS

需要 X11 或 Wayland（基于 wlroots 的合成器）。必须运行守护进程激活按键绑定才能生效。按键绑定可能与其他应用冲突。视平台而定，hint 模式可能无法标注所有可点击元素。

# INSTALL

```nix: nix profile install nixpkgs#warpd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdotool](/man/xdotool)(1), [keynav](/man/keynav)(1), [xbindkeys](/man/xbindkeys)(1)
