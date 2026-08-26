# TAGLINE

预览可用的 FIGlet 字体

# TLDR

**显示所有字体**

```showfigfonts```

**显示指定文本**

```showfigfonts "[Hello]"```

**显示某目录下的字体**

```showfigfonts -d [/usr/share/figlet]```

# SYNOPSIS

**showfigfonts** [_-d dir_] [_text_]

# PARAMETERS

**-d** _DIR_
> 字体目录。

_text_
> 要显示的示例文本。

# DESCRIPTION

**showfigfonts** 通过用每种可用 FIGlet 字体渲染示例文本来预览所有字体，方便直观比较各种样式并选择合适的 ASCII 艺术字体。默认情况下，每个字体的名称本身会被用作示例文本，但也可以通过参数指定自定义文本。

**-d** 选项允许预览任意目录中的字体，而不仅限于默认的 FIGlet 字体路径。输出会依次显示每个已安装字体的名称及其渲染结果，为选择字体提供了便捷的目录式参考。

# CAVEATS

大型字体目录需要较长时间处理。输出可能非常长。部分字体宽度较大。

# HISTORY

**showfigfonts** 随 **figlet** 一同分发，用于字体预览，帮助用户发现可用字体。

# INSTALL

```apt: sudo apt install figlet```

```dnf: sudo dnf install figlet```

```pacman: sudo pacman -S figlet```

```apk: sudo apk add figlet```

```zypper: sudo zypper install figlet```

```brew: brew install figlet```

```nix: nix profile install nixpkgs#figlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[figlet](/man/figlet)(1), [toilet](/man/toilet)(1), [banner](/man/banner)(1)
