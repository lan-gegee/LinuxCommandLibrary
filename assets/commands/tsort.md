# TAGLINE

对依赖对进行拓扑排序

# TLDR

**排序依赖**

```tsort [dependencies.txt]```

**从标准输入读取**

```echo -e "a b\nb c" | tsort```

**对 makefile 依赖排序**

```tsort [makefile_deps]```

# SYNOPSIS

**tsort** [_OPTION_] [_FILE_]

# PARAMETERS

_FILE_
> 包含以空白分隔的依赖对的输入文件。不指定文件（或使用 `-`）时，从标准输入读取。

**--help**
> 显示帮助信息。

**--version**
> 输出版本信息并退出。

# DESCRIPTION

**tsort** 对从标准输入或文件读取的一组依赖对执行拓扑排序。每行包含两个以空白分隔的项，第一项依赖于第二项。输出会按某种顺序列出所有项，保证每个被依赖项都出现在依赖它的项之前。

该工具常用于构建系统中确定编译顺序、在软件包管理器中解析安装顺序，以及任何必须按依赖顺序处理条目的场景。如果输入中存在环（循环依赖），tsort 会报告错误，因为不存在有效的排序。

输入行上只有单个项时，会引入该项而不声明依赖关系，确保它出现在输出中。

# INPUT FORMAT

```
a b    # a depends on b
b c    # b depends on c
c d    # c depends on d
```

# OUTPUT

按依赖顺序排列的项：d, c, b, a

# EXAMPLE

```
$ echo -e "main util\nutil lib\nlib" | tsort
lib
util
main
```

# CAVEATS

能检测环但无法解决。每行只能有一个依赖对。各项以空白分隔。

# HISTORY

**tsort** 是 POSIX 的一部分，自 Unix 早期版本就已存在。它最初用于在链接器命令中为目标文件排序。

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

[sort](/man/sort)(1), [make](/man/make)(1)
