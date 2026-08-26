# TAGLINE

Usenix FaceSaver 转 PGM 转换器

# TLDR

将 Usenix FaceSaver **转换为 PGM**

```fstopgm < [input.fs] > [output.pgm]```

# SYNOPSIS

**fstopgm** [_input_]

# DESCRIPTION

**fstopgm** 将 Usenix FaceSaver 格式图像转换为 PGM（Portable Graymap）格式。Usenix FaceSaver 是早期用于在在线目录系统中存储灰度人脸图像的格式。该工具属于 Netpbm 图像处理工具集，该工具集提供了在众多图形格式之间转换的实用程序。

转换过程从标准输入读取并向标准输出写入，因此适合与其他 Netpbm 工具进行管道操作。

# CAVEATS

Usenix FaceSaver 格式已过时，如今很少遇到。该工具是 Netpbm 套件的一部分，可能未包含在所有 Netpbm 发行版中。输入必须是有效的 FaceSaver 格式，否则转换会失败。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pgmtofs](/man/pgmtofs)(1), [netpbm](/man/netpbm)(1)

