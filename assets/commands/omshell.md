# TAGLINE

提供 OMAPI Shell 接口

# TLDR

**启动 OMAPI Shell**

```omshell```

**连接到服务器**

```omshell
> server [127.0.0.1]
> connect```

**设置密钥认证**

```omshell
> key [keyname] [secret]```

**创建租约**

```omshell
> new lease
> set ip-address = [192.168.1.100]
> create```

# SYNOPSIS

**omshell**

# PARAMETERS

**server** _ADDRESS_
> DHCP 服务器地址。

**connect**
> 连接到服务器。

**key** _NAME_ _SECRET_
> 设置认证密钥。

**new** _OBJECT_
> 创建新对象。

**open** _OBJECT_
> 打开已有对象。

# DESCRIPTION

**omshell** 提供 OMAPI Shell 接口，用于管理 ISC DHCP 服务器。

该工具通过 OMAPI 与 dhcpd 交互，允许运行时修改。

# CAVEATS

需要启用 OMAPI。属于 ISC DHCP 的一部分。建议启用认证。

# HISTORY

omshell 为通过 OMAPI 协议进行**运行时 DHCP 管理**而生。

# SEE ALSO

[dhcpd](/man/dhcpd)(1), [dhclient](/man/dhclient)(1)


# INSTALL

```apt: sudo apt install isc-dhcp-server```

<!-- packages: 2026-07-22 -->
