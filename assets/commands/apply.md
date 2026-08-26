# TAGLINE

对成组的参数重复执行某个命令。

# TLDR

**对每个参数应用一个命令**

```apply [command] [arg1] [arg2] [arg3]```

**使用占位符应用命令**

```apply "diff %1 %2" [file1] [file2] [file3] [file4]```

以**每次调用固定数量的参数**应用

```apply -2 diff [file1] [file2] [file3] [file4]```

**对每个文件执行 echo**（效果类似 ls）

```apply echo *```

**试运行**：显示将要运行的命令但不执行

```apply -d echo *```

**每个参数运行一次命令且不传入参数**

```apply -0 who [a] [b] [c]```

# SYNOPSIS

**apply** [**-a** _char_] [**-d**] [**-#**] _command_ _argument_...

# PARAMETERS

**-a** _char_
> 使用 _char_ 作为占位符（magic）字符，代替默认的 **%**。

**-#**
> 数字标志（如 **-2**）设置每次调用传入多少个参数。默认是 **-1**（每次一个参数）。使用 **-0** 时，命令对每个参数运行一次但不传入任何参数。如果命令中出现 **%d** 序列则忽略此项。

**-d**
> 试运行：打印将被执行的命令但不实际运行。

**%n**
> 在命令字符串中，**%1**、**%2**、... **%9** 分别替换为第 1、2、... 个尚未使用的参数。

# DESCRIPTION

**apply** 反复运行一个命令，每次调用传入指定数量的参数。它为跨多个参数执行命令提供了 **xargs** 或 Shell 循环之外的简单替代方案。

默认情况下，apply 每次向命令传递一个参数。使用 **-2** 时会将参数两两分组，适用于 **diff** 或 **cmp** 这类接收两个文件的命令。**%n** 占位符允许在命令字符串中灵活安排参数位置。

当命令包含空格或特殊字符时应当加引号。不使用占位符时，参数会追加到命令末尾。

# CAVEATS

此命令主要见于 BSD 系统和 macOS；不属于 GNU coreutils。Linux 用户通常改用 **xargs** 或 Shell 循环。使用 **-n** 时，参数总数必须能被 n 整除。

# HISTORY

**apply** 命令起源于 **20 世纪 80 年代**的 BSD Unix。在 **xargs** 和 **find -exec** 等更完善的工具普及之前，它提供了一种简单的命令迭代机制。该命令在 FreeBSD、OpenBSD 和 macOS 上仍然可用，但从未在 Linux 系统上广泛流行。

# INSTALL

```aur: yay -S outils-apply```

```apk: sudo apk add outils-apply```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[xargs](/man/xargs)(1), [parallel](/man/parallel)(1), [find](/man/find)(1)

# RESOURCES

```[Source code](https://github.com/freebsd/freebsd-src)```

```[Documentation](https://man.freebsd.org/cgi/man.cgi?apply)```

<!-- verified: 2026-06-11 -->
