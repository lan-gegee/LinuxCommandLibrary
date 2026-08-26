# TAGLINE

用于分析 Microsoft Office 文档的 Python 工具集合

# TLDR

**用 oleid 分析文档**

```oleid [document.doc]```

**提取 VBA 宏**

```olevba [document.xlsm]```

**检测恶意宏**

```mraptor [document.doc]```

**查找 RTF 漏洞利用代码**

```rtfobj [document.rtf]```

**分析 OLE 结构**

```olemeta [document.doc]```

**检查 Flash 内容**

```oleobj [document.pptx]```

# SYNOPSIS

**oletools** - 用于分析 Office 文档的 Python 工具集

# DESCRIPTION

**oletools** 是一套用于分析 Microsoft Office 文档（OLE、VBA、Office Open XML）的 Python 工具集合，常用于恶意软件分析和恶意文档检测。

该工具集包含多个针对不同分析任务的专用工具。

# INCLUDED TOOLS

```
oleid    - Quick analysis, indicators
olevba   - Extract/analyze VBA macros
mraptor  - Detect malicious VBA
olemeta  - Show metadata
oleobj   - Extract embedded objects
rtfobj   - Analyze RTF files
oletimes - Show timestamps
oledir   - List OLE directory
```

# INSTALLATION

```bash
pip install oletools
```

# CAVEATS

需要安装 Python 软件包。启发式检测可能存在误报。无法解密有密码保护的文件。

# HISTORY

oletools 由 **Philippe Lagadec** 创建，用于分析可能恶意的 Office 文档，在恶意软件分析和应急响应领域被广泛使用。

# INSTALL

```nix: nix profile install nixpkgs#oletools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[oleid](/man/oleid)(1), [olevba](/man/olevba)(1), [mraptor](/man/mraptor)(1), [yara](/man/yara)(1)
