# TAGLINE

显示 XML 命名空间信息

# TLDR

**显示命名空间信息**

```xml xmln [file.xml]```

# SYNOPSIS

**xml xmln** [_options_] [_file_]

# PARAMETERS

_file_
> 输入的 XML 文件。

# DESCRIPTION

**xml xmln** 显示 XML 文档中的命名空间信息。属于 xmlstarlet 工具集。它会列出已声明的命名空间及其前缀和 URI，有助于构造针对带命名空间元素的 XPath 表达式。

# CAVEATS

只能处理格式良好的 XML。默认命名空间（无前缀）会以无前缀形式报告；构造 XPath 查询时请使用别名。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-elements](/man/xml-elements)(1), [xml-select](/man/xml-select)(1)
