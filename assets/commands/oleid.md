# TAGLINE

分析 Microsoft Office 文档以发现潜在安全问题

# TLDR

**分析 Office 文档**

```oleid [document.doc]```

**分析多个文件**

```oleid [file1.docx] [file2.xlsx]```

**以 JSON 格式输出结果**

```oleid -j [document.xlsm]```

**分析有密码保护的 ZIP 压缩包**

```oleid -z [infected] [document.zip]```

# SYNOPSIS

**oleid** [_options_] _files_...

# PARAMETERS

**-j**, **--json**
> 以 JSON 格式输出结果。

**-v**, **--verbose**
> 输出详细信息和额外内容。

**-z** _PASSWORD_
> 打开 ZIP 加密文件的密码。

**-l** _LEVEL_
> 设置日志级别（DEBUG、INFO、WARNING、ERROR、CRITICAL）。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**oleid** 分析 Microsoft Office 文档（OLE 和 OpenXML 格式）以发现潜在的安全问题。它可以识别 VBA 宏、加密内容、外部链接、嵌入对象以及其他常见于恶意文档的指标。

oleid 属于 **oletools** 套件，可用于对可疑文档进行快速分诊。它检查的指标包括 OLE 格式有效性、应用程序名、加密状态、VBA 宏、自执行宏、嵌入的 Flash 对象以及 ObjectPool 流。

# INDICATORS

```
OLE format      - Valid OLE file structure
Application     - Creating application name
VBA Macros      - Contains VBA code
Auto-executable - Auto-run macros present
Encrypted       - MS Office encryption detected
ObjectPool      - Embedded OLE objects
Flash objects   - Embedded Flash content
```

# CAVEATS

属于启发式分析；可能产生误报。需要 **oletools** Python 软件包。未通过 **-z** 提供密码时无法分析加密文件。

# HISTORY

oleid 由 **Philippe Lagadec** 开发，是 **oletools** 的组成部分。oletools 是一个用于分析 Microsoft OLE2 文件（Structured Storage / Compound File Binary Format）及 MS Office 文档的 Python 工具集。

# INSTALL

```apk: sudo apk add py3-oletools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[olevba](/man/olevba)(1), [mraptor](/man/mraptor)(1), [oletools](/man/oletools)(1), [clamscan](/man/clamscan)(1)
