# TAGLINE

列出 XML 文档的元素结构

# TLDR

**列出文档中的所有元素**

```xml el [file.xml]```

**显示元素及其属性**

```xml el -a [file.xml]```

**显示元素及其属性和值**

```xml el -v [file.xml]```

**显示唯一的元素路径**

```xml el -u [file.xml]```

# SYNOPSIS

**xml el** [_options_] _file_

# PARAMETERS

_FILE_
> 输入的 XML 文件（用 - 表示 stdin）。

**-a**
> 显示每个元素的属性。

**-v**
> 显示属性和值。

**-u**
> 仅显示唯一的元素路径。

# DESCRIPTION

**xml el**（也接受 **xml elements** / **xml list**）以类似 XPath 的路径形式打印 XML 文档的元素结构，每行一条。它是 **xmlstarlet** 工具集的一部分。

可用于快速探索不熟悉的 XML 文件、生成元素层级摘要，或为 **xml sel** 查询构造模板。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-elements](/man/xml-elements)(1), [xml-select](/man/xml-select)(1), [xmlstarlet](/man/xmlstarlet)(1)
