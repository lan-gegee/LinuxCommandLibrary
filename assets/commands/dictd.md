# TAGLINE

DICT 协议词典服务器守护进程

# TLDR

**启动词典服务器**

```dictd```

**使用指定配置启动**

```dictd -c [/etc/dictd/dictd.conf]```

**在前台运行**（不脱离终端）

```dictd --nodetach```

**监听指定端口**

```dictd --port [2628]```

**限制并发连接数**

```dictd --limit [10]```

**使用指定的 PID 文件运行**

```dictd --pid [/var/run/dictd.pid]```

# SYNOPSIS

**dictd** [_options_]

# DESCRIPTION

**dictd** 是一个实现 DICT 协议（RFC 2229）的词典服务器守护进程。它通过 TCP 端口 2628 向客户端提供词典数据库服务，支持单词查询、释义、翻译和同义词库检索。

该服务器支持多种词典格式，可同时提供多个词典。客户端可以一次性跨所有已配置的数据库查询单词，也可以针对特定词典查询。协议支持多种搜索策略，包括精确匹配、前缀、后缀和模糊匹配。

dictd 数据库通常采用由 dictfmt 创建的 dictd 格式，dictfmt 可将各种源格式转换为带索引的词典文件。服务器能处理并发连接，并可通过访问控制进行配置。常用的词典数据库包括 WordNet、Elements、Jargon File 以及各种语言翻译词典。

# PARAMETERS

**-c** _file_
> 配置文件路径。

**--port** _port_
> TCP 端口（默认 2628）。

**--listen** _address_
> 监听地址。

**--limit** _n_
> 最大并发连接数。

**-i**, **--inetd**
> 以 inetd 模式运行，通过 stdin/stdout 通信。隐含 --fast-start。

**--nodetach**
> 在前台运行，不守护进程化。

**--depth** _length_
> 覆盖配置中的 depth 关键字。

**--delay** _seconds_
> 覆盖配置中的 delay 关键字。

**--fast-start**
> 启动时跳过数据库索引的预加载。

**--logfile** _file_
> 记录到指定文件而非 syslog。

**--syslog**
> 记录到 syslog（守护进程化时的默认行为）。

**--stderr**
> 记录到标准错误（隐含 --nodetach）。

**--pid** _file_
> PID 文件位置。

**-L**, **--license**
> 显示许可证。

**-V**, **--version**
> 显示版本。

# CONFIGURATION

**/etc/dictd/dictd.conf**（或 **/etc/dictd.conf**）
> 服务器配置文件，用于指定词典数据库位置、访问控制和服务器行为。该文件在启动时读取，收到 SIGHUP 时重新读取。

# CAVEATS

需要词典数据库文件。端口 2628 可能需要防火墙规则。大型词典会占用较多内存。查询需要客户端配合。

# HISTORY

**dictd** 于 **20 世纪 90 年代末**作为 **DICT** 项目的一部分开发。DICT 协议旨在取代较旧的词典协议并支持 Internet 词典服务。该项目同时提供服务器和客户端实现。

# INSTALL

```apt: sudo apt install dictd```

```dnf: sudo dnf install dictd```

```pacman: sudo pacman -S dictd```

```zypper: sudo zypper install dictd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dict](/man/dict)(1)
