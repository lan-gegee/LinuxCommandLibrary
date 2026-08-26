# TAGLINE

将文件分割成更小的片段

# TLDR

**将文件按每 1000 行分割**

```split [file]```

**用自定义前缀分割**

```split [file] [prefix_]```

**按指定的行数分割**

```split -l [500] [file]```

**按指定大小分割**

```split -b [10M] [file]```

**分割成 N 个等大的部分**

```split -n [5] [file]```

**使用数字后缀分割**

```split -d [file]```

**使用自定义后缀长度分割**

```split -a [4] [file]```

# SYNOPSIS

**split** [_options_] [_file_ [_prefix_]]

# PARAMETERS

**-l** _lines_, **--lines**=_lines_
> 每个输出文件包含指定的行数

**-b** _size_, **--bytes**=_size_
> 每个输出文件包含指定的字节数（K, M, G 后缀）

**-n** _chunks_, **--number**=_chunks_
> 生成指定数量的输出文件

**-d**, **--numeric-suffixes**
> 使用数字后缀而非字母后缀

**-a** _N_, **--suffix-length**=_N_
> 生成长度为 N 的后缀（默认：2）

**-e**, **--elide-empty-files**
> 使用 -n 时不生成空输出文件

**--verbose**
> 为每个输出文件打印一条消息

**--additional-suffix**=_suf_
> 在文件名后追加额外的后缀

**-x**, **--hex-suffixes**
> 使用十六进制后缀

# DESCRIPTION

**split** 将文件分割成更小的片段。默认情况下，它每 1000 行创建一个文件，文件名由前缀（默认：**x**）加后缀（aa, ab, ac, ...）组成。

该命令适用于因传输、处理或存储限制而需要拆分大文件的场景。它同时适用于文本文件和二进制文件。

大小规格接受以下后缀：**K**（千字节）、**M**（兆字节）、**G**（吉字节），也可使用表示 1000 的幂的 **KB**、**MB**、**GB**。

未指定文件或文件为 **-** 时，split 从 stdin 读取。

# CAVEATS

默认的 2 字符后缀将输出限制为 676 个文件（aa-zz）。如需更多分片，请用 **-a** 增加后缀长度，或用 **-d** 改用数字后缀。

分割二进制文件时，请使用 **-b**（字节）而不是 **-l**（行），以免在任意字节边界处损坏数据。

重组时使用 **cat prefix\*** > **original_file**。确保按正确的字母/数字顺序拼接文件。

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

[csplit](/man/csplit)(1), [cat](/man/cat)(1), [head](/man/head)(1), [tail](/man/tail)(1)
