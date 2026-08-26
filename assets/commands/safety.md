# TAGLINE

检查 Python 依赖中的已知漏洞

# TLDR

**扫描当前项目**中存在漏洞的依赖

```safety scan```

**检查 requirements 文件**中的已知漏洞

```safety check -r [requirements.txt]```

**扫描并以 JSON 格式输出结果**

```safety scan --output json```

**生成 SBOM**（软件物料清单）

```safety scan --output sbom```

**检查当前环境中已安装的软件包**

```safety check```

**显示详细的漏洞信息**

```safety check -r [requirements.txt] --full-report```

# SYNOPSIS

**safety** [_command_] [_options_]

# PARAMETERS

**scan**
> 扫描 Python 项目中的依赖漏洞和恶意软件包

**check**
> 检查 Python 依赖中的已知安全漏洞

**-r**, **--requirements** _FILE_
> 要检查的 requirements 文件路径

**--output** _FORMAT_
> 输出格式：text、json、sbom 或 html

**--full-report**
> 显示包含修复建议的完整漏洞报告

**--key** _API_KEY_
> 使用 Safety API 密钥以访问完整漏洞数据库

**--help**
> 显示帮助信息

# DESCRIPTION

**Safety** 是一款 Python 依赖漏洞扫描器，它对照 Safety DB（已知安全漏洞数据库）检查软件包。它能在开发环境、CI/CD 流水线和生产系统中识别存在漏洞或恶意的软件包。

该工具可扫描 requirements 文件、项目目录或整个 Python 环境。它提供带 CVE 编号的详细漏洞信息，并建议用于修复的安全软件包版本。

Safety 支持多种输出格式，包括纯文本、JSON、HTML 和 SBOM（软件物料清单），便于集成到安全工作流与合规要求中。

# CAVEATS

免费版本使用的漏洞数据库每月更新一次。完整数据库的漏洞数量是免费版的 3 倍，需要付费订阅。Safety CLI 3 要求 Python 3.9 或更高版本；较旧的 Python 版本必须使用 Docker 镜像。

# HISTORY

Safety 由 **PyUp.io** 开发，是一款旨在提升 Python 软件供应链安全的开源工具。该项目维护着 Safety DB——最全面的 Python 漏洞数据库之一。3.0 版本引入了扩展的扫描能力和 SBOM 支持。

# INSTALL

```brew: brew install safety```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pipenv](/man/pipenv)(1)
