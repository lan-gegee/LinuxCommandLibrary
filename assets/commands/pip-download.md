# TAGLINE

下载软件包而不安装

# TLDR

**下载软件包**

```pip download [package]```

**下载到指定目录**

```pip download -d [directory] [package]```

**下载特定版本**

```pip download [package]==[version]```

**为特定平台下载**

```pip download --platform [linux_x86_64] --only-binary=:all: [package]```

**从 requirements 文件下载**

```pip download -r requirements.txt```

# SYNOPSIS

**pip** **download** [_options_] _packages_...

# PARAMETERS

**-d**, **--dest** _dir_
> 下载目录。

**-r**, **--requirement** _file_
> 从 requirements 文件下载。

**--no-deps**
> 不下载依赖。

**--only-binary** _format_
> 仅下载二进制软件包。

**--platform** _platform_
> 为特定平台下载。

**--python-version** _version_
> 为特定 Python 版本下载。

# DESCRIPTION

**pip download** 下载软件包但不安装。将 wheel 或源码发行版下载到指定目录。适用于离线安装或创建本地软件包镜像。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pip-install](/man/pip-install)(1), [pip-wheel](/man/pip-wheel)(1)
