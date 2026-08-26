# TAGLINE

TigerVNC 远程桌面查看器

# TLDR

**连接到 VNC 服务器**

```vncviewer [hostname:display]```

**连接到特定端口**

```vncviewer [hostname::5901]```

**以全屏模式连接**

```vncviewer -FullScreen [hostname:1]```

**以只读模式连接**

```vncviewer -ViewOnly [hostname:1]```

**通过 SSH 隧道连接**

```vncviewer -via [gateway] [hostname:1]```

**使用密码文件连接**

```vncviewer -passwd [~/.vnc/passwd] [hostname:1]```

**监听反向连接**

```vncviewer -listen [5500]```

**设置首选编码**

```vncviewer -PreferredEncoding Tight [hostname:1]```

# SYNOPSIS

**vncviewer** [_options_] [_host_][:_display_]

**vncviewer** [_options_] [_host_][::_port_]

**vncviewer** [_options_] **-listen** [_port_]

# PARAMETERS

**-FullScreen**
> 以全屏模式启动。

**-FullScreenAllMonitors**
> 全屏时使用所有显示器。

**-Maximize**
> 最大化查看器窗口。

**-ViewOnly**
> 禁用键盘和鼠标输入。

**-Shared**
> 与已有连接共享桌面。

**-listen** _port_
> 监听反向连接（默认：5500）。

**-via** _gateway_
> 通过 SSH 网关建隧道。

**-passwd** _file_
> 密码文件的位置。

**-geometry** _WxH+X+Y_
> 初始窗口位置和大小。

**-PreferredEncoding** _encoding_
> 编码：Tight、ZRLE、hextile、raw。

**-QualityLevel** _n_
> JPEG 质量（0-9，默认：8）。

**-CompressLevel** _n_
> 压缩级别（0-6，默认：2）。

**-NoJPEG**
> 禁用 JPEG 压缩。

**-AutoSelect**
> 自动选择编码和格式。

**-AcceptClipboard**
> 接受来自服务器的剪贴板内容。

**-SendClipboard**
> 将剪贴板内容发送到服务器。

**-X509CA** _file_
> 用于 TLS 的 CA 证书。

**-Log** _config_
> 调试日志配置。

**-h**
> 显示帮助。

# DESCRIPTION

**TigerVNC**（vncviewer）是一款用于连接远程桌面的 VNC 客户端。它显示远程 VNC 服务器的图形桌面，并允许通过键盘和鼠标进行交互。

该查看器支持多种针对不同网络条件优化的编码：低带宽下采用带 JPEG 压缩的 Tight 编码，局域网内可采用 raw 或 hextile。自动编码选择会根据连接质量自适应调整。

安全特性包括 TLS 加密和多种身份验证方式。-via 选项提供 SSH 隧道，可通过不可信网络建立安全连接。

TigerVNC 还可以通过 -listen 模式充当反向连接客户端，此时由服务器主动向查看器发起连接。

# CAVEATS

显示编号从 0 开始（对应端口 5900）。双冒号用于指定原始端口号。部分功能需要服务器端支持。退出全屏模式可能需要特定平台的按键组合。

# HISTORY

**TigerVNC** 是 TightVNC 的分支，专注于性能和安全性的改进。它起源于 20 世纪 90 年代末 Olivetti Research Laboratory 开发的 VNC（Virtual Network Computing）技术。TigerVNC 广泛应用于企业环境和 Linux 发行版中。

# INSTALL

```dnf: sudo dnf install tigervnc```

```pacman: sudo pacman -S tigervnc```

```zypper: sudo zypper install tigervnc```

```nix: nix profile install nixpkgs#tigervnc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vncserver](/man/vncserver)(1), [x11vnc](/man/x11vnc)(1), [ssh](/man/ssh)(1)
