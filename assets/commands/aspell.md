# TAGLINE

交互式拼写检查器

# TLDR

**检查**一个文件

```aspell check [file.txt]```

使用**指定语言**检查

```aspell --lang=[es] check [file.txt]```

**列出**可用的词典

```aspell dicts```

从 **stdin** 检查

```echo "speling errror" | aspell list```

**检查 TeX/LaTeX 文件**（忽略 TeX 命令）

```aspell --mode=tex check [file.tex]```

创建**个人词典**

```aspell --lang=[en] create master [./custom.rws] < [wordlist.txt]```

# SYNOPSIS

**aspell** [_options_] _mode_ [_file_]

# DESCRIPTION

**aspell** 是一款旨在取代 ispell 的拼写检查器。它可以检查单个文件、作为管道过滤器工作，或为其他程序提供 C 库接口。

该工具支持多种语言和个人词典，其建议算法比旧的拼写检查器更好。

# PARAMETERS

**check** _file_
> 交互式检查文件

**list**
> 从 stdin 列出拼写错误的单词

**pipe**
> 输出带位置信息的拼写错误单词（供编辑器使用）

**-c** _file_
> 与 check 相同（GNU ispell 兼容）

**--lang=**_code_
> 语言代码（en、es、fr 等）

**--mode=**_mode_
> 解析模式（tex、html、markdown 等）

**--encoding=**_enc_
> 文件编码

**--add-extra-dicts=**_list_
> 额外的词典

**--personal=**_file_
> 个人词典文件

**--ignore=**_n_
> 忽略长度不超过 n 个字符的单词

**--ignore-case**
> 检查时不区分大小写

**dicts**
> 列出可用的词典

**dump** _mode_
> 导出词典信息

# CONFIGURATION

**/etc/aspell.conf**
> 系统级配置，用于设置默认语言、词典路径和选项。

**~/.aspell.conf**
> 用户级配置，覆盖系统默认值。

# CAVEATS

语言词典需要单独安装。个人词典格式与 ispell 不同。一些应用程序改用 hunspell。

# HISTORY

**aspell** 由 Kevin Atkinson 创建，于 **2001** 年首次发布，作为 ispell 的改进版本，具有更好的建议算法和 Unicode 支持。

# INSTALL

```apt: sudo apt install aspell```

```dnf: sudo dnf install aspell```

```pacman: sudo pacman -S aspell```

```apk: sudo apk add aspell```

```zypper: sudo zypper install aspell```

```brew: brew install aspell```

```nix: nix profile install nixpkgs#aspell```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ispell](/man/ispell)(1), [hunspell](/man/hunspell)(1), [spell](/man/spell)(1)
