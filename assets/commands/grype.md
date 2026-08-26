# TAGLINE

容器镜像和文件系统的漏洞扫描器

# TLDR

**扫描容器镜像**

```grype [image:tag]```

**扫描目录**

```grype dir:[path]```

**扫描 SBOM 文件**

```grype sbom:[sbom.json]```

**以 JSON 输出**

```grype [image] -o json```

**发现高危或严重漏洞时使 CI 失败**

```grype [image] --fail-on high```

**只显示有可用修复的漏洞**

```grype [image] --only-fixed```

**扫描并排除特定路径**

```grype dir:[path] --exclude "[glob_pattern]"```

# SYNOPSIS

**grype** [_options_] _source_

# PARAMETERS

**-o**, **--output** _format_
> 报告格式（table、json、cyclonedx、cyclonedx-json、sarif、template）。

**-f**, **--fail-on** _severity_
> 若发现达到或超过指定级别的漏洞则返回退出码 2（negligible、low、medium、high、critical）。

**--only-fixed**
> 只显示有可用修复的漏洞。

**--only-notfixed**
> 只显示没有可用修复的漏洞。

**--by-cve**
> 按 CVE 而不是原始漏洞 ID 组织结果。

**--add-cpes-if-none**
> 为缺少 CPE 的软件包生成 CPE。

**-s**, **--scope** _scope_
> 层分析范围（squashed、all-layers）。

**--exclude** _glob_
> 排除匹配给定 glob 模式的路径。

**--platform** _platform_
> 容器平台说明符（例如 linux/arm64）。

**-q**, **--quiet**
> 抑制日志输出。

**-v**, **--verbose**
> 提高详细程度（-v 为 info，-vv 为 debug）。

**-c**, **--config** _file_
> 指定配置文件。

**--file** _path_
> 将报告输出写入文件而不是 stdout。

**--vex** _document_
> 应用 VEX 文档过滤结果。

# DESCRIPTION

**grype** 是一款面向容器镜像和文件系统的漏洞扫描器。它通过比对漏洞数据库来识别软件包和依赖中的已知安全漏洞。

该工具可与 CI/CD 流水线集成，并以多种格式生成报告。它与 Syft 使用相同的源，可实现全面的软件组成分析。

# SOURCE TYPES

**image**: 容器镜像（默认）
**dir:**: 本地目录
**file:**: 单个文件
**sbom:**: SBOM 文件（Syft、CycloneDX、SPDX）
**registry:**: 远程容器仓库

# CAVEATS

需要定期更新数据库。可能出现误报。覆盖范围取决于生态系统。大型镜像扫描较慢。

# HISTORY

**grype** 由 **Anchore** 创建，是其开源安全工具链中与 Syft 并列的组成部分。它出现于 **2020 年**前后，旨在满足容器安全扫描需求，重点关注准确性和集成能力。

# INSTALL

```dnf: sudo dnf install grype```

```apk: sudo apk add grype```

```zypper: sudo zypper install grype```

```brew: brew install grype```

```nix: nix profile install nixpkgs#grype```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[syft](/man/syft)(1), [trivy](/man/trivy)(1), [snyk](/man/snyk)(1)
