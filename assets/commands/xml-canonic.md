# TAGLINE

生成规范的 XML 形式

# TLDR

**规范化 XML（W3C C14N）**

```xml canonic [file.xml]```

**排他式规范化**

```xml canonic --exc-c14n [file.xml]```

**不含注释地规范化**

```xml canonic --without-comments [file.xml]```

**从 stdin 读取**

```cat file.xml | xml canonic```

# SYNOPSIS

**xml** **canonic** [_options_] [_file_]

# DESCRIPTION

**xml canonic** 按照 W3C XML Canonicalization（C14N）规范生成输入文档的规范 XML 形式。规范化会统一空白、属性顺序、命名空间声明和字符编码，使两个逻辑等价的文档产生完全相同的字节流。

它是 **xmlstarlet** 命令行 XML 工具集的一部分。规范 XML 常用作计算 XML 数字签名（XML-DSig）加密摘要前的准备步骤，也用于可靠地比较文档。

# PARAMETERS

**--exc-c14n**
> 使用 Exclusive XML Canonicalization（EXC-C14N）而非默认的 Canonical XML 1.0。

**--without-comments**
> 在规范化输出中省略注释。

# CAVEATS

规范化是有损的：注释可能被去除、空白被统一、命名空间声明被改写。非规范化的格式差异会被有意消除。对规范化后的 XML 计算加密签名时，要求双方使用相同的 C14N 变体。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-c14n](/man/xml-c14n)(1), [xml-format](/man/xml-format)(1)
