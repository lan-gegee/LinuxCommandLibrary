# TAGLINE

ASCII 艺术火焰动画

# TLDR

在终端中**显示 ASCII 火焰**动画

```aafire```

以 **curses 驱动**运行（强制终端输出）

```aafire -driver curses```

以 **slang 驱动**运行以便在终端中显示

```aafire -driver slang```

以指定尺寸显示

```aafire -width [80] -height [25]```

# SYNOPSIS

**aafire** [_aalib-options_]

# PARAMETERS

**-driver** _name_
> 选择输出驱动（curses、slang、X11 等）

**-width** _n_
> 设置显示宽度（字符数）

**-height** _n_
> 设置显示高度（字符数）

**-bold**
> 启用粗体字符，使输出更亮

**-dim**
> 使用暗淡字符，使外观更暗

**-reverse**
> 使用反显模式

**-normal**
> 使用普通渲染模式

**-extended**
> 使用扩展 ASCII 字符集

**-eight**
> 使用 8 位 ASCII 字符

**-help**
> 显示可用选项和驱动

# DESCRIPTION

**aafire** 展示一段完全用 ASCII 字符渲染的火焰模拟动画。它是 aalib 库的演示程序，该库能把图形输出转换为基于文本的表现形式。

动画仅使用标准文本字符实时渲染出闪烁跳动的火焰，直接在终端或 X11 窗口中营造出有趣的视觉效果。这个程序展示了 aalib 只凭 ASCII 字符及其亮度层次就能表现复杂视觉信息的能力。

默认情况下，aalib 可能会尝试使用图形驱动。要确保输出停留在终端中，请显式使用 **curses** 或 **slang** 驱动。

# CAVEATS

默认驱动可能尝试打开 X11 窗口而不是在终端中显示。请使用 **-driver curses** 或 **-driver slang** 强制终端输出。性能取决于终端仿真能力，不同系统上的表现可能有所差异。

# HISTORY

**aafire** 属于 **Jan Hubicka** 在上世纪 **90 年代末**创建的 aalib（ASCII Art Library）。该库的开发目标是为各类应用提供 ASCII 艺术渲染能力，并因其纯文本环境下显示图形的创意方式而流行。它通过 MPlayer 等项目获得了更广泛的认知——MPlayer 曾利用 aalib 将视频播放为 ASCII 艺术。

# INSTALL

```apt: sudo apt install libaa-bin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bb](/man/bb)(1), [cmatrix](/man/cmatrix)(1), [sl](/man/sl)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/aa-project/)```

```[Homepage](https://aa-project.sourceforge.net/aalib/)```

<!-- verified: 2026-06-10 -->
