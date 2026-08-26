# TAGLINE

将 macOS 风格的换行符转换为 Unix 风格的换行符

# TLDR

转换 **file** 的换行符

```mac2unix [path/to/file]```

创建带 Unix 换行符的**新文件**

```mac2unix -n [path/to/file] [path/to/new_file]```

显示**文件信息**

```mac2unix -i [path/to/file]```

处理 **BOM**（字节顺序标记）

```mac2unix --keep-bom [path/to/file]```

# SYNOPSIS

**mac2unix** [_options_] [_file_...]

# DESCRIPTION

**mac2unix** 将 macOS 风格的换行符（CR）转换为 Unix 风格的换行符（LF）。它属于 dos2unix 软件包，用于处理文本文件格式转换。

# PARAMETERS

**-n, --newfile SRC DST**
> 将输出写入新文件

**-i, --info**
> 显示文件信息

**--keep-bom**
> 保留字节顺序标记

**--add-bom**
> 添加字节顺序标记

**--remove-bom**
> 移除字节顺序标记

**-k, --keepdate**
> 保留原始文件的日期

**-q, --quiet**
> 安静模式

# CAVEATS

经典 Mac OS（OS X 之前）使用 CR 换行符。现代 macOS 使用 Unix 的 LF 换行符。因此只有旧式文件才需要此工具。

# INSTALL

```apt: sudo apt install dos2unix```

```dnf: sudo dnf install dos2unix```

```pacman: sudo pacman -S dos2unix```

```apk: sudo apk add dos2unix```

```zypper: sudo zypper install dos2unix```

```brew: brew install dos2unix```

```nix: nix profile install nixpkgs#dos2unix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dos2unix](/man/dos2unix)(1), [unix2dos](/man/unix2dos)(1), [unix2mac](/man/unix2mac)(1)
