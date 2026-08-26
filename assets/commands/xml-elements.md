# TAGLINE

列出 XML 元素名称和路径

# TLDR

**列出元素名称**

```xml elements [file.xml]```

**带路径列出**

```xml elements -a [file.xml]```

**列出唯一元素**

```xml elements -u [file.xml]```

# SYNOPSIS

**xml elements** [_options_] _file_

# PARAMETERS

**-a**
> 显示每个元素的 XPath。

**-u**
> 仅显示唯一元素。

**-d** _depth_
> 最大深度。

# DESCRIPTION

**xml elements** 列出文档中的 XML 元素名称。属于 xmlstarlet 工具集。适用于探索 XML 结构和发现可用的元素路径。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-select](/man/xml-select)(1), [xml-list](/man/xml-list)(1)
