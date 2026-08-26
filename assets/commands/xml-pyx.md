# TAGLINE

将 XML 转换为面向行的 PYX 格式

# TLDR

**将 XML 文件转换为 PYX 格式**

```xml pyx [file.xml]```

**从 stdin 转换 XML**

```cat [file.xml] | xml pyx```

**使用 PYX 过滤去除 XML 文件中的所有属性**

```xml pyx [file.xml] | grep -v "^A" | xml depyx```

# SYNOPSIS

**xml pyx** [_xml-file_]

# PARAMETERS

_xml-file_
> 输入的 XML 文件。若省略则从 stdin 读取。

# DESCRIPTION

**xml pyx** 将 XML 文档转换为 PYX 表示法，这是一种源自 SGML ESIS 格式（ISO 8879）的面向行的表示方式。它属于 **XMLStarlet** 工具集（也可写作 `xmlstarlet pyx`）。

PYX 使用前缀表示法在单行中表示每个 XML 构件：`(` 表示开始标签，`)` 表示结束标签，`A` 表示属性，`-` 表示文本内容，`?` 表示处理指令。这种面向行的格式使你可以直接用 **grep**、**sed** 和 **awk** 等标准 Unix 文本工具处理 XML，无需 XML 解析器。

配套命令 **xml depyx**（或 **xml p2x**）可将 PYX 转换回 XML。

# CAVEATS

PYX 是一种简化的表示方式，可能无法保留注释或 CDATA 区段等全部 XML 特性。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-depyx](/man/xml-depyx)(1), [xml-p2x](/man/xml-p2x)(1), [xmlstarlet](/man/xmlstarlet)(1), [xml](/man/xml)(1)
