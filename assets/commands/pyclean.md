# TAGLINE

删除 Python 编译后的字节码文件

# TLDR

**删除字节码文件**

```pyclean [directory]```

**清理当前目录**

```pyclean .```

**清理指定软件包**

```pyclean -p [package_name]```

**详细输出**

```pyclean -v [directory]```

# SYNOPSIS

**pyclean** [_options_] [_directory_]

# PARAMETERS

_DIRECTORY_
> 要清理的目录。

**-p** _PACKAGE_
> 清理指定的软件包。

**-v**
> 详细输出。

**-q**
> 安静模式。

# DESCRIPTION

**pyclean** 从指定的目录树或 Debian 软件包中删除 Python 编译后的字节码文件（**.pyc**）和 **__pycache__** 目录。它可用于在 Python 版本变更后清理过期的字节码、减少磁盘占用，或准备干净的分发源码包。

该工具是 Debian Python 打包基础设施的一部分，可用 **-p** 标志针对特定软件包，也可递归清理任意目录。由于 Python 在导入时会自动重新生成字节码文件，删除它们不会产生持久影响，只是会短暂延长下一次导入的时间。

# CAVEATS

主要是 Debian/Ubuntu 工具（属于 **python-minimal** 软件包）。Python 会在下次导入时自动重新生成 .pyc 文件，因此删除是安全的，但会导致首次运行时略微变慢。`-p` 标志仅适用于 Debian 软件包。

# HISTORY

**pyclean** 是 Debian Python 打包基础设施的一部分，用于在软件包升级和卸载过程中清理字节码文件。

# SEE ALSO

[python](/man/python)(1), [py3clean](/man/py3clean)(1)
