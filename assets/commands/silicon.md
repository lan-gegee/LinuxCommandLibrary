# TAGLINE

生成精美的源代码图片

# TLDR

从文件生成代码图片

```silicon [source.rs] -o [code.png]```

从剪贴板生成

```silicon --from-clipboard -o [code.png]```

指定语言

```silicon --language [python] -o [code.png] < [code.py]```

使用特定主题

```silicon --theme [Dracula] [source.rs] -o [code.png]```

添加行号

```silicon --line-number [source.rs] -o [code.png]```

自定义背景颜色

```silicon --background ["#1e1e2e"] [source.rs] -o [code.png]```

添加阴影

```silicon --shadow-blur-radius [10] [source.rs] -o [code.png]```

列出可用主题

```silicon --list-themes```

# SYNOPSIS

**silicon** [_--language lang_] [_--theme name_] [_--output file_] [_options_] [_file_]

# PARAMETERS

**-o** _FILE_, **--output** _FILE_
> 输出图片文件。

**-l** _LANG_, **--language** _LANG_
> 用于高亮显示的源语言。

**--theme** _NAME_
> 配色主题。

**--list-themes**
> 显示可用主题。

**--list-fonts**
> 显示可用字体。

**--from-clipboard**
> 从剪贴板读取代码。

**--to-clipboard**
> 将图片写入剪贴板。

**-f** _FONT_, **--font** _FONT_
> 字体名称。

**--line-number**
> 显示行号。

**--line-offset** _NUM_
> 起始行号。

**--highlight-lines** _RANGE_
> 高亮特定行。

**--background** _COLOR_
> 背景颜色。

**--shadow-blur-radius** _PX_
> 阴影模糊半径。

**--shadow-offset-x** _PX_
> 阴影 X 偏移。

**--shadow-offset-y** _PX_
> 阴影 Y 偏移。

**--pad-horiz** _PX_
> 水平内边距。

**--pad-vert** _PX_
> 垂直内边距。

**--no-round-corner**
> 禁用圆角。

**--no-window-controls**
> 隐藏窗口按钮。

# DESCRIPTION

**silicon** 可以将源代码生成为精美图片。它会应用语法高亮、窗口装饰和样式，产出适合文档、演示文稿和社交媒体的图片。

语言可以从文件扩展名自动检测，也可以显式指定。该工具使用 syntect 进行高亮，支持大多数编程语言，并内置来自流行编辑器（VS Code、Sublime）的主题。

输出效果类似终端或编辑器窗口。窗口控件（macOS 风格的红绿灯按钮）增加真实感，阴影营造层次感，圆角带来现代感。

行号和行高亮有助于解释特定的代码片段。自定义字体保证输出清晰易读并保持等宽对齐。

剪贴板集成支持快捷的工作流：复制代码、运行 silicon、粘贴图片。这让代码截图的创建更加顺畅。

内边距、颜色和阴影都可以自定义，以匹配品牌规范或演示主题。

# CAVEATS

超长的行可能产生很宽的图片。并非所有终端主题都可用。使用自定义字体时必须已安装该字体。大段代码会生成很大的图片。只支持 PNG 输出（不支持 SVG）。行高亮语法可能比较难用。

# HISTORY

**silicon** 由 **Aloxaf** 于 **2019 年**前后创建，作为 carbon-now-cli 的 Rust 替代品。它用 Rust 编写，提供离线的代码图片生成。其名字源自硅晶片和芯片，暗喻代码变成"硬件"。它在开发者社区中广受欢迎，常用于分享代码片段。

# INSTALL

```pacman: sudo pacman -S silicon```

```brew: brew install silicon```

```nix: nix profile install nixpkgs#silicon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[carbon-now-cli](/man/carbon-now-cli)(1), [pygmentize](/man/pygmentize)(1), [bat](/man/bat)(1)
