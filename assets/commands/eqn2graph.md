# TAGLINE

公式描述转图形图像转换器

# TLDR

**将公式转换为**图片

```echo "x = {-b +- sqrt{b sup 2 - 4ac}} over 2a" | eqn2graph > [equation.png]```

**指定输出格式**

```echo "[equation]" | eqn2graph --format [svg]```

**设置字号**

```echo "[equation]" | eqn2graph -s [14]```

# SYNOPSIS

**eqn2graph** [_options_]

# PARAMETERS

**--format** _FORMAT_
> 输出格式：png、svg、pdf 等。

**-s** _SIZE_
> 字体磅值大小。

**-unsafe**
> 允许不安全的操作。

**-v**
> 详细模式。

# DESCRIPTION

**eqn2graph** 将 eqn 公式描述转换为图形图像。它是一个封装脚本，先用 groff 处理 eqn 输入，再把结果转换为各种图像格式。

该工具从标准输入读取采用 eqn 语法的公式文本，生成适合嵌入文档、网页或演示文稿的图像文件。

eqn2graph 适合在无需完整文档排版流程的情况下生成独立的公式图片。

# CAVEATS

需要 groff 和一个图像转换工具（通常是 GraphicsMagick 或 ImageMagick）。默认输出格式为 PNG。使用 eqn 语法而非 LaTeX 数学记号。

# HISTORY

eqn2graph 是 **groff** 工具集的一部分，提供了一种便捷方式，可从 eqn 预处理语言生成公式图像。

# INSTALL

```apt: sudo apt install groff```

```dnf: sudo dnf install groff```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[eqn](/man/eqn)(1), [groff](/man/groff)(1)
