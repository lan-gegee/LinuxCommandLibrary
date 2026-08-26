# TAGLINE

将 PYX 表示法转换回 XML

# TLDR

**将 PYX 转换为 XML**

```xml depyx [file.pyx]```

**从 stdin 转换**

```cat [file.pyx] | xml depyx```

# SYNOPSIS

**xml depyx** [_options_] [_file_]

# PARAMETERS

_file_
> 输入的 PYX 文件。

# DESCRIPTION

**xml depyx** 将 PYX 表示法转换回 XML。它是 **xmlstarlet** 工具集的一部分，可在用 **awk**、**sed** 或 **grep** 等面向行的工具处理文本之后，从面向行的 PYX 格式（基于 ESIS，ISO 8879）重建 XML 文档。

逆操作由 **xml pyx**（别名 **xml p2x**）执行，它将 XML 转换为 PYX。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-pyx](/man/xml-pyx)(1), [xml-p2x](/man/xml-p2x)(1), [xml-format](/man/xml-format)(1), [xml-select](/man/xml-select)(1)
