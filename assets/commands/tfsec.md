# TAGLINE

Terraform 静态安全扫描器

# TLDR

**扫描当前目录**中的安全问题

```tfsec```

**扫描指定目录**

```tfsec [path/to/terraform]```

**以 JSON 格式输出结果**

```tfsec --format json```

在扫描中**排除特定检查项**

```tfsec -e [check1,check2]```

**使用指定的 tfvars 文件**进行扫描

```tfsec --tfvars-file [terraform.tfvars]```

**仅显示高严重级别问题**

```tfsec --minimum-severity HIGH```

**将结果保存到文件**

```tfsec --format json --out [results.json]```

在扫描中**排除目录**

```tfsec --exclude-path [path/to/exclude]```

# SYNOPSIS

**tfsec** [_options_] [_directory_]

# PARAMETERS

**--format** _format_
> 输出格式：**default**、**json**、**csv**、**checkstyle**、**sarif**、**junit**、**gif** 或 **text**。

**--out** _file_
> 将结果写入文件而不是 stdout。

**-e**, **--exclude** _checks_
> 以逗号分隔的检查 ID 列表，将从扫描中排除。

**--exclude-path** _path_
> 从扫描中排除特定目录。

**--minimum-severity** _level_
> 按最低严重级别过滤结果：**LOW**、**MEDIUM**、**HIGH** 或 **CRITICAL**。

**--tfvars-file** _file_
> 在扫描中纳入 tfvars 文件里的变量值。

**--config-file** _file_
> 使用自定义配置文件（默认：tfsec-config.json）。

**--no-colour**, **--no-color**
> 禁用彩色输出（CI 流水线中很实用）。

**--soft-fail**
> 即使发现问题也以退出码 0 退出。

**--include-ignored**
> 包含已被标记为忽略的结果。

**--include-passed**
> 在输出中包含通过的检查项。

**--version**
> 显示版本信息并退出。

**-h**, **--help**
> 显示帮助消息并退出。

# DESCRIPTION

**tfsec** 是一款针对 Terraform 代码的静态分析安全扫描器。它在基础设施部署之前分析 Terraform 文件，检测潜在的安全错误配置、策略违规和最佳实践问题。

该扫描器可在本地和 CI/CD 流水线中运行，提供对开发者友好的输出以及附带文档说明的检查项。它支持多种输出格式以便与各类工具和平台集成。问题按严重级别分类，帮助排定修复工作的优先级。

tfsec 可通过命令行标志、配置文件或环境变量（以 **TFSEC_** 为前缀）进行配置。还可以使用行内注释来忽略 Terraform 文件中的特定警告。

# CAVEATS

tfsec 正在被弃用并合并到 **Trivy** 中。新项目请考虑改用 **trivy config**。现有 tfsec 用户应计划迁移到 Trivy，以获得持续的更新和支持。

# HISTORY

tfsec 由 **Liam Galvin** 创建，于 **2019** 年作为开源 Terraform 安全扫描器发布。它于 **2021** 年被 **Aqua Security** 收购，成为其开源安全工具组合的一部分。**2023** 年，Aqua 宣布 tfsec 将并入其全面的安全扫描器 **Trivy**，tfsec 进入维护模式。

# INSTALL

```brew: brew install tfsec```

```nix: nix profile install nixpkgs#tfsec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trivy](/man/trivy)(1), [terraform](/man/terraform)(1), [checkov](/man/checkov)(1), [terrascan](/man/terrascan)(1)
