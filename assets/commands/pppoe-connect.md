# TAGLINE

管理 PPPoE DSL 连接

# TLDR

**以默认配置启动 PPPoE 连接**

```sudo pppoe-connect```

**使用指定的配置文件连接**

```sudo pppoe-connect [/etc/ppp/pppoe.conf]```

# SYNOPSIS

**pppoe-connect** [_config_file_]

# PARAMETERS

_CONFIG_FILE_
> 配置文件路径。默认为 /etc/ppp/pppoe.conf。

# DESCRIPTION

**pppoe-connect** 是一个 shell 脚本，使用 Roaring Penguin 用户空间 PPPoE 客户端管理 PPPoE（PPP over Ethernet）连接。它读取配置文件，建立连接，并在连接断开时自动重新建立，同时将重连事件记录到 syslog。

每次连接断开时，如果 /etc/ppp/pppoe-lost 存在，pppoe-connect 就会执行它。通常应使用 **pppoe-start**，而不是直接调用 pppoe-connect。

# CAVEATS

需要配置好的 pppoe.conf 和 pppd。通常通过 pppoe-start 调用而不是直接运行。通过不同的 PIDFILE 设置和不同的配置文件可以支持多个连接。

# HISTORY

pppoe-connect 是 **Roaring Penguin PPPoE** 客户端软件包的一部分。

# INSTALL

```apt: sudo apt install pppoe```

```dnf: sudo dnf install rp-pppoe```

```pacman: sudo pacman -S rp-pppoe```

```apk: sudo apk add rp-pppoe```

```zypper: sudo zypper install rp-pppoe```

```nix: nix profile install nixpkgs#rp-pppoe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pppoe](/man/pppoe)(8), [pppoe-setup](/man/pppoe-setup)(8), [pppoe-stop](/man/pppoe-stop)(8), [pppd](/man/pppd)(8), [pppoe-discovery](/man/pppoe-discovery)(8)
