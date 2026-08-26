# TAGLINE

设置 TeX 程序的默认纸张尺寸

# TLDR

**显示当前纸张尺寸**

```tlmgr paper```

**为所有程序设置纸张尺寸**

```tlmgr paper [a4]```

**为特定程序设置纸张**

```tlmgr paper [dvips] [letter]```

**列出可用尺寸**

```tlmgr paper --list```

# SYNOPSIS

**tlmgr paper** [_program_] [_paper_]

# PARAMETERS

**--list**
> 列出可用的纸张尺寸。

_program_
> 特定程序（dvips、pdftex、xetex 等）。

_paper_
> 纸张尺寸（a4、letter 等）。

# DESCRIPTION

**tlmgr paper** 为 TeX 程序配置默认纸张尺寸。使 LaTeX、dvips 和 PDF 输出工具使用一致的纸张尺寸。TeX Live Manager 的组成部分。

# SEE ALSO

[tlmgr-conf](/man/tlmgr-conf)(1), [tlmgr](/man/tlmgr)(1)
