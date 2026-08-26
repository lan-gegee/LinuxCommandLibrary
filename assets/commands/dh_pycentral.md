# TAGLINE

用于 python-central 注册的过时 debhelper 命令

# TLDR

**向 pycentral 注册 Python 模块**

```dh_pycentral```

**以详细输出模式**处理

```dh_pycentral -v```

**处理指定软件包**

```dh_pycentral -p [package_name]```

# SYNOPSIS

**dh_pycentral** [_debhelper-options_]

# PARAMETERS

**-v**, **--verbose**
> 详细输出。

**-p** _PACKAGE_, **--package** _PACKAGE_
> 只处理指定软件包。

**-n**, **--no-scripts**
> 不修改 postinst/prerm 脚本。

# DESCRIPTION

**dh_pycentral** 曾是一个 debhelper 命令，用于向 python-central 注册 Python 模块。python-central 是一套管理可在多个 Python 版本之间共享的模块的系统。

该工具负责 Python 模块的字节码编译和按版本安装，确保它们能与系统上所有已安装的 Python 版本正确配合。

随着 python-central 从 Debian 中移除、由与现代化 Python 打包标准集成更好的 dh_python2/dh_python3 取代，此命令也已过时。

# CAVEATS

已过时并被弃用。现代软件包应改用 dh_python3。仅对维护遗留软件包或了解历史上的 Debian Python 打包方式有意义。

# HISTORY

dh_pycentral 是 **python-central** 的一部分，后者约于 **2006 年**为 Debian 的 Python 打包而开发。它先被 python-support 取代，随后又被 dh_python2/dh_python3 替代，并在 Python 2 弃用之后从 Debian 中移除。

# SEE ALSO

[dh](/man/dh)(1), [python](/man/python)(1)
