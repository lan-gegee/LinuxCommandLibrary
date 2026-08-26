# TAGLINE

处理 Shell 信号与清理工作

# TLDR

**列出**可用的信号名称

```trap -l```

列出当前的 **trap 命令**及其关联信号

```trap```

**收到信号时执行**命令

```trap 'echo "Caught signal SIGHUP"' SIGHUP```

**移除**信号的 trap 命令

```trap - SIGHUP SIGINT```

**忽略**某个信号

```trap '' SIGINT```

# SYNOPSIS

**trap** [_command_] [_signal_...]

**trap** **-l**

**trap** **-p** [_signal_...]

# PARAMETERS

**-l**
> 列出信号名称和编号

**-p** [_signal_]
> 打印指定信号的 trap 命令

_command_
> 收到信号时要执行的命令

**-** _signal_
> 将信号重置为默认行为

**''** _signal_
> 忽略该信号

# DESCRIPTION

**trap** 是一个 Shell 内建命令，在 Shell 收到信号时执行指定命令。它常用于脚本中的清理操作（删除临时文件）、优雅地处理中断，以及忽略那些原本会终止脚本的信号。

常见信号包括 SIGINT（Ctrl+C）、SIGTERM（终止请求）、SIGHUP（挂起）、EXIT（脚本退出）和 ERR（命令出错）。EXIT 伪信号会在脚本正常退出时触发。

# CAVEATS

trap 是 Shell 内建命令，不是外部命令。不同 Shell（bash、dash、zsh）之间的行为略有差异。某些信号（SIGKILL、SIGSTOP）无法被捕获。trap 会被子 Shell 继承，但不会被外部命令继承。

# HISTORY

起源于 Unix V7 (1979) 的 **Bourne shell**。捕获信号的概念来自 Unix 的信号处理机制。Bash 和其他现代 Shell 通过 ERR、DEBUG 等伪信号扩展了原有功能。

# INSTALL

```apk: sudo apk add execline```

```brew: brew install execline```

```nix: nix profile install nixpkgs#execline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kill](/man/kill)(1), [bash](/man/bash)(1)
