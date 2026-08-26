# TAGLINE

显示 X Window System 标志

# TLDR

**显示 X 标志**

```xlogo```

**以抗锯齿渲染显示**

```xlogo -render```

**以异形（非矩形）窗口显示**

```xlogo -shape```

**使用自定义颜色显示**

```xlogo -fg [blue] -bg [white]```

**以指定几何尺寸显示**

```xlogo -geometry [200x200+100+100]```

**在远程显示器上显示**

```xlogo -display [hostname:0]```

# SYNOPSIS

**xlogo** [_options_]

# PARAMETERS

**-render**
> 使用 RENDER 扩展实现抗锯齿边缘。

**-sharp**
> 与 -render 一起使用时，强制锐利边缘（1 位 alpha 通道）。

**-shape**
> 使用非矩形的窗口形状。

**-fg** _color_
> 前景色（标志颜色）。

**-bg** _color_
> 背景色。

**-geometry** _geom_
> 窗口大小和位置。

**-display** _name_
> 要使用的 X 显示器。

# DESCRIPTION

**xlogo** 在窗口中显示 X Window System 标志。它是一个极简的 X11 应用，主要用于测试 X server 连接性以及验证显示转发是否正常工作。

该程序相当于 X11 的 "hello world"，适合快速测试 X 是否正在运行且可访问。如果 xlogo 无法打开，则说明 X server、DISPLAY 变量或网络配置存在问题。

使用 -render 时，标志会采用抗锯齿边缘，外观更平滑。-shape 选项创建一个与标志轮廓一致的窗口，而不是矩形窗口。

# CAVEATS

设计上功能极简。需要正在运行的 X server 和正确的 DISPLAY 设置。属于老旧应用；现代测试可能采用其他方法。

# HISTORY

**xlogo** 自早期起就是 X Window System 的一部分，为 X server 功能提供简单的可视化测试。尽管简单，它在基本的 X11 连接性测试和 X11 概念演示方面仍然有用。

# INSTALL

```apt: sudo apt install x11-apps```

```dnf: sudo dnf install xlogo```

```zypper: sudo zypper install xlogo```

```nix: nix profile install nixpkgs#xlogo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xeyes](/man/xeyes)(1), [xclock](/man/xclock)(1), [xterm](/man/xterm)(1), [xdpyinfo](/man/xdpyinfo)(1)
