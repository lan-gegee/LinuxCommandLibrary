# TAGLINE

创建和解析 PKCS#12 文件

# TLDR

**用证书和密钥创建 PKCS12**

```openssl pkcs12 -export -out [certificate.p12] -inkey [private.key] -in [certificate.crt]```

**包含 CA 链**

```openssl pkcs12 -export -out [cert.p12] -inkey [key.pem] -in [cert.pem] -certfile [ca-chain.pem]```

**提取证书**

```openssl pkcs12 -in [certificate.p12] -clcerts -nokeys -out [certificate.crt]```

**提取私钥**

```openssl pkcs12 -in [certificate.p12] -nocerts -out [private.key]```

**全部提取为 PEM**

```openssl pkcs12 -in [certificate.p12] -out [all.pem] -nodes```

# SYNOPSIS

**openssl pkcs12** [_options_]

# PARAMETERS

**-export**
> 创建 PKCS12 文件。

**-in** _file_
> 输入文件。

**-out** _file_
> 输出文件。

**-inkey** _file_
> 私钥文件。

**-certfile** _file_
> 附加的证书。

**-nokeys**
> 不输出密钥。

**-nocerts**
> 不输出证书。

**-nodes**
> 不加密输出。

**-name** _name_
> 友好名称。

**-password** _arg_
> 输入/输出 PKCS#12 密码的来源（例如 `pass:secret`、`file:path`、`env:VAR`、`stdin`）。

**-passin** _arg_, **-passout** _arg_
> 分开的输入/输出密码来源。

**-legacy**
> 使用遗留算法以兼容较旧的软件（OpenSSL 3+）。

**-clcerts**
> 仅输出客户端证书（不含 CA）。

**-info**
> 打印关于 PKCS#12 文件结构的信息。

# DESCRIPTION

**openssl pkcs12** 用于创建和解析 PKCS#12 文件（.p12、.pfx）。这些文件将私钥、证书和 CA 链打包到单个加密文件中。

常用于在浏览器和应用程序中导入/导出证书。

# COMMON USES

```
- Export from browser/keychain
- Import to Java keystore
- Certificate backup
- Cross-platform transfer
```

# CAVEATS

PKCS12 密码可能被暴力破解。请使用强密码。遗留格式默认使用弱加密。

# HISTORY

PKCS#12 是 RSA Laboratories 制定的标准，作为便携式证书存储方案得到广泛支持。

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

[openssl-x509](/man/openssl-x509)(1), [openssl-rsa](/man/openssl-rsa)(1), [keytool](/man/keytool)(1)
