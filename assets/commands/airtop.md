# TAGLINE

基于 eBPF 的终端实时 802.11 Wi-Fi 射频仪表板（电波界的 htop）

# TLDR

启动实时 Wi-Fi 频谱仪表板

```airtop```

对 SSID 和 MAC 匿名化后运行（非常适合截图）

```airtop --anonymize```

从另一个终端强制进行 Wi-Fi 扫描以填充邻近网络

```nmcli dev wifi rescan```

# SYNOPSIS

**airtop** [_options_]

# DESCRIPTION

**airtop** 将 Linux 内核已经在处理的 Wi-Fi 流量转化为美观的实时终端仪表板。它显示：

- 带信号强度的附近接入点频谱图
- 每个站点随时间变化的 RSSI 曲线（盲文点阵图）
- 帧类型（信标、数据、deauth 等）的实时热力图
- RSSI 直方图和滚动更新的已发现网络列表

它**不需要**监听模式或原始套接字。它将 eBPF 程序挂载到常规的 `cfg80211`/`mac80211` 协议栈上，因此你的接口保持关联状态，连接不会中断。

这使得 airtop 在日常调试中极为实用："为什么我的视频通话总是掉线？"、"演示应该用哪个信道？"、"有人在发送 deauth 帧吗？"

# PARAMETERS

**--anonymize**  
> 用稳定的化名替换真实的 SSID 和 MAC 地址（network-01、station-02 等）

仪表板完全可交互：调整终端大小后布局会自动重排。建议的最小尺寸为 80×24。

# CAVEATS

- 只能看到你的接口当前所在信道上的流量（后台扫描期间可短暂瞥见其他信道）。
- 统计的是帧数，而不是空口时间或字节数。
- 需要启用了 BTF 的较新 Linux 内核（当前大多数发行版都满足）。

# SEE ALSO

[iw](/man/iw)(8), [nmcli](/man/nmcli)(1), [kismet](/man/kismet)(1)
