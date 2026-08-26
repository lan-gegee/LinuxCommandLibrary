# TAGLINE

创建油画效果

# TLDR

**应用油画效果**

```pamoil [input.pam] > [output.pam]```

**设置涂抹尺寸**

```pamoil -n [3] [input.pam] > [output.pam]```

# SYNOPSIS

**pamoil** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 PAM/PNM 文件。

**-n** _SIZE_
> 邻域大小（默认为 3）。

# DESCRIPTION

**pamoil** 创建油画效果。根据颜色的出现频率对颜色进行涂抹。

该工具应用艺术化滤镜。属于 Netpbm。

# CAVEATS

属于 Netpbm。尺寸越大处理越慢。属于艺术化效果。

# HISTORY

pamoil 是 **Netpbm** 的组成部分，用于应用油画效果。

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

[ppmrelief](/man/ppmrelief)(1), [pgmedge](/man/pgmedge)(1), [netpbm](/man/netpbm)(1)
