# TAGLINE

由 Netflix 提供支持的网速测试 CLI

# TLDR

**运行测速**

```fast```

**包含上传测试**

```fast --upload```

**单行输出**（适合脚本处理）

```fast --single-line```

**以 JSON 输出结果**

```fast --json```

**显示延迟和服务器位置**

```fast --verbose```

# SYNOPSIS

**fast** [_options_]

# PARAMETERS

**-u**, **--upload**
> 在下载速度之外再测量上传速度。

**--single-line**
> 减少间距，将输出打印在单行内。

**--json**
> 以 JSON 格式输出结果。

**--verbose**
> 包含延迟和服务器位置信息。

# DESCRIPTION

**fast** 是一款由 Netflix 的 Fast.com 服务驱动的命令行测速工具。它使用 Netflix 分布在全球的服务器测量下载速度，也可选测量上传速度。

该工具无需广告、操作简单，可快速测量带宽。适用于测试网络连接质量和 ISP 性能。

# OUTPUT

```
   $ fast

     Ping: 12ms
   Download: 95.2 Mbps
   (Upload test with --upload)
```

# CAVEATS

需要连接 Netflix 服务器的互联网。结果可能因地点和时间而异。某些 ISP 可能会对 Netflix 服务器限速。如需更详细的测试，请使用 speedtest-cli。

# HISTORY

fast-cli 作为 Netflix Fast.com 的命令行界面而创建。Netflix 于 **2016 年**推出 Fast.com，作为一个简单无广告的测速服务。该服务使用 Netflix 的内容分发网络。

# INSTALL

```nix: nix profile install nixpkgs#fast```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[speedtest-cli](/man/speedtest-cli)(1), [iperf](/man/iperf)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/sindresorhus/fast-cli)```

<!-- verified: 2026-07-15 -->
