# TAGLINE

处理 RFC 3161 时间戳权威（TSA）操作

# TLDR

**创建时间戳请求**

```openssl ts -query -data [file] -out [request.tsq]```

**创建时间戳响应**

```openssl ts -reply -queryfile [request.tsq] -signer [cert.pem] -out [response.tsr]```

**验证时间戳**

```openssl ts -verify -data [file] -in [response.tsr] -CAfile [ca.pem]```

**打印时间戳请求**

```openssl ts -query -in [request.tsq] -text```

# SYNOPSIS

**openssl** **ts** _command_ [_options_]

# PARAMETERS

**-query**
> 创建时间戳请求。

**-reply**
> 创建时间戳响应。

**-verify**
> 验证时间戳响应。

**-data** _file_
> 要加时间戳的数据文件。

**-in** _file_
> 输入文件。

**-out** _file_
> 输出文件。

**-text**
> 以人类可读形式打印。

**-config** _FILE_
> 指定自定义的 `openssl.cnf`。

**-queryfile** _FILE_
> 在生成响应（**-reply**）或验证（**-verify**）时，指向已有 TSQ 文件的路径。

**-digest** _HEX_
> 提供预先计算好的摘要，而不是对 `-data` 进行哈希。

**-no_nonce**
> 请求中不包含 nonce。

**-cert**
> 要求 TSA 将其证书包含在响应中。

**-signer** _FILE_
> **-reply** 所使用的签名证书（PEM）。

**-inkey** _FILE_|_URI_
> 与 `-signer` 匹配的私钥。

**-chain** _FILE_
> 要包含在响应链中的额外证书。

**-tspolicy** _OID_
> TSA 声明的策略 OID。

**-untrusted** _FILES_
> **-verify** 期间构建证书链所用的非受信中间证书。

**-CAfile** _FILE_, **-CApath** _DIR_, **-CAstore** _URI_
> **-verify** 期间使用的信任锚。

**-attime** _TIMESTAMP_
> 假设在特定时间点进行验证。

**-token_in**, **-token_out**
> 读/写裸 PKCS#7 令牌而非完整的 TimeStampResp。

# DESCRIPTION

**openssl ts** 处理 RFC 3161 时间戳权威（TSA）操作。它可以创建时间戳请求（TSQ）、以 TSA 服务器身份生成响应（TSR），以及验证已有的 TSR。它主要用于证明数据在特定时间以特定形式存在——例如文件公证、代码签名的会签以及归档完整性。

三种运行模式互斥：

- **-query** — 客户端侧创建请求。
- **-reply** — 服务器侧创建响应（需要签名者证书和密钥）。
- **-verify** — 客户端侧对照原始数据（或摘要）和信任库验证响应。

# CAVEATS

要求 TSA 证书能链接到所提供信任库中的某个 CA。使用 **-no_nonce** 会使响应可被重放——除非你要对接的协议强制要求，否则应避免。在 OpenSSL 3 系列中，该命令在手册中也可通过 `openssl-ts(1ssl)` 查看。

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

[openssl](/man/openssl)(1), [gpg](/man/gpg)(1)
