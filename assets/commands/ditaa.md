# TAGLINE

将 ASCII 字符画图表转换为图形

# TLDR

**将 ASCII 字符画转换为 PNG 图片**

```ditaa [input.txt] [output.png]```

**转换时禁用抗锯齿**

```ditaa -A [input.txt] [output.png]```

**转换时不带阴影**

```ditaa -S [input.txt] [output.png]```

**转换时使用圆角**

```ditaa -r [input.txt] [output.png]```

**缩放输出图片**

```ditaa -s [2.0] [input.txt] [output.png]```

**输出为 SVG**

```ditaa --svg [input.txt] [output.svg]```

**转换时使用透明背景**

```ditaa -T [input.txt] [output.png]```

# SYNOPSIS

**ditaa** [_options_] _input_ [_output_]

# PARAMETERS

**-A**, **--no-antialias**
> 禁用抗锯齿。

**-S**, **--no-shadows**
> 禁用投影阴影。

**-r**, **--round-corners**
> 方框使用圆角。

**-s**, **--scale** _factor_
> 按 factor 缩放输出。

**-T**, **--transparent**
> 使用透明背景。

**-E**, **--no-separation**
> 禁用形状边缘分离效果。

**-e**, **--encoding** _enc_
> 输入文件的编码。

**--svg**
> 输出为 SVG 而非 PNG。

**-t**, **--tabs** _n_
> 输入的制表符宽度。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**ditaa**（DIagrams Through ASCII Art）将 ASCII 字符画图表转换为正式的图形。它能识别用 ASCII 字符绘制的方框、线条和基本形状，并将它们渲染为位图或矢量图像。

输入使用标准 ASCII 字符：**+**、**-**、**|** 表示方框的角和边，**/** 和 **\\** 表示斜线，**=** 表示虚线，方框内的文字作为标签。类似 **{c:red}** 的颜色标记可以自定义外观。

该工具适用于文档编写场景：图表可以以 ASCII 形式保存在源文件中（可版本控制、可编辑），发布时再渲染为图片。

# ASCII ART EXAMPLE

```
+--------+   +-------+
|        +-->| ditaa |
| Source |   +-------+
|  File  |   |       |
|        |   | Image |
+--------+   +-------+
```

# CAVEATS

需要 Java 运行时环境。复杂图表可能无法按预期渲染。仅限于能用 ASCII 表示的形状。某些 Unicode 制表字符默认无法识别。

# HISTORY

ditaa 由 **Stathis Sideris** 于 **2004 年**创建，是一个开源 Java 应用。其设计理念源于希望在源码仓库中将图表保存为纯文本，同时能为文档生成美观的渲染版本。该工具已被集成到 Asciidoctor、Org-mode 等多种文档系统中。

# INSTALL

```dnf: sudo dnf install ditaa```

```pacman: sudo pacman -S ditaa```

```brew: brew install ditaa```

```nix: nix profile install nixpkgs#ditaa```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[graphviz](/man/graphviz)(1), [plantuml](/man/plantuml)(1), [mermaid](/man/mermaid)(1)
