# TAGLINE

向进程发送信号，通常用于终止它

# TLDR

使用默认的 SIGTERM 信号**终止**程序

```kill [process_id]```

**列出**可用的信号名称

```kill -l```

终止一个**后台作业**

```kill %[job_id]```

发送 **SIGHUP** 信号（对许多守护进程而言是重新加载）

```kill -HUP [process_id]```

发送 **SIGINT** 信号（类似 Ctrl+C）

```kill -INT [process_id]```

**强制杀死**程序（SIGKILL）

```kill -9 [process_id]```

**暂停**程序（SIGSTOP）

```kill -STOP [process_id]```

向具有同一**组 ID** 的所有进程发送信号

```kill -SIGUSR1 -[group_id]```

# SYNOPSIS

**kill** [_-signal_] _pid_...

**kill** _-l_

# DESCRIPTION

**kill** 向进程发送信号，通常用于将其停止。除 SIGKILL 和 SIGSTOP 外，所有信号都可以被进程捕获以执行干净的退出。默认发送的是 SIGTERM。

# PARAMETERS

**-l, --list**
> 列出信号名称，或将信号编号转换为名称

**-L, --table**
> 以表格形式列出信号名称和编号

**-s signal**
> 指定要发送的信号

**-signal**
> 按名称或编号指定信号（例如 -9、-KILL、-SIGKILL）

**-p, --pid**
> 仅打印进程 ID，不发送信号

**-q, --queue value**
> 使用 sigqueue(3) 发送信号并附带整数值

**pid**
> 要接收信号的进程 ID。PID 为 0 表示向当前进程组中的所有进程发送信号。PID 为 -1 表示向所有 PID > 1 的进程发送信号。

**%job_id**
> shell 作业控制中的作业 ID

# COMMON SIGNALS

**SIGTERM (15)**: 请求终止（默认）
**SIGKILL (9)**: 强制立即终止（不可被捕获）
**SIGHUP (1)**: 挂起；常用于重新加载配置
**SIGINT (2)**: 中断（Ctrl+C）
**SIGSTOP (19)**: 暂停进程（不可被捕获）
**SIGCONT (18)**: 继续已暂停的进程

# CAVEATS

SIGKILL（-9）应作为最后手段使用，因为它不允许进程进行清理。应先使用 SIGTERM，并给进程留出优雅退出的时间。

# HISTORY

自早期版本起就是标准 Unix 的组成部分。**kill** 命令自 **Version 4 AT&T UNIX**（1973 年）起即可用。

# INSTALL

```apt: sudo apt install procps```

```dnf: sudo dnf install uutils-coreutils```

```pacman: sudo pacman -S uutils-coreutils```

```apk: sudo apk add uutils-coreutils```

```zypper: sudo zypper install procps```

```brew: brew install procps```

```nix: nix profile install nixpkgs#procps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[killall](/man/killall)(1), [pkill](/man/pkill)(1), [pgrep](/man/pgrep)(1), [ps](/man/ps)(1), [top](/man/top)(1)
