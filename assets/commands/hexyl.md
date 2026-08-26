# TAGLINE

现代化的终端十六进制查看器

# TLDR

以十六进制**查看文件**

```hexyl [file]```

**显示指定长度**

```hexyl -n [100] [file]```

**跳过字节**

```hexyl --skip [50] [file]```

**以朴素风格显示**

```hexyl --plain [file]```

**从 stdin 读取**

```cat [file] | hexyl```

**不显示字符面板**

```hexyl --no-characters [file]```

# SYNOPSIS

**hexyl** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要显示的文件（用 - 表示 stdin）。

**-n**, **--length** _N_
> 要读取的字节数（支持 k、M、G 后缀和十六进制）。

**-c**, **--bytes** _N_
> --length 的别名。

**-s**, **--skip** _N_
> 跳过前 N 个字节（负值表示从末尾开始定位）。

**-o**, **--display-offset** _N_
> 在显示的文件偏移量上加上 N 个字节。

**--block-size** _SIZE_
> 块单元的大小（默认：512）。

**-v**, **--no-squeezing**
> 显示所有数据；不用星号折叠相同的行。

**--color** _WHEN_
> 彩色输出：always（默认）、auto、never。

**-p**, **--plain**
> 朴素输出（等价于 --no-characters --no-position --border=none --color=never）。

**--no-characters**
> 隐藏字符面板。

**--no-position**
> 隐藏位置偏移列。

**--border** _STYLE_
> 边框样式：unicode（默认）、ascii、none。

**--panels** _N_
> 十六进制数据面板的数量（或 'auto'）。

**--group-size** _N_
> 每组的字节数：1（默认）、2、4 或 8。

**--endianness** _ENDIAN_
> 组内字节序：little 或 big。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**hexyl** 是一款现代化的终端十六进制查看器。它以彩色输出显示文件内容，区分不同的字节类型。

该工具使用颜色突出 ASCII、非 ASCII、空字节和空白字符。它提供整洁易读的十六进制转储，并带有偏移量和字符视图。

# CAVEATS

需要支持颜色的终端。大文件可能较慢。使用 Rust 编写。

# HISTORY

hexyl 的创建旨在成为 xxd 和 hexdump 等传统十六进制转储工具的现代、彩色化替代品。

# INSTALL

```apt: sudo apt install hexyl```

```dnf: sudo dnf install hexyl```

```pacman: sudo pacman -S hexyl```

```apk: sudo apk add hexyl```

```zypper: sudo zypper install hexyl```

```brew: brew install hexyl```

```nix: nix profile install nixpkgs#hexyl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xxd](/man/xxd)(1), [hexdump](/man/hexdump)(1), [hd](/man/hd)(1)
