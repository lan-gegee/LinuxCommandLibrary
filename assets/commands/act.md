# TAGLINE

本地 GitHub Actions 运行器

# TLDR

**运行**默认工作流

```act```

**列出**所有可用的工作流

```act -l```

运行**特定的工作流**

```act -W [.github/workflows/ci.yml]```

运行**特定的作业**

```act -j [build]```

从文件加载**机密（secrets）**运行

```act --secret-file [.secrets]```

**试运行**，查看将执行的内容

```act -n```

以指定的**平台镜像**运行

```act -P ubuntu-latest=catthehacker/ubuntu:act-latest```

# SYNOPSIS

**act** [_-W workflow_] [_-j job_] [_-e event_] [_--secret-file file_] [_options_]

# DESCRIPTION

**act** 允许你使用 Docker 容器在本地运行 GitHub Actions 工作流。它解析工作流 YAML 文件，并在模拟 GitHub Actions 环境的容器中执行作业，无需推送到 GitHub 即可快速迭代和调试。

该工具支持大部分 GitHub Actions 功能，包括矩阵构建、机密、环境变量和制品。它会自动下载并缓存 action 仓库。

# PARAMETERS

**-W** _file_, **--workflows** _file_
> 工作流文件的路径（默认：.github/workflows/）

**-j** _job_, **--job** _job_
> 运行特定的作业

**-e** _file_, **--eventpath** _file_
> 事件 JSON 文件的路径

**--secret-file** _file_
> 从文件加载机密（KEY=VALUE 格式）

**-s** _secret_, **--secret** _secret_
> 设置一个机密（KEY=VALUE）

**--env-file** _file_
> 从文件加载环境变量

**-P** _platform_, **--platform** _platform_
> 为平台指定自定义 Docker 镜像（如 ubuntu-latest=catthehacker/ubuntu:act-latest）

**--input** _input_
> 设置一个工作流输入（KEY=VALUE）

**--input-file** _file_
> 从文件加载工作流输入

**--matrix** _matrix_
> 选择要运行的特定矩阵配置

**--action-offline-mode**
> 若已缓存则不拉取镜像或获取远程 action

**-l**, **--list**
> 列出可用的工作流和作业

**-n**, **--dryrun**
> 显示将要运行的内容但不实际执行

**-r**, **--reuse**
> 在多次运行之间复用容器

**-b**, **--bind**
> 以绑定方式挂载工作目录而非复制

**--container-architecture** _arch_
> 容器体系结构（amd64、arm64）

# CONFIGURATION

**~/.actrc**
> 用户级默认标志，应用于每次 act 调用。每行包含一个命令行标志（如 `-P ubuntu-latest=catthehacker/ubuntu:act-latest`）。

**.actrc**
> 项目级默认配置，格式与用户级文件相同。存在时覆盖用户级设置。

# CAVEATS

并非所有 GitHub Actions 功能都受支持；服务容器等托管运行器功能存在局限。大型工作流镜像初次下载可能很慢。某些 action 在本地的行为可能与在 GitHub 上不同。Docker 必须处于运行状态。

# HISTORY

**act** 由 Casey Lee（nektos）创建，首次发布于 **2019** 年。它旨在通过支持本地执行来改善 GitHub Actions 反馈周期缓慢的问题。该项目很快在 CI/CD 社区中流行起来。

# INSTALL

```dnf: sudo dnf install act```

```pacman: sudo pacman -S act```

```apk: sudo apk add act```

```zypper: sudo zypper install act```

```brew: brew install act```

```nix: nix profile install nixpkgs#act```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[docker](/man/docker)(1), [gh](/man/gh)(1), [make](/man/make)(1)
