# TAGLINE

ASCII 艺术字横幅生成器

# TLDR

**创建 ASCII 艺术**文字

```figlet "[Hello World]"```

**使用指定字体**

```figlet -f [slant] "[text]"```

**居中输出**

```figlet -c "[text]"```

**设置宽度**

```figlet -w [80] "[text]"```

**预览所有可用字体**

```showfigfonts```

# SYNOPSIS

**figlet** [_options_] [_message_]

# PARAMETERS

_MESSAGE_
> 要渲染成 ASCII 艺术字的文本。

**-f** _FONT_
> 要使用的字体文件。

**-w** _WIDTH_
> 输出宽度。

**-c**
> 输出居中。

**-l**
> 左对齐。

**-r**
> 右对齐。

**-k**
> 字距调整模式。

**-W**
> 全宽（不合并字符间距）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**figlet** 使用各种字体把文本渲染成大号的 ASCII 艺术字符。它常用于制作终端横幅、欢迎信息和风格化的文本输出。

多种字体提供了从简单块状字母到繁复设计的不同风格。该工具会调整字符间距（smushing），从而生成紧凑或舒展的输出。

如果没有给出消息，figlet 会从标准输入读取，因此支持管道输入。

# CAVEATS

可用字体因安装情况而异。过长的文本换行后可能不太美观。有些字体只有在特定的终端宽度下才有较好的效果。

# HISTORY

figlet（Frank, Ian & Glenn's Letters）由 Glenn Chappell 和 Ian Chai 于 1991 年创建。它成为 Unix 世界里制作 ASCII 横幅的经典工具，并催生了数百款社区创作的字体。

# INSTALL

```dnf: sudo dnf install figlet```

```pacman: sudo pacman -S figlet```

```apk: sudo apk add figlet```

```zypper: sudo zypper install figlet```

```brew: brew install figlet```

```nix: nix profile install nixpkgs#figlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[toilet](/man/toilet)(1), [banner](/man/banner)(1), [cowsay](/man/cowsay)(1), [showfigfonts](/man/showfigfonts)(6)

# RESOURCES

```[Homepage](http://www.figlet.org/)```

```[Source code](https://github.com/cmatsuoka/figlet)```

<!-- verified: 2026-07-15 -->
