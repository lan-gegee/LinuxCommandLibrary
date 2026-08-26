# TAGLINE

用于管理 Wi-Fi 网络的终端用户界面

# TLDR

以**站点模式**启动

```impala```

以**接入点模式**启动

```impala -m ap```

在各个区域之间**导航**

```Tab / Shift+Tab```

**选中**一个网络

```Space```

显示**快捷键**

```?```

# SYNOPSIS

**impala** [_options_]

# DESCRIPTION

**impala** 是一个用于管理 Wi-Fi 网络的终端用户界面（TUI）。它提供了一种交互方式，无需直接使用命令行即可扫描、连接和管理无线连接。

# PARAMETERS

**-m, --mode MODE**
> 设置运行模式："station"（默认）或 "ap"（接入点）

**-h, --help**
> 显示帮助信息

**-V, --version**
> 显示版本信息

# CAVEATS

需要相应的无线网卡和权限。接入点模式要求无线网卡支持 AP 模式。使用 iwd（iNet Wireless Daemon）作为后端。

# HISTORY

**impala** 的创建目的是为无线网络管理提供一个友好的 TUI，让在终端环境中管理 Wi-Fi 连接更加轻松。

# INSTALL

```pacman: sudo pacman -S impala```

```apk: sudo apk add impala```

```zypper: sudo zypper install impala```

```nix: nix profile install nixpkgs#impala```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iwctl](/man/iwctl)(1), [nmtui](/man/nmtui)(1), [nmcli](/man/nmcli)(1), [wpa_cli](/man/wpa_cli)(8)
