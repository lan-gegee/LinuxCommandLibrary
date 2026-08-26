# TAGLINE

列出可用的 X11 字体

# TLDR

**列出所有可用字体**

```xlsfonts```

**列出匹配模式的字体**

```xlsfonts -fn "*courier*"```

**列出字体及详细信息**

```xlsfonts -l```

**列出指定显示器上的字体**

```xlsfonts -display [hostname:0]```

**每行一个字体列出**

```xlsfonts -1```

**统计可用字体的数量**

```xlsfonts | wc -l```

**列出等宽字体**

```xlsfonts -fn "*-m-*"```

# SYNOPSIS

**xlsfonts** [**-display** _HOST:DISPLAY_] [**-l**] [**-ll**] [**-lll**] [**-m**] [**-C**] [**-1**] [**-w** _WIDTH_] [**-n** _COLUMNS_] [**-u**] [**-o**] [**-fn** _PATTERN_]

# PARAMETERS

**-display** _HOST:DISPLAY_
> 连接到指定的 X 显示器。

**-fn** _PATTERN_
> 仅列出匹配模式的字体（支持通配符）。

**-l**
> 以最少属性列出字体。

**-ll**
> 列出字体并显示更多属性。

**-lll**
> 列出字体并显示全部属性。

**-m**
> 使用最大输出宽度（通常为 79 列）。

**-C**
> 使用多列输出。

**-1**
> 强制单列输出。

**-w** _WIDTH_
> 多列输出的最大宽度。

**-n** _COLUMNS_
> 列数。

**-u**
> 不对输出排序。

**-o**
> 使用 OpenFont/QueryFont 而不是 ListFonts。

# DESCRIPTION

**xlsfonts** 列出 X server 字体路径中可用的字体。默认以多列方式列出所有字体。字体名称遵循 X Logical Font Description（XLFD）约定，包含铸造方、字族、字重、倾斜、宽度、样式、像素大小、点数大小、分辨率、间距、平均宽度和字符集等字段。

模式中可以包含通配符（* 匹配任意字符串，? 匹配单个字符）。常见用法包括按字族过滤（-fn "*helvetica*"）、按间距过滤（-fn "*-m-*" 表示等宽）或按大小过滤。

# CAVEATS

xlsfonts 只显示 X11 核心字体，不包括大多数应用使用的现代 fontconfig/Xft 字体。在安装了大量字体的系统上，输出可能非常庞大。字体路径和可用性取决于 X server 配置。

# HISTORY

xlsfonts 自 20 世纪 80 年代末最早的 X11 版本起就是 X Window System 工具的一部分。虽然现代应用通常使用 fontconfig 和 Xft 进行抗锯齿字体渲染，但 xlsfonts 在诊断 X11 核心字体可用性以及支持遗留应用方面仍然有用。

# INSTALL

```apt: sudo apt install x11-utils```

```dnf: sudo dnf install xlsfonts```

```zypper: sudo zypper install xlsfonts```

```nix: nix profile install nixpkgs#xlsfonts```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xfontsel](/man/xfontsel)(1), [fc-list](/man/fc-list)(1), [xset](/man/xset)(1)
