# TAGLINE

在终端中打印水平分隔线

# TLDR

**使用默认的 # 字符打印水平线**

```hr```

**用指定字符打印水平线**

```hr [=]```

**用不同字符打印多条水平线**

```hr [#] [-]```

**用多字符模式打印水平线**

```hr [-#-]```

# SYNOPSIS

**hr** [_characters_ ...]

# DESCRIPTION

**hr** 打印横跨整个终端宽度的水平分隔线。每个参数用作在一行内重复的字符或模式。若不给参数，默认使用 **#**。多个参数会产出多行，一个参数一行。

终端宽度由 `tput cols` 决定；若不可用，则回退到 **COLUMNS** 环境变量，若两者都不可用则使用 80 列。

# CAVEATS

存在多个功能各异的 **hr** 实现。最常见的（LuRsT/hr）是一个纯 Bash 脚本，没有任何标志或选项。其他实现可能支持颜色或宽度控制等额外特性。

# INSTALL

```apk: sudo apk add hr```

```brew: brew install hr```

```nix: nix profile install nixpkgs#hr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[echo](/man/echo)(1), [printf](/man/printf)(1), [tput](/man/tput)(1)
