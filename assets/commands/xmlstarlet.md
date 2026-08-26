# TAGLINE

命令行 XML 处理工具集

# TLDR

**使用 XPath 表达式选择节点**

```xmlstarlet sel -t -v "[xpath]" [file.xml]```

**格式化/美化打印** XML 文件

```xmlstarlet fo [file.xml]```

**依据 schema 校验 XML 文件**

```xmlstarlet val -s [schema.xsd] [file.xml]```

**编辑 XML 文件**（更新节点值）

```xmlstarlet ed -u "[xpath]" -v "[new_value]" [file.xml]```

**使用 XSLT 样式表转换 XML**

```xmlstarlet tr [stylesheet.xsl] [file.xml]```

**列出 XML 文档的元素结构**

```xmlstarlet el [file.xml]```

**为 XML 转义特殊字符**

```echo "[text]" | xmlstarlet esc```

**检查 XML 文件的格式良好性**

```xmlstarlet val --well-formed [file.xml]```

# SYNOPSIS

**xmlstarlet** [_global_options_] _command_ [_command_options_] [_arguments_]

# PARAMETERS

**sel** (**select**)
> 使用 XPath 表达式选择或查询 XML 节点。

**ed** (**edit**)
> 通过插入、删除、更新或重命名节点来编辑 XML 文档。

**tr** (**transform**)
> 对 XML 文档执行 XSLT 转换。

**val** (**validate**)
> 依据 DTD 或 XML Schema 校验 XML 文档。

**fo** (**format**)
> 用适当的缩进格式化 XML 文档以提高可读性。

**el** (**elements**)
> 显示 XML 文档的元素结构。

**c14n** (**canonic**)
> 规范化 XML 文档（C14N）。

**ls** (**list**)
> 将目录内容列为 XML。

**esc** (**escape**)
> 转义文本中的特殊 XML 字符。

**unesc** (**unescape**)
> 将 XML 实体反转义为原始字符。

**pyx**
> 将 XML 转换为 PYX 格式。

**p2x** (**depyx**)
> 将 PYX 转换回 XML。

**--version**
> 显示版本信息。

**--help**
> 显示帮助消息。

# DESCRIPTION

**XMLStarlet** 是一个命令行 XML 工具集，为处理 XML 文件提供 Unix 风格的工具。它让你能用熟悉的 shell 命令模式查询、转换、校验和编辑 XML 文档，就像 grep、sed 和 awk 处理纯文本一样。

该工具集使用 XPath 选择节点，支持 XSLT 进行转换。它可以依据 DTD、XML Schema（XSD）和 RelaxNG 进行校验。基于 libxml2 和 libxslt 库构建，提供了健壮的 XML 处理能力。

每个命令都有自己的选项；使用 **xmlstarlet command --help** 可查看特定命令的详细帮助。

# CAVEATS

XMLStarlet 要求输入的 XML 格式良好；格式错误的文档会导致错误。它主要支持 XPath 1.0 和 XSLT 1.0，缺少新规范中的特性。命名空间处理可能比较复杂，可能需要显式声明前缀。

# HISTORY

XMLStarlet 由 **Mikhail Grushinskiy** 创建，于 **2002** 年首次发布。它的开发是为了满足能与 Unix shell 工作流集成的命令行 XML 处理工具的需求。该项目托管在 SourceForge 上，至今仍在维护，是脚本环境中处理 XML 的标准工具。

# INSTALL

```apt: sudo apt install xmlstarlet```

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xsltproc](/man/xsltproc)(1), [xmllint](/man/xmllint)(1), [jq](/man/jq)(1), [yq](/man/yq)(1)
