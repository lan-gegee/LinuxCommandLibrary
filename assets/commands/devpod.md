# TAGLINE

在任何基础设施上获得可复现的开发环境

# TLDR

**创建新工作区**

```devpod up [github.com/user/repo]```

**使用指定 provider 创建工作区**

```devpod up [github.com/user/repo] --provider [docker]```

**列出工作区**

```devpod list```

**通过 SSH 连接到工作区**

```devpod ssh [workspace_name]```

**停止一个工作区**

```devpod stop [workspace_name]```

**删除一个工作区**

```devpod delete [workspace_name]```

**添加一个 provider**

```devpod provider add [kubernetes]```

# SYNOPSIS

**devpod** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：up、list、ssh、stop、delete、provider。

**up** _SOURCE_
> 从 git 仓库、文件夹或镜像创建工作区。

**--provider** _PROVIDER_
> 指定基础设施 provider。

**--ide** _IDE_
> 要使用的 IDE（vscode、openvscode、cursor 等）。

**list**
> 列出所有工作区。

**ssh** _WORKSPACE_
> 通过 SSH 进入工作区。

**stop** _WORKSPACE_
> 停止运行中的工作区。

**delete** _WORKSPACE_
> 删除工作区。

**--help**
> 显示帮助信息。

# DESCRIPTION

**DevPod** 是一款开源工具，基于 devcontainer.json 规范创建可复现的开发环境。它通过支持 Docker、Kubernetes、云虚拟机等多种 provider 来抽象底层基础设施。

DevPod 工作区可以从 git 仓库、本地目录或容器镜像创建。该工具会自动配置基础设施、构建 dev container 并连接你的 IDE。它支持 VS Code、JetBrains IDE 以及 SSH 访问。

其 provider 架构允许同一开发环境既可以在本地用 Docker 运行，也可以在云端基础设施上远程运行，无论环境在哪里都保持一致。

# CONFIGURATION

**.devcontainer/devcontainer.json**
> 定义开发环境的 Dev container 配置。

**~/.devpod/provider/**
> 不同基础设施后端的 provider 配置。

# CAVEATS

需要为目标基础设施配置好 provider。云端 provider 会产生费用。大型 dev container 初始搭建可能较慢。某些功能需要特定的 IDE 集成。

# HISTORY

DevPod 由 **Loft Labs** 创建并于 **2023 年**发布。它的定位是云开发环境中立的开源替代方案，并支持 devcontainer 规范。

# INSTALL

```nix: nix profile install nixpkgs#devpod```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[devcontainer](/man/devcontainer)(1), [docker](/man/docker)(1), [code](/man/code)(1)

# RESOURCES

```[Source code](https://github.com/loft-sh/devpod)```

```[Homepage](https://devpod.sh)```

```[Documentation](https://devpod.sh/docs)```

<!-- verified: 2026-07-11 -->
