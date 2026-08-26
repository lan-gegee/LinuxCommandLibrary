# TAGLINE

修复被截断的图像

# TLDR

**修复截断的图像**

```pamfixtrunc [truncated.pam] > [fixed.pam]```

**用指定值填充**

```pamfixtrunc -fillvalue=[0] [truncated.pam] > [fixed.pam]```

# SYNOPSIS

**pamfixtrunc** [_options_] [_file_]

# PARAMETERS

_FILE_
> 被截断的 PAM/PNM 文件。

**-fillvalue** _VALUE_
> 用于填充缺失像素的值。

# DESCRIPTION

**pamfixtrunc** 修复被截断的图像，补齐缺失的数据。

该工具用于补全不完整的文件。是 Netpbm 的一部分。

# CAVEATS

属于 Netpbm 工具集。填充缺失数据后，原始数据无法恢复。

# HISTORY

pamfixtrunc 是 **Netpbm** 中用于修复截断图像文件的工具。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm-extras```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pamfix](/man/pamfix)(1), [netpbm](/man/netpbm)(1)
