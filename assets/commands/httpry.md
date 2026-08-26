# TAGLINE

专门的 HTTP 数据包嗅探器

# TLDR

**捕获 HTTP 流量**

```sudo httpry -i [eth0]```

**按端口过滤**

```sudo httpry -i [eth0] 'port 8080'```

**记录到文件**

```sudo httpry -i [eth0] -o [http.log]```

**从 pcap 文件读取**

```httpry -r [capture.pcap]```

**自定义输出格式**

```sudo httpry -i [eth0] -f [method,host,request-uri]```

# SYNOPSIS

**httpry** [_options_] [_filter_]

# PARAMETERS

_FILTER_
> BPF 风格的捕获过滤表达式，语法与 tcpdump 相同。

**-i** _DEVICE_
> 要监听的以太网接口。若省略，httpry 会轮询系统并选择找到的第一个接口。

**-r** _FILE_
> 从已有的 pcap 捕获文件读取数据包，而不是进行实时捕获。不需要 root 权限。

**-o** _FILE_
> 用于写入解析后数据包数据的输出文件。

**-f** _FORMAT_
> 要输出的 HTTP 字段的逗号分隔列表（例如 `method,host,request-uri`）。

**-m** _METHODS_
> 要解析的请求方法的逗号分隔列表（例如 `GET,POST`）。

**-n** _COUNT_
> 解析指定数量的 HTTP 数据包后退出。默认为 0（一直运行）。

**-d**
> 以守护进程方式运行；状态输出写入 syslog。需要配合 **-o**。

**-b** _FILE_
> 将所有处理过的 HTTP 数据包写入二进制 pcap 转储文件。

**-p**
> 不将接口置于混杂模式。

**-q**
> 抑制非关键输出（启动横幅、统计信息等）。

**-u** _USER_
> 打开捕获设备后将权限降为指定用户。

**-h**
> 显示帮助信息。

# DESCRIPTION

**httpry** 是一款专门的 HTTP 数据包嗅探器。它可以捕获实时流量或读取 pcap 文件，并以紧凑、可定制的面向行的格式记录 HTTP 请求和响应的元数据——方法、主机、URI、请求头——而非完整的数据包转储。

该工具专注于解析 HTTP 头，而非通用的数据包捕获，因此非常适合持续记录和分析 Web 流量。输出字段可通过 **-f** 选择，它还可以作为后台守护进程运行并将日志写入 syslog。

# CAVEATS

实时捕获需要 root 权限（或相应的能力）才能打开网络接口；使用 **-r** 从 pcap 文件读取则不需要。只能解析明文 HTTP——加密的 HTTPS 流量对它不可见。基于 libpcap 构建。该项目自 2018 年以来没有发布过新版本，实际上已无人维护。

# HISTORY

httpry 由 **Jason Bittel** 于 **2005 年**前后创建，是一款轻量级、专门用于记录 HTTP 流量的工具，可作为通用数据包嗅探器的替代方案。它后来迁移到 GitHub 上，位于 jbittel/httpry。

# INSTALL

```apt: sudo apt install httpry```

```dnf: sudo dnf install httpry```

```apk: sudo apk add httpry```

```brew: brew install httpry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [httpflow](/man/httpflow)(1), [ngrep](/man/ngrep)(1)

# RESOURCES

```[Source code](https://github.com/jbittel/httpry)```

<!-- verified: 2026-07-19 -->
