# TAGLINE

控制 Ctrl+Alt+Del 组合键的行为

# TLDR

**获取**当前设置

```ctrlaltdel```

将 Ctrl+Alt+Del 设置为**立即**重启（硬重启）

```sudo ctrlaltdel hard```

将 Ctrl+Alt+Del 设置为**平稳**重启（软重启）

```sudo ctrlaltdel soft```

# SYNOPSIS

**ctrlaltdel** [_hard_|_soft_]

# DESCRIPTION

**ctrlaltdel** 控制内核在控制台上按下 Ctrl+Alt+Del 时的行为。该设置决定系统是立即重启，还是允许进程平稳关闭。

设为 "hard" 时，系统立即重启。设为 "soft" 时，会向 PID 1（init/systemd）发送 SIGINT 信号，由其执行平稳关机。

# PARAMETERS

**hard**
> 不做任何准备立即重启

**soft**
> 向 init 发送 SIGINT 以实现平稳重启

# CAVEATS

更改该设置需要 root 权限。属于 util-linux。在现代 systemd 系统上，无论此设置如何，Ctrl+Alt+Del 信号都由 systemd 处理。

# HISTORY

这一控制机制源自早期 Unix 时代，当时人们普遍直接使用物理控制台。选择三键组合正是为了使其难以被误按。

# INSTALL

```apt: sudo apt install util-linux-extra```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[reboot](/man/reboot)(8), [shutdown](/man/shutdown)(8), [systemctl](/man/systemctl)(1)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

<!-- verified: 2026-06-26 -->
