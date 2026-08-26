# TAGLINE

管理 ICE 授权条目

# TLDR

**列出条目**

```iceauth list```

**提取到文件**

```iceauth extract [auth-file]```

**添加条目**

```iceauth add [protocol] [address] [auth-name] [auth-data]```

**从文件合并**

```iceauth merge [auth-file]```

# SYNOPSIS

**iceauth** [_options_] [_command_]

# PARAMETERS

_COMMAND_
> 命令（list、add、remove、extract、merge）。

**list**
> 列出授权条目。

**add**
> 添加条目。

**remove**
> 移除条目。

**extract**
> 提取到文件。

**merge**
> 从文件合并。

**--help**
> 显示帮助信息。

# DESCRIPTION

**iceauth** 管理 ICE（Inter-Client Exchange，客户端间交换）授权条目。ICE 用于 X11 客户端之间的通信。

该工具处理 X 会话管理器及类似应用程序的认证记录，其作用类似于 X 显示连接中的 xauth。

# CAVEATS

X11 特有。由会话管理器使用。属于底层工具。

# HISTORY

iceauth 是 **X.Org** 的组成部分，用于管理 ICE 协议认证，应用于 X 会话管理。

# INSTALL

```apt: sudo apt install x11-xserver-utils```

```dnf: sudo dnf install iceauth```

```apk: sudo apk add iceauth```

```zypper: sudo zypper install iceauth```

```nix: nix profile install nixpkgs#iceauth```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xauth](/man/xauth)(1), [Xorg](/man/Xorg)(1)
