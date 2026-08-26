# TAGLINE

构建自定义不可变 Linux 镜像

# TLDR

**从配方文件构建自定义镜像**

```bluebuild build [recipe.yml]```

**构建并推送**到容器仓库（registry）

```bluebuild build --push [recipe.yml]```

**从配方生成 Containerfile**

```bluebuild generate [recipe.yml]```

在新目录中**创建新的 BlueBuild 项目**

```bluebuild new [project-name]```

在当前的空目录中**初始化 BlueBuild 项目**

```bluebuild init```

**校验配方文件**是否有错误

```bluebuild validate [recipe.yml]```

**本地构建并将运行中的系统 rebase 到该镜像**

```bluebuild switch [recipe.yml]```

**将运行中的系统升级**到最新的 BlueBuild 镜像

```bluebuild upgrade```

# SYNOPSIS

**bluebuild** [_command_] [_options_] [_recipe_]

# PARAMETERS

**build** _recipe_
> 生成模板文件并使用 Docker、Podman 或 Buildah 构建镜像。

**generate** _recipe_
> 生成用于构建配方的 Containerfile，并打印或写出。

**new** _name_
> 基于官方模板在新目录中创建新的 BlueBuild 项目。

**init**
> 在当前空目录中搭建新的 BlueBuild 项目。

**validate** _recipe_
> 在构建前检查配方及其模块是否有错误。

**switch** _recipe_
> 在本地构建镜像，将其导出为 oci-archive tar 包，然后将运行中的系统 rebase 或 upgrade 到它。以普通用户身份运行，仅在需要时请求 sudo。

**rebase** _recipe_
> 本地构建并将当前 rpm-ostree 系统 rebase 到生成的镜像。

**upgrade** _recipe_
> 本地构建并将当前 rpm-ostree 系统升级到生成的镜像。

**generate-iso** _recipe_
> 从配方生成离线的 ISO 安装镜像。

**completions** _shell_
> 将 bash、zsh、fish 等 shell 的补全脚本打印到标准输出。

**upgrade**（不带配方）
> 将 bluebuild CLI 自身升级到最新版本。

**--push**
> 将构建好的镜像推送到已配置的容器仓库（build 命令）。

**--registry** _url_
> 覆盖要推送到的容器仓库（build 命令）。

**--rechunk**
> 对镜像层重新分块（rechunk），使更新更高效（build 命令）。

**-v**, **--verbose**
> 启用详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**BlueBuild** 是一款基于 Universal Blue 和 Fedora Atomic 创建自定义不可变 Linux 镜像的工具。它使用 YAML 配方文件以声明式方式定义镜像定制内容，包括软件包、脚本和系统配置。

该工具简化了构建自定义 rpm-ostree 镜像的过程，这些镜像可部署在 Fedora Silverblue、Kinoite 或其他 Fedora atomic 变体上。配方可以指定基础镜像、添加/移除软件包、包含自定义脚本以及配置系统设置。

BlueBuild 通过一个可复用的 GitHub Action 与 GitHub Actions 集成实现自动化 CI/CD 构建；**generate** 命令产出构建所用的 Containerfile。镜像通常托管在 GitHub Container Registry（ghcr.io）上。

用户可以使用 **bluebuild switch** 将现有的 Fedora Atomic 系统切换到本地构建的镜像，或通过 **rebase** 和 **upgrade** 切换到已发布的镜像。该项目提供了一个可复用模块库，覆盖常见定制需求，如添加 Flatpak 仓库、配置字体或安装开发工具。

# CAVEATS

本地构建需要 Podman 或 Docker。GitHub Actions 集成需要仓库写权限和容器仓库凭证。配方更改可能需要完整重建镜像。由于架构或环境差异，本地构建的镜像可能与 CI 构建的镜像不同。

# HISTORY

**BlueBuild** 于 **2023 年**从 Universal Blue 社区中兴起，旨在简化 Fedora Atomic 桌面的自定义镜像创建。它的诞生源于人们对不可变 Linux 发行版日益增长的兴趣以及对易用定制工具的需求。该项目在原始的 Containerfile/Dockerfile 构建之上提供了更高层次的抽象。

# SEE ALSO

[podman](/man/podman)(1), [rpm-ostree](/man/rpm-ostree)(1), [docker](/man/docker)(1), [buildah](/man/buildah)(1)

# RESOURCES

```[Source code](https://github.com/blue-build/cli)```

```[Homepage](https://blue-build.org/)```

```[Documentation](https://blue-build.org/how-to/setup/)```

<!-- verified: 2026-06-19 -->
