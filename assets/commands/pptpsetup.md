# TAGLINE

配置和管理 PPTP VPN 隧道

# TLDR

**创建 PPTP 隧道**

```pptpsetup --create [tunnel] --server [host] --username [user] --password [pass]```

**删除隧道**

```pptpsetup --delete [tunnel]```

**以加密方式创建**

```pptpsetup --create [tunnel] --server [host] --username [user] --password [pass] --encrypt```

# SYNOPSIS

**pptpsetup** [_options_]

# PARAMETERS

**--create** _NAME_
> 创建隧道。

**--delete** _NAME_
> 删除隧道。

**--server** _HOST_
> 服务器地址。

**--username** _USER_
> 身份验证用户名。

**--password** _PASS_
> 身份验证密码。

**--encrypt**
> 启用加密。

# DESCRIPTION

**pptpsetup** 是一个辅助脚本，用于简化 PPTP VPN 隧道配置的创建和管理。它在 **/etc/ppp/peers/** 中生成所需的 peer 配置文件，并将身份验证凭据存储在相应的 secrets 文件中。

**--encrypt** 选项为隧道启用 MPPE 加密。可以使用 **pon** 启动、使用 **poff** 停止由 pptpsetup 创建的隧道（通过隧道名称）。

# CAVEATS

PPTP 已被弃用。会在 /etc/ppp/ 中创建文件。

# HISTORY

pptpsetup 提供 **PPTP 隧道配置**的管理功能。

# INSTALL

```apt: sudo apt install pptp-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pptp](/man/pptp)(8), [pppd](/man/pppd)(8), [pon](/man/pon)(1)
