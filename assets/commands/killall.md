# TAGLINE

向运行指定命令的所有进程发送信号

# TLDR

按名称**终止所有进程**

```killall [process_name]```

**强制杀死进程**（SIGKILL）

```killall -9 [process_name]```

**发送指定的信号**

```killall -s [SIGTERM] [process_name]```

**只杀死属于你的进程**

```killall -u $(whoami) [process_name]```

**交互模式**（杀死前确认）

```killall -i [process_name]```

**杀死匹配正则表达式的进程**

```killall -r "[pattern]"```

**详细模式** —— 报告信号是否成功发送

```killall -v [process_name]```

**等待进程终止**

```killall -w [process_name]```

**列出所有已知的信号名称**

```killall -l```

**杀死早于**指定时长的进程

```killall -o 1h [process_name]```

# SYNOPSIS

**killall** [_-signal_] [_-eiIqrvw_] [_-u user_] [_-g group_] [_-o time_] [_-y time_] [_name ..._]

# PARAMETERS

**-e**, **--exact**
> 对于非常长的名称要求精确匹配。默认情况下，killall 会将名称截断为 15 个字符。

**-I**, **--ignore-case**
> 不区分大小写匹配。

**-i**, **--interactive**
> 杀死前请求确认。

**-l**, **--list**
> 列出已知的信号名称。

**-q**, **--quiet**
> 未杀死任何进程时也不报错。

**-r**, **--regexp**
> 将名称解释为扩展正则表达式。

**-s**, **--signal** _signal_
> 发送指定的信号（名称或编号）。

**-u**, **--user** _user_
> 只杀死属于指定用户的进程。

**-g**, **--process-group**
> 杀死整个进程组而非单个进程。

**-v**, **--verbose**
> 报告信号是否成功发送。

**-w**, **--wait**
> 等待被杀死的进程实际终止。

**-o**, **--older-than** _time_
> 杀死存活时间超过指定时长的进程。

**-y**, **--younger-than** _time_
> 杀死存活时间短于指定时长的进程。

**-n**, **--ns** _PID_
> 与给定 PID 的 PID 命名空间进行匹配。

**-V**, **--version**
> 显示版本信息。

**-Z**, **--context** _pattern_
> 只杀死 SELinux 上下文匹配的进程（仅限 SELinux）。

# COMMON SIGNALS

**SIGTERM (15)**
> 优雅终止（默认）。

**SIGKILL (9)**
> 强制杀死（不可被捕获）。

**SIGHUP (1)**
> 挂起（通常会触发重载配置）。

**SIGINT (2)**
> 中断（类似 Ctrl+C）。

**SIGSTOP (19)**
> 暂停进程。

**SIGCONT (18)**
> 恢复已暂停的进程。

# DESCRIPTION

**killall** 向运行指定命令的所有进程发送信号。与需要进程 ID 的 **kill** 不同，killall 直接按进程名操作，便于终止一个程序的多个实例。

默认情况下，killall 发送 SIGTERM（信号 15），请求进程优雅终止。进程可以捕获该信号并在退出前完成清理。当进程不响应 SIGTERM 时可以使用 SIGKILL（-9），但要注意这会阻止进程清理。

名称匹配针对的是命令名（即 ps 中显示的名称）。-r 标志启用正则表达式匹配，支持灵活的模式。-i 则会在每个进程被杀死前提示确认。

-w 标志使 killall 等待所有进程真正终止后才返回。这在脚本中很有用——需要确保进程已停止后再继续执行后续步骤。

基于时间的过滤（-o、-y）允许只杀死运行时间长于或短于指定时长的进程（例如 "1h" 表示一小时，"30m" 表示三十分钟，"1d" 表示一天）。

# CAVEATS

Linux（psmisc）版本与 BSD/macOS 版本的行为存在差异。macOS 上的语法和选项差别很大。要小心常见名称 —— killall java 可能会杀死超出预期的进程。root 可以杀死任何进程；普通用户只能杀死自己的进程。

# HISTORY

**killall** 起源于 BSD Unix。Linux 版本是 **psmisc** 软件包的一部分，独立维护且功能与 BSD 版本不同。几十年来该命令一直是标准 Unix 工具，但各系统实现上的差异要求编写可移植脚本时多加注意。

# INSTALL

```apt: sudo apt install psmisc```

```dnf: sudo dnf install psmisc```

```pacman: sudo pacman -S psmisc```

```apk: sudo apk add psmisc```

```zypper: sudo zypper install psmisc```

```nix: nix profile install nixpkgs#psmisc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kill](/man/kill)(1), [pkill](/man/pkill)(1), [pgrep](/man/pgrep)(1), [ps](/man/ps)(1), [pidof](/man/pidof)(1)
