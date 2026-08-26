# TAGLINE

实时 Web 日志分析器与交互式查看器

# TLDR

以交互模式**分析**一个或多个日志文件

```goaccess [path/to/logfile1] [path/to/logfile2] ...```

使用指定的 **log-format** 或预定义格式

```goaccess [path/to/logfile] --log-format=[format|combined]```

从 **stdin** 分析日志

```tail -f [path/to/logfile] | goaccess -```

分析日志并将结果实时写入 **HTML** 文件

```goaccess [path/to/logfile] -o [path/to/file.html] --real-time-html```

# SYNOPSIS

**goaccess** [_options_] _logfile_

# PARAMETERS

**-o**, **--output** _FILE_
> 输出到指定文件（根据扩展名生成 HTML、JSON 或 CSV）

**--log-format** _FORMAT_
> 指定日志格式字符串，或使用预定义格式：COMBINED、COMMON 等

**--real-time-html**
> 通过 WebSocket 实时更新 HTML 报告

**--ws-url** _URL_
> 实时 HTML 所用的 WebSocket URL

**-a**, **--agent-list**
> 启用完整的 user-agent 解析

**-d**, **--with-output-resolver**
> 启用 IP 解析器以进行地理位置定位

**-e**, **--exclude-ip** _IP_
> 将指定 IP 排除在统计之外

**--ignore-panel** _PANEL_
> 在输出中忽略特定面板

**--geoip-database** _FILE_
> 用于地理位置定位的 GeoIP 数据库

# DESCRIPTION

**goaccess** 是一款开源的实时 Web 日志分析器与交互式查看器。它解析 Web 服务器日志（Apache、Nginx 等），在终端仪表板中显示统计信息，或生成 HTML/JSON/CSV 报告。

功能包括基于流式日志的实时分析、地理位置查询、user-agent 解析，以及针对访问者、请求、来源页面（referrer）、404 错误、操作系统和浏览器的详细指标。

交互式终端模式提供基于 ncurses 的仪表板，支持逐层深入查看。HTML 报告可以通过 WebSocket 连接实时更新。

# CONFIGURATION

**~/.goaccessrc**
> 用户级配置文件，用于设置日志格式、输出选项等默认值。

**/etc/goaccess/goaccess.conf**
> 系统级配置文件，包含默认日志格式、日期/时间格式和面板设置。

# CAVEATS

日志格式必须与实际日志格式一致，不匹配会导致解析失败。实时 HTML 功能需要有正在运行的 goaccess 进程。处理大型日志文件可能占用大量内存。

# HISTORY

goaccess 由 Gerardo Orellana 创建，于 **2009 年**首次发布。作为云计算分析服务的轻量级、注重隐私的替代方案，它广受欢迎，尤其适合快速分析服务器日志。

# INSTALL

```apt: sudo apt install goaccess```

```dnf: sudo dnf install goaccess```

```pacman: sudo pacman -S goaccess```

```apk: sudo apk add goaccess```

```zypper: sudo zypper install goaccess```

```brew: brew install goaccess```

```nix: nix profile install nixpkgs#goaccess```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[awstats](/man/awstats)(1), [nginx](/man/nginx)(8), [apache2](/man/apache2)(8)
