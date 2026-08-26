# TAGLINE

在 X11 窗口内显示弹跳的线框或实心多面体动画

# TLDR

显示一个会不断变换位置的**线框二十面体**

```ico -sleep [0.1]```

显示带彩色面的**实心**二十面体

```ico -faces -noedges -colors [red] -bg [blue]```

显示指定尺寸和移动增量的**立方体**

```ico -obj cube -size [100x100] -delta +1+2```

显示带线宽和线程数的**反转线框**

```ico -i -lw [10] -threads [5]```

# SYNOPSIS

**ico** [_options_]

# PARAMETERS

**-sleep** _SECONDS_
> 两次位置更新之间的延迟

**-obj** _OBJECT_
> 要显示的多面体（icosahedron、cube、octahedron 等）

**-size** _WxH_
> 多面体的像素尺寸

**-delta** _+X+Y_
> 每帧移动量

**-faces**
> 绘制实心面而非线框

**-noedges**
> 不绘制棱边

**-colors** _COLOR_
> 面或棱边的颜色

**-bg** _COLOR_
> 背景色

**-lw** _WIDTH_
> 线框棱边的线宽

**-i**
> 反转（交换前景色与背景色）

**-threads** _N_
> 渲染线程数

# DESCRIPTION

**ico** 在 X11 窗口内显示弹跳的线框或实心多面体动画。它是一个简单的演示程序，可展示包括二十面体、立方体和八面体在内的多种几何形状。

动画会让多面体在窗口中持续移动并在边缘反弹。各种选项可控制外观、速度和渲染风格。

# CAVEATS

需要 X11 显示服务器。主要用作演示程序，没有实际用途。使用多线程时可能消耗大量 CPU。

# HISTORY

ico 是经典的 X11 演示程序之一，起源于 **20 世纪 80 年代中期** MIT 的 X Window System 早期时代。它作为标准发行版的一部分被收录进 X.Org 发布版。

# INSTALL

```apt: sudo apt install x11-apps```

```zypper: sudo zypper install ico```

```nix: nix profile install nixpkgs#ico```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xeyes](/man/xeyes)(1), [xlogo](/man/xlogo)(1)
