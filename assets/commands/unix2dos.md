# TAGLINE

将 Unix 换行符转换为 DOS 格式

# TLDR

将文件的**换行符改为** DOS 风格

```unix2dos [path/to/file]```

**创建**一份带 DOS 风格换行符的副本

```unix2dos -n [path/to/file] [path/to/new_file]```

**显示**文件信息

```unix2dos -i [path/to/file]```

**保留/添加/移除**字节顺序标记（BOM）

```unix2dos --keep-bom|--add-bom|--remove-bom [path/to/file]```

# SYNOPSIS

**unix2dos** [_options_] [_file_...]

# PARAMETERS

**-n, --newfile _infile_ _outfile_**
> 写入新文件而不是原地修改

**-i, --info _flags_**
> 显示文件信息（换行符、BOM）

**-k, --keepdate**
> 使输出文件的日期与输入相同

**--keep-bom**
> 保留字节顺序标记（BOM）

**--add-bom**
> 添加字节顺序标记（BOM）

**--remove-bom**
> 移除字节顺序标记（BOM）

**-q, --quiet**
> 安静模式，抑制警告

# DESCRIPTION

**unix2dos** 将文本文件从 Unix 换行格式（LF）转换为 DOS/Windows 格式（CRLF）。默认原地修改文件，也可以用 **-n** 选项写入新文件。

该工具常用于为 Windows 系统准备文件，或处理要求换行符一致的跨平台项目。

# CAVEATS

不要处理二进制文件。大文件的处理效率较高。该工具可处理 UTF-8 及其他编码。属于 dos2unix 软件包的一部分。

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

[dos2unix](/man/dos2unix)(1), [unix2mac](/man/unix2mac)(1), [mac2unix](/man/mac2unix)(1)
