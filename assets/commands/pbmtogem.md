# TAGLINE

将 PBM 图像转换为 GEM .img 格式

# TLDR

**将 PBM 图像转换为 GEM IMG 格式**

```pbmtogem [input.pbm] > [output.img]```

**从 stdin 转换**

```cat [input.pbm] | pbmtogem > [output.img]```

# SYNOPSIS

**pbmtogem** [_pbmfile_]

# DESCRIPTION

**pbmtogem** 读取 PBM 图像作为输入，输出压缩的 GEM .img 文件。GEM（Graphics Environment Manager）曾是 Atari ST 电脑和早期 IBM PC 上使用的 GUI 系统。

未指定输入文件时，程序从标准输入读取。输出总是写入标准输出。该工具不支持对重复行进行压缩。

属于 **Netpbm** 工具集。

# CAVEATS

不支持对输出中的重复行进行压缩。GEM IMG 格式已基本过时，主要具有历史意义。

# HISTORY

pbmtogem 由 **David Beckemeyer** 和 **Jef Poskanzer** 创建，是 Netpbm 套件的一部分。

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

[gemtopbm](/man/gemtopbm)(1), [gemtopnm](/man/gemtopnm)(1), [pbmtomacp](/man/pbmtomacp)(1)
