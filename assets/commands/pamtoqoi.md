# TAGLINE

将 PAM/PNM 图像转换为 QOI 格式

# TLDR

**将 PAM 转换为 QOI 格式**

```pamtoqoi [input.pam] > [output.qoi]```

# SYNOPSIS

**pamtoqoi** [_file_]

# DESCRIPTION

**pamtoqoi** 将 PAM/PNM 图像转换为 QOI（Quite OK Image）格式。QOI 是一种快速无损的图像格式，设计目标是简单与高速。属于 Netpbm 工具集。

# PARAMETERS

**-quiet**
> 抑制提示信息。

**-version**
> 显示程序版本并退出。

# CAVEATS

输入必须是 PAM（Portable Arbitrary Map）或 PNM 图像。QOI 只支持 RGB 和 RGBA；灰度输入可能被拒绝或被自动转换。

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

[qoitopam](/man/qoitopam)(1), [pnmtopng](/man/pnmtopng)(1), [pamtopnm](/man/pamtopnm)(1), [pam](/man/pam)(5), [pnm](/man/pnm)(5)
