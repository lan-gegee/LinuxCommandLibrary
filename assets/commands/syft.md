# TAGLINE

从镜像生成软件物料清单

# TLDR

**为容器镜像生成 SBOM**

```syft [alpine:latest]```

**以 JSON 格式生成 SBOM**

```syft [alpine:latest] -o json```

**生成 CycloneDX 格式的 SBOM**

```syft [alpine:latest] -o cyclonedx-json```

**生成 SPDX 格式的 SBOM**

```syft [alpine:latest] -o spdx-json```

**扫描本地目录**

```syft dir:[/path/to/project]```

**扫描 Docker 归档**

```syft docker-archive:[image.tar]```

**输出多种格式**

```syft [image] -o spdx-json=[sbom.spdx.json] -o cyclonedx-json=[sbom.cdx.json]```

# SYNOPSIS

**syft** [_source_] [_options_]

**syft** _command_ [_options_]

# PARAMETERS

**-o**, **--output** _format_
> 输出格式：syft-table、syft-json、cyclonedx-json、cyclonedx-xml、spdx-json、spdx-tag-value、github-json。

**-s**, **--scope** _scope_
> 层选择方式：squashed（默认）、all-layers、deep-squashed。

**--platform** _platform_
> 容器镜像的平台（例如 linux/arm64）。

**--source-name** _name_
> 设置被分析目标的名称。

**--source-version** _version_
> 设置被分析目标的版本。

**--file** _path_
> 将输出写入文件而非标准输出。

**--from** _source_
> 显式指定来源类型（例如 docker、registry、dir）。

**-t**, **--template** _file_
> 用于自定义输出的 Go 模板文件路径。

**-q**, **--quiet**
> 抑制所有日志输出。

**-v**, **--verbose**
> 提高详细程度（-v = info，-vv = debug）。

**--select-catalogers** _list_
> 添加、移除和过滤 cataloger。

**--exclude** _glob_
> 从扫描中排除路径（可重复使用）。

**-c**, **--config** _file_
> 配置文件路径。

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# SOURCE TYPES

**docker:**_image_ - 使用 Docker 守护进程

**podman:**_image_ - 使用 Podman 守护进程

**registry:**_image_ - 直接从 registry 拉取

**docker-archive:**_file_ - Docker save 生成的 tar 包

**oci-archive:**_file_ - OCI 归档 tar 包

**oci-dir:**_path_ - OCI layout 目录

**dir:**_path_ - 文件系统目录

**file:**_path_ - 单个文件

# DESCRIPTION

**syft** 是一个从容器镜像和文件系统生成软件物料清单（SBOM）的 CLI 工具。它能识别多个生态系统中的软件包、库和依赖。

支持的生态系统包括容器镜像（Docker、OCI、Podman、Singularity）、编程语言（Java、Python、JavaScript、Ruby、Go、Rust、.NET）以及 Linux 发行版（Alpine、Debian、RHEL 等）。

输出格式包括满足合规要求所需的行业标准 CycloneDX 和 SPDX，以及用于与 Anchore 工具集成的原生格式。生成的 SBOM 可供 Grype 等漏洞扫描器使用。

# CAVEATS

准确性取决于镜像中软件包元数据的质量。某些动态链接或内嵌（vendored）的依赖可能无法检测到。大型镜像的扫描需要较长时间。私有镜像可能需要 registry 身份验证。

# HISTORY

**syft** 由 Anchore 创建，是一款开源 SBOM 生成工具。它应对的是日益增长的供应链安全要求和软件透明度法规。该工具支持多种 SBOM 标准，以满足不同行业的合规需求。

# INSTALL

```pacman: sudo pacman -S syft```

```apk: sudo apk add syft```

```zypper: sudo zypper install syft```

```brew: brew install syft```

```nix: nix profile install nixpkgs#syft```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grype](/man/grype)(1), [docker](/man/docker)(1), [trivy](/man/trivy)(1), [cosign](/man/cosign)(1)
