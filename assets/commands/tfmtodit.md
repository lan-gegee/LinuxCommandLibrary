# TAGLINE

为 groff 转换 TeX 字体度量

# TLDR

从 TeX 字体度量文件**创建字体描述文件**

```tfmtodit [tfm_file] [map_file] [font]```

**创建特殊字体**描述文件

```tfmtodit -s [tfm_file] [map_file] [font]```

**使用 gf 文件**获取额外的字体度量信息

```tfmtodit -g [gf_file] [tfm_file] [map_file] [font]```

**指定倾斜字符**位置

```tfmtodit -k [skewchar] [tfm_file] [map_file] [font]```

**显示版本号**

```tfmtodit -v```

# SYNOPSIS

**tfmtodit** [**-sv**] [**-g** _gf_file_] [**-k** _skewchar_] _tfm_file_ _map_file_ _font_

# PARAMETERS

**-s**
> 在字体描述文件中添加 special 指令。当希望当前字体中找不到字形时转而搜索该字体时使用。

**-g** _gf_file_
> 使用 Metafont 生成的、包含 special 和 numspecial 命令的 gf 文件来获取额外的字体度量信息。

**-k** _skewchar_
> 指定倾斜字符位置。第二分量为倾斜字符的字距（kern）将被忽略。可用十进制、八进制（前导 0）或十六进制（前导 0x）表示。

**-v**
> 打印版本号并退出。

# DESCRIPTION

**tfmtodit** 为 groff 的 DVI 输出设备创建字体描述文件。它将 TeX Font Metrics（TFM）文件转换为 groff 所需的格式。

_tfm_file_ 是该字体的 TeX 字体度量文件。_map_file_ 将 groff 字符标识符分配给字体中的字形索引，由形如 `i c1 ... cn` 的行组成，其中 i 是字形位置，c1 到 cn 是字形标识符。输出以 groff_font(5) 格式写入指定的 _font_ 文件。

对于数学排版，groff 需要 TFM 文件中没有的额外字体度量信息。这是因为 TeX 使用单独的数学斜体字体，而 groff 在数学中使用普通斜体字体。这些额外信息来自 Computer Modern 字体的 Metafont 程序中的 math_fit 宏参数。

# CAVEATS

该工具专为 DVI 输出设备设计，可能无法与其他 groff 输出设备正确配合工作。正确的数学排版需要通过 **-g** 选项提供来自 Metafont gf 文件的补充字体度量数据。

# HISTORY

**tfmtodit** 是 **groff**（GNU troff）项目的一部分，该项目始于 **1990** 年，是 Unix troff 排版系统的自由软件替代品。该工具弥合了 TeX 字体度量与 groff 字体描述格式之间的差距，使 TeX 字体能够配合 groff 的 DVI 输出使用。

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

[groff](/man/groff)(1), [grodvi](/man/grodvi)(1), [groff_font](/man/groff_font)(5), [troff](/man/troff)(1)
