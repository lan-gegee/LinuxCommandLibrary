# TAGLINE

分析系统启动性能

# TLDR

**打印**上次系统启动耗时

```systemd-analyze```

按初始化时间排序，**列出**所有正在运行的单元

```systemd-analyze blame```

**打印**启动关键单元链的树状图

```systemd-analyze critical-chain```

**生成**展示服务启动时间线的 SVG

```systemd-analyze plot > [path/to/file.svg]```

将依赖关系图**绘制**为 SVG

```systemd-analyze dot | dot -T svg > [path/to/file.svg]```

**显示**运行中单元的安全评分

```systemd-analyze security```

**查看**所有不带注释的 udev 规则

```systemd-analyze cat-config udev/rules.d --tldr```

# SYNOPSIS

**systemd-analyze** [_command_] [_options_]

# PARAMETERS

**blame**
> 按启动时间排序列出单元

**critical-chain**
> 显示单元启动的关键路径

**plot**
> 生成启动过程的 SVG 时序图

**dot**
> 生成 DOT 格式的依赖关系图

**security**
> 分析安全与沙箱设置

**verify**
> 校验单元文件语法

**cat-config**
> 显示合并后的配置文件

**time**
> 显示启动耗时摘要（默认）

# DESCRIPTION

**systemd-analyze** 提供关于系统启动性能和 systemd 单元配置的详细信息。它帮助识别启动缓慢的服务并调试启动问题。

**blame** 和 **critical-chain** 命令通过定位瓶颈来优化启动时间，特别有用。**security** 命令则审计单元的沙箱配置。

# CAVEATS

某些命令进行可视化时需要 graphviz（dot）。启动计时数据只有在系统完全启动后才可用。安全评分只是建议性指标，并非强制要求。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [journalctl](/man/journalctl)(1), [bootctl](/man/bootctl)(1)
