# TAGLINE

执行底层公钥操作

# TLDR

**使用私钥签名数据（对原始输入进行哈希）**

```openssl pkeyutl -sign -rawin -digest sha256 -in [data] -inkey [key.pem] -out [signature]```

**验证签名**

```openssl pkeyutl -verify -rawin -digest sha256 -in [data] -sigfile [sig] -inkey [key.pem]```

**使用公钥以 OAEP 填充加密数据**

```openssl pkeyutl -encrypt -in [data] -pubin -inkey [pub.pem] -pkeyopt rsa_padding_mode:oaep -out [encrypted]```

**使用私钥解密数据**

```openssl pkeyutl -decrypt -in [encrypted] -inkey [key.pem] -out [decrypted]```

**通过 ECDH 派生共享密钥**

```openssl pkeyutl -derive -inkey [key.pem] -peerkey [peer_pub.pem] -out [secret]```

# SYNOPSIS

**openssl** **pkeyutl** [_options_]

# PARAMETERS

**-sign**
> 对输入数据进行签名并输出签名结果。需要私钥。

**-verify**
> 用 **-sigfile** 指定的签名文件验证输入数据。

**-verifyrecover**
> 从签名中恢复原始数据。仅限 RSA。

**-encrypt**
> 使用公钥加密输入数据。

**-decrypt**
> 使用私钥解密输入数据。

**-derive**
> 使用对方公钥派生共享密钥（ECDH/DH）。

**-encap**
> 向对方公钥封装共享密钥（KEM 操作，如 ML-KEM）。

**-decap**
> 解封装以恢复共享密钥（KEM 操作，如 ML-KEM）。

**-in** _FILE_
> 输入文件（未指定时为 stdin）。

**-out** _FILE_
> 输出文件（未指定时为 stdout）。

**-secret** _FILE_
> 封装/解封装操作中共享密钥的输出文件。

**-inkey** _FILE_|_URI_
> 输入密钥文件。默认为私钥；用 **-pubin** 或 **-certin** 提供公钥。

**-sigfile** _FILE_
> 签名文件，**-verify** 操作必需。

**-peerkey** _FILE_
> 对方公钥文件，与 **-derive** 配合用于 ECDH/DH 密钥协商。

**-pubin**
> 将通过 **-inkey** 提供的密钥视为公钥。

**-certin**
> 将通过 **-inkey** 提供的内容视为证书，并从中提取公钥。

**-keyform** _PEM_|_DER_|_P12_
> 密钥文件的格式。默认为 PEM。

**-peerform** _PEM_|_DER_|_P12_
> 对方密钥文件的格式。默认为 PEM。

**-passin** _ARG_
> 加密私钥的口令来源（如 `pass:secret`、`env:VAR`、`file:path`）。

**-rawin**
> 将输入视为未经哈希的原始数据。工具会使用 **-digest** 指定的算法在内部对其进行哈希。Ed25519/Ed448 必需此选项，RSA-PSS 签名也建议使用。

**-digest** _ALGORITHM_
> 设置 **-rawin** 时使用的哈希算法（如 `sha256`、`sha512`）。RSA/DSA/ECDSA 默认为 SHA-256，SM2 默认为 SM3。

**-pkeyopt** _opt_:_value_
> 设置算法特定的选项。可重复使用。常用选项：
>
> - `rsa_padding_mode:pkcs1|oaep|pss|none` — RSA 填充模式（默认：`pkcs1`）
> - `rsa_oaep_md:digest` — OAEP 标签所用的哈希（默认：`sha1`）
> - `rsa_mgf1_md:digest` — PSS 或 OAEP 的 MGF1 摘要
> - `rsa_pss_saltlen:len|digest|max|auto` — PSS 盐值长度
> - `distid:string` — SM2 区分 ID（签名/验签必须一致）

**-kdf** _ALGORITHM_
> 要使用的密钥派生函数（如 `TLS1-PRF`、`HKDF`）。

**-kdflen** _LENGTH_
> KDF 操作的输出长度（字节）。

**-rev**
> 在处理前反转输入缓冲区的字节序。与 **-rawin** 不兼容。

**-hexdump**
> 以十六进制转储形式显示输出数据。

**-asn1parse**
> 将输出解析并以 ASN.1 形式显示。

# DESCRIPTION

**openssl pkeyutl** 执行底层公钥密码学操作，包括签名、验签、加密、解密、密钥派生以及密钥封装/解封装（KEM）。它与具体算法无关，可用于 OpenSSL 支持的任何密钥类型，包括 RSA、EC、DSA、Ed25519、Ed448、X25519、X448、SM2 以及 ML-DSA 和 ML-KEM 等后量子算法。

与更高层的 OpenSSL 命令不同，它直接处理数据，可以对填充方案、摘要选择和密钥协商协议进行细粒度控制。默认情况下它期望输入已经过摘要计算；传入 **-rawin** 并配合 **-digest** 可让工具在操作前自行哈希数据。

对于 Ed25519 和 Ed448，整个输入文件会一次性加载到内存中处理；这些算法不支持预哈希。

# CAVEATS

属于 OpenSSL 的一部分。非 raw 操作的输入大小限制为 `EVP_MAX_MD_SIZE`（64 字节）；任意长度的输入请使用 **-rawin**。RSA PKCS#1 v1.5 解密采用隐式拒绝（填充失败时返回确定性的随机明文）以缓解 Bleichenbacher 攻击。新的 RSA 加密应用请使用 OAEP 填充（`-pkeyopt rsa_padding_mode:oaep`）。Ed25519/Ed448 的签名和验签会将整个文件加载到内存中。

# HISTORY

**openssl pkeyutl** 为所有算法提供公钥操作，在 RSA 特定用途上取代了较早的 **rsautl** 子命令。KEM 操作（**-encap**/**-decap**）和后量子算法支持是在 OpenSSL 3.x 中加入的。

# SEE ALSO

[openssl](/man/openssl)(1), [openssl-pkey](/man/openssl-pkey)(1), [openssl-genpkey](/man/openssl-genpkey)(1), [openssl-dgst](/man/openssl-dgst)(1)
