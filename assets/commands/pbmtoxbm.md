# TAGLINE

将 PBM 位图图像转换为 X11 位图格式

# TLDR

**将 PBM 转换为 X 位图**

```pbmtoxbm [input.pbm] > [output.xbm]```

**以自定义名称转换**

```pbmtoxbm -name [icon] [input.pbm] > [icon.xbm]```

# SYNOPSIS

**pbmtoxbm** [_options_] [_file_]

# PARAMETERS

**-name** _name_
> 输出中的变量名。

# DESCRIPTION

**pbmtoxbm** 将 PBM 位图图像转换为 X11 位图格式（.xbm）。X 位图是可在 X11 应用中使用的 C 源文件。属于 Netpbm 工具集。

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

[xbmtopbm](/man/xbmtopbm)(1)
