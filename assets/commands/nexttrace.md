# TAGLINE

带 ASN、地理位置和丰富输出的可视化路由跟踪工具

# TLDR

对主机执行**跟踪**

```nexttrace [example.com]```

**快速模式** / 地图相关选项

```nexttrace --help```

用于脚本的 **JSON** 输出

```nexttrace --json [host]```

# SYNOPSIS

**nexttrace** [*options*] *host*

# DESCRIPTION

**nexttrace**（NTrace）是一款增强版 traceroute，支持多种协议，并提供 ASN 查询、地理定位和精美的终端输出。项目由 **nxtrace/NTrace-core** 开发；面向用户的二进制文件通常为 **nexttrace**。可通过软件包管理器获取，也有面向多种架构的发行版构建。

# PARAMETERS

*host*

> 目标主机名或 IP。

常用标志（名称因版本而异）：协议选择（ICMP/TCP/UDP）、最大跳数、并行探测、语言以及 **--json**。请始终以 **nexttrace --help** 为准。

# CAVEATS

某些探测类型可能需要原始套接字/特权。地理定位数据库可能不准确。请尊重远程网络——不要滥用高频探测。

# INSTALL

```brew: brew install nexttrace```

```nix: nix profile install nixpkgs#nexttrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[traceroute](/man/traceroute)(8), [mtr](/man/mtr)(8), [tracepath](/man/tracepath)(8)

# RESOURCES

```[Source code](https://github.com/nxtrace/NTrace-core)```

```[Homepage](https://nxtrace.org)```

<!-- verified: 2026-07-19 -->
