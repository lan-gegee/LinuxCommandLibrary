# TAGLINE

管理开发容器的 CLI

# TLDR

**构建 dev container**

```devcontainer build --workspace-folder [.]```

**启动 dev container**

```devcontainer up --workspace-folder [.]```

在容器中**执行命令**

```devcontainer exec --workspace-folder [.] [command]```

在容器中**打开 shell**

```devcontainer exec --workspace-folder [.] bash```

**读取配置**

```devcontainer read-configuration --workspace-folder [.]```

**列出 features**

```devcontainer features list```

**生成模板**

```devcontainer templates apply -t [python]```

**以 JSON 显示解析后的配置**

```devcontainer read-configuration --workspace-folder [.] --include-merged-configuration```

# SYNOPSIS

**devcontainer** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：build、up、exec、read-configuration、features、templates。

**--workspace-folder** _PATH_
> 包含 .devcontainer 配置的工作区路径。

**build**
> 构建 dev container 镜像。

**up**
> 创建并启动容器。

**exec** _COMMAND_
> 在容器中运行命令。

**read-configuration**
> 输出解析后的配置。

**features list**
> 列出可用的 dev container features。

**templates apply** **-t** _template_
> 将 dev container 模板应用到工作区。

**run-user-commands**
> 在容器中运行用户命令（postCreateCommand 等）。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**devcontainer** 是管理由 Dev Container 规范定义的开发容器的 CLI。它可以在命令行中构建、运行容器化开发环境并与之交互。

Dev container 借助 Docker 容器提供可复现的开发环境。.devcontainer/devcontainer.json 中的配置定义了项目所需的容器镜像、扩展、设置和 features。

该 CLI 让 dev container 工作流无需 IDE 即可运转，适用于 CI/CD 流水线、远程开发和开发环境自动化搭建。

# CONFIGURATION

**.devcontainer/devcontainer.json**
> 配置文件，定义容器镜像、features、扩展和环境设置。

# CAVEATS

需要 Docker 或兼容的容器运行时。配置必须遵循 Dev Container 规范。某些 features 需要特定的基础镜像。复杂环境会消耗较多资源。

# HISTORY

Dev Container CLI 由 **Microsoft** 作为 Dev Containers 规范的一部分发布（**2022 年**）。它将 VS Code Dev Containers 的功能延伸到命令行工作流和其他工具。

# INSTALL

```brew: brew install devcontainer```

```nix: nix profile install nixpkgs#devcontainer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1), [code](/man/code)(1)
