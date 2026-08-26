# TAGLINE

功能全面的安全漏洞扫描器

# TLDR

扫描容器镜像中的漏洞

```trivy image [image_name:tag]```

扫描本地文件系统

```trivy fs [path/to/directory]```

扫描 git 仓库

```trivy repo [https://github.com/user/repo]```

扫描配置文件（Terraform、Kubernetes 等）

```trivy config [path/to/configs]```

以 JSON 格式输出结果

```trivy image --format json [image_name]```

仅显示严重和高危漏洞

```trivy image --severity CRITICAL,HIGH [image_name]```

忽略暂无修复方案的漏洞

```trivy image --ignore-unfixed [image_name]```

扫描并生成 SBOM

```trivy image --format cyclonedx [image_name]```

# SYNOPSIS

**trivy** [_global options_] _command_ [_command options_] _target_

# PARAMETERS

**image**, **i**
> 扫描容器镜像中的漏洞。

**filesystem**, **fs**
> 扫描本地文件系统或目录。

**repository**, **repo**
> 扫描远程 git 仓库。

**config**, **conf**
> 扫描配置文件中的错误配置。

**kubernetes**, **k8s**
> 扫描 Kubernetes 集群。

**rootfs**
> 扫描根文件系统（例如解压后的容器镜像）。

**sbom**
> 扫描 SBOM 文件中的漏洞。

**server**, **s**
> 以服务器模式运行 Trivy。

**plugin**, **p**
> 管理 Trivy 插件。

**--severity** _levels_
> 要显示的严重级别列表，逗号分隔：**UNKNOWN**、**LOW**、**MEDIUM**、**HIGH**、**CRITICAL**。

**--format** _format_
> 输出格式：**table**、**json**、**sarif**、**template**、**cyclonedx**、**spdx**、**spdx-json**、**github**。

**--output** _file_
> 将结果写入文件。

**--ignore-unfixed**
> 只显示有修复方案可用的漏洞。

**--pkg-types** _types_
> 要扫描的软件包类型列表，逗号分隔。

**--scanners** _scanners_
> 要启用的扫描器列表，逗号分隔：**vuln**、**misconfig**、**secret**、**license**。

**--cache-dir** _dir_
> 指定数据库的缓存目录。

**-q**, **--quiet**
> 屏蔽进度条和日志输出。

**-d**, **--debug**
> 启用调试模式。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**Trivy** 是由 Aqua Security 开发的全面安全扫描器。它能够检测操作系统软件包和应用依赖中的漏洞、基础设施错误配置、暴露的机密信息以及软件许可证问题。

Trivy 支持多种扫描目标，包括容器镜像、文件系统、git 仓库、虚拟机镜像和 Kubernetes 集群。它可与 CI/CD 流水线集成，并能以多种格式输出结果以适配不同的工具与平台。

漏洞数据库会自动下载并缓存。Trivy 可以生成 CycloneDX 和 SPDX 格式的软件物料清单 (SBOM)，也可以扫描现有的 SBOM 文件以查找已知漏洞。

# CAVEATS

首次运行时下载漏洞数据库需要联网。对于隔离网络环境，可以预先下载数据库并通过 **--cache-dir** 指定，或托管在私有 OCI 仓库中。扫描容器镜像需要可用的容器运行时或对镜像仓库的访问权限。

# HISTORY

Trivy 由 **Teppei Fukuda** 创建，于 **2019 年**首次发布，当时是一个容器漏洞扫描器。它于 **2019 年**被 **Aqua Security** 收购，此后逐步扩展为全面的安全扫描器。**2023 年**，**tfsec**（Terraform 安全扫描器）被合并进 Trivy，整合了 Aqua 的开源安全工具。如今 Trivy 已成为使用最广泛的开源漏洞扫描器之一。

# INSTALL

```dnf: sudo dnf install trivy```

```pacman: sudo pacman -S trivy```

```zypper: sudo zypper install trivy```

```brew: brew install trivy```

```nix: nix profile install nixpkgs#trivy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [tfsec](/man/tfsec)(1), [grype](/man/grype)(1), [syft](/man/syft)(1), [snyk](/man/snyk)(1)
