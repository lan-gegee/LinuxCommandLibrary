# TAGLINE

从 Debian 软件包中提取 debconf 模板。

# TLDR

从软件包中**提取** debconf 模板

```apt-extracttemplates [package.deb]```

提取到**特定目录**

```apt-extracttemplates -t [/tmp/templates] [package.deb]```

从**多个软件包**提取

```apt-extracttemplates [package1.deb] [package2.deb]```

# SYNOPSIS

**apt-extracttemplates** [_-t tempdir_] _packages_

# DESCRIPTION

**apt-extracttemplates** 从 Debian 软件包中提取 debconf 模板和配置脚本。APT 在软件包安装过程中内部使用它来收集配置信息。

对每个软件包，它会输出四行内容：软件包名、版本、模板文件名和配置脚本文件名。提取出的模板包含 debconf 在安装期间用于配置软件包的问题。

# PARAMETERS

**-t** _dir_, **--tempdir** _dir_
> 提取文件的存放目录

**-c** _file_, **--config-file** _file_
> 配置文件

**-o** _option_
> 设置任意的 APT 配置选项

# CAVEATS

这主要是一个 APT 内部工具。大多数用户通过前端工具与 debconf 交互，而不是直接提取模板。

# HISTORY

**apt-extracttemplates** 是 APT 软件包管理基础设施的组成部分，为 debconf 配置系统提供支持。

# INSTALL

```apt: sudo apt install apt-utils```

```dnf: sudo dnf install apt-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [dpkg](/man/dpkg)(1), [dpkg-deb](/man/dpkg-deb)(1)
