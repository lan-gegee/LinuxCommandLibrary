# TAGLINE

Unicode 字符映射表浏览器

# TLDR

**打开字符映射表**

```charmap```

按名称**搜索字符**

```charmap --search "[heart]"```

**复制字符到剪贴板**

```charmap --copy "[character]"```

# SYNOPSIS

**charmap** [_options_]

# DESCRIPTION

**charmap** 是一款 Unicode 字符映射表应用，通常是 GNOME 桌面的一部分。它可以浏览和搜索所有 Unicode 字符、查看字符详情以及把字符复制到剪贴板。

该应用按 Unicode 区块组织显示字符，并支持按文字系统（script）、语言或搜索词过滤。每个字符都会显示其码点、官方名称及相关信息。

# PARAMETERS

**--search** _text_
> 按名称搜索字符。

**--copy** _char_
> 复制字符到剪贴板。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# CAVEATS

需要图形环境。字符能否显示取决于已安装的字体。如果字体不包含某些字符，它们可能显示为方框。

# HISTORY

**charmap** 是 **GNOME** 桌面环境的一部分。字符映射工具自早期图形界面时代就已存在，帮助用户输入键盘上没有的字符。GNOME 版本名为 **gucharmap**，创建于 2000 年代初。

# INSTALL

```apt: sudo apt install gucharmap```

```dnf: sudo dnf install gucharmap```

```pacman: sudo pacman -S gucharmap```

```zypper: sudo zypper install gucharmap```

```brew: brew install gucharmap```

```nix: nix profile install nixpkgs#gucharmap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdotool](/man/xdotool)(1), [xclip](/man/xclip)(1)
