# TAGLINE

网络安全监测与分析框架

# TLDR

**分析 pcap 文件**

```zeek -r [capture.pcap]```

**用指定脚本分析 pcap**

```zeek -r [capture.pcap] [script.zeek]```

**在网卡上捕获实时流量**

```sudo zeek -i [eth0]```

**以本地站点策略运行**

```zeek -r [capture.pcap] local```

**输出版本并退出**

```zeek --version```

# SYNOPSIS

**zeek** [_options_] [_file_...]

# PARAMETERS

**-r** _file_
> 从 pcap 文件读取数据包

**-i** _interface_
> 从网络接口捕获

**-C**
> 忽略校验和错误

**-e** _code_
> 执行 Zeek 脚本代码

**-f** _filter_
> 应用 BPF 过滤器

**-N**
> 列出所有可用的插件并退出。

**-w** _file_
> 将原始数据包写入文件。

**-b**, **--bare-mode**
> 不从 base/ 目录加载脚本。

**--parse-only**
> 解析脚本后退出。

**--version**
> 输出版本并退出。

# DESCRIPTION

**Zeek**（原名 Bro）是一个专注于安全监测的强大网络分析框架。与显示原始流量的数据包嗅探器不同，Zeek 会解析网络活动，并生成关于连接、协议和检测到的威胁的高级日志。

Zeek 处理网络流量（实时的或来自 pcap 文件）并生成结构化日志：**conn.log** 记录连接、**http.log** 记录 HTTP 流量、**dns.log** 记录 DNS 查询、**ssl.log** 记录 TLS 连接，还有更多其他日志。

该工具使用自定义脚本语言定义分析逻辑。脚本可以检测入侵、从流量中提取文件、识别协议以及生成自定义日志。**local.zeek** 策略会加载站点特定的配置。

输出日志默认以制表符分隔，便于使用 **zeek-cut** 等工具解析或导入 SIEM 系统。

# CAVEATS

对于高流量网络，Zeek 需要大量 CPU 和内存。请相应地调整 worker 数量和分析深度。

其脚本语言有一定的学习曲线。编写自定义分析器之前，先从内置脚本入手。

实时捕获需要 root 权限或相应的能力（capabilities）。pcap 文件分析可以普通用户身份运行。

生产部署应配置好日志轮转与管理。

# INSTALL

```brew: brew install zeek```

```nix: nix profile install nixpkgs#zeek```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [tshark](/man/tshark)(1), [suricata](/man/suricata)(8)
