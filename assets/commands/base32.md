# TAGLINE

编码和解码 base32 数据。

# TLDR

**编码**为 base32

```base32 [file]```

**解码** base32

```base32 -d [file.b32]```

编码**字符串**

```echo [text] | base32```

解码**字符串**

```echo [ENCODED] | base32 -d```

# SYNOPSIS

**base32** [_options_] [_file_]

# DESCRIPTION

**base32** 使用 base32 编码对数据进行编码和解码。Base32 用 32 个 ASCII 字符（A-Z 和 2-7）表示二进制数据，适合大小写不敏感的系统以及需要人类可读令牌的场景。

该工具是 GNU coreutils 的一部分，适用于在 URL、文件名或其他对 base64 大小写敏感或特殊字符有问题的场景中编码数据。

# PARAMETERS

**-d**, **--decode**
> 解码 base32 数据

**-i**, **--ignore-garbage**
> 解码时忽略非字母表字符

**-w**, **--wrap=**_cols_
> 按指定宽度换行（默认：76，0 = 不换行）

# FEATURES

- 大小写不敏感的编码
- 无特殊字符（URL 安全）
- 符合 RFC 4648 标准的实现
- 使用 = 字符填充

# WORKFLOW

```bash
# Encode file
base32 file.bin > file.b32

# Decode file
base32 -d file.b32 > file.bin

# Encode string
echo "Hello World" | base32

# Decode string
echo "JBSWY3DPEBLW64TMMQ======" | base32 -d
```

# CAVEATS

比 base64 编码体积大 20%。不如 base64 常见。填充字符在某些上下文中可能需要转义。大小写不敏感，但输出为大写。

# HISTORY

**base32** 在 GNU coreutils 版本 **8.25**（2016）中加入，实现了 RFC 4648 规定的 base32 编码。

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

[base64](/man/base64)(1), [basenc](/man/basenc)(1), [b2sum](/man/b2sum)(1), [uuencode](/man/uuencode)(1)

# RESOURCES

```[Source code](https://github.com/coreutils/coreutils)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/base32-invocation.html)```

<!-- verified: 2026-06-19 -->
