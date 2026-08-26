# TAGLINE

使用 Perl 表达式重命名文件

# TLDR

**用 Perl 表达式重命名**

```prename 's/old/new/' [*.txt]```

**试运行**

```prename -n 's/pattern/replacement/' [files]```

**文件名转为小写**

```prename 'y/A-Z/a-z/' [*]```

**移除空格**

```prename 's/ /_/g' [*]```

**添加前缀**

```prename 's/^/prefix_/' [*]```

**在扩展名前添加后缀**

```prename 's/(\.[^.]+)$/_suffix$1/' [*]```

**详细输出**

```prename -v 's/old/new/' [files]```

# SYNOPSIS

**prename** [_-n_] [_-v_] [_-f_] _expression_ _files_

# PARAMETERS

**-n**, **--no-act**
> 试运行，显示将要进行的更改。

**-v**, **--verbose**
> 显示重命名操作。

**-f**, **--force**
> 覆盖已存在的文件。

**-0**, **--null**
> 以 null 分隔输入。

**-e** _EXPR_
> 要应用的表达式。

**-E** _EXPR_
> 类似 -e，但不产生警告。

# DESCRIPTION

**prename**（Perl rename）使用 Perl 表达式重命名文件。它提供强大的基于模式的重命名能力。

s/// 替换运算符用于替换文本。全局标志 g 替换所有匹配项。

转换运算符 y/// 用于变换字符集。对大小写转换很有用。

Perl 代码可以用 $_ 引用文件名。复杂的变换都可以实现。

试运行会显示将会发生什么。应用前务必先测试模式。

多个表达式可串联变换。每个 -e 会追加一个操作。

# CAVEATS

需要 Perl 语法。可能与 util-linux 的 rename 冲突。必要时使用完整路径。

# HISTORY

**prename** 由 **Larry Wall**（Perl 之父）编写，通常随 Perl 以 **rename** 的名称发行。它与更简单的 util-linux rename 命令不同。

# INSTALL

```dnf: sudo dnf install prename```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rename](/man/rename)(1), [mv](/man/mv)(1), [mmv](/man/mmv)(1), [perl](/man/perl)(1)
