# TAGLINE

测量网络连接速度

# TLDR

**运行测速**

```speed-test```

**JSON 输出**

```speed-test --json```

**以字节为单位输出**

```speed-test --bytes```

**详细输出**

```speed-test --verbose```

# SYNOPSIS

**speed-test** [_--json_] [_--bytes_] [_--verbose_]

# PARAMETERS

**--json**
> JSON 输出格式。

**--bytes**
> 以字节/秒为单位显示。

**--verbose**
> 详细输出。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# DESCRIPTION

**speed-test** 通过对 speedtest.net 服务器测试下载速度、上传速度和 ping 延迟来衡量网络连接性能。它会自动选择最近的服务器，以提供有代表性的结果。

默认情况下，该工具以兆比特每秒（Mbps）显示结果，也可选择以字节每秒显示。JSON 输出模式可用于与监控脚本和仪表盘集成。

结果反映的是你的设备与所选测试服务器之间的连接速度；由于网络路由、拥塞和 ISP 对等互联安排的不同，与其他目标之间的速度可能有所差异。

# OUTPUT

结果显示：
- Ping（延迟，单位 ms）
- 下载速度（Mbps）
- 上传速度（Mbps）
- 服务器位置

# CAVEATS

结果因服务器而异。网络状况会影响测量结果。可能存在 ISP 限速。

# HISTORY

**speed-test** 是一个用于命令行测速的 npm 软件包。它采用与 speedtest.net 相同的方法论。

# INSTALL

```aur: yay -S speed-test```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[speedtest-cli](/man/speedtest-cli)(1), [fast](/man/fast)(1), [iperf](/man/iperf)(1)
