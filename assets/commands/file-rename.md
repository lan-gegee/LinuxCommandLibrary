# TAGLINE

基于 Perl 正则表达式的文件批量重命名

# TLDR

**用 Perl 表达式重命名**

```file-rename 's/old/new/' [files]```

**重命名为小写**

```file-rename 'y/A-Z/a-z/' [files]```

**试运行以预览更改**

```file-rename -n 's/pattern/replacement/' [files]```

**把空格替换为下划线**

```file-rename 's/ /_/g' [files]```

**为文件添加前缀**

```file-rename 's/^/prefix_/' [files]```

**修改文件扩展名**

```file-rename 's/\.jpeg$/.jpg/' [*.jpeg]```

**移除文件名中的编号前缀**

```file-rename 's/^\d+_//' [files]```

# SYNOPSIS

**file-rename** [_options_] _expression_ [_files_...]

# PARAMETERS

**-n**, **--no-act**
> 试运行，只显示将要进行的操作。

**-v**, **--verbose**
> 打印被重命名文件的名称。

**-f**, **--force**
> 覆盖已存在的文件。

**-0**, **--null**
> 从标准输入读取以空字符结尾的数据（配合 find -print0 使用）。

**-d**, **--filename**
> 只重命名文件名部分，不改动目录部分。

**-e** _expression_
> 对文件名应用表达式。多个 -e 选项可以串联使用。

# DESCRIPTION

**file-rename**（也称 rename 或 prename）使用 Perl 正则表达式重命名多个文件，提供强大的基于模式的转换能力。与简单的 mv 操作不同，它能够同时对多个文件名执行复杂的替换、大小写转换和模式匹配。

该工具支持完整的 Perl 正则语法，包括捕获组、前瞻/后顾断言和转换（transliteration）操作。常见用途包括批量重命名、删除或替换字符、修改文件扩展名以及统一文件名格式。

file-rename 的试运行模式（-n）可以在执行前预览更改，避免意外的破坏性操作。强制标志（-f）则允许在名字冲突时覆盖已有文件。

# CAVEATS

rename 存在多个实现。本文档介绍的是 Perl 版本（prename），而非 util-linux 版本。

# INSTALL

```nix: nix profile install nixpkgs#file-rename```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rename](/man/rename)(1), [mv](/man/mv)(1), [mmv](/man/mmv)(1), [find](/man/find)(1), [perl](/man/perl)(1), [sed](/man/sed)(1)
