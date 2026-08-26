# TAGLINE

对称加密与解密工具

# TLDR

**加密文件**：AES-256-CBC 加 PBKDF2

```openssl enc -aes-256-cbc -pbkdf2 -in [plaintext] -out [encrypted]```

**解密文件**

```openssl enc -d -aes-256-cbc -pbkdf2 -in [encrypted] -out [plaintext]```

**加密并以 base64 输出**

```openssl enc -aes-256-cbc -pbkdf2 -a -in [plaintext] -out [encrypted.b64]```

**显式指定密码**来源进行加密

```openssl enc -aes-256-cbc -pbkdf2 -pass pass:[password] -in [file] -out [encrypted]```

只**打印密钥和 IV** 而不加密

```openssl enc -aes-256-cbc -pbkdf2 -P -pass pass:[password]```

**列出可用的密码算法**

```openssl enc -list```

# SYNOPSIS

**openssl enc** [_options_]

# PARAMETERS

**-e**
> 加密输入数据（默认）。

**-d**
> 解密输入数据。

**-in** _FILE_
> 输入文件。

**-out** _FILE_
> 输出文件。

**-a**, **-base64**
> 对数据进行 Base64 编码/解码。

**-pass** _SOURCE_
> 密码来源（如 pass:password、file:pathname、env:var、stdin）。

**-k** _PASSWORD_
> 用于密钥派生的密码。已被 -pass 取代。

**-pbkdf2**
> 使用 PBKDF2 密钥派生（推荐；默认迭代次数 10000）。

**-iter** _COUNT_
> 覆盖 PBKDF2 迭代次数。

**-salt**
> 密钥派生时使用随机盐值（默认）。

**-nosalt**
> 不使用盐值。除测试外不建议。

**-K** _KEY_
> 十六进制形式的实际加密密钥。

**-iv** _IV_
> 十六进制形式的实际初始化向量。

**-P**
> 打印密钥和 IV 后退出；不执行加密或解密。

**-p**
> 打印密钥和 IV，然后继续执行加密/解密。

**-list**
> 列出所有支持的密码算法。

**-nopad**
> 禁用标准的块填充。

# DESCRIPTION

**openssl enc** 使用各种密码算法执行对称加密和解密。它是 OpenSSL 中的通用加密命令。

该命令支持众多密码算法，包括 AES、DES、Blowfish、Camellia、ChaCha20 等。从密码派生密钥时，应使用 **-pbkdf2** 进行加盐的安全密钥派生（默认已启用）。输出可以是二进制形式，也可以用 **-a** 进行 base64 编码。

常见用途包括文件加密、创建加密备份以及数据保护工作流。

# CAVEATS

不使用 **-pbkdf2** 时，OpenSSL 会采用易受字典攻击的旧式密钥派生函数。**-k** 选项已被 **-pass** 取代。除测试外使用 **-nosalt** 并不安全。密码丢失即意味着数据丢失。

# HISTORY

openssl enc 是开源密码学工具包 **OpenSSL** 的一部分。它通过命令行提供对称加密算法，用于数据保护。

# SEE ALSO

[openssl](/man/openssl)(1), [gpg](/man/gpg)(1), [age](/man/age)(1)
