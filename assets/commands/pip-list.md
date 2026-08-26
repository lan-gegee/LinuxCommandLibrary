# TAGLINE

列出已安装的 Python 软件包及版本

# TLDR

**列出已安装的软件包**

```pip list```

**列出过期的软件包**

```pip list --outdated```

**以 JSON 格式列出**

```pip list --format json```

**仅列出用户级安装的软件包**

```pip list --user```

**列出可编辑安装的软件包**

```pip list --editable```

**列出未被其他软件包依赖的软件包**

```pip list --not-required```

**在输出中排除某个软件包**

```pip list --exclude [pip] --exclude [setuptools]```

# SYNOPSIS

**pip** **list** [_options_]

# PARAMETERS

**-o**, **--outdated**
> 仅显示已过期的软件包。

**-u**, **--uptodate**
> 仅显示最新的软件包。

**-e**, **--editable**
> 仅显示可编辑安装的软件包。

**-l**, **--local**
> 仅显示虚拟环境中的软件包。

**--user**
> 仅显示用户级安装的软件包。

**--format** _format_
> 输出格式（columns、freeze、json）。

**--not-required**
> 显示未被其他软件包依赖的软件包。

**--exclude** _pkg_
> 在输出中排除指定的软件包（可重复使用）。

**--path** _dir_
> 限制为指定安装路径中的软件包。

**--exclude-editable**
> 在输出中排除可编辑安装的软件包。

**--include-editable**
> 在输出中包含可编辑安装的软件包。

# DESCRIPTION

**pip list** 显示已安装的 Python 软件包及其版本。可按过期、最新或可编辑安装进行过滤。支持多种输出格式，包括便于脚本处理的 JSON。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pip-freeze](/man/pip-freeze)(1), [pip-show](/man/pip-show)(1)
