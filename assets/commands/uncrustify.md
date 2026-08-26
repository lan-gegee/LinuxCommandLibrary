# TAGLINE

可配置的多语言源代码格式化工具

# TLDR

**格式化文件**并输出到 stdout

```uncrustify -c [config.cfg] -f [source.c]```

**格式化并写入输出文件**

```uncrustify -c [config.cfg] -f [source.c] -o [output.c]```

**原地格式化文件**并创建备份

```uncrustify -c [config.cfg] --replace [file1.c] [file2.c]```

**原地格式化文件**且不备份

```uncrustify -c [config.cfg] --no-backup [*.c]```

**显式指定语言**

```uncrustify -c [config.cfg] -l [CPP] -f [source.cpp]```

**生成默认配置**

```uncrustify --show-config > [uncrustify.cfg]```

**处理文件列表中的文件**

```uncrustify -c [config.cfg] -F [filelist.txt]```

# SYNOPSIS

**uncrustify** [_options_] [_files ..._]

# PARAMETERS

**-c** _cfg_
> 使用指定的配置文件（或 '-' 表示默认值）。

**-f** _file_
> 处理单个文件，输出到 stdout。

**-o** _file_
> 将输出写入指定文件。

**-F** _file_
> 读取要处理的文件列表（每行一个，'-' 表示 stdin）。

**-l** _lang_
> 语言覆盖：C、CPP、D、CS、JAVA、PAWN、VALA、OC、OC+。

**--replace**
> 原地替换源文件（会创建备份）。

**--no-backup**
> 替换文件时不创建备份。

**--mtime**
> 保留被替换文件的修改时间。

**--frag**
> 将输入视为代码片段，并应用合适的首行缩进。

**--show-config**
> 将生效的配置打印到 stdout。

**--update-config**
> 输出包含当前设置的新配置文件。

**--update-config-with-doc**
> 输出带有用法注释的配置文件。

**--set** _key=value_
> 覆盖配置选项。

**-q**
> 安静模式，不向 stderr 输出。

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**uncrustify** 是一个高度可配置的源代码美化工具，支持 C、C++、C#、Objective-C、D、Java、Pawn 和 VALA。它按照指定的样式规则自动格式化代码，控制缩进、空格、对齐和换行。

配置通过一个包含数百个选项的配置文件控制。默认位置是 **$UNCRUSTIFY_CONFIG** 或 **~/.uncrustify.cfg**。先用 **--show-config** 生成初始配置，再逐步定制。

uncrustify 可以处理单个文件、文件列表或整个源码树。它支持原地编辑，可选择是否备份。

# CONFIGURATION

**$UNCRUSTIFY_CONFIG**
> 指定配置文件路径的环境变量。

**~/.uncrustify.cfg**
> 未设置 -c 选项或环境变量时使用的默认用户配置文件。

# CAVEATS

配置复杂度较高；建议从生成的默认值入手，逐步调整。不同的代码风格可能需要大量的配置调优。使用 **--no-backup** 前，务必先在备份或受版本控制的代码上测试。

# HISTORY

uncrustify 由 **Ben Gardner** 创建，首次发布于 **2005 年**。它被设计为一个支持多语言的高度灵活的代码格式化工具。该项目现已支持超过 700 个配置选项，使其成为现有最可定制的代码格式化工具之一。

# INSTALL

```apt: sudo apt install uncrustify```

```dnf: sudo dnf install uncrustify```

```pacman: sudo pacman -S uncrustify```

```apk: sudo apk add uncrustify```

```zypper: sudo zypper install uncrustify```

```brew: brew install uncrustify```

```nix: nix profile install nixpkgs#uncrustify```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang-format](/man/clang-format)(1), [astyle](/man/astyle)(1), [indent](/man/indent)(1)
