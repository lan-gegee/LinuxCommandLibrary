# TAGLINE

获取或设置进程的 I/O 调度类别和优先级

# TLDR

以指定的 I/O **类别和优先级**运行命令

```ionice -c [1|2|3] -n [0-7] [command]```

按 **PID** 设置运行中进程的 I/O 类别

```ionice -c [class] -p [pid]```

**打印**进程的 I/O 调度类别和优先级

```ionice -p [pid]```

以 **idle** 优先级运行（仅在没有其他进程需要 I/O 时使用）

```ionice -c 3 [command]```

**忽略**设置优先级失败

```ionice -t -n [priority] -p [pid]```

# SYNOPSIS

**ionice** [_options_] [_command_]

# PARAMETERS

**-c**, **--class** _CLASS_
> 调度类别：1（实时）、2（尽力而为）、3（空闲）

**-n**, **--classdata** _LEVEL_
> 类别内的优先级：0（最高）到 7（最低）

**-p**, **--pid** _PID_
> 应用于给定 PID 的进程

**-P**, **--pgid** _PGID_
> 应用于进程组

**-u**, **--uid** _UID_
> 应用于某用户的全部进程

**-t**, **--ignore**
> 忽略设置优先级的失败

# DESCRIPTION

**ionice** 获取或设置进程的 I/O 调度类别和优先级，控制磁盘 I/O 请求相对于其他进程的调度方式。

**调度类别：**
- **Realtime (1)** - 最高优先级，保证 I/O 访问（需要 root）
- **Best-effort (2)** - 默认类别，根据优先级公平共享 I/O
- **Idle (3)** - 仅在没有其他进程需要时才获得 I/O 时间

# CAVEATS

只对 CFQ（Completely Fair Queuing）I/O 调度器有效。实时类别需要 root 权限。BFQ 和 mq-deadline 调度器的优先级语义不同。

# HISTORY

ionice 作为 util-linux 的一部分引入，让用户可以控制 CFQ I/O 调度器的优先级特性；该特性在 Linux 内核 2.6.13（**2005 年**）中加入。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nice](/man/nice)(1), [renice](/man/renice)(1)
