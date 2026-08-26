# TAGLINE

检测 Microsoft Office 文档中的恶意 VBA 宏

# TLDR

**扫描文档中的宏**

```mraptor [document.doc]```

**扫描多个文件**

```mraptor [*.doc]```

**递归扫描目录**

```mraptor -r [directory/]```

**以 JSON 输出**

```mraptor -j [document.xlsm]```

**匹配特定模式**

```mraptor -m [pattern] [document.doc]```

# SYNOPSIS

**mraptor** [_options_] _files_...

# PARAMETERS

**-r**, **--recursive**
> 递归扫描目录。

**-j**, **--json**
> JSON 输出。

**-m** _pattern_
> 匹配特定模式。

**-l** _level_
> 日志级别。

**-z** _password_
> ZIP 密码。

# DESCRIPTION

**mraptor**（Macro Raptor）检测 Microsoft Office 文档中的恶意 VBA 宏。它分析宏代码，识别恶意软件中常见的可疑模式。

作为 oletools 套件的一部分，mraptor 可对潜在危险的文档进行快速分诊。

# DETECTION FLAGS

```
A - AutoExec (auto-run)
W - Write file
X - Execute
S - Suspicious keywords
```

# RISK LEVELS

```
SAFE      - No macros or no suspicious code
LOW       - Macros but no execution
MEDIUM    - Some suspicious patterns
HIGH/VERY HIGH - Strong malware indicators
```

# CAVEATS

基于启发式方法；可能存在误报。无法检测所有恶意软件。属于 oletools 软件包。

# HISTORY

mraptor 由 **Philippe Lagadec** 开发，是 **oletools** 的一部分，后者是一套用于分析 Microsoft Office 文档的 Python 工具集。

# INSTALL

```apk: sudo apk add py3-oletools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[olevba](/man/olevba)(1), [oleid](/man/oleid)(1), [oletools](/man/oletools)(1), [yara](/man/yara)(1)
