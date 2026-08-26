# TAGLINE

用指定命令替换当前进程的 Shell 内建命令

# TLDR

**执行**指定命令并**替换**当前 Shell

```exec [command -with -flags]```

以**空环境**执行

```exec -c [command -with -flags]```

作为**登录 Shell** 执行

```exec -l [command -with -flags]```

以**其他名称**作为 argv[0] 执行

```exec -a [name] [command -with -flags]```

将 Shell 的所有 **stdout 重定向**到文件

```exec >[path/to/logfile]```

将 **stdout 和 stderr 一并重定向**到文件

```exec >[path/to/logfile] 2>&1```

在**文件描述符** 3 上打开一个文件用于读取

```exec 3<[path/to/file]```

**关闭**文件描述符 3

```exec 3>&-```

# SYNOPSIS

**exec** [_-cl_] [_-a name_] [_command_] [_arguments_] [_redirection ..._]

# PARAMETERS

**-c**
> 以基本为空的环境执行命令，清除继承的环境变量。

**-l**
> 在 argv[0] 开头放置一个短横线，使该命令表现为登录 Shell。

**-a** _name_
> 将 _name_ 作为 argv[0] 传给所执行的命令，而非实际的命令名。

# DESCRIPTION

**exec** 用指定的命令替换当前 shell 进程，不创建子进程。exec 完成后，shell 会话即告结束，因为 shell 进程已不复存在。

如果未指定命令但提供了重定向，这些重定向将在当前 Shell 中生效。这样可以为后续的所有命令重定向 stdin、stdout 或 stderr，并打开或关闭任意文件描述符。

如果命令无法执行，非交互式 Shell 会退出，除非设置了 **execfail** shell 选项。交互式 Shell 在 exec 失败时不会退出。

# CAVEATS

Shell 内建命令。exec 完成后 Shell 即终止，因此脚本中位于 exec 之后的任何命令都不会运行。不带命令的文件描述符重定向会在当前 Shell 中持续生效。bash、zsh 及其他 POSIX Shell 之间的行为可能略有差异。

# INSTALL

```apk: sudo apk add execline```

```brew: brew install execline```

```nix: nix profile install nixpkgs#execline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [sh](/man/sh)(1), [env](/man/env)(1), [zsh](/man/zsh)(1)
