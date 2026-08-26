# TAGLINE

将 PAM/PNM 图像转换为 Motif/X11 GUI 开发使用的 UIL 格式

# TLDR

**将 PAM 转换为 UIL 格式**

```pamtouil [input.pam] > [output.uil]```

**指定输出名称**

```pamtouil -name [iconname] [input.pam] > [output.uil]```

# SYNOPSIS

**pamtouil** [_options_] [_file_]

# PARAMETERS

**-name** _string_
> UIL 图标的名称。

# DESCRIPTION

**pamtouil** 将 PAM/PNM 图像转换为 UIL（User Interface Language）格式，用于 Motif/X11 的 GUI 开发。属于 Netpbm 工具集。

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

[ppmtouil](/man/ppmtouil)(1), [ppmtoxpm](/man/ppmtoxpm)(1)
