# TAGLINE

渲染 TheDraw ANSI 字体文本

# TLDR

**查看 TheDraw 文件**

```tdf [font.tdf]```

**列出文件中的字体**

```tdf -l [font.tdf]```

**渲染文本**

```tdf -f [font.tdf] "[text]"```

**使用文件中的指定字体**

```tdf -f [font.tdf] -n [fontname] "[text]"```

# SYNOPSIS

**tdf** [_-f file_] [_-l_] [_-n name_] [_options_] [_text_]

# PARAMETERS

**-f** _FILE_
> 字体文件。

**-l**
> 列出字体。

**-n** _NAME_
> 字体名称。

**-c** _COLOR_
> 颜色模式。

**--help**
> 显示帮助。

# DESCRIPTION

**tdf** 使用 TheDraw 字体文件（.tdf）渲染文本。这种格式起源于 BBS 时代，用于制作彩色的 ANSI 艺术文字横幅。每个 TDF 文件可以包含多种字体，可以按名称选择特定字体。

该工具读取 TheDraw 字体定义，将纯文本转换为带有颜色和特殊字符的大型风格化 ANSI 艺术。**-l** 标志可列出 TDF 文件中的所有可用字体，便于在渲染前浏览字体集合。

# CAVEATS

需要 TDF 文件。属于复古格式。可用字体有限。

# HISTORY

**tdf** 使用 **TheDraw** ANSI 字体文件显示文本，这是 BBS 时代流行的一种格式。

# INSTALL

```brew: brew install tdf```

```nix: nix profile install nixpkgs#tdf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[figlet](/man/figlet)(1), [toilet](/man/toilet)(1), [banner](/man/banner)(1)
