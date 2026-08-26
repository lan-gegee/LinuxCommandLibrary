# TAGLINE

将 awk 脚本转换为 Perl

# TLDR

**转换** awk 脚本为 Perl

```a2p [script.awk] > [script.pl]```

以**指定字段分隔符**转换

```a2p -F: [script.awk] > [script.pl]```

转换并**禁用空白切分**

```a2p -n [script.awk] > [script.pl]```

# SYNOPSIS

**a2p** [_-Dnumber_] [_-Fcharacter_] [_-n_] [_-o_] [_filename_]

# DESCRIPTION

**a2p**（awk to perl）是一个把 awk 脚本转换为 Perl 程序的翻译器。它读取命令行指定的 awk 脚本（未给文件时从标准输入读取），并将等价的 Perl 代码输出到标准输出。

生成的 Perl 代码会尽量贴近地模仿 awk 的行为，包括隐式输入循环、字段切分、模式匹配和输出格式的处理。虽然输出可能不是最优雅的 Perl 代码，但它为迁移提供了可用的起点。

# PARAMETERS

**-D**_number_
> 设置调试标志

**-F**_character_
> 指定字段分隔符（对应 awk 的 -F 选项）。默认按空白字符切分字段

**-n**
> 禁用对输入行的自动 split()。想手动处理行切分时使用此选项

**-o**
> 在输出的 Perl 代码中以注释形式打印原 awk 脚本。便于对比原始代码与转换后的代码

# CAVEATS

生成的 Perl 代码可能需要手动清理，才能获得更好的风格和性能。一些复杂的 awk 结构或 GNU awk 扩展可能无法完美转换。该翻译器假定的是 POSIX awk 行为。

**a2p** 已被弃用，并在 Perl 5.22（2015 年）中从 Perl 核心发行版中移除。现代 Perl 不再附带它。请只在较旧的系统上使用它，或者直接用 Perl 重写 awk 脚本。

# HISTORY

**a2p** 由 Perl 之父 Larry Wall 编写，最早随 **1987 年**发布的 Perl 1.0 一同出现。在 Perl 被定位为 awk、sed 和 shell 脚本替代品的年代，它是最早一批帮助用户从 Unix 脚本工具迁移到 Perl 的工具之一。它在 Perl 5.22（2015 年）中被移出 Perl 核心发行版。

# INSTALL

```apk: sudo apk add perl-app-a2p```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[awk](/man/awk)(1), [perl](/man/perl)(1)

# RESOURCES

```[Homepage](https://www.perl.org/)```

```[Documentation](https://perldoc.perl.org/perl5220delta)```

<!-- verified: 2026-06-10 -->
