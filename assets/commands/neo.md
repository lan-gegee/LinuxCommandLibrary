# TAGLINE

模拟《黑客帝国》中的数字雨

# TLDR

**播放默认的黑客帝国数字雨动画**

```neo```

**以指定颜色播放**

```neo -c [green|red|blue|cyan|gold|rainbow|purple|pink|vaporwave]```

**使用指定字符集播放**

```neo --charset [katakana|ascii|cyrillic|greek|braille|runic|binary|hex]```

**调整滚动速度和雨滴密度**

```neo -S [12] -d [1.5]```

**在数字雨中显示居中的消息**

```neo -m "[message]"```

**以异步滚动和 256 色模式播放**

```neo -S 12 -a --colormode=256```

# SYNOPSIS

**neo** [_options_]

# PARAMETERS

**-c, --color** _color_
> 设置前景文字颜色。可选：**green**、**green2**、**green3**、**yellow**、**orange**、**red**、**blue**、**cyan**、**gold**、**rainbow**、**purple**、**pink**、**pink2**、**vaporwave**、**gray**

**-S, --speed** _num_
> 设置滚动速度

**-d, --density** _num_
> 控制屏幕上出现的雨滴数量（默认：1.0）

**--charset** _name_
> 要使用的字符集：**ascii**、**extended**、**english**、**dec**、**digits**、**punc**、**bin**、**hex**、**katakana**、**greek**、**cyrillic**、**arabic**、**hebrew**、**devanagari**、**braille**、**runic**

**--chars** _range_
> 通过十六进制码指定自定义 Unicode 字符范围

**--colormode** _mode_
> 颜色分配方式：**0** 为随机（默认），**1** 为渐变

**-m, --message** _text_
> 显示居中的 ASCII 文字，随字符流过而逐渐显现

**-a, --async**
> 启用更快的异步滚动

**-F, --fullwidth**
> 使用全角字符渲染

**--noglitch**
> 禁用故障效果

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**neo** 重现了《黑客帝国》电影中标志性的数字雨效果。随机字符流在终端屏幕上无尽下落，高度还原了电影中 Cypher 向 Neo 解释代码的场景。它还模仿了许多细节，如半角片假名字符、不均匀的颜色、故障和闪烁。

动画可通过不同的字符集、调色板、滚动速度和密度设置进行自定义。交互控制允许实时调节：方向键控制速度和故障强度，数字键切换颜色。

# CAVEATS

性能取决于终端模拟器的能力。GPU 加速的终端能显著提升渲染效果。Unicode 字符集需要相应的字体支持。不支持原生 Windows；请改用 WSL。

# HISTORY

**neo** 由 **st3w** 创建，是对 **CMatrix**（原作者 Chris Allegretta）的现代重写版。它增加了 **32 位色彩**和完整的 **Unicode 支持**，超越了原版 CMatrix 的能力。该项目可用于 Linux、macOS 和 FreeBSD。

# INSTALL

```apt: sudo apt install neo-cli```

```dnf: sudo dnf install neo```

```nix: nix profile install nixpkgs#neo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmatrix](/man/cmatrix)(1), [sl](/man/sl)(1)
