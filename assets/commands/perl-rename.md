# TAGLINE

使用 Perl 正则表达式重命名文件

# TLDR

**用正则替换重命名**

```perl-rename 's/old/new/' [*.txt]```

**文件名转小写**

```perl-rename 'y/A-Z/a-z/' [*]```

**文件名转大写**

```perl-rename 'y/a-z/A-Z/' [*]```

**添加前缀**

```perl-rename 's/^/prefix_/' [*]```

**在扩展名前添加后缀**

```perl-rename 's/(\.\w+)$/_suffix$1/' [*]```

**预览更改**（试运行）

```perl-rename -n 's/old/new/' [*.txt]```

**把空格替换为下划线**

```perl-rename 's/ /_/g' [*]```

**从名称中去除数字**

```perl-rename 's/\d//g' [*]```

# SYNOPSIS

**perl-rename** [_-n_] [_-v_] [_-f_] _expression_ [_files_]

# PARAMETERS

**-n**, **--no-act**
> 试运行，只显示将会发生的改动。

**-v**, **--verbose**
> 在重命名发生时将其显示出来。

**-f**, **--force**
> 覆盖已存在的文件。

**-0**, **--null**
> 从 stdin 读取以 NUL 结尾的文件名。

**-d**, **--filename**
> 仅重命名文件名，不处理目录。

**-e** _EXPR_
> 表达式（可以使用多个）。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# DESCRIPTION

**perl-rename** 使用 Perl 正则表达式重命名文件。在批量重命名方面比基本的 mv 更强大。

表达式会修改包含文件名的 $_ 变量。常见操作是用 s/// 做替换、用 y/// 做字符转换。

Perl 完整的正则语法都可用：字符类、反向引用、前瞻断言等。多个 -e 表达式可以串联使用。

试运行模式（-n）只显示更改而不执行。处理复杂表达式时应先用它验证一遍。

该工具能正确处理文件名中的特殊字符、空格和 Unicode。给表达式加引号可以防止 Shell 解释。

不同的系统可能把这个命令叫作 rename、prename 或 file-rename。底层功能是相同的。

# CAVEATS

表达式出错可能导致文件被错误重命名。请先用 -n。在某些系统上可能与 util-linux 的 rename 冲突。需要 Perl。

# HISTORY

**perl-rename** 由 Perl 之父 **Larry Wall** 编写，作为一个示例脚本分发。有多种打包版本，包括 prename（Debian）和 file-rename。它展示了 Perl 的文本处理能力在实际文件管理中的应用。

# INSTALL

```pacman: sudo pacman -S perl-rename```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rename](/man/rename)(1), [mmv](/man/mmv)(1), [mv](/man/mv)(1), [perl](/man/perl)(1)
