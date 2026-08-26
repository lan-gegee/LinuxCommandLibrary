# TAGLINE

以交互方式配置 PPP 拨号连接

# TLDR

**启动交互式 PPP 配置菜单**（需要 root 权限）

```sudo pppconfig```

**创建新的提供商**配置

```sudo pppconfig create [provider_name]```

**修改现有的提供商**配置

```sudo pppconfig change [provider_name]```

**删除提供商**配置

```sudo pppconfig delete [provider_name]```

**快速修改电话号码、用户名或密码**

```sudo pppconfig quickchange [provider_name]```

# SYNOPSIS

**pppconfig** [_action_] [_provider_]

# PARAMETERS

**create** _provider_
> 创建新的提供商配置。

**change** _provider_
> 修改现有的提供商配置。

**delete** _provider_
> 删除现有的提供商配置。

**quickchange** _provider_
> 只修改电话号码、用户名和密码。

**--help**
> 显示帮助。

# DESCRIPTION

**pppconfig** 是 Debian 系统上用于配置 PPP（Point-to-Point Protocol，点对点协议）拨号连接的交互式文本工具。它引导用户设置调制解调器参数、电话号码、认证凭据和连接选项。

该工具在 **/etc/ppp/peers/** 中创建提供商配置文件，可与 **pon** 和 **poff** 配合来启动和停止连接。它支持 PAP 和 CHAP 两种认证方式，并可配置多个 ISP 配置文件。

# CAVEATS

Debian 专属工具。用于拨号网络。

# HISTORY

pppconfig 为 **Debian** 的 PPP 连接配置而创建。

# INSTALL

```aur: yay -S pppconfig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pppd](/man/pppd)(8), [pon](/man/pon)(1), [poff](/man/poff)(1), [pppoeconf](/man/pppoeconf)(8)
