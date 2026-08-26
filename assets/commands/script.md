# TAGLINE

将终端会话录制到文件

# TLDR

**记录**一个新会话到名为 "typescript" 的文件

```script```

**记录**会话到自定义文件路径

```script [path/to/session.out]```

**追加**到已有文件

```script -a [logfile.log]```

**记录**计时信息到单独的文件

```script -t 2> [path/to/timing_file]```

**写出**数据时立即刷新（实时写入）

```script -f [path/to/file]```

**静默执行**，不显示开始和结束消息

```script -q [logfile.log]```

**停止**录制

```exit```

# SYNOPSIS

**script** [_options_] [_file_]

# PARAMETERS

**-a, --append**
> 将输出追加到已有文件

**-f, --flush**
> 每次写入后立即刷新输出

**-q, --quiet**
> 静默模式（不显示开始和结束消息）

**-t, --timing[=_file_]**
> 输出供 scriptreplay 使用的计时数据

**-c, --command _command_**
> 运行指定命令而非交互式 shell

**-e, --return**
> 返回子进程的退出码

**-O, --log-out _file_**
> 将 stdout 记录到文件（结构化格式）

# DESCRIPTION

**script** 将所有终端输出记录到一个 typescript 文件中。它会创建一个派生的 shell，并捕获终端上显示的所有内容（包括输入和输出），直到会话以 **exit** 或 **Ctrl-D** 结束。

如果捕获了计时信息，录制的会话可以使用 **scriptreplay** 重放。这对于制作教程、记录操作流程或审计终端会话非常有用。

# CAVEATS

typescript 文件包含控制字符和转义序列。请使用 **cat -v** 或 **less -R** 查看。大型会话可能产生非常大的文件。该命令属于 util-linux 软件包。

# HISTORY

**script** 命令首次出现于 3.0BSD。自 20 世纪 80 年代初以来，它一直是用于录制终端会话的标准 Unix 工具。

# INSTALL

```apt: sudo apt install bsdutils```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scriptreplay](/man/scriptreplay)(1), [scriptlive](/man/scriptlive)(1), [tee](/man/tee)(1), [ttyrec](/man/ttyrec)(1)
