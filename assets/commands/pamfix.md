# TAGLINE

修复损坏的 Netpbm 图像

# TLDR

**裁剪超出 maxval 的样本值**

```pamfix -clip [corrupted.pam] > [fixed.pam]```

**提高 maxval 以容纳超范围值**

```pamfix -changemaxval [corrupted.pam] > [fixed.pam]```

**在第一个非法样本值处截断图像**

```pamfix -truncate [corrupted.pam] > [fixed.pam]```

**修复并输出详细信息**

```pamfix -clip -verbose [corrupted.pam] > [fixed.pam]```

# SYNOPSIS

**pamfix** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 PAM/PNM 文件。未指定时从标准输入读取。

**-clip**
> 将超出头部所述 maxval 的所有像素值裁剪为 maxval。不能与 **-changemaxval** 组合使用。

**-changemaxval**
> 提高 maxval 以容纳超出头部所述 maxval 的像素值，同时降低每个样本所表示的比例。不能与 **-clip** 组合使用。

**-truncate**
> 在第一个非法样本值处截断图像。当既未指定 **-clip** 也未指定 **-changemaxval** 时，这是处理超范围值的默认行为。

**-verbose**
> 向标准错误报告修复的详细信息。

# DESCRIPTION

**pamfix** 读取一个大部分是 Netpbm 图像但可能存在某些类型损坏的流，并生成一幅有效的 Netpbm 图像，尽可能保留原始信息。它处理两种主要损坏类型：被截断的流和非法的超大样本值。属于 Netpbm 软件包的一部分。

# CAVEATS

不能同时指定 **-clip** 和 **-changemaxval**。可能无法修复所有类型的损坏。截断方式可能造成部分数据丢失。

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

[pamfixtrunc](/man/pamfixtrunc)(1), [pamfile](/man/pamfile)(1), [pamvalidate](/man/pamvalidate)(1), [pamcut](/man/pamcut)(1), [netpbm](/man/netpbm)(1)
