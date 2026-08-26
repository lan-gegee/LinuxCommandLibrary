# TAGLINE

面向运行 X11 的 Linux 系统的屏幕亮度和色温管理器

# TLDR

**启动 gummy 守护进程**（调整生效前必须先运行）

```gummy start```

在所有屏幕上将**色温**设为 3400K

```gummy -t [3400]```

在指定屏幕上将**亮度**设为 60%

```gummy -b [60] -s [1]```

**启用基于屏幕内容的自动亮度**

```gummy -B [1]```

**启用自动色温**并设置日出/日落时间

```gummy -T [1] -y [06:00] -u [16:30]```

在指定屏幕上**禁用自动亮度**

```gummy -B [0] -s [1]```

# SYNOPSIS

**gummy** **start**

**gummy** [_options_]

# PARAMETERS

**start**
> 启动 gummy 后台守护进程，用于应用亮度/色温调整。

**-t** _KELVIN_
> 手动设置屏幕色温。

**-T** _0|1_
> 切换是否基于日出/日落时间自动调整色温。

**-b** _PERCENT_
> 手动设置屏幕亮度。

**-B** _0|1|2_
> 切换自动亮度：0 = 关闭，1 = 基于捕获的屏幕内容，2 = 基于环境光传感器（如果可用）。

**-y** _HH:MM_
> 设置自动色温所使用的日出时间。

**-u** _HH:MM_
> 设置自动色温所使用的日落时间。

**-s** _NUMBER_
> 将给定选项应用于特定屏幕（从 0 开始编号）而非所有屏幕。

**-h**
> 打印帮助信息。

# DESCRIPTION

**gummy** 是一款面向 X11 的命令行屏幕管理器，可以自动或手动地按屏幕或全局调整亮度和色温。亮度通过 gamma（在受支持的嵌入式显示器上还包括背光）来调节，而色温调节会减少蓝光，以减轻夜间用眼疲劳。

自动亮度既可以跟随捕获的屏幕内容（根据当前显示的内容估算环境亮度），也可以使用环境光传感器（如果存在）。自动色温遵循可配置的日出/日落时间。无论是自动模式还是让更改持久生效，都必须运行 **gummy start** 守护进程。

# CAVEATS

需要 X11；在 Wayland 下无法工作。上游 `Fushko/gummy` 仓库已在 GitHub 上不可用；`Gitoffthelawn/gummy` 等 fork/镜像延续了该代码。另有独立的配置图形界面 **gummy-conf**，适合不想直接使用 CLI 的用户。

# HISTORY

**gummy** 由 **Francesco Fusco** 创建，是一款轻量级、基于守护进程的工具，用于在 Linux/X11 上管理屏幕亮度和色温，是 Redshift 类工具的替代品。

# INSTALL

```nix: nix profile install nixpkgs#gummy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[redshift](/man/redshift)(1), [xrandr](/man/xrandr)(1), [brightnessctl](/man/brightnessctl)(1)

# RESOURCES

```[Source code](https://github.com/Gitoffthelawn/gummy)```

<!-- verified: 2026-07-17 -->
