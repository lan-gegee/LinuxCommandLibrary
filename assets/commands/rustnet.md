# TAGLINE

带深度包检测的按进程网络监视器

# TLDR

**启动**交互式网络 TUI

```rustnet```

**显示帮助** / 选项

```rustnet --help```

# SYNOPSIS

**rustnet** [*options*]

# DESCRIPTION

**rustnet** 是一个终端 UI，用于实时查看 Linux/macOS/Windows 上每个进程的网络活动。它将连接和流量归因到具体进程，并可执行深度包检测以获得更丰富的协议洞察。它是跨平台的，并在设计上考虑了沙箱机制，以便更安全地访问数据包。

# PARAMETERS

大多数控制在启动后的 TUI 内交互完成。CLI 标志用于选择网卡接口、刷新率和过滤模式——已安装版本的可用选项请参见 **rustnet --help**。

要获得完整的 DPI 功能，可能需要 root 权限或 **CAP_NET_RAW** / 抓包权限。

# CAVEATS

抓包可能需要提升的权限，在共享机器上可能比较敏感。性能开销随流量增大而上升。对于深度取证分析而言，它不能取代 **wireshark**。

# INSTALL

```pacman: sudo pacman -S rustnet```

```brew: brew install rustnet```

```nix: nix profile install nixpkgs#rustnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ss](/man/ss)(8), [iftop](/man/iftop)(1), [nethogs](/man/nethogs)(8), [tcpdump](/man/tcpdump)(1)

# RESOURCES

```[Source code](https://github.com/domcyrus/rustnet)```

<!-- verified: 2026-07-19 -->
