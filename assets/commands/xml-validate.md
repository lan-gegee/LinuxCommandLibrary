# TAGLINE

依据 schema 校验 XML

# TLDR

**依据内嵌 DTD 校验**

```xml val [file.xml]```

**依据 XSD schema 校验**

```xml val --xsd [schema.xsd] [file.xml]```

**依据 RelaxNG schema 校验**

```xml val --relaxng [schema.rng] [file.xml]```

**仅检查格式良好性**（不做 schema 校验）

```xml val --well-formed [file.xml]```

**校验多个文件**

```xml val [file1.xml] [file2.xml]```

**使用内嵌的 schema 引用校验**

```xml val -E [file.xml]```

# SYNOPSIS

**xml val** [_options_] _file_...

# PARAMETERS

**--xsd** _file_
> 依据 XML Schema 校验。

**--dtd** _file_
> 依据 DTD 校验。

**--relaxng** _file_
> 依据 RelaxNG schema 校验。

**--well-formed**
> 仅检查格式良好性。

**-E**, **--embed**
> 使用内嵌 schema。

**-e**, **--err**
> 打印错误信息。

# DESCRIPTION

**xml val**（或 `xml validate`）依据 schema 校验 XML 文档。属于 XMLStarlet 工具集。支持 DTD、XML Schema（XSD）和 RelaxNG 校验。有效时返回退出码 0，否则返回非零值。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-format](/man/xml-format)(1), [xmllint](/man/xmllint)(1)
