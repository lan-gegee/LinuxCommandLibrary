# TAGLINE

用多种进制编码进行编码和解码。

# TLDR

用 base64 **编码**

```basenc --base64 [file]```

用 base32 **编码**

```basenc --base32 [file]```

**解码** base64

```basenc --base64 -d [file.b64]```

使用 **base16**（十六进制）

```basenc --base16 [file]```

使用 **base2**（二进制）

```basenc --base2 [file]```

# SYNOPSIS

**basenc** _encoding_ [_options_] [_file_]

# DESCRIPTION

**basenc** 是统一的编码/解码工具，支持多种进制编码，包括 base64、base32、base16（十六进制）、base2（二进制）、z85 等。它将原先分散在多个工具中的功能整合到一起。

该工具是 GNU coreutils 的一部分，为各种编码方案提供单一接口。

# PARAMETERS

**--base64**
> Base64 编码

**--base64url**
> Base64 URL 安全编码

**--base32**
> Base32 编码

**--base32hex**
> 扩展十六进制字母表的 Base32

**--base58**
> Base58 编码（避免视觉上易混淆的字符；便于人工抄录）

**--base16**
> Base16（十六进制）

**--base2lsbf**
> Base2（二进制），最低有效位在前

**--base2msbf**
> Base2（二进制），最高有效位在前

**--z85**
> Z85 编码（ZeroMQ）

**-d**, **--decode**
> 解码数据

**-w**, **--wrap=**_cols_
> 每 _cols_ 个字符对编码后的行换行（默认：76，0 = 不换行）

**-i**, **--ignore-garbage**
> 忽略非字母表字符

# WORKFLOW

```bash
# Base64 encode
basenc --base64 file.bin

# Base32 decode
basenc --base32 -d file.b32

# Hexadecimal
basenc --base16 file.bin

# Binary representation
echo "A" | basenc --base2msbf
```

# CAVEATS

必须且只能指定一种编码选项。使用 **--z85** 时，编码输入长度必须是 4 字节的倍数，解码输入是 5 的倍数。工具相对较新（旧系统上没有）；在 basenc 不可用时请退回使用 base64/base32。

# HISTORY

**basenc** 在 GNU coreutils 版本 **8.31**（2019）中加入，为多种编码方案提供统一接口。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[base64](/man/base64)(1), [base32](/man/base32)(1), [b2sum](/man/b2sum)(1), [xxd](/man/xxd)(1)

# RESOURCES

```[Source code](https://github.com/coreutils/coreutils)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/basenc-invocation.html)```

<!-- verified: 2026-06-19 -->
