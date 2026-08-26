# TAGLINE

停止 pueue 守护进程

# TLDR

**关闭 pueue 守护进程**

```pueue shutdown```

# SYNOPSIS

**pueue** **shutdown**

# DESCRIPTION

**pueue shutdown** 远程关闭 pueue 守护进程。所有正在运行的任务都会被终止。排队和暂存的任务保持原状态，在守护进程重启后恢复。仅当守护进程不是由服务管理器启动时才应使用此命令。

# CAVEATS

运行中的任务会被立即终止而不会执行完成。如果守护进程由服务管理器（如 systemd）启动，请改用该服务管理器来停止它。

# INSTALL

```pacman: sudo pacman -S pueue```

```apk: sudo apk add pueue```

```zypper: sudo zypper install pueue```

```brew: brew install pueue```

```nix: nix profile install nixpkgs#pueue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pueue](/man/pueue)(1), [pueue-status](/man/pueue-status)(1), [pueue-stash](/man/pueue-stash)(1)
