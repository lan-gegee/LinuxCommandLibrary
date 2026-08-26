# TAGLINE

virtualenv 的便利封装工具

# TLDR

**创建虚拟环境**

```mkvirtualenv [envname]```

**使用指定 Python 版本创建**

```mkvirtualenv -p [python3.11] [envname]```

**创建时安装软件包**

```mkvirtualenv -i [package] [envname]```

**从 requirements 文件创建**

```mkvirtualenv -r [requirements.txt] [envname]```

**激活环境**

```workon [envname]```

**列出环境**

```workon```

**停用环境**

```deactivate```

**移除环境**

```rmvirtualenv [envname]```

**复制一个环境**

```cpvirtualenv [source] [dest]```

**切换到项目目录**

```cdproject```

**在所有环境中运行命令**

```allvirtualenv [command]```

# SYNOPSIS

**mkvirtualenv** _envname_

**workon** [_envname_]

**rmvirtualenv** _envname_

# COMMANDS

**mkvirtualenv** [_-a project_path_] [_-i package_] [_-r requirements_file_] _envname_
> 创建环境。选项 -a、-i、-r 由 virtualenvwrapper 处理；所有其他选项都会传给 virtualenv。

**workon** [_envname_]
> 激活环境；不提供名称时列出全部环境。

**deactivate**
> 退出当前环境。

**rmvirtualenv** _envname_
> 删除环境。

**cpvirtualenv** _source_ _dest_
> 复制现有环境。

**cdproject**
> 切换到关联的项目目录。

**setvirtualenvproject** [_virtualenv_path_ _project_path_]
> 将项目目录与环境关联。

**allvirtualenv** _command_
> 在所有环境中运行一条命令。

**lsvirtualenv** [_-b_] [_-l_]
> 列出所有环境（-b 简要，-l 详细）。

# DESCRIPTION

**virtualenvwrapper** 是一组 shell 扩展，用于增强标准的 virtualenv 工具来管理 Python 虚拟环境。它提供了便捷的封装命令，用于创建、激活、切换和删除环境，并将它们集中在一处，而不是分散在各项目目录中。

核心工作流围绕 `workon` 命令（列出与切换环境）、`mkvirtualenv`（创建）以及 `rmvirtualenv`（删除）展开。所有环境都存储在一个可配置的目录中（通常是 `~/.virtualenvs`），无论项目代码位于何处，都便于查找和管理。

该工具还支持项目目录关联，激活环境时可自动切换目录，并提供在关键生命周期事件（如环境创建、激活和停用）时运行的钩子脚本，以实现自定义自动化。

# CAVEATS

需要进行 shell 配置：在你的 shell 配置文件中 source virtualenvwrapper.sh 脚本。所有环境存储在同一目录（默认：~/.virtualenvs），可通过 WORKON_HOME 环境变量配置。

# HISTORY

**virtualenvwrapper** 由 **Doug Hellmann** 开发，旨在让 Python 虚拟环境的管理更加轻松。

# INSTALL

```brew: brew install virtualenvwrapper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virtualenv](/man/virtualenv)(1), [venv](/man/venv)(1), [pip](/man/pip)(1)
