# TAGLINE

统一的代码质量检查与格式化工具

# TLDR

在项目中初始化 trunk

```trunk init```

检查已更改文件中的问题

```trunk check```

检查仓库中的所有文件

```trunk check --all```

检查并自动修复问题

```trunk check --fix```

格式化已更改的文件

```trunk fmt```

格式化仓库中的所有文件

```trunk fmt --all```

仅运行特定的 linter

```trunk check --filter [eslint]```

升级 trunk 及所有受管理的工具

```trunk upgrade```

# SYNOPSIS

**trunk** _command_ [_options_]

# PARAMETERS

**init**
> 在当前仓库中初始化 trunk 配置，创建 `.trunk/trunk.yaml` 文件。

**check** [_paths..._]
> 对已更改的文件运行所有启用的 linter。不带 `--all` 时，只检查相对于上游分支有修改的文件。

**fmt** [_paths..._]
> 使用启用的格式化工具格式化代码。等同于 `trunk check --fix --filter` 应用到所有格式化工具。

**upgrade**
> 升级 trunk CLI 和所有受管理的工具版本。

**actions**
> 管理 trunk actions（git 钩子、通知等）。

**tools**
> 管理 linter 和格式化工具的安装。

**login**
> 向 Trunk 平台进行身份认证。

**--all**
> 检查或格式化仓库中的所有文件，而不只是已更改的文件。

**--fix**
> 自动应用支持自动修复的问题修复。

**--filter** _linter_
> 将检查限制到指定的 linter 或格式化工具。

**--upstream** _branch_
> 显式设置用于变更检测的上游分支（默认自动检测）。

**--no-progress**
> 在检查过程中不显示进度报告。

**--ci**
> 以 CI 模式运行，采用相应的输出格式。

**--output** _format_
> 设置输出格式（例如 text、json）。

# DESCRIPTION

**trunk** 是一个代码质量工具，通过统一界面管理多个 linter 和格式化工具。它会自动检测并为你的代码库配置合适的工具，提供静态分析、格式化和 CI 集成能力。

默认情况下，trunk 以 hold-the-line 模式运行：只检查相对于上游分支有变更的文件，避免既有问题阻碍新的工作。使用 `--all` 可检查整个仓库。

配置存储在 `.trunk/trunk.yaml` 中，可以在其中启用、禁用或自定义 linter、格式化工具和 actions。

# SEE ALSO

[eslint](/man/eslint)(1), [prettier](/man/prettier)(1)
