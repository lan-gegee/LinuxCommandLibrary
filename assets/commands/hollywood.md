# TAGLINE

用电影里常见的那种虚假"黑客"画面填满你的终端

# TLDR

**用好莱坞式技术黑话填满控制台**

```hollywood```

指定屏幕的**分屏数量**

```hollywood -s [4]```

**静音运行**（关闭主题曲）

```hollywood -q```

显示**帮助**

```hollywood -h```

# SYNOPSIS

**hollywood** [**-s** _SPLITS_] [**-q**|**--quiet**|**--nosound**]

# PARAMETERS

**-s**, **--splits** _SPLITS_
> 将屏幕分割成的窗格数量。

**-q**, **--quiet**, **--nosound**
> 禁用主题曲。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**hollywood** 用好莱坞式的夸张"技术黑话"填满你的控制台。它会将 byobu/tmux 控制台分割为多个窗格，显示各种看起来很忙碌的活动，如十六进制转储、网络流量、系统日志和滚动的代码。

这些显示纯属视觉效果——它并不会执行任何真正的入侵行为或修改系统。它通过以最低调度优先级运行各个小部件来尽量避免拖累系统。它专为娱乐、电影道具或唬人设计。

显示的活动包括：
- 滚动的十六进制数据
- 假装的系统日志
- 网络监控界面
- 代码编译输出
- 目录列表
- 各种系统工具

# CAVEATS

需要安装 byobu、tmux 及其他多种工具。建议安装 cmatrix、htop、ccze、speedometer 等软件包以获得完整效果。由于同时运行大量进程，CPU 占用率较高。按 Ctrl+C 退出。

# HISTORY

hollywood 由 Canonical 的 Dustin Kirkland 作为趣味副业项目创建。它因重现好莱坞电影中那种计算机上不断滚动着令人费解数据流的不真实"黑客"场景而流行起来。

# INSTALL

```zypper: sudo zypper install hollywood```

```nix: nix profile install nixpkgs#hollywood```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [byobu](/man/byobu)(1), [cmatrix](/man/cmatrix)(1)
