# TAGLINE

查看远程虚拟机的显示画面

# TLDR

**连接到 SPICE 服务器**

```remote-viewer spice://[host]:[port]```

**连接到 VNC 服务器**

```remote-viewer vnc://[host]:[port]```

使用 virt-viewer 文件查看远程桌面

```remote-viewer [path/to/connection.vv]```

以全屏模式**连接**

```remote-viewer -f spice://[host]:[port]```

使用自定义窗口标题**连接**

```remote-viewer -t "[My VM]" spice://[host]:[port]```

以指定缩放级别**连接**

```remote-viewer -z [150] spice://[host]:[port]```

# SYNOPSIS

**remote-viewer** [_options_] [_URI_|_file_]

# PARAMETERS

**-f**, **--full-screen**
> 以全屏模式启动。

**-t** _TITLE_, **--title** _TITLE_
> 设置窗口标题。

**-z** _PCT_, **--zoom=** _PCT_
> 显示窗口的缩放级别（百分比）。

**-v**, **--verbose**
> 显示有关连接的信息。

**--spice-controller**
> 使用 SPICE 控制器初始化连接。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本号。

# DESCRIPTION

**remote-viewer** 是一个简单的远程显示客户端，支持 SPICE 和 VNC 协议。它可以连接到远程虚拟机或物理系统并显示其图形输出。

连接参数可以通过命令行上的 URI 指定，也可以通过 virt-viewer 配置文件指定。配置文件还支持其他参数，如主机、端口、TLS 设置、用户名和密码。

# CAVEATS

需要与连接协议（SPICE、VNC）对应的客户端库。显示质量取决于网络带宽。

# HISTORY

属于 **virt-viewer** 的一部分，为虚拟机管理提供远程显示工具，通常与 libvirt 和 QEMU/KVM 配合使用。

# INSTALL

```apt: sudo apt install virt-viewer```

```dnf: sudo dnf install virt-viewer```

```pacman: sudo pacman -S virt-viewer```

```apk: sudo apk add virt-viewer```

```zypper: sudo zypper install virt-viewer```

```nix: nix profile install nixpkgs#virt-viewer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virt-viewer](/man/virt-viewer)(1), [virt-manager](/man/virt-manager)(1)
