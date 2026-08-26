# TAGLINE

高级系统与进程活动监视器

# TLDR

**启动** atop

```atop```

显示每个进程的**内存**占用

```atop -m```

显示**磁盘**信息

```atop -d```

显示每个进程的完整**命令行**

```atop -c```

显示**线程级别**的资源利用率

```atop -y```

显示**每个用户的进程**数量

```atop -au```

# SYNOPSIS

**atop** [_-m_] [_-d_] [_-c_] [_-y_] [_-au_] [_interval_ [_samples_]]

# DESCRIPTION

**atop** 是一款面向 Linux 系统的高级交互式监视器，同时展示系统级和进程级活动。它会突出显示已达到临界负载的资源，并提供历史数据记录功能。

# PARAMETERS

**-m**
> 显示每个进程的内存占用

**-d**
> 显示磁盘信息

**-c**
> 显示每个进程的完整命令行（包括参数）

**-y**
> 显示线程级别的资源利用率

**-a**
> 仅显示活动进程

**-u**
> 显示用户统计信息

**-g**
> 显示常规输出（默认）

**-1**
> 显示每秒平均值而非每间隔平均值

**-r file**
> 从文件读取原始数据而非实时系统

**-w file**
> 将原始数据写入文件以供日后分析

# KEYBOARD SHORTCUTS

**g**: 常规输出
**m**: 内存详情
**d**: 磁盘详情
**n**: 网络详情
**c**: 每个进程的命令行
**u**: 用户统计
**p**: 进程活动
**?**: 帮助

# CONFIGURATION

**/etc/atoprc**
> 系统级配置，用于默认显示选项和间隔。

**~/.atoprc**
> 用户级配置，覆盖系统默认值。

# CAVEATS

部分功能需要 root 权限。以高频监控时会消耗较多资源。

# HISTORY

由 Gerlof Langeveld 开发。旨在提供比 **top** 更详细的系统监控，并支持历史数据记录。

# INSTALL

```apt: sudo apt install atop```

```dnf: sudo dnf install atop```

```pacman: sudo pacman -S atop```

```apk: sudo apk add atop```

```zypper: sudo zypper install atop```

```brew: brew install atop```

```nix: nix profile install nixpkgs#atop```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[top](/man/top)(1), [htop](/man/htop)(1), [btop](/man/btop)(1), [glances](/man/glances)(1)

# RESOURCES

```[Homepage](https://www.atoptool.nl/)```

```[Source code](https://github.com/Atoptool/atop)```

<!-- verified: 2026-06-17 -->
