# TAGLINE

用于加密操作和 SSL/TLS 协议的强大工具包

# TLDR

**生成私钥**

```openssl genrsa -out [private.key] [2048]```

**生成证书签名请求**

```openssl req -new -key [private.key] -out [request.csr]```

**生成自签名证书**

```openssl req -x509 -newkey rsa:4096 -keyout [key.pem] -out [cert.pem] -days [365] -nodes```

**查看证书详情**

```openssl x509 -in [certificate.crt] -text -noout```

**检查证书是否过期**

```openssl x509 -enddate -noout -in [certificate.crt]```

**验证证书链**

```openssl verify -CAfile [ca.crt] [certificate.crt]```

**测试 SSL 连接**

```openssl s_client -connect [host:443]```

**加密文件**

```openssl enc -aes-256-cbc -salt -in [plaintext.txt] -out [encrypted.enc]```

**解密文件**

```openssl enc -aes-256-cbc -d -in [encrypted.enc] -out [decrypted.txt]```

**生成随机字节**

```openssl rand -base64 [32]```

# SYNOPSIS

**openssl** _command_ [_options_] [_arguments_]

# DESCRIPTION

**OpenSSL** 是一个用于加密操作、SSL/TLS 协议和证书管理的强大工具包。它提供生成密钥、创建证书、加密数据、测试连接以及执行各种密码学功能的命令。

该工具包支持众多算法：加密（AES、DES、ChaCha20）、哈希（SHA、MD5）和公钥密码（RSA、ECDSA、Ed25519）。它还可以作为客户端或服务器来测试 SSL/TLS 连接。

无论是管理证书的系统管理员、实现安全通信的开发者，还是分析加密配置的安全专业人员，OpenSSL 都是必不可少的工具。

# COMMON COMMANDS

**genrsa**
> 生成 RSA 私钥。

**req**
> 证书签名请求操作。

**x509**
> 证书操作。

**rsa**
> RSA 密钥处理。

**enc**
> 对称加密/解密。

**dgst**
> 消息摘要（哈希）。

**s_client**
> 用于测试的 SSL/TLS 客户端。

**s_server**
> 用于测试的 SSL/TLS 服务器。

**verify**
> 证书验证。

**rand**
> 随机数生成。

**pkcs12**
> PKCS#12 操作。

**ca**
> 证书颁发机构（CA）操作。

# PARAMETERS

**-in** _file_
> 输入文件。

**-out** _file_
> 输出文件。

**-noout**
> 不输出（仅查看时使用）。

**-text**
> 人类可读的输出。

**-nodes**
> 不对私钥做 DES 加密。

**-days** _n_
> 证书有效期限。

**-subj** _subject_
> 证书主题 DN。

# CAVEATS

旧版本存在已知漏洞（请定期更新）。加密命令会以交互方式提示输入密码。自签名证书会触发浏览器警告。部分遗留算法（MD5、DES）已不安全。

# HISTORY

**OpenSSL** 源自 **SSLeay**，由 **Eric Young** 和 **Tim Hudson** 于 **1995 年**创建。当 SSLeay 停止开发后，该项目于 **1998 年**分叉为 OpenSSL。它在互联网安全中具有举足轻重的地位，不过 **2014 年**的 **Heartbleed** 漏洞暴露了其维护方面的困境，由此带来了更多资金支持以及 OpenBSD 发起的 **LibreSSL** 分叉。

# INSTALL

```apt: sudo apt install openssl```

```dnf: sudo dnf install openssl```

```pacman: sudo pacman -S openssl```

```apk: sudo apk add openssl```

```zypper: sudo zypper install openssl```

```brew: brew install openssl```

```nix: nix profile install nixpkgs#openssl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh-keygen](/man/ssh-keygen)(1), [certbot](/man/certbot)(1), [gpg](/man/gpg)(1), [stunnel](/man/stunnel)(1)
