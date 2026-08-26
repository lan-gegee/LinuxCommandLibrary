# TAGLINE

显示 Poetry 命令帮助

# TLDR

**显示一般帮助**

```poetry help```

**获取某命令的帮助**

```poetry help [command]```

**显示 install 的帮助**

```poetry help install```

# SYNOPSIS

**poetry help** [_command_]

# PARAMETERS

_COMMAND_
> 要获取帮助的命令。

# DESCRIPTION

**poetry help** 显示 Poetry 命令的帮助信息，包括可用选项、参数和用法示例。不带参数调用时显示 Poetry 的一般帮助；给定命令名时显示该特定命令的详细帮助。

这等同于在任何 Poetry 命令上使用 **--help** 标志。

# CAVEATS

也可通过 --help 标志获取。

# HISTORY

poetry help 为 Poetry 命令提供**内置文档**。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1)
