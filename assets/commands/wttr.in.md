# TAGLINE

面向控制台的天气预报服务

# TLDR

**获取当前位置的天气**（基于 IP）

```curl wttr.in```

**获取指定城市的天气**

```curl wttr.in/[Paris]```

**获取地标或命名地点的天气**

```curl "wttr.in/~[Eiffel Tower]"```

**只获取当前天气**（无预报）

```curl wttr.in/[London]?0```

**获取单行天气摘要**

```curl "wttr.in/[Berlin]?format=3"```

**以公制单位获取天气**

```curl wttr.in/[NewYork]?m```

**获取月相**

```curl wttr.in/moon```

**获取 PNG 格式的天气图片**

```curl wttr.in/[Tokyo].png --output weather.png```

# SYNOPSIS

**curl** **wttr.in**/[_location_][?_options_]

# PARAMETERS

_location_
> 城市名、机场代码（3 个字母）、GPS 坐标、区域代码或域名。

**?0**
> 只显示当前天气（无预报）。

**?1**
> 显示当前天气和今天的预报。

**?2**
> 显示当前天气以及今明两天的预报。

**?m**
> 使用公制（SI）单位。

**?u**
> 使用 USCS（美制）单位。

**?n**
> 窄版输出，只显示白天和夜间。

**?q**
> 安静版输出，不带 "Weather report" 标题。

**?Q**
> 极简安静版（无 "Weather report" 文本，也无城市名）。

**?format=**_string_
> 单行输出的自定义格式。预设：1-4。自定义：%c（天气状况）、%t（气温）、%w（风力）、%h（湿度）、%l（位置）、%m（月相）。

**?T**
> 禁用终端转义序列（便于管道处理）。

**?F**
> 不显示 "Follow" 一行。

**?d**
> 输出限制为标准控制台字体字形。

**?M**
> 以 m/s 显示风速。

**?lang=**_code_
> 设置语言（如 lang=de 表示德语）。也可以用子域名形式：fr.wttr.in。

**.png**
> 返回 PNG 图片格式的天气而不是文本。

# DESCRIPTION

**wttr.in** 是一项面向控制台的天气预报服务，可通过 curl、wget 或 httpie 等 HTTP 客户端访问。它以 ASCII art 格式直接在终端中提供天气信息，无需安装任何东西。

该服务支持多种地点类型：城市名、3 字母机场代码、GPS 坐标、区域代码、域名（加 @ 前缀）以及地标（加 ~ 前缀）。不给定地点时，它会根据你的 IP 地址确定位置。

输出可以按不同用途定制：完整的 3 天预报、仅当前天气、适合状态栏（tmux、shell 提示符）的单行格式，或 PNG 图片。v2 端点（v2.wttr.in）提供包含历史数据在内的扩展数据。

wttr.in 支持多种语言以及公制和英制单位。该服务每天处理数百万次查询，可免费使用。

# CAVEATS

需要网络连接和 HTTP 客户端（curl、wget）。基于 IP 的定位在使用 VPN 或代理时可能不准确。请求过多可能触发限速。要获得最佳效果，ASCII art 显示需要宽度足够且支持 Unicode 的终端。

# HISTORY

**wttr.in** 由 **Igor Chubin** 大约于 **2016 年**创建，作为 wego 天气客户端的封装，用以展示面向控制台的 Web 服务。它经由 Hacker News 和社交媒体走红，如今每天处理数千万次查询。该服务仍在持续维护和改进，不断加入新功能。

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [wego](/man/wego)(1)
