# TAGLINE

将 Perl POD 文档转换为纯文本

# TLDR

**将 POD 转换为纯文本**

```pod2text [file.pod]```

**输出到文件**

```pod2text [file.pod] > [output.txt]```

**指定宽度**

```pod2text -w [80] [file.pod]```

**宽松排版**

```pod2text -l [file.pod]```

# SYNOPSIS

**pod2text** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 POD 文件。

**-w** _WIDTH_
> 输出宽度（列数）。

**-l**, **--loose**
> 宽松的段落排版。

**-q** _QUOTES_
> 引号字符。

**-c**, **--color**
> 使用 ANSI 颜色。

# DESCRIPTION

**pod2text** 将 Perl POD（Plain Old Documentation）转换为适合终端显示的格式化纯文本。它把标题、列表、代码块及其他 POD 格式渲染为可读的 ASCII 输出。

**-w** 选项设置输出的列宽，**-l** 启用带额外间距的宽松段落排版，**-c** 启用 ANSI 彩色输出以增强终端可读性。它是标准 Perl 发行版的一部分。

# CAVEATS

Perl 特有格式。标准 Perl 的一部分。

# HISTORY

pod2text 是为了在**终端查看** Perl 文档而创建的。

# INSTALL

```apt: sudo apt install perl```

```dnf: sudo dnf install perl```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl```

```zypper: sudo zypper install perl```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pod2man](/man/pod2man)(1), [pod2html](/man/pod2html)(1), [perldoc](/man/perldoc)(1)
