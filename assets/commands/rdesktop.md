# TAGLINE

开源远程桌面协议（RDP）客户端

# TLDR

**连接到远程计算机**

```rdesktop -u [username] -p [password] [host:3389]```

**以全屏模式连接**

```rdesktop -u [username] -p [password] -f [host]```

**使用自定义分辨率**

```rdesktop -u [username] -p [password] -g [1920]x[1080] [host]```

**使用域账号连接**

```rdesktop -u [username] -p [password] -d [domain] [host]```

**使用 16 位色深并通过压缩提升性能**

```rdesktop -u [username] -a 16 -z [host]```

**重定向剪贴板和声音**

```rdesktop -u [username] -r clipboard:PRIMARYCLIPBOARD -r sound:local [host]```

# SYNOPSIS

**rdesktop** [**-u** _user_] [**-p** _pass_] [**-d** _domain_] [**-f**] [**-g** _WxH_] [**-a** _bpp_] _host_[:_port_]

# PARAMETERS

**-u** _username_
> 用于身份验证的用户名。

**-p** _password_
> 密码（用 `-` 表示交互式提示输入）。

**-d** _domain_
> Windows 域名。

**-f**
> 全屏模式（按 Ctrl+Alt+Enter 切换）。

**-g** _WxH_
> 桌面几何尺寸（如 1920x1080）。

**-a** _bpp_
> 颜色深度（8、15、16、24、32）。

**-k** _layout_
> 键盘布局。

**-r** _device_
> 设备重定向（剪贴板、声音、磁盘、打印机）。

**-z**
> 启用 RDP 数据流压缩。

**-x** _experience_
> 带宽性能模式：b[roadband]、m[odem] 或 l[an]。

**-0**
> 连接到服务器的控制台会话。

**-T** _title_
> 设置窗口标题。

# DESCRIPTION

**rdesktop** 是一款开源的远程桌面协议（RDP）客户端，用于连接 Windows 机器。它让 Linux 用户可以远程访问 Windows 桌面和应用程序。

该工具支持多种 RDP 功能，包括剪贴板共享、声音重定向以及磁盘/打印机映射。

# CAVEATS

工具较老，较新的 RDP 版本建议考虑 xfreerdp。在命令行上传递密码不安全。部分现代 RDP 功能不受支持。网络级身份验证（NLA）可能需要额外配置。

# HISTORY

**rdesktop** 是最早的开源 RDP 客户端之一，其诞生是为了让 Linux 用户能够连接 Windows 终端服务。在微软公布协议规范之前，它就对 RDP 协议进行了逆向工程。

# INSTALL

```apt: sudo apt install rdesktop```

```dnf: sudo dnf install rdesktop```

```pacman: sudo pacman -S rdesktop```

```apk: sudo apk add rdesktop```

```zypper: sudo zypper install rdesktop```

```nix: nix profile install nixpkgs#rdesktop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xfreerdp](/man/xfreerdp)(1), [vinagre](/man/vinagre)(1), [remmina](/man/remmina)(1)
