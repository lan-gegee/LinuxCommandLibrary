# TAGLINE

命令行网络测速客户端

# TLDR

**运行测速**

```speedtest-cli```

**简洁输出**

```speedtest-cli --simple```

**列出服务器**

```speedtest-cli --list```

**使用指定服务器**

```speedtest-cli --server [12345]```

**JSON 输出**

```speedtest-cli --json```

**跳过下载测试**

```speedtest-cli --no-download```

**跳过上传测试**

```speedtest-cli --no-upload```

**以字节显示**

```speedtest-cli --bytes```

# SYNOPSIS

**speedtest-cli** [_--simple_] [_--server id_] [_--json_] [_options_]

# PARAMETERS

**--simple**
> 简洁输出。

**--list**
> 列出服务器。

**--server** _ID_
> 指定服务器。

**--json**
> JSON 输出。

**--csv**
> CSV 输出。

**--csv-header**
> 打印 CSV 表头行。

**--no-download**
> 跳过下载测试。

**--no-upload**
> 跳过上传测试。

**--single**
> 使用单一连接而非多连接。

**--bytes**
> 以字节/秒而非比特/秒显示。

**--share**
> 生成包含结果图片的分享 URL。

**--secure**
> 使用 HTTPS 而非 HTTP。

**--source** _address_
> 绑定到指定的源 IP 地址。

**--timeout** _seconds_
> 设置 HTTP 超时时间（默认：10）。

**--exclude** _ID_
> 将某台服务器排除在选择之外。

# DESCRIPTION

**speedtest-cli** 是一款基于 Python 的命令行工具，使用 Speedtest.net 基础设施测试网络带宽。它针对 Ookla 的全球服务器网络测量下载速度、上传速度和 ping 延迟。

该工具支持多种输出模式，包括 simple（单行指标）、JSON 和 CSV，便于脚本编写和监控集成。share 选项会生成一个 URL，指向 Speedtest.net 上结果图片。可以按 ID 选择特定的测试服务器，也可以单独跳过下载或上传测试以加快部分测量。

配合 **--secure** 标志，该工具默认使用 HTTPS 连接，并可以按字节每秒而非比特每秒显示结果。它由社区维护，与 Ookla 官方的 **speedtest** CLI 二进制文件是不同的项目。

# CAVEATS

基于 Python，需要安装。服务器可用性各异。结果与浏览器测速有所不同。

# HISTORY

**speedtest-cli** 由 **Matt Martz** 创建，作为 Speedtest.net 的 CLI 工具。它使自动化和脚本化的网络测速成为可能。

# INSTALL

```dnf: sudo dnf install speedtest-cli```

```pacman: sudo pacman -S speedtest-cli```

```apk: sudo apk add speedtest-cli```

```zypper: sudo zypper install speedtest-cli```

```brew: brew install speedtest-cli```

```nix: nix profile install nixpkgs#speedtest-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iperf](/man/iperf)(1), [fast](/man/fast)(1), [curl](/man/curl)(1)
