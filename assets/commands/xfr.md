# TAGLINE

带实时 TUI 和 QUIC 的现代 iperf3 替代品

# TLDR

**启动测试服务器**

```xfr server```

**针对服务器运行客户端测试**

```xfr client -c [192.168.1.1]```

**使用 QUIC 传输进行测试**

```xfr client -c [host] --quic```

# SYNOPSIS

**xfr** _server_|_client_ [_options_]

# DESCRIPTION

**xfr** 是一个网络性能测试工具，其实时 TUI 提供实时吞吐量图表、每条流的统计信息以及多客户端服务器仪表盘。它支持 TCP、UDP 和 QUIC 协议，具有可配置的比特率限速和多种输出格式（纯文本、JSON、CSV）。

# HISTORY

**xfr** 由 **lance0** 创建，使用 **Rust** 编写。

# INSTALL

```zypper: sudo zypper install xfr```

```nix: nix profile install nixpkgs#xfr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iperf3](/man/iperf3)(1), [nuttcp](/man/nuttcp)(1)
