# TAGLINE

逐行比较两个已排序的文件

# TLDR

**比较两个已排序的文件**

```comm [file1] [file2]```

**显示第一个文件独有的行**

```comm -23 [file1] [file2]```

**显示第二个文件独有的行**

```comm -13 [file1] [file2]```

**显示两个文件共有的行**

```comm -12 [file1] [file2]```

**使用自定义分隔符进行比较**

```comm --output-delimiter='|' [file1] [file2]```

**比较未排序的文件**

```comm <(sort [file1]) <(sort [file2])```

# SYNOPSIS

**comm** [_option_]... _file1_ _file2_

# DESCRIPTION

**comm** 逐行比较两个已排序的文件。它产生三列输出：file1 独有的行、file2 独有的行以及两者共有的行。属于 GNU coreutils。

# PARAMETERS

**-1**
> 抑制第 1 列（file1 独有的行）

**-2**
> 抑制第 2 列（file2 独有的行）

**-3**
> 抑制第 3 列（共有行）

**--check-order**
> 检查输入是否已正确排序

**--nocheck-order**
> 跳过排序顺序校验

**--output-delimiter=** _STR_
> 用 STR 分隔各列

**--total**
> 输出汇总计数

**-z**, **--zero-terminated**
> 行分隔符为 NUL

**--help**
> 显示帮助

**--version**
> 显示版本

# OUTPUT COLUMNS

```
unique_to_file1
        unique_to_file2
                common_to_both
```

# CAVEATS

输入文件必须已排序。未排序的文件可借助进程替换处理：comm <(sort f1) <(sort f2)。比较遵循 LC_COLLATE 规则。

# HISTORY

**comm** 源自 **AT&T Unix** 第 4 版（1973）。在 Linux 上属于 GNU coreutils。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sort](/man/sort)(1), [diff](/man/diff)(1), [uniq](/man/uniq)(1)
