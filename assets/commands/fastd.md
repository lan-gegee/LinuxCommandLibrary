# TAGLINE

快速安全的 VPN 守护进程

# TLDR

**以配置启动 fastd**

```fastd --config [/etc/fastd/fastd.conf]```

**生成密钥对**

```fastd --generate-key```

**从私钥显示公钥**

```fastd --show-key --secret [secret.key]```

**以前台模式启动**

```fastd --config [config] --log-level debug```

**校验配置**语法

```fastd --verify-config --config [config]```

**作为守护进程运行**并使用 PID 文件

```fastd --config [config] --daemon --pid-file [/var/run/fastd.pid]```

# SYNOPSIS

**fastd** [_options_]

# PARAMETERS

**--config** _file_
> 配置文件路径。

**--generate-key**
> 生成新密钥对。

**--show-key**
> 显示公钥。

**--secret** _file_
> 私钥文件。

**--log-level** _level_
> 日志级别（fatal、error、warn、info、verbose、debug）。

**--verify-config**
> 校验配置语法。

**--daemon**
> 作为守护进程运行。

**--pid-file** _file_
> 将 PID 写入文件。

**--user** _user_
> 降权到指定用户运行。

**--interface** _name_
> TUN/TAP 接口名称。

# CONFIGURATION

**/etc/fastd/fastd.conf**
> 主配置文件，定义接口、对端节点、加密方法和网络设置。

# DESCRIPTION

**fastd** 是一个快速而安全的 VPN 守护进程，专为构建网状网络和隧道传输流量而设计。它常用于 Freifunk 社区无线网络中，创建加密的网状拓扑。

该工具支持多种加密方法，针对低延迟、高性能的 VPN 连接进行了优化。它使用 UDP 传输，支持多种认证和加密算法。配置文件定义对端节点、网络接口和安全参数。

# INSTALL

```apt: sudo apt install fastd```

```dnf: sudo dnf install fastd```

```pacman: sudo pacman -S fastd```

```brew: brew install fastd```

```nix: nix profile install nixpkgs#fastd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wg](/man/wg)(8), [openvpn](/man/openvpn)(8), [ipsec](/man/ipsec)(8)
