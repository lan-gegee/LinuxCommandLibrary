# TAGLINE

将 PBM 位图转换为 MGR 窗口系统格式

# TLDR

**将 PBM 转换为 MGR 格式**

```pbmtomgr [input.pbm] > [output.mgr]```

**从 stdin 转换**

```cat [input.pbm] | pbmtomgr > [output.mgr]```

# SYNOPSIS

**pbmtomgr** [_file_]

# PARAMETERS

_file_
> 输入的 PBM 文件。省略时从 stdin 读取。

# DESCRIPTION

**pbmtomgr** 读取 PBM 图像作为输入，并输出 MGR 位图。MGR 是 20 世纪 80 年代 Bellcore 开发的窗口管理器，是 X Window System 的轻量替代品。属于 Netpbm 工具集。

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

[mgrtopbm](/man/mgrtopbm)(1), [xbmtopbm](/man/xbmtopbm)(1)
