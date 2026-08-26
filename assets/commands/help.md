# TAGLINE

显示 shell 内建命令的相关信息

# TLDR

**获取内建命令的帮助**

```help [cd]```

**列出所有内建命令**

```help```

**简短描述**

```help -d [command]```

**man page 格式**

```help -m [command]```

**显示用法概要**

```help -s [command]```

# SYNOPSIS

**help** [_options_] [_pattern_]

# PARAMETERS

_PATTERN_
> Shell 内建命令名称或模式。

**-d**
> 仅显示简短描述。

**-m**
> 以 man page 格式显示。

**-s**
> 仅显示用法概要。

# DESCRIPTION

**help** 显示 shell 内建命令的相关信息。它是一个 Bash 内建命令，为 shell 内建的命令提供文档。

该命令显示 Bash 内建命令的用法、选项和描述。适合用于了解 cd、export、source 等命令。

# CAVEATS

仅限 Bash 使用。只适用于内建命令，不适用于外部命令。外部命令请使用 man。

# HISTORY

help 自早期版本起就是 **Bash** 的一部分，为 shell 命令提供内置文档。

# SEE ALSO

[man](/man/man)(1), [info](/man/info)(1), [bash](/man/bash)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/bash.git)```

```[Homepage](https://www.gnu.org/software/bash/)```

```[Documentation](https://www.gnu.org/software/bash/manual/)```

<!-- verified: 2026-07-19 -->
