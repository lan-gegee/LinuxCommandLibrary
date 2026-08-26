# TAGLINE

对 XML 文档进行规范化（xmlstarlet c14n）

# TLDR

**保留注释的包含式规范化**（W3C XML C14N 1.0）

```xml c14n --with-comments [file.xml]```

**去除注释的包含式规范化**

```xml c14n --without-comments [file.xml]```

**保留注释的排他式规范化**（XML EXC-C14N）

```xml c14n --exc-with-comments [file.xml]```

**不保留注释的排他式规范化**

```xml c14n --exc-without-comments [file.xml]```

**规范化由 XPath 表达式文件选出的子集**

```xml c14n --without-comments [file.xml] [xpath.xml]```

**从 stdin 读取**

```cat [file.xml] | xml c14n --with-comments -```

# SYNOPSIS

**xml c14n** _mode_ _xml-file_ [_xpath-file_] [_inclusive-ns-list_]

# PARAMETERS

_MODE_（必填，且只能有一个）
> **--with-comments**、**--without-comments**、**--exc-with-comments**、**--exc-without-comments** 四者之一。

_XML-FILE_
> 要规范化的 XML 文档。使用 **-** 表示从 stdin 读取。

_XPATH-FILE_
> 可选的 XML 文件，其根元素的文本内容是一个 XPath 表达式，用于选择要规范化的节点集。

_INCLUSIVE-NS-LIST_
> 仅用于排他式 C14N：以空格分隔的命名空间前缀列表，这些前缀将被视为包含式的（例如 `'soap xsd'`）。

# DESCRIPTION

**xml c14n** 是 **xmlstarlet** 的规范化子命令。它按照 W3C **Canonical XML 1.0** 或 **Exclusive XML Canonicalization 1.0** 规范生成字节级稳定的 XML 文档序列化结果。在生成或验证 XML 数字签名（XML-DSig）之前，工具必须先计算该结果，以便语义等价的文档哈希出相同的值。

包含式规范化会保留祖先命名空间声明；排他式规范化（被 SAML、WS-Security 等使用）则会丢弃它们，除非在包含式命名空间前缀列表中明确列出。

# CAVEATS

模式标志与位置相关——每次调用都必须在输入文件之前提供四个模式选项中的一个。XPath 参数本身是一个包含 XPath 的 XML 文件，而不是命令行上的字面表达式。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xmlstarlet](/man/xmlstarlet)(1), [xml-canonic](/man/xml-canonic)(1), [xml-format](/man/xml-format)(1), [xmllint](/man/xmllint)(1)
