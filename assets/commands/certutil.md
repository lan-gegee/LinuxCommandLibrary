# TAGLINE

NSS 证书数据库管理

# TLDR

**列出数据库中的证书**

```certutil -L -d [~/.pki/nssdb]```

**向数据库添加证书**

```certutil -A -n "[alias]" -t "CT,," -d [~/.pki/nssdb] -i [cert.pem]```

**生成密钥对**

```certutil -G -d [~/.pki/nssdb] -n "[keyname]"```

**删除证书**

```certutil -D -n "[alias]" -d [~/.pki/nssdb]```

**创建自签名证书**

```certutil -S -n "[alias]" -x -t "CT,," -d [~/.pki/nssdb] -s "CN=[hostname]"```

**显示证书详情**

```certutil -L -d [~/.pki/nssdb] -n "[alias]"```

# SYNOPSIS

**certutil** [_options_]

# DESCRIPTION

**certutil** 管理 NSS（Network Security Services）数据库中的密钥和证书。它可以创建、修改、列出和删除基于 NSS 库构建的应用程序所使用的证书与密钥对，这些应用包括 Firefox、Thunderbird 和 Chromium 系浏览器。

NSS 数据库以目录形式存储证书，现代版本使用 SQLite（通过 `sql:` 前缀指定）。该工具处理完整的证书生命周期，包括生成密钥对、创建自签名证书、导入 CA 证书以及管理信任标志——后者控制证书在 SSL、电子邮件签名和代码签名中的使用方式。

信任标志的格式为 "SSL,Email,Object Signing"，其中 `C` 表示受信任的 CA，`T` 表示可用于客户端认证的可信证书。

# PARAMETERS

**-A**
> 向数据库添加证书

**-D**
> 从数据库删除证书

**-L**
> 列出证书

**-G**
> 生成新的密钥对

**-S**
> 创建并添加自签名证书

**-R**
> 生成证书请求

**-C**
> 根据请求创建证书

**-K**
> 列出数据库中的密钥

**-d** _dir_
> 数据库目录（SQLite 需加 sql: 前缀）

**-n** _name_
> 证书昵称/别名

**-t** _trust_
> 信任标志（如 "CT,,"）

**-i** _file_
> 输入文件

**-o** _file_
> 输出文件

**-x**
> 自签名证书

**-s** _subject_
> 主题 DN 字符串

**-v** _months_
> 有效期（月）

# DATABASE TYPES

**sql:dir**: SQLite 数据库（推荐）

**dbm:dir**: 旧式 BerkeleyDB 格式

# TRUST FLAGS

格式："SSL,Email,Object Signing"（如 "CT,,"）

**C**: 受信任的 CA

**T**: 可用于客户端认证

**p**: 有效对等方

# CAVEATS

需要 nss-tools 软件包。现代数据库请使用 sql: 前缀。该工具会处理敏感密钥；请以最小权限运行。

# INSTALL

```apt: sudo apt install libnss3-tools```

```dnf: sudo dnf install nss-tools```

```apk: sudo apk add nss-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [modutil](/man/modutil)(1)
