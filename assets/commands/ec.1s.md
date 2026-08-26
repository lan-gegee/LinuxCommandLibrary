# TAGLINE

椭圆曲线密钥操作

# TLDR

**查看 EC 密钥**

```openssl ec -in [key.pem] -text -noout```

**生成 EC 私钥**

```openssl ecparam -genkey -name [prime256v1] -out [key.pem]```

**转换 EC 密钥格式**

```openssl ec -in [key.pem] -outform DER -out [key.der]```

# SYNOPSIS

**openssl ec** [_options_]

# PARAMETERS

**-in** _FILE_
> 输入密钥文件。

**-out** _FILE_
> 输出密钥文件。

**-text**
> 以文本形式打印密钥。

**-noout**
> 不输出编码后的密钥。

**-outform** _FORMAT_
> 输出格式：PEM、DER。

**-param_enc** _TYPE_
> 参数编码类型。

**--help**
> 显示帮助信息。

# DESCRIPTION

**openssl ec** 处理椭圆曲线（EC）密钥操作，包括读取、写入和转换 EC 私钥。与 RSA 相比，椭圆曲线密码学能以更小的密钥长度提供同等的强安全性。

该命令读取多种格式的 EC 密钥，并能以 PEM 或 DER 编码输出。它用于 TLS 配置和数字签名中的密钥管理。

EC 密钥先用 ecparam 以命名曲线生成，再用 ec 命令进行格式转换或检查。

# CAVEATS

曲线的选择会影响安全性和兼容性。某些曲线存在已知弱点。并非所有系统都支持所有曲线。

# HISTORY

随着椭圆曲线密码学成为 TLS 标准，OpenSSL 添加了 EC 支持。EC 能以显著更小的密钥提供与 RSA 同等的安全性。

# SEE ALSO

[openssl](/man/openssl)(1)
