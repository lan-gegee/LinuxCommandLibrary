# TAGLINE

移除已安装的 Python 软件包

# TLDR

**卸载软件包**

```pip uninstall [package]```

**卸载且不显示确认提示**

```pip uninstall -y [package]```

**一次性卸载多个软件包**

```pip uninstall [package1] [package2]```

**卸载 requirements 文件中列出的所有软件包**

```pip uninstall -r [requirements.txt]```

**从 requirements 文件卸载并自动确认**

```pip uninstall -y -r [requirements.txt]```

# SYNOPSIS

**pip** **uninstall** [_options_] _package_...

**pip** **uninstall** [_options_] **-r** _requirements-file_...

# PARAMETERS

**-r** _FILE_, **--requirement** _FILE_
> 卸载给定 requirements 文件中列出的所有软件包。可以多次使用。

**-y**, **--yes**
> 不请求确认卸载删除操作。

**--root-user-action** _ACTION_
> 以 root 身份运行 pip 时的处理方式（warn、ignore）。

**--no-input**
> 禁用输入提示。

**-v**, **--verbose**
> 输出更多信息。可重复使用。

**-q**, **--quiet**
> 输出更少信息。

# DESCRIPTION

**pip uninstall** 移除已安装的 Python 软件包。除非使用 `-y`，否则在移除每个软件包前都会请求确认。

Pip 会移除软件包文件、入口点脚本和元数据，但**不会**自动移除随该软件包一起安装的依赖。以"可编辑"模式（`pip install -e`）安装的软件包以及直接从 VCS URL 安装的软件包也可以按名称移除。

由系统软件包管理器（如 `apt`、`dnf`）安装的软件包，或未通过 pip 元数据安装的软件包，无法用 pip 卸载。

# CAVEATS

以 root 身份对系统 Python 运行 `pip uninstall` 可能破坏操作系统；建议使用虚拟环境或 `--user` 安装。依赖永远不会被自动移除，因此卸载顶层软件包后可能残留孤立软件包。可使用 `pip list` 或 `pip-autoremove` 来查找孤立软件包。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pip-install](/man/pip-install)(1), [pip3](/man/pip3)(1), [pipx](/man/pipx)(1)
