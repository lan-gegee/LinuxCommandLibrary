# TAGLINE

列出已安装的 Python 3 解释器版本

# TLDR

**列出已安装的 Python 3 版本**

```py3versions -i```

**显示受支持的版本**

```py3versions -s```

**显示默认版本**

```py3versions -d```

**只显示版本号**（可与 -i、-s 或 -d 组合）

```py3versions -v -i```

# SYNOPSIS

**py3versions** [_options_]

# PARAMETERS

**-i**, **--installed**
> 显示已安装的受支持 python3 版本。

**-s**, **--supported**
> 显示该发行版支持的 python3 版本。

**-d**, **--default**
> 显示默认的 python3 版本。

**-r**, **--requested**
> 从 debian/control 读取 X-Python3-Version 字段并显示匹配的版本。

**-v**, **--version**
> 将输出限制为仅版本号（如 3.10 而非 python3.10）。

# DESCRIPTION

**py3versions** 报告 Debian 和 Ubuntu 系统上可用的 Python 3 解释器版本信息。它区分已安装的版本、发行版支持的版本以及系统使用的默认版本。

该工具是 Debian 的 **python3-minimal** 软件包的一部分，主要供打包工具和维护者脚本用来确定针对哪些 Python 版本进行编译或清理。**-i** 显示已安装的版本，**-s** 显示受支持的版本，**-d** 显示默认版本。受支持的版本列表按从低到高排序，默认版本排在最后。

# CAVEATS

Debian/Ubuntu 专用。属于 python3-minimal。

# HISTORY

py3versions 是用于 Python 3 版本管理的 **Debian 工具**。

# INSTALL

```apt: sudo apt install python3-minimal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python3](/man/python3)(1), [pyversions](/man/pyversions)(1), [update-alternatives](/man/update-alternatives)(1)
