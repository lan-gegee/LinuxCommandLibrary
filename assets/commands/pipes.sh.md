# TAGLINE

动画管道终端屏保

# TLDR

**运行管道动画**

```pipes.sh```

**设置管道数量**

```pipes.sh -p [5]```

**设置帧率**（默认：75）

```pipes.sh -f [75]```

**设置管道颜色**（0-7，可指定多个）

```pipes.sh -c 1 2 3```

**设置管道样式**（0=heavy，1=arc，2=light，3=double，4=ASCII）

```pipes.sh -t [0]```

**不使用粗体颜色**

```pipes.sh -B```

**重置屏幕**

```pipes.sh -r [2000]```

# SYNOPSIS

**pipes.sh** [_options_...]

# PARAMETERS

**-p** _N_
> 管道数量（默认：1）。

**-f** _FPS_
> 帧率（默认：75）。

**-c** _COLOR_
> 管道颜色，以空格分隔的 0-7 值（默认：1 2 3 4 5 6 7 0）。

**-t** _TYPE_
> 管道样式：0=heavy、1=arc、2=light、3=double、4=ASCII 制表符、5=slashes、6=dots、7=circles、8=railway、9=knobby。

**-s** _N_
> 直角接头的概率，5-15（默认：13）。

**-r** _LIMIT_
> 绘制 LIMIT 个字符后重置屏幕（默认：2000）。

**-R**
> 随机化起始位置和方向。

**-B**
> 禁用粗体效果。

**-C**
> 禁用颜色。

**-K**
> 触碰屏幕边缘时不改变颜色和样式。

**-v**
> 打印版本号。

**-h**
> 显示帮助。

# DESCRIPTION

**pipes.sh** 在终端中展示不断生长的动画管道，效果类似屏保。管道从屏幕边缘出发，向随机方向延伸并随机转弯，形成日益复杂的图案。

多条管道可以同时运行，各自使用不同的颜色。多种字符集提供了不同的视觉风格，从简单的 ASCII 制表符到 Unicode 方块字符。颜色模式从单色到完整的彩虹循环不等。

帧率参数控制动画的流畅度和 CPU 占用。周期性重置会清空屏幕，防止累积的管道轨迹造成视觉混乱。

# CAVEATS

CPU 占用随管道数量增加而上升。终端必须支持 ANSI 颜色。在大尺寸终端中效果最佳。

# HISTORY

**pipes.sh** 是经典"管道"屏保效果的 bash 实现，已成为流行的终端娱乐和桌面装饰脚本。

# INSTALL

```aur: yay -S pipes.sh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmatrix](/man/cmatrix)(1), [sl](/man/sl)(1), [asciiquarium](/man/asciiquarium)(1)
