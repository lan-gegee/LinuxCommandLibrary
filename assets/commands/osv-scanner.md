# TAGLINE

使用 OSV 数据库扫描依赖中的已知漏洞

# TLDR

**递归扫描目录**

```osv-scanner scan -r [directory]```

**扫描指定的锁文件**

```osv-scanner scan --lockfile [package-lock.json]```

**扫描 SBOM 文件**

```osv-scanner scan --sbom [sbom.json]```

**以 JSON 格式输出结果**

```osv-scanner scan -r [directory] --format json```

**扫描 Docker 镜像**

```osv-scanner scan --docker [image:tag]```

**扫描并生成引导式修复报告**

```osv-scanner fix -r [directory]```

# SYNOPSIS

**osv-scanner** _command_ [_options_] [_targets_]

# PARAMETERS

**scan**
> 扫描依赖中的漏洞。

**fix**
> 生成引导式修复建议。

**-r**, **--recursive** _DIR_
> 递归扫描目录中的锁文件和清单文件。

**--lockfile** _FILE_
> 扫描指定的锁文件（自动检测生态系统）。

**--sbom** _FILE_
> 扫描 SBOM 文件（支持 SPDX 和 CycloneDX）。

**--docker** _IMAGE_
> 扫描 Docker 镜像中的漏洞。

**--format** _FORMAT_
> 输出格式：table（默认）、json、markdown、sarif。

**--config** _FILE_
> osv-scanner.toml 配置文件的路径。

**--call-analysis**
> 启用调用图分析，过滤不可达的漏洞（Go、Rust）。

**--no-ignore**
> 不遵循配置文件中的 ignore 条目。

**--verbosity** _LEVEL_
> 设置日志详细级别：error、warn、info、verbose。

**--help**
> 显示帮助信息。

# DESCRIPTION

**osv-scanner** 通过查询 **OSV.dev** 数据库来扫描项目依赖中的已知漏洞。该数据库聚合了来自 GitHub Advisory Database、PyPI、RubyGems 和 crates.io 等多个来源的漏洞数据。

该工具能自动检测并解析大多数主流软件包生态系统的锁文件，包括 npm、pip、Go modules、Cargo、Maven、NuGet 等。它还可以扫描 SPDX 或 CycloneDX 格式的 SBOM 文件以及 Docker 容器镜像。

**fix** 子命令提供引导式修复，在尽量减少破坏性变更的前提下建议可解决所检测到漏洞的版本升级。

调用图分析（支持 Go 和 Rust）可以判断存在漏洞的代码路径是否真的会被项目触达，从而减少误报。

# CAVEATS

需要网络访问以查询 OSV.dev 数据库。漏洞覆盖范围取决于各生态系统向 OSV 提交的数据。调用图分析仅适用于 Go 和 Rust 项目。

# HISTORY

osv-scanner 由 **Google** 于 **2022 年 12 月**发布，作为 OSV.dev 漏洞数据库的前端。其设计目标是为依赖扫描提供一个免费的开源替代方案。用于引导式修复的 **fix** 子命令于 2024 年加入。

# INSTALL

```pacman: sudo pacman -S osv-scanner```

```apk: sudo apk add osv-scanner```

```zypper: sudo zypper install osv-scanner```

```brew: brew install osv-scanner```

```nix: nix profile install nixpkgs#osv-scanner```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm-audit](/man/npm-audit)(1), [trivy](/man/trivy)(1), [grype](/man/grype)(1), [snyk](/man/snyk)(1)
