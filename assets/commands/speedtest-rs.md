# TAGLINE

基于 Rust 的网络测速工具

# TLDR

**运行测速**

```speedtest-rs```

**列出服务器**

```speedtest-rs --list```

**使用指定服务器**

```speedtest-rs --server [server-id]```

**简洁输出**

```speedtest-rs --simple```

**跳过下载测试**

```speedtest-rs --no-download```

**跳过上传测试**

```speedtest-rs --no-upload```

# SYNOPSIS

**speedtest-rs** [_--server id_] [_--simple_] [_options_]

# PARAMETERS

**--list**
> 列出服务器。

**--server** _ID_
> 服务器 ID。

**--simple**
> 最简输出。

**--no-download**
> 跳过下载测试。

**--no-upload**
> 跳过上传测试。

**--bytes**
> 以字节/秒显示。

# DESCRIPTION

**speedtest-rs** 是用 Rust 编写的网络测速客户端，兼容 Speedtest.net 服务器。它使用与原版 speedtest-cli 相同的服务器基础设施测量下载速度、上传速度和 ping 延迟。

作为编译好的 Rust 二进制文件，与基于 Python 的替代方案相比，它启动更快、资源占用更低。该工具提供相同的核心功能，包括列出服务器、按 ID 选择服务器、简洁输出模式，以及独立跳过下载或上传测试的能力。

# CAVEATS

依赖网络状况。服务器选择很重要。使用 Speedtest.net 服务。

# HISTORY

**speedtest-rs** 是 Speedtest.net CLI 的 Rust 实现，提供网络速度测量功能。

# INSTALL

```nix: nix profile install nixpkgs#speedtest-rs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[speedtest-cli](/man/speedtest-cli)(1), [iperf](/man/iperf)(1), [curl](/man/curl)(1)
