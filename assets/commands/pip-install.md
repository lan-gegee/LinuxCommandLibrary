# TAGLINE

从 PyPI 和其他来源安装 Python 软件包

# TLDR

**安装软件包**

```pip install [package]```

**安装特定版本**

```pip install [package]==[version]```

**从 requirements 文件安装**

```pip install -r requirements.txt```

**以可编辑模式安装**

```pip install -e [path]```

**升级软件包**

```pip install --upgrade [package]```

**安装到用户目录**

```pip install --user [package]```

# SYNOPSIS

**pip** **install** [_options_] _packages_...

# PARAMETERS

**-r**, **--requirement** _file_
> 从 requirements 文件安装。

**-e**, **--editable** _path_
> 以可编辑/开发模式安装。

**-U**, **--upgrade**
> 将软件包升级到最新版本。

**--user**
> 安装到用户 site-packages 目录。

**--no-deps**
> 不安装依赖。

**--pre**
> 包含预发布版本。

**-i**, **--index-url** _url_
> 使用自定义软件包索引。

**--extra-index-url** _url_
> 额外的软件包索引。

**-t**, **--target** _dir_
> 安装到指定目录。

**--force-reinstall**
> 即使已是最新版本也重新安装。

# DESCRIPTION

**pip install** 从 Python Package Index（PyPI）和其他来源安装 Python 软件包。它负责依赖解析、下载、必要时从源码构建，并将软件包放入目标环境。

软件包可以通过名称、版本约束（**==**、**>=**、**~=**）、requirements 文件、本地目录、Git URL 或 wheel 文件来指定。开发期间使用 **-e** 进行可编辑安装，它会创建指向源码目录的链接而不是复制文件。**--user** 标志将软件包安装到用户 site-packages 目录，无需 root 权限。

默认情况下，pip 会解析并安装所有依赖。使用 **--no-deps** 可跳过依赖安装以便更严格地控制。**--pre** 标志会在解析过程中包含预发布和开发版本。可通过 **-i** 为私有仓库指定自定义软件包索引。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pip-uninstall](/man/pip-uninstall)(1), [pip-download](/man/pip-download)(1)
