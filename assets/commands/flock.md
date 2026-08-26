# TAGLINE

在 Shell 脚本中管理咨询性文件锁

# TLDR

以**文件锁**运行命令

```flock /tmp/lock.lock command```

以**非阻塞**方式运行（已加锁则失败）

```flock -n /tmp/lock.lock command```

以 10 秒**超时**运行

```flock -w 10 /tmp/lock.lock command```

加锁失败时使用**自定义退出码**

```flock -n -E 42 /tmp/lock.lock command```

持锁执行 **shell 命令**

```flock /tmp/lock.lock -c "command1 && command2"```

使用**共享**（读）锁

```flock -s /tmp/lock.lock command```

# SYNOPSIS

**flock** [_options_] _file_|_directory_ _command_ [_arguments_]

**flock** [_options_] _file_|_directory_ **-c** _command_

**flock** [_options_] _number_

# DESCRIPTION

**flock** 在 Shell 脚本中管理文件锁。它在持有指定文件或目录上的锁的同时执行命令，必要时会创建锁文件。默认情况下，该命令会无限等待锁变为可用。这可用于确保同一时间只有一个命令实例在运行。

# PARAMETERS

**-c, --command**
> 通过 shell 执行单条命令字符串

**-e, -x, --exclusive**
> 获取排他（写）锁（默认）

**-s, --shared**
> 获取共享（读）锁

**-n, --nb, --nonblock**
> 锁不可用时立即失败

**-w, --wait, --timeout SECONDS**
> 若在指定秒数内未能获取锁则失败

**-o, --close**
> 在执行命令之前关闭文件描述符

**-u, --unlock**
> 手动释放锁

**-E, --conflict-exit-code NUM**
> 使用 -n 或超时而加锁失败时的退出码（默认：1）

**-F, --no-fork**
> 执行命令之前不 fork

**--verbose**
> 报告获取锁所花费的时间

# CAVEATS

**flock** 不能检测死锁情况。在某些网络文件系统（如 NFS 和 CIFS）上，文件锁的支持有限。当使用 -n 或 -w 选项且无法获取锁时，flock 会以 -E 指定的退出码退出（默认 1）。

# HISTORY

**flock** 是 **util-linux** 软件包的一部分，提供了对 flock(2) 系统调用的 shell 层访问。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add flock```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flock](/man/flock)(2)
