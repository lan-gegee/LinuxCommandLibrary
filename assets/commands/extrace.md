# TAGLINE

系统级跟踪 exec() 系统调用

# TLDR

跟踪系统上**所有**程序的执行

```sudo extrace```

只跟踪某个命令的**后代**进程

```sudo extrace [command]```

打印每个进程的当前工作**目录**

```sudo extrace -d```

解析每个可执行文件的**完整路径**

```sudo extrace -l```

显示运行每个进程的**用户**

```sudo extrace -u```

# SYNOPSIS

**extrace** [_options_] [_command_]

# DESCRIPTION

**extrace** 在整个系统范围内跟踪 exec() 系统调用，以监控 Linux 上的程序执行。它捕获每一次程序执行，显示命令行、进程层级，并可选地显示用户、工作目录和环境变量。

与跟踪单个进程的 strace 不同，extrace 监控整个系统或特定进程树内的所有执行活动。它特别适合安全审计（检测可疑的进程执行）、调试派生多个子进程的复杂脚本，以及了解软件包安装或自动化任务期间的系统行为。

该工具订阅 Linux 内核的 netlink 进程连接器（需要 **CONFIG_CONNECTOR** 和 **CONFIG_PROC_EVENTS**）来接收 exec 通知，因此无需向每个进程附加调试器即可捕获活动。

# PARAMETERS

**-d**
> 打印每个进程的工作目录

**-e**
> 打印进程环境（不可读时显示 '-'）

**-f**
> 扁平输出，不带树状缩进

**-l**
> 解析并显示可执行文件的完整路径

**-q**
> 安静模式；不打印 exec() 的参数

**-t**
> 打印每个进程的退出状态和持续时间

**-u**
> 显示运行每个进程的用户

**-o** _file_
> 将跟踪输出写入 _file_

**-p** _pid_
> 只跟踪指定 PID 的后代进程

# CAVEATS

需要 root 权限以及启用了进程连接器的内核。仅限 Linux。大量跟踪时可能影响系统性能。

# INSTALL

```apt: sudo apt install extrace```

```zypper: sudo zypper install extrace```

```nix: nix profile install nixpkgs#extrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[strace](/man/strace)(1), [ltrace](/man/ltrace)(1), [auditd](/man/auditd)(8)

# RESOURCES

```[Source code](https://github.com/leahneukirchen/extrace)```

<!-- verified: 2026-07-15 -->
