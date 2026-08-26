# TAGLINE

现代的 Python 项目管理工具

# TLDR

**创建新项目**

```hatch new [project-name]```

**构建软件包**

```hatch build```

**运行测试**

```hatch run test```

**进入环境**

```hatch shell```

**发布到 PyPI**

```hatch publish```

**查看或提升项目版本**

```hatch version```

# SYNOPSIS

**hatch** [_options_] _command_ [_args_]

# PARAMETERS

**new** _name_
> 创建新项目。

**build**
> 构建发行版。

**publish**
> 发布到软件包索引。

**run** _cmd_
> 在环境中运行命令。

**shell**
> 进入项目环境。

**env** _subcommand_
> 管理环境。

**test**
> 跨多个环境运行测试。

**fmt**
> 格式化代码。

**version**
> 查看/提升版本。

**clean**
> 移除构建产物。

# DESCRIPTION

**Hatch** 是一个现代、可扩展的 Python 项目管理工具。它在同一个工具中处理项目创建、构建、发布、环境管理和测试。它是 Python Packaging Authority（PyPA）推荐的官方构建后端。

Hatch 使用 pyproject.toml 作为配置，并遵循现行的 PEP 标准。它提供可复现的环境，并通过可配置的矩阵实现多环境测试。

# PYPROJECT.TOML

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "myproject"
version = "0.1.0"

[tool.hatch.envs.default]
dependencies = ["pytest"]

[tool.hatch.envs.default.scripts]
test = "pytest {args}"
```

# CAVEATS

相对较新；生态仍在发展壮大。工作流与 pip/setuptools 不同。环境管理方式与 virtualenv 有差异。某些场景可能需要插件。

# HISTORY

Hatch 由 **Ofek Lev** 创建，作为传统 Python 打包工具的现代替代品。它遵循现行的 PEP 标准，旨在简化 Python 项目的生命周期。

# INSTALL

```dnf: sudo dnf install hatch```

```brew: brew install hatch```

```nix: nix profile install nixpkgs#hatch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [poetry](/man/poetry)(1), [flit](/man/flit)(1), [pdm](/man/pdm)(1)
