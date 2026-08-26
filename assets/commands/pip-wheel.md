# TAGLINE

从 Python 软件包构建 wheel 归档

# TLDR

**从软件包构建 wheel**

```pip wheel [package]```

**将 wheel 构建到目录**

```pip wheel -w [wheeldir] [package]```

**从 requirements 文件构建**

```pip wheel -r requirements.txt```

**从本地项目构建 wheel**

```pip wheel .```

# SYNOPSIS

**pip** **wheel** [_options_] _packages_...

# PARAMETERS

**-w**, **--wheel-dir** _dir_
> 将 wheel 构建到指定目录。

**-r**, **--requirement** _file_
> 从 requirements 文件构建。

**--no-deps**
> 不构建依赖。

**--no-build-isolation**
> 禁用构建隔离。

**--src** _dir_
> 可编辑项目的源码目录。

# DESCRIPTION

**pip wheel** 为软件包及其依赖构建 wheel 归档。wheel 是预构建的二进制发行版，安装速度比源码发行版更快。适用于为离线安装或部署创建本地 wheel。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pip-download](/man/pip-download)(1), [pip-install](/man/pip-install)(1)
