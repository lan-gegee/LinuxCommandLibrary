# TAGLINE

编码和解码 base64 数据。

# TLDR

**编码**为 base64

```base64 [file]```

**解码** base64

```base64 -d [file.b64]```

编码**字符串**

```echo [text] | base64```

解码**字符串**

```echo [ENCODED] | base64 -d```

**不换行**

```base64 -w 0 [file]```

# SYNOPSIS

**base64** [_options_] [_file_]

# DESCRIPTION

**base64** 使用 base64 编码对数据进行编码和解码。Base64 用 64 个可打印 ASCII 字符表示二进制数据，适合通过电子邮件或 JSON 等纯文本通道传输二进制数据。

该工具是 GNU coreutils 的一部分，广泛用于在配置文件中编码凭据、证书和二进制数据。

# PARAMETERS

**-d**, **--decode**
> 解码 base64 数据

**-i**, **--ignore-garbage**
> 解码时忽略非字母表字符

**-w**, **--wrap=**_cols_
> 按指定宽度换行（默认：76，0 = 不换行）

# FEATURES

- 标准 RFC 4648 编码
- 相比二进制体积增大 33%
- URL 与文件名安全的变体
- 使用 = 字符填充

# WORKFLOW

```bash
# Encode file
base64 file.bin > file.b64

# Decode file
base64 -d file.b64 > file.bin

# Encode for use in JSON (no wrapping)
cat image.png | base64 -w 0

# Decode string
echo "SGVsbG8gV29ybGQ=" | base64 -d
```

# COMMON USES

- **HTTP Basic Auth** - `Authorization: Basic <base64-encoded-credentials>`
- **Data URLs** - `data:image/png;base64,iVBORw0KG...`
- **Kubernetes secrets** - 在 YAML 清单中编码
- **JWT tokens** - 头部与载荷部分

# CAVEATS

不是加密（极易还原）。体积增大约 33%。换行在某些上下文中可能引起问题。URL 安全变体需要不同的字符。

# HISTORY

**base64** 自 GNU coreutils 版本 **6.0**（2006）起就是其中一员，实现了 RFC 4648（2006）标准化的 base64 编码。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add base64```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[base32](/man/base32)(1), [basenc](/man/basenc)(1), [b2sum](/man/b2sum)(1), [openssl](/man/openssl)(1)

# RESOURCES

```[Source code](https://github.com/coreutils/coreutils)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/base64-invocation.html)```

<!-- verified: 2026-06-19 -->
