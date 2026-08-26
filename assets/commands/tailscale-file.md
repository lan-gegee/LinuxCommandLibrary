# TAGLINE

在 Tailscale 设备之间传输文件

# TLDR

**向设备发送文件**

```tailscale file cp [file] [device]:```

**接收文件**

```tailscale file get [directory]```

**列出待接收的文件**

```tailscale file get --wait=false .```

# SYNOPSIS

**tailscale** **file** _command_ [_options_]

# PARAMETERS

**cp** _file_ _target_
> 向设备发送文件。

**get** _directory_
> 接收待处理的文件。

**--wait**
> 等待文件到来。

# DESCRIPTION

**tailscale file** 借助 Taildrop 功能在你的 Tailscale 网络中的设备之间传输文件。文件通过加密的 WireGuard 连接从一台设备直接发送到另一台，不经过云存储或第三方服务器。

**cp** 子命令将文件发送到目标设备，目标以其 Tailscale 主机名加冒号表示。**get** 子命令把待处理的文件接收到本地目录。默认情况下，接收方会等待传入的传输；**--wait=false** 标志可列出待处理文件而不阻塞。传输支持 Linux、macOS、Windows、iOS 和 Android 等跨平台使用。

# INSTALL

```dnf: sudo dnf install tailscale```

```pacman: sudo pacman -S tailscale```

```apk: sudo apk add tailscale```

```zypper: sudo zypper install tailscale```

```brew: brew install tailscale```

```nix: nix profile install nixpkgs#tailscale```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tailscale](/man/tailscale)(1)
