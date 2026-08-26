# TAGLINE

终止当前 Shell 或脚本的 Shell 内建命令

# TLDR

以成功状态**退出 Shell**

```exit```

**以指定的**状态码退出

```exit [1]```

脚本中**出错时退出**

```set -e; exit```

# SYNOPSIS

**exit** [_status_]

# PARAMETERS

_STATUS_
> 退出状态码（0-255）。0 表示成功。

# DESCRIPTION

**exit** 是一个 shell 内建命令，用于终止当前 Shell 或脚本。可选的退出状态会传递给父进程；按惯例 0 表示成功。

在脚本中，exit 会立即停止执行。在交互式 Shell 中，它会结束当前会话。父进程可以通过 shell 脚本中的 $? 获取退出状态。

退出码具有约定俗成的含义：0 表示成功，1 表示一般错误，2 表示用法错误，126-127 表示执行问题。

# CAVEATS

非零退出可能触发 set -e 终止脚本。状态码限于 0-255。子 Shell 的退出相互独立。trap 可能在实际退出前运行。

# HISTORY

exit 是 POSIX shell 的基本内建命令，自原始 Bourne shell 起就存在。其语义在所有 Unix Shell 中保持一致。

# INSTALL

```apk: sudo apk add execline```

```brew: brew install execline```

```nix: nix profile install nixpkgs#execline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [trap](/man/trap)(1)
