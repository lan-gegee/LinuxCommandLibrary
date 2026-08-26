# TAGLINE

X11 合成窗口管理器

# TLDR

**以默认设置启动**（阴影和渐变）

```xcompmgr```

**启用阴影**并使用自定义偏移和不透明度

```xcompmgr -c -l [left_offset] -t [top_offset] -o [opacity]```

**启用阴影和渐变**并设置过渡步长

```xcompmgr -cCfF -D [fade_time_ms]```

**仅启用**窗口状态间的**渐变效果**

```xcompmgr -fF```

**以更柔和的阴影运行**（更大的半径、更透明）

```xcompmgr -c -r [shadow_radius] -o [0.5]```

**在 dock 和面板窗口上禁用阴影**

```xcompmgr -c -n```

# SYNOPSIS

**xcompmgr** [_-d display_] [_-r radius_] [_-o opacity_] [_-l left_] [_-t top_] [_-cCfFnsSdD_]

# PARAMETERS

**-d** _display_
> 指定要管理的 display。

**-c**
> 为窗口启用客户端阴影。

**-C**
> 对带有 _NET_WM_WINDOW_TYPE_DOCK 的 dock/面板窗口禁用阴影。

**-f**
> 窗口打开/关闭时淡入淡出。

**-F**
> 不透明度变化时对窗口进行渐变处理。

**-r** _radius_
> 阴影半径，以像素为单位（默认：12）。

**-o** _opacity_
> 阴影不透明度（0.0 到 1.0，默认：0.75）。

**-l** _offset_
> 阴影的左侧偏移量，以像素为单位（默认：-15）。

**-t** _offset_
> 阴影的顶部偏移量，以像素为单位（默认：-15）。

**-n**
> 常规客户端阴影（无渐变）。

**-s**
> 启用同步 X 操作以便调试。

**-S**
> 为带形状（shape）的窗口启用阴影。

**-D** _time_
> 渐变时间步长，以毫秒为单位（默认：10）。

**-a**
> 窗口打开/关闭时禁用渐变。

**-I** _opacity_
> 淡入时每步的不透明度变化量（默认：0.028）。

**-O** _opacity_
> 淡出时每步的不透明度变化量（默认：0.03）。

# DESCRIPTION

**xcompmgr** 是 X Window System 的合成窗口管理器，为窗口添加投影、透明和渐变过渡等视觉效果。它作为一个独立的合成器运行，可与任何符合 ICCCM/EWMH 规范的窗口管理器配合工作。

该合成器使用 X Composite 扩展将窗口内容重定向到离屏像素图（pixmap），然后在显示之前将它们与特效合成。这使得无需伪透明技术就能实现真正的透明。可以使用 **transset** 等工具为单个窗口设置不透明度。

常见的配置是将阴影（-c）和渐变（-f）选项组合使用，以获得精致的桌面外观。阴影的外观通过半径、偏移和不透明度参数控制。对于配置较低的机器，可以用 -C 在 dock 和面板上禁用阴影，以减少视觉干扰。

# CAVEATS

需要启用 Composite、Damage、Fixes 和 Render 等 X 扩展。可能与内置合成的窗口管理器冲突（请先禁用它们的合成器）。性能取决于图形驱动的质量；软件渲染可能较慢。不支持 **picom** 等现代合成器所具备的模糊或动画等高级特效。

# HISTORY

**xcompmgr** 由 Keith Packard 编写，在约 **2004 年** X Composite 扩展问世后作为示例合成管理器发布。它是一个概念验证和参考实现，展示了 X.Org 的合成能力。虽然功能可用，但它后来被功能更丰富的合成器取代，先是 **compton**，后来是 **picom**，后者提供了更多特效和更好的性能。

# INSTALL

```apt: sudo apt install xcompmgr```

```dnf: sudo dnf install xcompmgr```

```pacman: sudo pacman -S xcompmgr```

```zypper: sudo zypper install xcompmgr```

```nix: nix profile install nixpkgs#xcompmgr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[picom](/man/picom)(1), [compton](/man/compton)(1), [transset](/man/transset)(1), [xwininfo](/man/xwininfo)(1)
