# TAGLINE

生成顺序数据或随机数据

# TLDR

**生成序列**

```jot [10]```

**生成数值范围**

```jot [10] [1] [100]```

**按步长生成**

```jot - [1] [100] [5]```

**随机数**

```jot -r [5] [1] [100]```

**重复字符串**

```jot -b [string] [5]```

**格式化输出**

```jot -w "[%02d]" [10]```

# SYNOPSIS

**jot** [_options_] [_reps_ [_begin_ [_end_ [_step_]]]]

# PARAMETERS

_REPS_
> 重复次数。

_BEGIN_
> 起始值。

_END_
> 结束值。

_STEP_
> 步长。

**-r**
> 随机值。

**-b** _STRING_
> 重复字符串。

**-w** _FORMAT_
> printf 格式。

**-s** _STRING_
> 分隔符。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jot** 用于生成顺序数据或随机数据。它可以产出数字、字符或格式化的字符串。

该工具适合生成测试数据和数列，支持多种输出格式。

# CAVEATS

BSD 工具。不在 GNU coreutils 中。如需可移植性请改用 seq。

# HISTORY

jot 起源于 **BSD Unix**，是一个数据生成工具。它比 seq 更加灵活。

# INSTALL

```apt: sudo apt install athena-jot```

```apk: sudo apk add outils-jot```

```brew: brew install jot```

```nix: nix profile install nixpkgs#jot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[seq](/man/seq)(1), [yes](/man/yes)(1), [printf](/man/printf)(1)
