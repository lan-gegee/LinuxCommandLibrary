# TAGLINE

生成密码学安全的随机字节

# TLDR

**生成 32 个随机字节**，以十六进制表示

```openssl rand -hex 32```

**生成 32 个随机字节**，以 base64 编码

```openssl rand -base64 32```

**生成原始随机字节**并写入文件

```openssl rand -out [random.bin] 256```

**生成随机密码**（24 个 base64 字符）

```openssl rand -base64 18```

**生成 1 KB 随机数据**

```openssl rand -out [random.bin] 1K```

# SYNOPSIS

**openssl rand** [**-hex**] [**-base64**] [**-out** _file_] _num_

# PARAMETERS

**-hex**
> 以十六进制字符串输出随机字节（每字节 2 个字符）

**-base64**
> 以 base64 编码输出随机字节

**-out** _file_
> 将输出写入文件而不是标准输出

**-rand** _file_
> 使用指定文件作为额外的随机种子来源

**-help**
> 显示用法信息

_num_
> 要生成的随机字节数（支持 K/M/G/T 后缀）

# DESCRIPTION

**openssl rand** 使用 OpenSSL 的 CSPRNG（密码学安全伪随机数生成器）生成密码学安全的伪随机字节。在从操作系统的熵源正确播种的情况下，其输出可提供 256 位的安全性。

该命令常用于生成随机密码、加密密钥、初始化向量和其他安全令牌。不指定编码选项时输出原始二进制字节，在终端中可能无法正常显示。

在现代操作系统上，OpenSSL 会自动从可信的系统熵源（类 Unix 系统上的 /dev/urandom）获取种子。若熵不足，该命令会失败。

# CAVEATS

原始输出（未加 **-hex** 或 **-base64**）包含可能含有不可打印字符的二进制数据。要在终端显示或在 Shell 中使用，请先通过编码处理。

输出字符数与字节数不同：十六进制输出的字符数是字节数的 2 倍，base64 输出约为字节数的 4/3 倍（外加填充字符）。

用于生成密码时，base64 编码包含 +、/、= 等字符，在某些场景下可能需要转义。

# SEE ALSO

[openssl](/man/openssl)(1), [dd](/man/dd)(1), [head](/man/head)(1)
