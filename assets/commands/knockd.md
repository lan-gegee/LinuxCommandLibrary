# TAGLINE

端口敲门（port knocking）的服务器组件

# TLDR

以**守护进程**方式启动 knockd

```knockd -d```

使用**指定的配置**文件

```knockd -c [path/to/knockd.conf]```

# SYNOPSIS

**knockd** [_options_]

# PARAMETERS

**-d**, **--daemon**
> 在后台作为守护进程运行

**-c**, **--config** _FILE_
> 使用指定的配置文件

**-i**, **--interface** _IF_
> 要监听的网络接口

**-D**, **--debug**
> 输出调试消息

**-l**, **--lookup**
> 为日志条目解析 DNS 名称

# DESCRIPTION

**knockd** 是端口敲门的服务器组件。它监听特定的连接尝试序列，并在检测到有效序列时执行命令。

/etc/knockd.conf 中的配置定义了敲门序列及对应的命令。典型用途是在收到正确的敲门序列后为 SSH 访问打开防火墙端口。

打开 SSH 的示例配置：
```
[openSSH]
sequence = 7000,8000,9000
command = /sbin/iptables -A INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
```

# CAVEATS

如果不使用加密协议，敲门序列有可能被嗅探到。fwknop 等单包认证（SPA）工具可能更安全。必须保护配置文件免受未经授权的访问。

# HISTORY

端口敲门于 **21 世纪初**作为一种隐晦式安全（security through obscurity）技术被提出。尽管 SPA 等更先进的技术已经出现，knockd 仍是最流行的实现之一。

# INSTALL

```apt: sudo apt install knockd```

```dnf: sudo dnf install knock```

```pacman: sudo pacman -S knockd```

```apk: sudo apk add knock```

```zypper: sudo zypper install knockd```

```brew: brew install knock```

```nix: nix profile install nixpkgs#knock```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[knock](/man/knock)(1), [iptables](/man/iptables)(8)
