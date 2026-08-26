# TAGLINE

双向文本分页器

# TLDR

**查看文件内容**

```yap [file]```

**以指定页面大小查看**

```yap -[20] [file]```

**查看时不清屏**

```yap -c [file]```

**禁用下划线处理**

```yap -u [file]```

**显示行号**

```yap -n [file]```

**从指定行开始查看**

```yap +[100] [file]```

# SYNOPSIS

**yap** [-cnuq] [-_num_] [+_command_] [_file_...]

# PARAMETERS

**-**_num_
> 将页面大小设置为 num 行。

**-c**
> 每页滚动显示而不是清除屏幕。

**-u**
> 对 nroff 输出禁用下划线处理。

**-n**
> 显示行号。

**-q**
> 仅在显式退出命令时才退出。

**+**_command_
> 启动时执行命令。

# COMMANDS

**SPACE**：显示下一页。

**RETURN**：显示下一行。

**b**：向后翻页。

**s**：向前跳过若干行。

**f**：向前跳过若干页。

**g**：跳到文件开头。

**G**：跳到文件末尾。

**/pattern**：向后搜索 pattern（正向）。

**?pattern**：向前搜索 pattern（反向）。

**n**：重复上一次搜索。

**m**：在当前页设置标记。

**'**：返回标记处。

**h**：显示帮助。

**q** 或 **Q**：退出。

# DESCRIPTION

**yap**（Yet Another Pager）是一个文本文件查看器，每次显示一屏内容。它的特色功能是双向翻页，即使从标准输入读取时也能前后导航。

该分页器能处理 nroff 格式的文本，针对终端适当地处理下划线和粗体序列。它支持搜索、位置标记以及与其他 Unix 分页器类似的各种导航命令。

# ENVIRONMENT

**YAP**：预设的默认选项标志。

**TERM**：用于屏幕处理的终端类型。

# CAVEATS

在现代系统上较少见。大多数用户更喜欢 less 或 more，它们提供类似的功能以及更多特性。

# HISTORY

**yap** 是为 MINIX（Andrew S. Tanenbaum 的类 Unix 教学操作系统）开发的。它提供了基本的分页功能，并显著地增加了向后滚动能力，这是原始 more 命令所不具备的。后来 less 分页器凭借类似的双向能力成为了标准方案。

# INSTALL

```brew: brew install yap```

```nix: nix profile install nixpkgs#yap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [more](/man/more)(1), [pg](/man/pg)(1), [cat](/man/cat)(1)
