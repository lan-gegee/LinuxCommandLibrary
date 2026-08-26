# TAGLINE

按索引号从多图像 PAM 流中提取指定的图像

# TLDR

**从流中提取指定的图像**

```pampick [0] [2] [5] < [input.pam] > [output.pam]```

# SYNOPSIS

**pampick** _index_ [_index_ ...] < _file_

# PARAMETERS

_index_
> 要提取的图像索引（从 0 开始）。

# DESCRIPTION

**pampick** 按索引号从多图像 PAM 流中提取指定的图像。适用于从动画或视频序列中挑选帧。属于 Netpbm 工具集。

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

[pamsplit](/man/pamsplit)(1)
