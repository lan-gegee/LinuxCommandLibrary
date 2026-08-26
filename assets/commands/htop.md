# TAGLINE

交互式进程查看器和系统监视器

# TLDR

**启动 htop**

```htop```

**显示特定用户的进程**

```htop -u [username]```

**只显示包含指定字符串的进程**

```htop -F [string]```

**以树状视图启动**

```htop -t```

**按内存使用量排序**

```htop -s PERCENT_MEM```

**单色模式**

```htop -C```

**显示帮助**

```htop -h```

# SYNOPSIS

**htop** [_options_]

# DESCRIPTION

**htop** 是一个基于 ncurses 的交互式进程查看器和系统监视器，旨在作为传统 top 命令更强大的替代品。它的全屏界面在顶部以彩色条形计量表显示每核心 CPU 利用率、内存和交换空间的使用情况，下方则是所有运行进程组成的可滚动、可排序表格。与 top 不同，htop 支持完整的鼠标交互，并提供直观的键盘快捷键来完成日常任务。

用户可以实时过滤进程列表（F4）、按名称搜索进程（F3），以及切换树状视图（F5）以展示父子进程层级。向进程发送信号也很简单——按下 F9 会弹出信号菜单（SIGTERM、SIGKILL、SIGHUP 等），可将其发送给一个或多个已标记的进程。进程优先级（nice 值）可直接调整，设置界面（F2）还允许完全自定义要显示的列和计量表，并且这些配置会在会话之间持久保存。

# PARAMETERS

**-u** _user_, **--user=** _user_
> 只显示指定用户的进程。

**-p** _pid_, **--pid=** _pid_
> 只显示指定的 PID。

**-t**, **--tree**
> 以树状视图模式启动。

**-s** _column_, **--sort-key=** _column_
> 按指定列排序。

**-d** _delay_, **--delay=** _delay_
> 更新间隔，单位为十分之一秒。

**-C**, **--no-color**
> 单色模式。

**-F** _string_, **--filter=** _string_
> 只显示包含指定字符串的进程。

**-H**, **--highlight-changes**
> 高亮显示新增或有变化的进程。

**--readonly**
> 禁用进程操作。

# KEYBOARD CONTROLS

**F1** / **h**: 帮助界面
**F2** / **S**: 设置菜单
**F3** / **/**: 搜索
**F4** / **\\**: 过滤
**F5** / **t**: 切换树状视图
**F6** / **>**: 排序列菜单
**F9** / **k**: 杀死进程
**F10** / **q**: 退出
**Space**: 标记进程
**U**: 取消所有标记
**c**: 标记进程及其子进程

# CAVEATS

某些功能需要 root 权限（更改优先级、杀死其他用户的进程）。过高的刷新频率可能影响系统性能。进程信息只是一个快照，两次刷新之间可能发生变化。

# HISTORY

**htop** 由 **Hisham Muhammad** 于 **2004 年**创建，目标是成为 Linux 上更易用的进程查看器。它解决了用户对 top 界面不友好、缺乏交互性的普遍抱怨。在维护一度中断之后，该项目由一个社区团队 fork 为 **htop-dev** 并继续开发。htop 已成为 Linux 系统上事实上的交互式进程查看器。

# INSTALL

```apt: sudo apt install htop```

```dnf: sudo dnf install htop```

```pacman: sudo pacman -S htop```

```apk: sudo apk add htop```

```zypper: sudo zypper install htop```

```brew: brew install htop```

```nix: nix profile install nixpkgs#htop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[top](/man/top)(1), [ps](/man/ps)(1), [pstree](/man/pstree)(1), [atop](/man/atop)(1), [btop](/man/btop)(1)
