# TAGLINE

向 troff 字体文件添加字体度量信息

# TLDR

向 troff 字体文件**添加**字体度量

```addftinfo [resolution] [unitwidth] [font] < [input.tfm] > [output.tfm]```

为 **300 dpi** 分辨率添加度量

```addftinfo 300 300 TR < times-roman.tfm > TR.tfm```

# SYNOPSIS

**addftinfo** [_-v_] _resolution_ _unitwidth_ _font_ < _input_ > _output_

# DESCRIPTION

**addftinfo** 是 groff（GNU troff）的一个实用程序，用于向 troff 字体文件添加计算得出的字体度量信息。它会读取字体文件，计算排版所需的额外度量，然后输出增强后的字体文件。

该工具通常在 groff 字体安装流程中使用，用来补充基础字体文件里不一定包含的度量项，例如字符的高度和深度。

# PARAMETERS

**resolution**
> 设备分辨率，单位为每英寸点数

**unitwidth**
> 定义字体单位宽度时的磅值

**font**
> groff 字体名（R、I、B、BI 等）

**-v**, **--version**
> 打印版本信息

# CAVEATS

输入必须是有效的 troff 字体描述文件。输出的度量为计算所得的近似值，可能与实际的字体渲染效果不完全一致。此工具仅适用于 groff 排版系统。

# HISTORY

**addftinfo** 是 GNU groff 的一部分。GNU groff 自 **1989** 年起开始开发，作为 Unix troff 排版系统的自由替代品。这个实用程序就是为了简化字体安装而诞生的。

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

[groff](/man/groff)(1), [troff](/man/troff)(1), [afmtodit](/man/afmtodit)(1), [tfmtodit](/man/tfmtodit)(1)
