# TAGLINE

以 requirements 格式输出已安装的软件包

# TLDR

**列出已安装的软件包**

```pip freeze```

**输出到 requirements 文件**

```pip freeze > requirements.txt```

**包含包括 pip 和 setuptools 在内的所有软件包**

```pip freeze --all```

**排除可编辑安装的软件包**

```pip freeze --exclude-editable```

**排除特定软件包**

```pip freeze --exclude [package]```

**仅列出当前虚拟环境中的软件包**

```pip freeze --local```

# SYNOPSIS

**pip** **freeze** [_options_]

# PARAMETERS

**-r**, **--requirement** _file_
> 按 requirements 文件的顺序输出。

**-l**, **--local**
> 仅显示虚拟环境中的软件包。

**--user**
> 仅显示用户级安装的软件包。

**--exclude** _package_
> 在输出中排除某个软件包。

**--all**
> 包含所有软件包，包括通常被排除的 pip 和 setuptools。

**--exclude-editable**
> 排除可编辑安装的软件包。

**--path** _directory_
> 将列出的软件包限制在指定的安装路径中。

**-q**, **--quiet**
> 降低输出的详细程度。

# DESCRIPTION

**pip freeze** 以 requirements 格式输出已安装的软件包。每个软件包都会显示其确切版本（package==version）。这是捕获 Python 环境依赖以保证可复现性的标准方法。默认情况下，pip、setuptools、wheel 和 distribute 不会出现在输出中；使用 **--all** 可将其包含在内。软件包按不区分大小写的排序顺序列出。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pip-list](/man/pip-list)(1), [pip-install](/man/pip-install)(1), [pip-show](/man/pip-show)(1)
