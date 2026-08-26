# TAGLINE

监视文件描述符活动

# TLDR

**监视进程的所有文件描述符**

```peekfd [pid]```

**监视特定的文件描述符（例如 stdout=1）**

```peekfd [pid] [1]```

**去除重复的读/写输出（对开启回显的终端有用）**

```peekfd -d [pid]```

**不显示各数据块的头部信息**

```peekfd -n [pid]```

**跟随新创建的子进程**

```peekfd -c [pid]```

**8 位干净输出（不对字节做后处理）**

```peekfd -8 [pid]```

# SYNOPSIS

**peekfd** [_options_] _pid_ [_fd_...]

# PARAMETERS

_PID_
> 要监视的进程 ID（必需）。

_FD_
> 用于限定输出的一个或多个文件描述符编号（如 0、1、2）。若省略，则显示全部文件描述符。

**-8**, **--eight-bit-clean**
> 不对读写的字节做任何后处理。输出为原始二进制数据。

**-n**, **--no-headers**
> 不显示标明所转储字节来源（pid/fd）的头部信息。

**-c**, **--follow**
> 同时转储目标进程创建的所有子进程中的文件描述符活动。

**-d**, **--duplicates-removed**
> 从输出中去除重复的读写。监视启用了本地回显的终端时很有用。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**peekfd** 使用 ptrace 附着到运行中的进程，并打印它在指定文件描述符上读取和写入的字节。它可以用来窥探 stdin/stdout/stderr 或任意已打开的文件和套接字，而无需重启进程。

默认显示所有被跟踪的文件描述符，每块数据前都有一个标明 pid 和 fd 的头部。-8、-n、-d 和 -c 标志用于调整输出格式和子进程的处理方式。

# CAVEATS

属于 **psmisc**。需要内核的 ptrace 支持和足够的权限（通常是同一用户或 CAP_SYS_PTRACE；启用 Yama 的发行版可能需要禁用 `ptrace_scope`）。极快的 I/O 突发可能导致丢失字节。跟踪会使目标进程稍微变慢。

# HISTORY

**peekfd** 随 **psmisc** 软件包发布，与 fuser、killall、pstree 等工具同属一套。它最初由 Trent Waddington 编写。

# INSTALL

```apt: sudo apt install psmisc```

```dnf: sudo dnf install psmisc```

```pacman: sudo pacman -S psmisc```

```zypper: sudo zypper install psmisc```

```nix: nix profile install nixpkgs#psmisc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[strace](/man/strace)(1), [ltrace](/man/ltrace)(1), [lsof](/man/lsof)(1), [fuser](/man/fuser)(1), [pstree](/man/pstree)(1)
