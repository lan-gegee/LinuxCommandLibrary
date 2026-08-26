# TAGLINE

Guacamole 代理守护进程，Apache Guacamole 的核心组件

# TLDR

**启动 guacd 守护进程**

```guacd```

**以前台模式运行**

```guacd -f```

**监听指定地址和端口**

```guacd -b [0.0.0.0] -l [4822]```

**以调试日志级别运行**

```guacd -f -L debug```

**指定 PID 文件**

```guacd -p [/var/run/guacd.pid]```

# SYNOPSIS

**guacd** [_options_]

# PARAMETERS

**-b** _address_
> 绑定到指定地址。

**-l** _port_
> 监听指定端口（默认 4822）。

**-f**
> 以前台模式运行。

**-L** _level_
> 日志级别（error、warning、info、debug）。

**-p** _file_
> PID 文件位置。

**-C** _file_
> SSL 证书文件。

**-K** _file_
> SSL 私钥文件。

# DESCRIPTION

**guacd** 是 Guacamole 代理守护进程，Apache Guacamole 的核心组件。它负责处理 Guacamole Web 应用与远程桌面协议（VNC、RDP、SSH、Telnet、Kubernetes）之间的连接。它用 C 语言编写以保证性能，将这些协议转换为 Guacamole 协议，供浏览器访问。

# INSTALL

```dnf: sudo dnf install guacd```

```apk: sudo apk add guacamole-server```

```nix: nix profile install nixpkgs#guacamole-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sshd](/man/sshd)(1)
