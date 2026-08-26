# TAGLINE

在隔离环境中安装 Python CLI 应用

# TLDR

**在隔离环境中安装应用**

```pipx install [httpie]```

**运行应用而不安装**

```pipx run [black] [file.py]```

**列出已安装的应用**

```pipx list```

**升级某个应用**

```pipx upgrade [youtube-dl]```

**升级所有应用**

```pipx upgrade-all```

**卸载应用**

```pipx uninstall [ansible]```

**向应用环境注入额外软件包**

```pipx inject [ipython] [matplotlib]```

**重新安装所有应用**

```pipx reinstall-all```

# SYNOPSIS

**pipx** _command_ [_options_] [_package_]

# PARAMETERS

**install** _PACKAGE_
> 在隔离环境中安装软件包。

**run** _PACKAGE_ [_args_]
> 在临时环境中运行应用。

**uninstall** _PACKAGE_
> 卸载软件包。

**upgrade** _PACKAGE_
> 升级软件包。

**upgrade-all**
> 升级所有已安装的软件包。

**list**
> 列出已安装的应用。

**inject** _APP_ _PACKAGES_
> 向应用的环境添加软件包。

**uninject** _APP_ _PACKAGES_
> 移除注入的软件包。

**reinstall** _PACKAGE_
> 重新安装软件包。

**reinstall-all**
> 重新安装所有软件包。

**ensurepath**
> 将 pipx 目录加入 PATH。

**--include-deps**
> 包含依赖项的可执行文件。

**--python** _PYTHON_
> 要使用的 Python 解释器。

**--system-site-packages**
> 包含系统软件包。

**--pip-args** _ARGS_
> 传给 pip 的参数。

**--force**
> 强制安装。

**--verbose**
> 详细输出。

# DESCRIPTION

**pipx** 将 Python 命令行应用安装到相互隔离的虚拟环境中。每个应用都有独立的环境，既避免依赖冲突，又让可执行文件全局可用。

与 pip install 不同，pipx 为每个工具创建单独的环境。这意味着 black、flake8 和 ansible 等应用即使要求冲突的软件包版本也能共存。

run 命令无需永久安装即可执行应用：下载、运行、清理——非常适合一次性使用或试用新工具。频繁运行的软件包会被缓存以提升速度。

inject 可向应用环境添加额外的软件包。当应用有插件或可选依赖需要一起安装时很有用。

ensurepath 命令配置 Shell 的 PATH 使其包含 pipx 的二进制位置。通常在初次安装 pipx 后执行一次即可。

# CONFIGURATION

**PIPX_HOME**
> 覆盖 pipx 数据的基础目录（默认：~/.local/pipx）。

**PIPX_BIN_DIR**
> 覆盖应用符号链接所在目录（默认：~/.local/bin）。

**PIPX_DEFAULT_PYTHON**
> 为新环境设置默认的 Python 解释器。

# CAVEATS

仅适用于命令行应用，不适用于库。每个应用都要占用磁盘空间存放其环境。注入的软件包可能导致冲突。Python 版本在安装时固定。某些应用可能需要系统依赖。

# HISTORY

**pipx** 由 **Chad Smith** 于 **2018 年**前后创建，目的是干净地安装 Python CLI 工具。其灵感来自 Node.js 生态中的 npx。该项目已成为 PyPA 推荐的应用安装工具，而库的安装仍推荐使用 pip。

# INSTALL

```dnf: sudo dnf install pipx```

```apk: sudo apk add pipx```

```brew: brew install pipx```

```nix: nix profile install nixpkgs#pipx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pipenv](/man/pipenv)(1), [poetry](/man/poetry)(1), [virtualenv](/man/virtualenv)(1)
