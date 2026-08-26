# TAGLINE

OpenLDAP 独立目录服务器

# TLDR

**以默认配置启动 slapd**

```sudo slapd```

**使用指定的配置文件启动**

```sudo slapd -f [/etc/openldap/slapd.conf]```

**启动并输出调试信息**（保持在前台）

```sudo slapd -d [1]```

**监听指定的 URL**

```sudo slapd -h "ldap://127.0.0.1:389/ ldaps:///"```

**以工具模式运行**（如 slapcat）

```slapd -T cat```

**显示版本信息**后退出

```slapd -VV```

不启动，仅**测试配置**

```slapd -T test```

# SYNOPSIS

**slapd** [**-4**|**-6**] [**-d** _debug-level_] [**-f** _config-file_] [**-F** _config-dir_] [**-h** _URLs_] [**-T** _tool_] [**-V**[**V**[**V**]]]

# PARAMETERS

**-f** _config-file_
> 指定 slapd 配置文件。默认：**/etc/openldap/slapd.conf**。

**-F** _config-dir_
> 指定 slapd 配置目录。默认：**/etc/openldap/slapd.d**。

**-d** _debug-level_
> 启用调试。slapd 将不会 fork，而是保持在终端上。调试级别是一个位串，每个位控制不同的调试信息。

**-h** _URLs_
> 指定要监听的 LDAP URL。示例：**ldap://**、**ldaps://**、用于基于 IPC 的 LDAP 的 **ldapi:///**。

**-4**
> 仅监听 IPv4 地址。

**-6**
> 仅监听 IPv6 地址。

**-T** _tool_
> 以工具模式运行。工具包括：**add**（slapadd）、**cat**（slapcat）、**dn**（slapdn）、**index**（slapindex）、**modify**（slapmodify）、**passwd**（slappasswd）、**schema**（slapschema）、**test**（slaptest）。

**-V**[**V**[**V**]]
> 打印版本信息。**-VV** 打印后退出。**-VVV** 还会包含静态 overlay 和后端的信息。

**-u**
> 以指定用户身份运行。

**-g**
> 以指定组身份运行。

**-r** _directory_
> chroot 到指定目录。

**-n** _service-name_
> 指定用于日志记录的服务名。

# DESCRIPTION

**slapd** 即 Stand-alone LDAP Daemon（独立 LDAP 守护进程），是 OpenLDAP 的核心服务器组件。它在配置的端口上监听 LDAP 连接（默认 LDAP 为 389，LDAPS 为 636），并响应 bind、search、add、modify、delete 等 LDAP 操作。

slapd 支持多种用于数据存储的后端（包括 MDB、HDB、BDB 和 LDAP 代理）、用于扩展功能的 overlay（如访问日志、密码策略和复制），以及包括 SASL 在内的多种身份验证机制。

配置既可以通过传统的 **slapd.conf** 文件提供，也可以通过 **slapd.d/** 中较新的基于 LDAP 的 **cn=config** 配置提供。该守护进程通常在开机时启动，并作为后台服务运行。

# CONFIGURATION

**/etc/openldap/slapd.conf**
> 传统的平面文件配置，包含后端、schema、ACL 和数据库设置。

**/etc/openldap/slapd.d/**
> 基于 LDAP 的配置目录（cn=config），可在运行时修改而无需重启。

**/etc/openldap/schema/**
> LDAP 对象类和属性的 schema 定义文件。

# CAVEATS

带 **-d** 标志运行会阻止守护进程化，仅用于调试。若配置目录（**-F**）与配置文件（**-f**）同时存在，前者优先。LDAPS 需要正确配置的 TLS 证书。写操作需要配置适当的 ACL。

# HISTORY

**slapd** 是 OpenLDAP 项目的一部分，该项目是轻量级目录访问协议的开源实现。OpenLDAP 的开发始于 **1998 年**的密歇根大学，是最初 U-M LDAP 项目的延续。该软件已发展为部署最广泛的 LDAP 服务器之一，被用于用户认证、通讯录和目录服务。项目目前仍在积极开发并定期发布新版本。

# INSTALL

```apt: sudo apt install slapd```

```dnf: sudo dnf install openldap```

```pacman: sudo pacman -S openldap```

```apk: sudo apk add openldap```

```brew: brew install openldap```

```nix: nix profile install nixpkgs#openldap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ldapsearch](/man/ldapsearch)(1), [ldapadd](/man/ldapadd)(1), [ldapmodify](/man/ldapmodify)(1)
