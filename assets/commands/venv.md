# TAGLINE

创建 Python 虚拟环境

# TLDR

**创建虚拟环境**

```python -m venv [venv]```

**创建时可使用系统软件包**

```python -m venv --system-site-packages [venv]```

**激活（bash/zsh）**

```source [venv]/bin/activate```

**激活（fish）**

```source [venv]/bin/activate.fish```

**停用**

```deactivate```

**清空环境**

```python -m venv --clear [venv]```

# SYNOPSIS

**python -m venv** [_--system-site-packages_] [_--clear_] _path_

# PARAMETERS

**--system-site-packages**
> 包含系统软件包。

**--clear**
> 清空已有内容。

**--without-pip**
> 不安装 pip。

**--upgrade**
> 升级脚本。

**--prompt** _TEXT_
> 自定义提示符。

# DESCRIPTION

**venv** 创建轻量级的 Python 虚拟环境，将项目依赖与系统 Python 安装隔离。每个虚拟环境拥有自己的 site-packages 目录，可以安装不同版本的软件包而互不冲突。

该模块是 Python 标准库的一部分，无需额外安装。激活脚本会修改 shell 的 PATH 以使用虚拟环境的 Python 和 pip，执行 **deactivate** 则回到系统环境。

# CAVEATS

需要 Python 3.3+。更早版本请用 virtualenv。与路径绑定。

# HISTORY

**venv** 在 Python 3.3 中加入标准库，成为推荐的虚拟环境创建方式。

# SEE ALSO

[virtualenv](/man/virtualenv)(1), [pip](/man/pip)(1), [python](/man/python)(1)
