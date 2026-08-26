# TAGLINE

解析和校验 XML 文档

# TLDR

**检查 XML 文件是否格式良好**

```xmllint [file.xml]```

**格式化并美化打印** XML 文件

```xmllint --format [file.xml]```

**依据 DTD 校验**

```xmllint --valid [file.xml]```

**依据 XSD schema 校验**

```xmllint --schema [schema.xsd] [file.xml]```

**使用 XPath 提取数据**

```xmllint --xpath "[//element/@attribute]" [file.xml]```

**就地格式化**（输出到同一文件）

```xmllint --format [file.xml] -o [file.xml]```

**从输出中移除空白节点**

```xmllint --noblanks [file.xml]```

# SYNOPSIS

**xmllint** [_options_] _xmlfile..._

# PARAMETERS

**--format**
> 重新排版并为输出重新缩进

**--valid**
> 依据文档中声明的 DTD 进行校验

**--schema** _file_
> 依据指定的 XSD schema 校验

**--relaxng** _file_
> 依据 RelaxNG schema 校验

**--dtdvalid** _file_
> 依据指定的 DTD 校验

**--xpath** _expression_
> 计算 XPath 表达式并打印结果

**--output** _file_, **-o** _file_
> 将输出写入指定文件

**--noout**
> 抑制正常输出（配合校验使用很有用）

**--noblanks**
> 从输出中移除可忽略的空白节点

**--encode** _encoding_
> 以指定编码输出

**--html**
> 将输入解析为 HTML 而非 XML

**--recover**
> 尝试从解析错误中恢复

**--nonet**
> 不从网络获取外部实体

**--c14n**
> 对输出进行规范化处理（用于数字签名）

**--shell**
> 进入交互式 shell 模式

**--version**
> 显示版本信息

# DESCRIPTION

**xmllint** 是来自 **libxml2** 库的命令行 XML 解析器和处理器。它可以解析 XML 文件以检查格式良好性、依据 DTD 或 schema（XSD、RelaxNG）校验文档、格式化 XML 以提高可读性，以及使用 XPath 表达式查询文档。

该工具在 shell 脚本和自动化工作流中处理 XML 数据时不可或缺。它能检测语法错误、依据各种 schema 类型进行校验、用 XPath 提取特定数据，以及对 XML 输出进行转换或清理。

常见用途包括校验配置文件、从 XML API 提取数据、将机器生成的 XML 格式化为人类可读的形式，以及在用 XSLT 做进一步转换之前预处理 XML。

# CAVEATS

XPath 支持仅限于 XPath 1.0；需要 XPath 2.0+ 时请使用 **saxon** 等工具。大文件可能消耗大量内存，因为整个文档都会被加载。外部实体展开默认启用，处理不可信输入时可能带来安全风险；对不可信数据请使用 **--nonet** 和 **--noent** 标志。某些格式错误的 HTML 文档可能需要 **--html --recover** 组合才能解析。

# HISTORY

**xmllint** 是 **libxml2** 项目的一部分，该项目由 **Daniel Veillard** 自 **1998** 年起创建。该库及其工具成为类 Unix 系统上的标准 XML 处理工具集，被 GNOME、PHP 以及无数其他项目采用。它在大多数 Linux 发行版和 macOS 上默认安装。该工具持续维护和更新，以支持不断演进的 XML 标准。

# INSTALL

```apt: sudo apt install libxml2-utils```

```apk: sudo apk add libxml2-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xsltproc](/man/xsltproc)(1), [xmlstarlet](/man/xmlstarlet)(1), [jq](/man/jq)(1), [yq](/man/yq)(1), [xq](/man/xq)(1)
