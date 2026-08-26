# TAGLINE

基于 Cloudflare 的网络测速 CLI

# TLDR

**运行**测速

```speed-cloudflare-cli```

无需安装，通过 npx **运行**

```npx speed-cloudflare-cli```

以 JSON 格式**输出**结果

```speed-cloudflare-cli --json```

# SYNOPSIS

**speed-cloudflare-cli** [**--json**]

# PARAMETERS

**--json**
> 以 JSON 格式输出结果，而非人类可读的彩色控制台输出。

# DESCRIPTION

**speed-cloudflare-cli** 是一个 Node.js 命令行工具，使用 Cloudflare 位于 **speed.cloudflare.com** 的测速基础设施来测量你的互联网连接速度与稳定性。它测试下载速度、上传速度和延迟，并报告包括抖动（jitter）在内的指标。

该工具先进行 20 次延迟测量，然后用 5 种负载大小（100kB 至 100MB）测试下载速度，用 3 种负载大小（11kB 至 1MB）测试上传速度。结果报告第 90 百分位速度（单位 Mbps）。输出包括服务器位置（城市和 IATA 代码）、你的 IP 地址、延迟统计（最小值、最大值、平均值、中位数、抖动）、下载速度和上传速度。

# CAVEATS

需要 Node.js 和 npm。测试针对 Cloudflare 最近的边缘服务器；服务器选择是自动的，无法覆盖。结果仅反映到 Cloudflare 网络的连接质量，可能与其他测速服务的结果不同。该软件包自约 2021 年起未再更新，在较新的 Node.js 版本上可能存在兼容性问题。

# HISTORY

**speed-cloudflare-cli** 由 **KNawm** 创建，是为 Cloudflare 测速服务构建的社区 CLI。Cloudflare 于 **2020 年 9 月**推出了其基于浏览器的测速服务。该 CLI 使用相同的 API 端点从终端进行测量。用 JavaScript 编写，采用 MIT 许可证。最新版本为 2.0.3。

# INSTALL

```pacman: sudo pacman -S cloudflare-speed-cli```

```brew: brew install cloudflare-speed-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[speedtest-cli](/man/speedtest-cli)(1), [fast](/man/fast)(1), [iperf](/man/iperf)(1), [speed-test](/man/speed-test)(1)
