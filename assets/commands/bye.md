# TAGLINE

退出 Shell

# TLDR

**退出当前 shell** 会话

```bye```

**以特定状态码**退出

```bye [exit_code]```

# SYNOPSIS

**bye** [_n_]

# DESCRIPTION

**bye** 是一个 zsh 内置命令，用于终止当前 shell 会话。它在功能上与 **exit** 完全相同。调用时会先运行所有 **EXIT** trap 和 zshexit 钩子，然后关闭 shell。

如果提供了可选的数字参数，它会作为返回给父进程的退出状态。不带参数时，使用最后执行的命令的退出状态。

# CAVEATS

**bye** 为 zsh 特有，在 bash 或其他 shell 中不可用。为了可移植性，请改用 **exit**。如果有正在运行的后台作业，zsh 在第一次尝试退出时可能会发出警告。

# HISTORY

**bye** 作为 **exit** 的便捷别名被包含在 **zsh** 中，反映了 FTP 客户端等交互式系统和一些早期 Unix shell 中常见的命令用法。

# SEE ALSO

[exit](/man/exit)(1), [logout](/man/logout)(1), [zsh](/man/zsh)(1)
