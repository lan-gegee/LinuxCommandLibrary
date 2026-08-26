# TAGLINE

XMLStarlet 命令行 XML 工具集

# TLDR

**校验 XML**

```xml val [file.xml]```

**格式化/美化打印**

```xml fo [file.xml]```

**XPath 查询**

```xml sel -t -v "[//element]" [file.xml]```

**用 XSLT 转换**

```xml tr [transform.xsl] [file.xml]```

**就地编辑**

```xml ed -u "[//node]" -v "[value]" [file.xml]```

# SYNOPSIS

**xml** _command_ [_options_] _files_

# PARAMETERS

**val**
> 校验。

**fo**
> 格式化。

**sel**
> 选择（XPath）。

**tr**
> 转换。

**ed**
> 编辑。

**-t** **-v** _XPATH_
> 模板取值。

# DESCRIPTION

**xml** 是 XMLStarlet 的主命令，XMLStarlet 是一个全面的命令行 XML 工具集，用于查询、编辑、校验和转换 XML 文档。它提供一组子命令，覆盖常见的 XML 处理任务，无需完整的编程语言。

主要子命令包括：**val** 依据 DTD 或 schema 校验 XML，**fo** 美化打印和重新排版 XML，**sel** 使用 XPath 表达式选择数据，**ed** 就地编辑 XML 元素和属性，**tr** 应用 XSLT 转换。每个子命令都有针对其特定操作的一组选项。

XMLStarlet 为 shell 脚本和自动化而设计，可以将 XML 处理任务集成到管道和构建脚本中。它遵循 Unix 组合式约定，从文件或 stdin 读取并写入 stdout。

# CAVEATS

仅限 XMLStarlet。XPath 语法复杂。子命令众多。

# HISTORY

**XMLStarlet**（xml 命令）是一个用于查询、校验和转换 XML 的命令行工具集。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xmllint](/man/xmllint)(1), [xsltproc](/man/xsltproc)(1), [jq](/man/jq)(1)
