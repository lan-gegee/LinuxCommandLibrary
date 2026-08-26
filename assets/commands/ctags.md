# TAGLINE

源代码标签索引生成器

# TLDR

为当前目录**生成标签**

```ctags *```

递归**生成标签**

```ctags -R```

为特定文件**生成标签**

```ctags [file1.c] [file2.c]```

输出到指定文件

```ctags -f [tags] -R [src/]```

追加到已有的标签文件

```ctags -a [newfile.c]```

列出支持的语言

```ctags --list-languages```

列出某种语言的标签种类

```ctags --list-kinds=[c]```

# SYNOPSIS

**ctags** [_options_] [_file_...]

# DESCRIPTION

**ctags** 生成索引文件（tags），将源代码中的标识符映射到其定义处。这使文本编辑器和 IDE 能够在大型代码库中快速跳转到函数定义、类声明、变量及其他编程结构。

该工具解析数十种编程语言的源代码，提取函数名、类、方法、变量、宏和类型定义等符号。它会创建一个 tags 文件（默认名为 **tags**），其中包含符号名称、所在文件位置以及用于定位它的搜索模式。

Vim、Emacs 等现代编辑器及众多 IDE 都使用 ctags 文件来实现"跳转到定义"、符号补全和代码导航等功能。Universal Ctags 是持续维护的分支，比原版 Exuberant Ctags 支持更多语言和特性。

# PARAMETERS

**-R**, **--recurse**
> 递归处理目录

**-f** _file_, **-o** _file_
> 将标签输出到文件

**-a**, **--append**
> 追加到已有的标签文件

**-L** _file_, **--file-list** _file_
> 从文件读取文件名列表

**--languages** _list_
> 只处理指定语言

**--language-force** _lang_
> 强制使用指定语言

**--exclude** _pattern_
> 排除匹配模式的文件

**--extras** _flags_
> 额外的标签条目

**--fields** _flags_
> 要包含的字段

**--kinds-\<lang\>** _kinds_
> 要包含的标签种类

**--list-languages**
> 列出支持的语言

**--list-kinds**[=_lang_]
> 列出标签种类

**--list-maps**
> 列出文件扩展名映射

# CONFIGURATION

**~/.ctags**
> 用户配置文件，用于设置标签生成选项和语言定义。

**~/.ctags.d/**
> 存放模块化配置文件的目录，可针对不同语言和设置分别配置。

**.ctags.d/**
> 项目级配置目录，用于仓库专属的标签设置。

# TAG KINDS

**c**：类

**f**：函数

**m**：类成员

**v**：变量

**t**：类型定义

**d**：宏定义

# IMPLEMENTATIONS

**Universal Ctags**：持续维护的分支

**Exuberant Ctags**：最初版本（已停止维护）

# CAVEATS

输出文件默认名为 'tags'。可与 Vim 的 :tag 命令或 Ctrl-] 配合使用。建议使用 Universal Ctags 而非 Exuberant Ctags。大型代码库可能生成很大的标签文件。代码变更后需重新生成。

# HISTORY

**ctags** 最初于 20 世纪 70 年代末作为 BSD Unix 项目的一部分开发。Darren Hiebert 编写的 **Exuberant Ctags** 于 1996 年成为主流实现，增加了对众多语言的支持。**Universal Ctags** 于 2014 年从其分叉而来，是现在持续维护的版本，支持现代语言。

# INSTALL

```dnf: sudo dnf install ctags```

```pacman: sudo pacman -S ctags```

```apk: sudo apk add ctags```

```zypper: sudo zypper install ctags```

```brew: brew install ctags```

```nix: nix profile install nixpkgs#ctags```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[etags](/man/etags)(1), [vim](/man/vim)(1), [cscope](/man/cscope)(1)

# RESOURCES

```[Source code](https://github.com/universal-ctags/ctags)```

```[Homepage](https://ctags.io)```

```[Documentation](https://docs.ctags.io)```

<!-- verified: 2026-06-26 -->
