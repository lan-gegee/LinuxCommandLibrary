# TAGLINE

将运行中的进程重新连接到新终端

# TLDR

将进程**接入**当前终端

```reptyr [pid]```

按**进程名**接入

```reptyr $(pidof [htop])```

# SYNOPSIS

**reptyr** [**-s**] [**-T**] _pid_

# PARAMETERS

**-s**
> 通过 script 方式接入（兼容性更好）

**-T**
> 接入进程及其子进程

**-l**
> 列出可接入的 PID

**-v**
> 详细输出

**pid**
> 要接入的进程 ID

# DESCRIPTION

**reptyr** 将运行中的进程移动到新终端。当你在普通终端中启动了长时间运行的命令，之后才意识到它应该在 screen 或 tmux 中运行时，该工具非常宝贵。

它使用 ptrace 重新设置进程的控制终端，使其能够从新终端接收输入并向其发送输出。

# CAVEATS

需要 ptrace 能力（可能需要 root 或调整 sysctl）。某些进程可能因终端状态而无法工作。先用 Ctrl+Z 和 bg 将进程放入后台。进程必须属于当前用户。

# HISTORY

**reptyr** 由 **Nelson Elhage** 创建，用于解决一个常见问题：希望把运行中的进程移动到另一个终端或 screen 会话，而又不想重启它。

# INSTALL

```apt: sudo apt install reptyr```

```dnf: sudo dnf install reptyr```

```pacman: sudo pacman -S reptyr```

```apk: sudo apk add reptyr```

```zypper: sudo zypper install reptyr```

```nix: nix profile install nixpkgs#reptyr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[screen](/man/screen)(1), [tmux](/man/tmux)(1), [nohup](/man/nohup)(1), [disown](/man/disown)(1)
