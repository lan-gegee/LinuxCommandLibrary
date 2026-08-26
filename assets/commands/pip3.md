# TAGLINE

Python 3 软件包安装器

# TLDR

**安装软件包**

```pip3 install [package]```

**安装特定版本**

```pip3 install [package]==[version]```

**升级软件包**

```pip3 install --upgrade [package]```

**卸载软件包**

```pip3 uninstall [package]```

**列出已安装的软件包**

```pip3 list```

# SYNOPSIS

**pip3** [_command_] [_options_] [_packages_...]

# PARAMETERS

**install** _package_
> 安装软件包。

**uninstall** _package_
> 移除软件包。

**list**
> 列出已安装的软件包。

**freeze**
> 以 requirements 格式输出已安装的软件包。

**show** _package_
> 显示软件包详情。

**--user**
> 安装到用户 site-packages 目录。

**-r** _file_
> 从 requirements 文件安装。

# DESCRIPTION

**pip3** 是 Python 3 的软件包安装器。功能上与 **pip** 完全相同，但明确面向 Python 3 环境。在同时安装了 Python 2 和 Python 3 的系统上，pip3 可确保软件包安装到正确的解释器中。

pip3 默认从 **Python Package Index**（PyPI）下载软件包。它处理依赖解析和版本约束，并且可以从本地文件、版本控制 URL 或 requirements 文件进行安装。使用 **pip3 install -r requirements.txt** 可从 requirements 文件安装。

# CAVEATS

使用虚拟环境（**venv**）以避免与系统软件包冲突。**--user** 标志无需 root 即可安装到用户目录。在某些系统上，在虚拟环境之外使用 pip3 需要 **--break-system-packages** 标志。

# HISTORY

pip 由 **Ian Bicking** 于 **2008 年**创建，作为 easy_install 的替代品。它成为标准的 Python 软件包安装器，自 Python **3.4** 版本起随 Python 附带。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [python3](/man/python3)(1)
