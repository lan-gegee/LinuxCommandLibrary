# TAGLINE

管理 Java 密钥库和证书

# TLDR

**生成密钥对**

```keytool -genkeypair -alias [mykey] -keystore [keystore.jks]```

**列出密钥库内容**

```keytool -list -keystore [keystore.jks]```

**导出证书**

```keytool -exportcert -alias [mykey] -keystore [keystore.jks] -file [cert.cer]```

**导入证书**

```keytool -importcert -alias [trusted] -file [cert.cer] -keystore [keystore.jks]```

**修改密钥库密码**

```keytool -storepasswd -keystore [keystore.jks]```

**删除条目**

```keytool -delete -alias [mykey] -keystore [keystore.jks]```

**生成证书签名请求（CSR）**

```keytool -certreq -alias [mykey] -keystore [keystore.jks] -file [request.csr]```

**从文件打印证书详情**

```keytool -printcert -file [cert.cer]```

**将 PKCS#12 密钥库导入 JKS 密钥库**

```keytool -importkeystore -srckeystore [keystore.p12] -srcstoretype PKCS12 -destkeystore [keystore.jks]```

# SYNOPSIS

**keytool** _command_ [_options_]

# PARAMETERS

**-genkeypair**
> 生成密钥对。

**-list**
> 列出密钥库条目。

**-exportcert**
> 导出证书。

**-importcert**
> 导入证书或证书链。

**-certreq**
> 生成证书签名请求（CSR）。

**-printcert**
> 打印证书文件的内容。

**-importkeystore**
> 从另一个密钥库导入条目。

**-delete**
> 删除密钥库条目。

**-changealias**
> 更改条目的别名。

**-genseckey**
> 生成秘密（对称）密钥。

**-alias** _NAME_
> 条目别名。

**-keystore** _FILE_
> 密钥库文件。

**-storetype** _TYPE_
> 密钥库类型（JKS、PKCS12）。

**-storepass** _PASS_
> 密钥库密码。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**keytool** 是 Java 开发工具包自带的密钥和证书管理工具。它可以生成加密密钥对、创建证书签名请求（CSR）、导入和导出 X.509 证书，并管理存储私钥和受信任证书链的密钥库——Java 应用程序在 SSL/TLS、代码签名和身份验证时会用到这些内容。

该工具支持多种密钥库格式，包括传统的 Java KeyStore（JKS）和业界标准的 PKCS#12 格式。它常用于为基于 Java 的 Web 服务器配置 HTTPS、通过导入 CA 证书建立信任关系，以及查看现有密钥库的内容。密钥库中的每个条目由一个别名标识，访问由密钥库级密码保护，还可选地为每个密钥设置单独的密码。

# CAVEATS

属于 JDK 的一部分，凡安装了 Java 的环境均可使用。Java 9 起默认密钥库类型从 JKS 变更为 PKCS12。应妥善保管密钥库密码和密钥密码。`-storepass` 标志会使密码暴露在进程列表中；省略它可改为交互式输入。

# HISTORY

keytool 自早期版本起就是 **JDK** 的组成部分，为 Java 应用程序提供证书和密钥管理功能。

# SEE ALSO

[openssl](/man/openssl)(1), [java](/man/java)(1), [jarsigner](/man/jarsigner)(1)
