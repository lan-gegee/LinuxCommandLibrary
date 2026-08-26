# TAGLINE

交互式 X11 字体选择器

# TLDR

**启动字体选择器**

```xfontsel```

**以字体模式过滤器启动**

```xfontsel -pattern "[*medium*]"```

**退出时将所选字体打印到 stdout**

```xfontsel -print```

**显示自定义示例文本**

```xfontsel -sample "[The quick brown fox]"```

**显示缩放字体**

```xfontsel -scaled```

# SYNOPSIS

**xfontsel** [_options_]

# PARAMETERS

**-pattern** _fontname_
> 过滤匹配模式的字体。

**-print**
> 退出时将所选字体名称打印到 stdout。

**-sample** _text_
> 用于预览的自定义示例文本。

**-sample16** _text_
> 16 位字体的示例文本。

**-sampleUCS** _text_
> UCS 字体的示例文本。

**-scaled**
> 在选择中包含缩放字体。

**-noscaled**
> 从选择中排除缩放字体。

**-display** _name_
> 要使用的 X 显示器。

# DESCRIPTION

**xfontsel** 提供一个交互式图形界面，用于使用 XLFD（X Logical Font Description，X 逻辑字体描述）名称浏览和选择 X11 核心字体。它为 14 段 XLFD 字体名称的每个组成部分显示下拉菜单。

点击某个字段名会显示按先前选择过滤后的可用选项。星号（*）充当通配符。界面会显示所选字体的预览，完整的 XLFD 名称可以复制到剪贴板。

所选字体名称会成为 PRIMARY 文本选择和 PRIMARY_FONT 选择，从而可以粘贴到终端模拟器和其他应用程序中。

# CAVEATS

仅显示 X11 核心字体（XLFD），不支持现代的 fontconfig/FreeType 字体。在使用 Xft 字体的现代系统上用途有限。属于已被图形化字体选择器取代的老旧工具。

# HISTORY

**xfontsel** 由 Ralph R. Swick 在 Digital Equipment Corporation/MIT Project Athena 创建。在 XLFD 字体是 X11 主要字体系统的年代，它是必备工具。现代系统主要使用 fontconfig 和 Xft，因此 xfontsel 主要用于老旧应用。

# INSTALL

```apt: sudo apt install x11-utils```

```dnf: sudo dnf install xfontsel```

```apk: sudo apk add xfontsel```

```zypper: sudo zypper install xfontsel```

```nix: nix profile install nixpkgs#xfontsel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xlsfonts](/man/xlsfonts)(1), [fc-list](/man/fc-list)(1), [xterm](/man/xterm)(1)
