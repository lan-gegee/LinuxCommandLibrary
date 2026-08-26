# TAGLINE

创建隔离的 Python 环境

# TLDR

**创建虚拟环境**

```virtualenv [venv]```

**使用指定 Python 创建**

```virtualenv -p [python3.11] [venv]```

**创建时不安装 pip**

```virtualenv --no-pip [venv]```

**创建时可访问系统软件包**

```virtualenv --system-site-packages [venv]```

**激活环境**（bash/zsh）

```source [venv]/bin/activate```

**激活环境**（fish）

```source [venv]/bin/activate.fish```

**停用环境**

```deactivate```

**使用最新的种子包创建**

```virtualenv --download [venv]```

# SYNOPSIS

**virtualenv** [_options_] _dest_

# DESCRIPTION

**virtualenv** 创建隔离的 Python 环境。每个环境拥有自己的 Python 二进制文件和独立的已安装软件包集合，让不同项目可以使用不同的依赖而不产生冲突。

激活后，虚拟环境会修改 PATH 以使用该环境的 Python 和 pip，将软件包安装与系统 Python 隔离。这对构建可复现的开发环境至关重要。

virtualenv 是 Python 最早的虚拟环境工具，早于内置的 venv 模块。它提供额外功能，例如选择 Python 版本以及更快的环境创建速度。

# PARAMETERS

**-p** _python_, **--python=** _python_
> 要使用的 Python 解释器。

**--system-site-packages**
> 允许访问系统 site-packages。

**--no-pip**
> 不安装 pip。

**--no-setuptools**
> 不安装 setuptools。

**--no-wheel**
> 不安装 wheel。

**--download**
> 下载最新的 pip/setuptools/wheel。

**--no-download**
> 使用内置的 pip/setuptools/wheel。

**--clear**
> 清空已有环境。

**--copies**
> 使用复制而不是符号链接。

**--prompt** _text_
> 为激活的环境自定义提示符前缀。

**--activators** _list_
> 要生成的激活器（逗号分隔：bash、fish、cshell、powershell 等）。

**-v**, **--verbose**
> 提高输出详细程度。

**-q**, **--quiet**
> 降低输出详细程度。

# CAVEATS

每个新 shell 中都必须重新激活环境。环境中嵌入了绝对路径，因此不可迁移。指定的 Python 版本必须存在于系统中。基本需求可考虑使用 python -m venv。

# HISTORY

**virtualenv** 由 **Ian Bicking** 于 **2007 年**创建，用于解决 Python 缺乏内置环境隔离的问题。在 Python 3.3 将 venv 加入标准库之前，它一直是 Python 开发的标准工具。凭借额外特性以及对 Python 2（历史）的支持，virtualenv 至今仍然流行。

# INSTALL

```apk: sudo apk add py3-virtualenv```

```brew: brew install virtualenv```

```nix: nix profile install nixpkgs#virtualenv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [pip](/man/pip)(1), [pyenv](/man/pyenv)(1), [venv](/man/venv)(1)
