# TAGLINE

将 PNM 转换为 X Window Dump 格式

# TLDR

**将 PNM 转换为 XWD 格式**

```pnmtoxwd [input.pnm] > [output.xwd]```

**指定视觉类**

```pnmtoxwd -directcolor [input.pnm] > [output.xwd]```

# SYNOPSIS

**pnmtoxwd** [_options_] [_file_]

# PARAMETERS

**-pseudocolor**
> 使用 PseudoColor 视觉类。

**-directcolor**
> 使用 DirectColor 视觉类。

# DESCRIPTION

**pnmtoxwd** 将 PNM 图像转换为 X Window Dump（XWD）格式。属于 Netpbm 工具集。

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

[xwdtopnm](/man/xwdtopnm)(1), [pnmtorast](/man/pnmtorast)(1)
