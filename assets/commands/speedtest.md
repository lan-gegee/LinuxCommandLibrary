# TAGLINE

Ookla 官方网络测速 CLI

# TLDR

**运行测速**

```speedtest```

**列出服务器**

```speedtest --servers```

**使用指定服务器**

```speedtest --server-id [12345]```

**输出为 JSON**

```speedtest --format json```

**接受许可协议**

```speedtest --accept-license```

**显示进度**

```speedtest --progress yes```

# SYNOPSIS

**speedtest** [_--server-id id_] [_--format fmt_] [_options_]

# PARAMETERS

**--servers**
> 列出附近的服务器。

**--server-id** _ID_
> 选择服务器。

**--format** _FMT_
> 输出格式（json, csv）。

**--progress** _BOOL_
> 显示进度。

**--accept-license**
> 接受 EULA。

**--accept-gdpr**
> 接受隐私条款。

# DESCRIPTION

**speedtest** 是 Ookla 官方的命令行界面，用于测量网络连接性能。它通过连接 Ookla 的全球测试服务器网络，测量下载速度、上传速度、延迟（ping）和抖动（jitter）。

该工具会自动选择最近的服务器进行测试，也可以按 ID 指定特定服务器。结果包含关于连接质量的详细指标，结构化输出格式（JSON、CSV）便于与监控脚本和仪表盘集成。

首次使用需要接受 Ookla 许可协议和 GDPR 条款。该 CLI 是一个独立分发的编译二进制文件，与基于 Python 的 speedtest-cli 不同，它采用 Ookla 原生的测试方法，结果更为准确。

# CAVEATS

需要接受许可协议。依赖网络状况。仅限 Ookla 服务器。

# HISTORY

**speedtest** 是 **Ookla**——Speedtest.net 网络测速服务背后的公司——的官方 CLI。

# INSTALL

```dnf: sudo dnf install speedtest```

```apk: sudo apk add perl-app-speedtest```

```nix: nix profile install nixpkgs#speedtest```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[speedtest-cli](/man/speedtest-cli)(1), [iperf3](/man/iperf3)(1), [ping](/man/ping)(1)
