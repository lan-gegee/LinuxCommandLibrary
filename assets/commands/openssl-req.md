# TAGLINE

创建和处理证书签名请求

# TLDR

**生成带新密钥的 CSR**

```openssl req -new -newkey rsa:[4096] -keyout [private.key] -out [request.csr]```

**用现有密钥生成 CSR**

```openssl req -new -key [private.key] -out [request.csr]```

**生成自签名证书**

```openssl req -x509 -newkey rsa:[4096] -keyout [key.pem] -out [cert.pem] -days [365] -noenc```

**查看 CSR 内容**

```openssl req -in [request.csr] -text -noout```

**校验 CSR 签名**

```openssl req -in [request.csr] -verify -noout```

**在命令行上指定主题生成 CSR**

```openssl req -new -key [private.key] -out [request.csr] -subj "/C=[US]/ST=[State]/L=[City]/O=[Org]/CN=[example.com]"```

**使用配置文件生成 CSR**

```openssl req -new -config [openssl.cnf] -keyout [key.pem] -out [request.csr]```

**生成带 SAN 扩展的自签名证书**

```openssl req -x509 -newkey rsa:[4096] -keyout [key.pem] -out [cert.pem] -days [365] -noenc -addext "subjectAltName=DNS:[example.com],DNS:[www.example.com]"```

# SYNOPSIS

**openssl req** [_options_]

# PARAMETERS

**-new**
> 生成新的 CSR。

**-x509**
> 输出证书而不是 CSR。

**-newkey** _type:bits_
> 生成新密钥。

**-key** _file_
> 使用现有密钥。

**-keyout** _file_
> 密钥输出文件。

**-out** _file_
> 输出文件。

**-days** _n_
> 有效期（仅与 -x509 搭配使用）。

**-noenc**
> 不加密输出的密钥。取代已弃用的 -nodes。

**-nodes**
> 不加密密钥。在 OpenSSL 3.0 中已弃用；请改用 -noenc。

**-subj** _subj_
> 设置主题 DN（例如 /C=US/O=Org/CN=host）。

**-addext** _ext_
> 添加证书扩展（例如 subjectAltName=DNS:example.com）。

**-config** _file_
> 使用替代配置文件。

**-text**
> 以人类可读的形式打印 CSR 或证书。

**-noout**
> 抑制编码后请求的输出。

**-verify**
> 校验 CSR 上的签名。

**-in** _file_
> 输入的 CSR 文件。

**-inform** _DER|PEM_
> 输入格式。默认为 PEM。

**-outform** _DER|PEM_
> 输出格式。默认为 PEM。

**-*digest***
> 用于签署请求的消息摘要（例如 -sha256、-sha384）。

# DESCRIPTION

**openssl req** 创建和处理证书签名请求（CSR）。它还可以生成用于测试的自签名证书。

CSR 会提交给证书颁发机构（CA）以换取签名的证书。

# SUBJECT FORMAT

```bash
openssl req -new -key key.pem -out csr.pem \
  -subj "/C=US/ST=State/L=City/O=Org/CN=example.com"
```

# CAVEATS

自签名证书未经手动导入不会被浏览器信任。-nodes 标志自 OpenSSL 3.0 起已弃用；请改用 -noenc。CSR 不包含私钥。

# HISTORY

证书请求功能自 OpenSSL 的 SSL/TLS 实现起源之初就是其组成部分。

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

[openssl](/man/openssl)(1), [openssl-x509](/man/openssl-x509)(1), [openssl-ca](/man/openssl-ca)(1), [openssl-genpkey](/man/openssl-genpkey)(1), [openssl-pkey](/man/openssl-pkey)(1), [openssl-rsa](/man/openssl-rsa)(1)
