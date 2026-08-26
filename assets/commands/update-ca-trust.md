# TAGLINE

管理系统 CA 证书信任库

# TLDR

**更新 CA 证书信任库**

```sudo update-ca-trust extract```

**更新信任库（简写形式）**

```sudo update-ca-trust```

**检查当前信任配置**

```update-ca-trust check```

# SYNOPSIS

**update-ca-trust** [_command_]

# COMMANDS

**extract**: 重建合并后的 CA 证书文件。

**check**: 校验信任配置的一致性。

# CERTIFICATE LOCATIONS

**添加受信任的证书：**
> /etc/pki/ca-trust/source/anchors/

**拉黑的证书：**
> /etc/pki/ca-trust/source/blacklist/

**输出目录：**
> /etc/pki/ca-trust/extracted/

# DESCRIPTION

**update-ca-trust** 在基于 Red Hat 的发行版上管理系统的 CA 证书信任库。它把来自多个来源的证书整合成统一的文件，供应用程序进行 SSL/TLS 验证时使用。

放入 anchors 目录的证书会被加入信任库；blacklist 目录中的证书则被显式标记为不受信任。PEM 和 DER 格式均受支持。

添加或删除证书后，需要运行 update-ca-trust extract 来重建合并的信任文件。此后，读取 /etc/pki/ca-trust/extracted/ 的应用程序就会使用更新后的证书。

# CAVEATS

更改必须运行 extract 之后才会生效。某些应用程序会缓存证书，需要重启。基于 Debian 的系统应改用 update-ca-certificates。不正确的证书可能导致 SSL 连接受损。

# HISTORY

**update-ca-trust** 是 Red Hat Enterprise Linux、Fedora 和 CentOS 上 ca-certificates 软件包的一部分。它取代了较旧的证书管理方法，提供了统一的信任配置方案，同时兼容 OpenSSL 和 NSS 两种库。

# SEE ALSO

[update-ca-certificates](/man/update-ca-certificates)(8), [openssl](/man/openssl)(1), [trust](/man/trust)(1), [p11-kit](/man/p11-kit)(8)
