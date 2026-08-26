# TAGLINE

交互式的跨平台进程查杀工具

# TLDR

**交互式进程查杀**

```fkill```

**按名称查杀**

```fkill [process_name]```

**按端口查杀**

```fkill :[port]```

**按 PID 查杀**

```fkill [pid]```

**强制杀死**

```fkill -f [process_name]```

**静默查杀**（始终返回退出码 0）

```fkill -s [process_name]```

**同时查杀多个目标**（名称、PID 和端口）

```fkill [process_name] [pid] :[port]```

SIGTERM 失败时**超时后强制杀死**

```fkill -t [5] [process_name]```

# SYNOPSIS

**fkill** [_options_] [_target_...]

# PARAMETERS

**-f**, **--force**
> 强制杀死（用 SIGKILL 替代 SIGTERM）。

**-s**, **--silent**
> 静默杀死进程，并始终以退出码 0 结束。

**-v**, **--verbose**
> 在交互列表中把进程参数连同名称一起显示。

**-t** _N_, **--force-timeout** _N_
> 进程在 _N_ 秒后仍未退出时强制将其杀死。

**--smart-case**
> 除非模式中含有大写字母，否则不区分大小写进行匹配。

**--case-sensitive**
> 强制对进程名区分大小写匹配。

# DESCRIPTION

**fkill** 是一款跨平台进程查杀工具，带有交互式界面。它通过模糊搜索来挑选要终止的进程，支持多种定位方式。

该工具可以按名称、PID 或端口号杀死进程（端口前加 **:**，例如 `:8080`），并且一次可以指定多个目标。在交互模式下，它会展示一个可搜索的运行中进程列表（附带 CPU 与内存占用），你可以用方向键加模糊匹配来选中目标。

它以 Node.js 编写并通过 npm 分发（`npm install --global fkill-cli`），在 Linux、macOS 和 Windows 上行为一致。

# CAVEATS

需要 Node.js。在 Unix 上，杀死系统进程通常需要 **sudo**。匹配是模糊的，确认前务必核对选中的进程——尤其是在交互模式下，默认会采用排名第一的匹配结果。

# INSTALL

```pacman: sudo pacman -S fkill```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kill](/man/kill)(1), [pkill](/man/pkill)(1)
