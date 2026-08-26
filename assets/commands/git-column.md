# TAGLINE

按列显示数据

# TLDR

**将输入排成多列（列优先布局）**

```seq 1 24 | git column --mode=column --padding=[5]```

**将输入排成多列（行优先布局）**

```seq 1 21 | git column --mode=row --padding=[5]```

**按指定的终端宽度排版输入**

```echo "[one two three four five six]" | git column --mode=column --width=[40]```

**为每行添加缩进**

```seq 1 12 | git column --mode=column --indent="[  ]"```

# SYNOPSIS

**git** **column** [_options_]

# PARAMETERS

**--command** _name_
> 通过配置变量 column._name_ 和 column.ui 查找布局模式。

**--mode** _mode_
> 指定布局模式。支持的值包括 column（自上而下填充列）、row（从左到右填充行）和 plain（不排版）。

**--raw-mode** _n_
> 与 **--mode** 相同，但接受以数字编码的模式。主要供已解析过布局模式的其他命令使用。

**--width** _width_
> 指定终端宽度。默认情况下 **git column** 会检测终端宽度，检测不到时回退到 80。

**--indent** _string_
> 打印在每行开头的字符串。

**--nl** _string_
> 打印在每行末尾的字符串，含换行符。

**--padding** _N_
> 列之间的空格数量。默认为一个空格。

# DESCRIPTION

**git column** 是一个实用命令，将标准输入排版为多列表格，每行输入占据一个单元格。Git 内部主要用它以节省空间的列式格式显示各种列表（如分支名、标签列表或文件清单），但它也可以作为独立的格式化工具使用。

该命令从标准输入读取数据，根据终端宽度或指定约束将其排成多列。它支持不同的布局模式：列优先（自上而下填充列）、行优先（从左到右填充行）或 plain（不排版）。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[column](/man/column)(1), [git-branch](/man/git-branch)(1), [git-tag](/man/git-tag)(1)
