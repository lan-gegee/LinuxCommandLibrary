# TAGLINE

基于控制台的网络流量监控工具

# TLDR

**显示**所有接口的流量摘要

```vnstat```

**显示**指定接口的流量摘要

```vnstat -i [network_interface]```

**显示**指定接口的实时流量统计

```vnstat -l -i [network_interface]```

**显示**带柱状图的小时流量统计

```vnstat -hg```

**测量并显示** 30 秒内的平均流量

```vnstat -tr 30```

# SYNOPSIS

**vnstat** [_options_] [_interface_]

# PARAMETERS

**-i, --iface _interface_**
> 选择指定的接口

**-l, --live**
> 显示实时流量统计

**-hg, --hoursgraph**
> 以柱状图显示小时级统计

**-tr, --traffic _seconds_**
> 在指定时长内测量流量

**-d, --days**
> 显示按天统计

**-m, --months**
> 显示按月统计

**-t, --top**
> 显示流量最高的日子

**-s, --short**
> 使用简短的输出格式

**--json**
> 以 JSON 格式输出

**--xml**
> 以 XML 格式输出

# DESCRIPTION

**vnstat** 是一个基于控制台的网络流量监控工具，会为选定的网络接口记录流量日志。它使用内核的接口统计信息，因此资源占用极低。

守护进程（vnstatd）在后台持续收集数据，而 vnstat 命令负责查询并显示已收集的统计信息。数据保存在数据库中，重启后依然保留。

# CAVEATS

需要 vnstatd 守护进程正在运行才能收集数据。初始统计需要时间积累。重新配置接口可能导致流量计数器重置。统计基于内核计数器，而非数据包检查。

# INSTALL

```apt: sudo apt install vnstat```

```dnf: sudo dnf install vnstat```

```pacman: sudo pacman -S vnstat```

```apk: sudo apk add vnstat```

```zypper: sudo zypper install vnstat```

```brew: brew install vnstat```

```nix: nix profile install nixpkgs#vnstat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vnstatd](/man/vnstatd)(8), [iftop](/man/iftop)(8), [nethogs](/man/nethogs)(8), [nload](/man/nload)(1)
