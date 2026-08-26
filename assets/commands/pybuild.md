# TAGLINE

为 Debian 构建 Python 软件包

# TLDR

**构建 Python 软件包**

```pybuild --build```

**安装到目录**

```pybuild --install --dest-dir [dir]```

**清理构建**

```pybuild --clean```

**使用指定 Python 构建**

```pybuild --interpreter python3```

# SYNOPSIS

**pybuild** [_options_]

# PARAMETERS

**--build**
> 构建软件包。

**--install**
> 安装软件包。

**--clean**
> 清理构建文件。

**--dest-dir** _DIR_
> 安装目录。

**--interpreter** _PYTHON_
> Python 解释器。

**-s** _SYSTEM_
> 构建系统。

# DESCRIPTION

**pybuild** 是一个 Debian 辅助工具，在 Debian 打包过程中构建和安装 Python 软件包。它封装了包括 setuptools、flit、poetry 和 meson-python 在内的多种 Python 构建系统，为 **dh-python** debhelper 序列提供统一接口。

该工具会从源码包自动检测合适的构建系统，并在需要时处理多个 Python 版本的构建。它通常通过 debhelper 规则间接调用而非直接使用，但也可手动调用以调试打包问题。

# CAVEATS

Debian 打包工具。属于 dh-python。

# HISTORY

pybuild 是 Debian Python 打包中 **dh-python** 的一部分。

# SEE ALSO

[dh](/man/dh)(1), [debhelper](/man/debhelper)(7), [python](/man/python)(1)
