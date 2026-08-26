# TAGLINE

应用生命游戏的规则

# TLDR

**运行一次生命游戏迭代**

```pbmlife [input.pbm] > [output.pbm]```

**迭代多代**

```pbmlife [input.pbm] | pbmlife | pbmlife > [output.pbm]```

# SYNOPSIS

**pbmlife** [_file_]

# PARAMETERS

_FILE_
> 输入的 PBM 文件（初始状态）。

# DESCRIPTION

**pbmlife** 应用生命游戏的规则，执行单代演化。

该工具模拟元胞自动机，即 Conway 生命游戏。

# CAVEATS

Netpbm 的组成部分。每次调用演化一代。串联使用可实现动画效果。

# HISTORY

pbmlife 属于 **Netpbm**，实现了 Conway 生命游戏。

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

[pbm](/man/pbm)(5), [pbmmake](/man/pbmmake)(1), [netpbm](/man/netpbm)(1)
