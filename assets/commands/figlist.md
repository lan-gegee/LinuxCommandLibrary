# TAGLINE

figlet 字体列表实用工具

# TLDR

**列出可用的 figlet 字体**

```figlist```

# SYNOPSIS

**figlist** [_options_]

# DESCRIPTION

**figlist** 通过扫描默认的 figlet 字体目录（通常是 /usr/share/figlet）来枚举所有已安装的 figlet 字体和控制文件。它提供了一种简便方式来发现可用的字体名，供 figlet 命令使用。

输出同时包含 .flf 字体文件和 .flc 控制文件，展示全部可用的字符渲染选项。这比手动翻阅字体目录方便得多。

在尝试不同的文字横幅样式，或编写需要在渲染前确认字体是否存在的脚本时，figlist 尤其实用。

# INSTALL

```apt: sudo apt install figlet```

```dnf: sudo dnf install figlet```

```pacman: sudo pacman -S figlet```

```apk: sudo apk add figlet```

```zypper: sudo zypper install figlet```

```brew: brew install figlet```

```nix: nix profile install nixpkgs#figlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[figlet](/man/figlet)(6), [showfigfonts](/man/showfigfonts)(6)

# RESOURCES

```[Source code](https://github.com/cmatsuoka/figlet)```

```[Homepage](http://www.figlet.org/)```

<!-- verified: 2026-07-15 -->
