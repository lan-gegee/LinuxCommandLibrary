# TAGLINE

检查 NetworkManager 是否报告网络已连接

# TLDR

查明**网络是否已连接**并打印结果

```nm-online```

等待连接 **n 秒**（默认 30 秒）

```nm-online --timeout [n]```

# SYNOPSIS

**nm-online** [_options_]

# PARAMETERS

**-t, --timeout _seconds_**
> 等待连接的时间（默认：30 秒）

**-q, --quiet**
> 不打印任何内容，只设置退出状态

**-s, --wait-for-startup**
> 若 NetworkManager 未运行则等待其启动

**-x, --exit**
> 若 NetworkManager 未运行则立即退出

# DESCRIPTION

**nm-online** 检查 NetworkManager 是否报告网络已连接。它会等待网络连接可用，因此对于需要在继续执行前确保网络连通性的脚本非常有用。

该命令会一直阻塞，直到建立连接或达到超时时间。退出状态表示结果：0 表示已连接，非零表示在超时时间内没有连接。

它常用于依赖网络的 systemd service 文件或 init 脚本中，为等待 NetworkManager 建立连接提供了一种可靠的方式。

# CAVEATS

依赖于 NetworkManager 作为网络管理守护进程。当 NetworkManager 报告有连通性时即返回成功，但这不一定意味着可以完整访问互联网（例如强制门户）。默认的 30 秒超时可能因使用场景而偏长或偏短。

# INSTALL

```apt: sudo apt install network-manager```

```pacman: sudo pacman -S networkmanager```

```apk: sudo apk add networkmanager```

```nix: nix profile install nixpkgs#networkmanager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmcli](/man/nmcli)(1), [nmtui](/man/nmtui)(1), [NetworkManager](/man/NetworkManager)(8)
