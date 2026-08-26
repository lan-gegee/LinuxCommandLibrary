# TAGLINE

发起 PPP 拨号连接

# TLDR

**启动 PPP 连接**

```pon```

**启动特定提供商的连接**

```pon [provider]```

**以调试模式启动**

```pon [provider] debug```

# SYNOPSIS

**pon** [_provider_] [_options_]

# PARAMETERS

_PROVIDER_
> PPP 提供商名称。

**debug**
> 启用调试输出。

# DESCRIPTION

**pon** 使用指定的提供商配置发起 PPP（点对点协议）连接。提供商配置存储在 **/etc/ppp/peers/** 中，定义了包括电话号码、身份验证和调制解调器设置在内的连接参数。

不带提供商参数时使用默认提供商。**debug** 选项启用详细日志输出到 syslog。使用 **poff** 终止连接。

# CAVEATS

仅适用于 PPP。与 poff 命令配套使用。属于老旧的拨号上网方式。

# HISTORY

pon 为 Linux 系统上的 **PPP 连接**建立而创建。

# INSTALL

```apt: sudo apt install ppp```

```dnf: sudo dnf install ppp```

```pacman: sudo pacman -S ppp```

```apk: sudo apk add ppp-daemon```

```zypper: sudo zypper install ppp```

```nix: nix profile install nixpkgs#ppp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poff](/man/poff)(1), [pppd](/man/pppd)(8), [pppconfig](/man/pppconfig)(8)
