# TAGLINE

执行消息摘要操作

# TLDR

**计算文件的 SHA256 哈希**

```openssl dgst -sha256 [file]```

**计算 MD5 哈希**

```openssl dgst -md5 [file]```

**以 coreutils 兼容格式输出哈希**

```openssl dgst -sha256 -r [file]```

**计算哈希并将输出写入文件**

```openssl dgst -sha256 -out [hash.txt] [file]```

**使用密钥创建 HMAC**

```openssl dgst -sha256 -hmac "[secret_key]" [file]```

**用私钥签署文件**

```openssl dgst -sha256 -sign [private.pem] -out [signature.bin] [file]```

**用公钥校验签名**

```openssl dgst -sha256 -verify [public.pem] -signature [signature.bin] [file]```

# SYNOPSIS

**openssl** **dgst** [_options_] [_file_...]

# PARAMETERS

**-sha256**, **-sha512**, **-sha384**, **-sha1**, **-md5**
> 要使用的哈希算法。默认为 sha256。

**-sign** _keyfile_
> 使用指定文件中的私钥签署摘要。

**-verify** _keyfile_
> 使用指定文件中的公钥校验签名。

**-prverify** _keyfile_
> 使用指定文件中的私钥校验签名。

**-signature** _file_
> 用于校验的签名文件。

**-hmac** _key_
> 使用给定密钥创建哈希 MAC。

**-out** _filename_
> 输出文件名。默认为标准输出。

**-r**
> 以 coreutils 兼容格式输出哈希。

**-hex**
> 以十六进制转储输出（默认）。

**-binary**
> 以二进制形式输出摘要。

**-c**
> 以冒号分隔的两位一组的形式打印摘要。

**-keyform** _arg_
> 密钥格式：PEM、DER、P12 或 ENGINE。

**-passin** _arg_
> 私钥密码来源。

**-sigopt** _nm:v_
> 在签署或校验期间向签名算法传递选项。

**-list**
> 打印支持的摘要算法列表。

# DESCRIPTION

**openssl dgst** 以十六进制形式输出文件的消息摘要。它支持多种算法，包括 SHA-256、SHA-512、SHA-384、SHA-1 和 MD5。还可以使用非对称密钥生成和校验数字签名，以及创建 HMAC。如果未指定文件，则使用标准输入。

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

[openssl](/man/openssl)(1), [sha256sum](/man/sha256sum)(1), [openssl-genrsa](/man/openssl-genrsa)(1), [openssl-rsa](/man/openssl-rsa)(1)
