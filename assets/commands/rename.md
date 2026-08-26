# TAGLINE

批量重命名多个文件

# TLDR

**rename** 可能指向多个同名命令

查看 **Perl 版本**的文档

```tldr perl-rename```

查看 **util-linux 版本**的文档

```tldr rename.util```

# SYNOPSIS

**rename** [_options_] _expression_ _replacement_ _files_...

# DESCRIPTION

**rename** 是一个批量重命名文件的命令。存在两种主要实现：

**Perl rename**（也称为 prename 或 rename.ul）使用 Perl 正则表达式实现强大的模式匹配。常见于基于 Debian 的系统。

**util-linux rename** 使用简单的字符串替换。它替换每个文件名中第一次出现的字符串。常见于基于 Red Hat 的系统。

使用 **rename --version** 或 **file $(which rename)** 检查安装的是哪个版本。

# INSTALL

```apk: sudo apk add util-linux-misc```

```brew: brew install rename```

```nix: nix profile install nixpkgs#rename```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[perl-rename](/man/perl-rename)(1), [rename.util](/man/rename.util)(1), [mv](/man/mv)(1), [mmv](/man/mmv)(1)
