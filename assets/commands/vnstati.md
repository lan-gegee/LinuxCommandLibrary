# TAGLINE

生成网络流量图表图片

# TLDR

输出最近两个月、各天和全部历史的流量**摘要**

```vnstati --summary --iface [network_interface] --output [path/to/output.png]```

输出有史以来**流量最大的 10 天**

```vnstati --top 10 --iface [network_interface] --output [path/to/output.png]```

输出最近 12 个月的**每月**流量统计

```vnstati --months --iface [network_interface] --output [path/to/output.png]```

输出最近 24 小时的**每小时**流量统计

```vnstati --hours --iface [network_interface] --output [path/to/output.png]```

# SYNOPSIS

**vnstati** [_options_] **-o** _file_ | **--output** _file_

# PARAMETERS

**-i**, **--iface** _interface_
> 选择要使用的接口

**-o**, **--output** _file_
> 输出文件名（PNG 格式）

**-s**, **--summary**
> 输出流量摘要

**--top** _count_
> 输出流量最高的若干天

**-h**, **--hours**
> 输出小时级流量统计

**-d**, **--days**
> 输出每日流量统计

**-m**, **--months**
> 输出每月流量统计

**-y**, **--years**
> 输出每年流量统计

**-5**, **--fiveminutes**
> 输出 5 分钟分辨率的统计

**--style** _num_
> 调整视觉外观（0-4）

**-c**, **--cache** _time_
> 仅当数据库比指定时间新时才更新输出

**--headertext** _text_
> 自定义页眉文本

**--transparent**
> 切换背景透明度

# DESCRIPTION

**vnstati** 从 vnStat 的网络流量数据生成 PNG 图片，以图形方式展示带宽使用情况。它读取与 vnstat 相同的数据库，并输出适合嵌入网页或报告的图形摘要。

该工具支持多种时间范围（小时、日、月、年），可以生成流量摘要、用量最高日和 5 分钟分辨率的图表。多种样式选项允许自定义外观。

# CAVEATS

需要 vnstat 守护进程正在运行并收集数据。仅支持 PNG 输出格式。接口必须在 vnstat 数据库中已有流量数据。

# HISTORY

属于 Teemu Toivola 的 **vnStat** 项目。vnstati 的加入提供了图形输出能力，常用于为基于网页的监控面板和报告生成带宽图表。

# INSTALL

```apt: sudo apt install vnstati```

```dnf: sudo dnf install vnstat```

```pacman: sudo pacman -S vnstat```

```apk: sudo apk add vnstat```

```zypper: sudo zypper install vnstat```

```brew: brew install vnstat```

```nix: nix profile install nixpkgs#vnstat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vnstat](/man/vnstat)(1), [nethogs](/man/nethogs)(8), [iftop](/man/iftop)(8)
