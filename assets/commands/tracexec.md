# TAGLINE

用于 execve 系统调用和执行前行为的跟踪器

# TLDR

**跟踪 bash 发起的所有 exec 调用**

```tracexec log -- bash```

**启动 TUI 模式跟踪构建系统**

```tracexec tui -- make```

**使用伪终端的 TUI 模式**

```tracexec tui -t -- bash```

# SYNOPSIS

**tracexec** [_options_] _command_

# DESCRIPTION

**tracexec** 帮助你弄清楚运行一条命令时有哪些程序被执行、是如何执行的。它可用于调试构建系统、理解 shell 脚本，以及追踪专有软件会运行哪些程序。在使用伪终端的 TUI 模式下，你可以查看 exec 事件详情并与进程交互。

# HISTORY

**tracexec** 由 **Levi Zim**（kxxt）创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S tracexec```

```nix: nix profile install nixpkgs#tracexec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[strace](/man/strace)(1), [ltrace](/man/ltrace)(1)
