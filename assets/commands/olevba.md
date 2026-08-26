# TAGLINE

提取并分析 VBA 宏

# TLDR

**分析 Office 文档**

```olevba [document.docx]```

**显示 VBA 代码**

```olevba -c [document.xlsm]```

**解码混淆字符串**

```olevba -d [document.doc]```

**JSON 输出**

```olevba --json [document.docm]```

**分析目录中的所有文件**

```olevba [directory/]```

# SYNOPSIS

**olevba** [_options_] _file_...

# PARAMETERS

_FILE_
> 要分析的 Office 文档。

**-c**
> 显示 VBA 源代码。

**-d**
> 解码混淆字符串。

**--json**
> JSON 输出格式。

**-a**
> 显示全部信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**olevba** 提取并分析 VBA 宏，检测恶意的 Office 文档。

该工具检查文档中内嵌的宏，属于 oletools 安全工具套件的一部分。

# CAVEATS

属于安全分析工具。是 oletools 的一部分。需要 Python 环境。

# HISTORY

olevba 作为 **oletools** 的组成部分而创建，用于 Office 文档安全分析。

# INSTALL

```apk: sudo apk add py3-oletools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[oletools](/man/oletools)(1), [mraptor](/man/mraptor)(1), [oleid](/man/oleid)(1)
