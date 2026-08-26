# TAGLINE

列出 Debian 上可用的 Python 解释器版本

# TLDR

**列出已安装的 Python 版本**

```pyversions -i```

**显示受支持的版本**

```pyversions -s```

**显示默认版本**

```pyversions -d```

**显示请求的版本**

```pyversions -r```

# SYNOPSIS

**pyversions** [_options_]

# PARAMETERS

**-i**, **--installed**
> 列出已安装的 Python 版本。

**-s**, **--supported**
> 列出当前 Debian 发行版支持的 Python 版本。

**-d**, **--default**
> 打印默认的 Python 版本（**/usr/bin/python** 指向的目标）。

**-r**, **--requested** [_pkg_|_setup.py_|_debian/control_]
> 打印软件包源所请求的 Python 版本（默认为当前目录下的 **debian/control**）。

**-v**, **--version**
> 与上述选项之一配合使用，同时打印对应的解释器路径。

# DESCRIPTION

**pyversions** 是 Debian 专用的辅助工具，用于报告系统中可用的 **Python 2** 解释器版本信息。它列出已安装的版本、默认版本、当前 Debian 发行版支持的版本，以及源码包通过 **debian/control** 中 **X-Python-Version** 字段请求的版本。Debian 的 Python 打包基础设施（debhelper、dh_python2）用它来驱动构建时的决策。

Python 3 对应的工具是 **py3versions**，如今应使用后者；**pyversions** 本身随 Python 2 一起在 **Debian 11（bullseye）** 中退役，并在后续发行版中被移除。

# CAVEATS

Debian/Ubuntu 专用且仅支持 Python 2。提供它的软件包（**python**）已在 Debian 11+ 和 Ubuntu 20.04+ 中移除。现代系统请改用 **py3versions**。

# HISTORY

**pyversions** 随 Debian 的 **python-minimal** / **python** 软件包发布，曾是 Debian 打包中查询 Python 2 版本的标准方式。在 Python 2 于 **2020-01-01** 终止支持后，该工具随语言一同被弃用，并从当前的 Debian/Ubuntu 发行版中移除。

# SEE ALSO

[python](/man/python)(1), [py3versions](/man/py3versions)(1), [update-alternatives](/man/update-alternatives)(1)
