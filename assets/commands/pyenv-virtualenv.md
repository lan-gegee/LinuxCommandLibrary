# TAGLINE

用 pyenv 管理 Python 虚拟环境

# TLDR

**创建 virtualenv**

```pyenv virtualenv [3.11.0] [myproject]```

**列出 virtualenv**

```pyenv virtualenvs```

**激活 virtualenv**

```pyenv activate [myproject]```

**停用 virtualenv**

```pyenv deactivate```

**删除 virtualenv**

```pyenv virtualenv-delete [myproject]```

**设置目录级 virtualenv**

```pyenv local [myproject]```

**使用当前版本创建**

```pyenv virtualenv [myproject]```

# SYNOPSIS

**pyenv virtualenv** [_version_] _name_

**pyenv activate** _name_

**pyenv deactivate**

# PARAMETERS

**virtualenv** _VERSION_ _NAME_
> 创建新的 virtualenv。

**virtualenvs**
> 列出 virtualenv。

**activate** _NAME_
> 激活 virtualenv。

**deactivate**
> 停用当前环境。

**virtualenv-delete** _NAME_
> 删除 virtualenv。

# DESCRIPTION

**pyenv-virtualenv** 是一个 pyenv 插件，在 pyenv 版本管理的基础上管理 Python 虚拟环境。它创建与特定 Python 版本绑定的隔离环境，每个环境拥有独立的一套已安装软件包，并无缝集成到 pyenv 的版本切换流程中。

由该插件创建的虚拟环境会作为普通的 pyenv 版本出现，可用 **pyenv activate** 手动激活，或通过 **pyenv local** 设置本地版本来自动激活。当 **.python-version** 文件引用某个 virtualenv 名称时，进入该目录会自动激活对应环境，离开时自动停用，实现无摩擦的按项目工作流。

# CAVEATS

需要先安装 pyenv。可能需要配置 shell 集成。某些情况下比 venv 慢。

# HISTORY

**pyenv-virtualenv** 由 pyenv 社区创建为 pyenv 插件，将 virtualenv 管理引入 pyenv 工作流。

# INSTALL

```brew: brew install pyenv-virtualenv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pyenv](/man/pyenv)(1), [virtualenv](/man/virtualenv)(1), [python](/man/python)(1), [pip](/man/pip)(1)
