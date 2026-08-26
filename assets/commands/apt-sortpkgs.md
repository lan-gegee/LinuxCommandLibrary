# TAGLINE

对软件包索引文件排序

# TLDR

对一个 Packages 文件**排序**

```apt-sortpkgs [Packages] > [Packages.sorted]```

对 **Sources** 文件排序

```apt-sortpkgs -s [Sources] > [Sources.sorted]```

# SYNOPSIS

**apt-sortpkgs** [_-s_] _file_

# DESCRIPTION

**apt-sortpkgs** 将 Debian 软件包索引文件（Packages 或 Sources 文件）按一致的顺序排列。这对于比较文件或确保可复现的输出很有用。

该工具读取索引文件，按软件包名称的字母顺序排序，然后输出排序后的版本。

# PARAMETERS

**-s**, **--source**
> 将输入视为 Sources 文件而不是 Packages

**-o** _option_
> 设置配置选项

**-c** _file_
> 读取额外的配置

# CAVEATS

主要用于仓库维护和文件比较。正常的 APT 操作不需要它。大文件可能占用大量内存。

# HISTORY

**apt-sortpkgs** 是 APT 套件的组成部分，供需要索引文件具有确定性顺序的仓库维护者使用。

# INSTALL

```apt: sudo apt install apt-utils```

```dnf: sudo dnf install apt-utils```

```pacman: sudo pacman -S apt```

```apk: sudo apk add apt```

```brew: brew install apt```

```nix: nix profile install nixpkgs#apt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt-ftparchive](/man/apt-ftparchive)(1)
