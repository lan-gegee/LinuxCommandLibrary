# TAGLINE

Web 侦察与 OSINT 框架

# TLDR

**启动 recon-ng** 交互式控制台

```recon-ng```

**创建或加载工作区**

```recon-ng -w [workspace_name]```

**列出可用模块**

```marketplace search```

**安装模块**

```marketplace install [module_name]```

**加载模块**

```modules load [module_name]```

**显示模块选项**

```options list```

**运行已加载的模块**

```run```

# SYNOPSIS

**recon-ng** [**-w** _workspace_] [**-r** _resource_] [_options_]

# PARAMETERS

**-w** _workspace_
> 创建或加载指定的工作区

**-r** _resource_
> 执行资源文件（自动化脚本）

**--no-analytics**
> 禁用匿名使用情况跟踪

**--no-version**
> 禁用启动时的版本检查

**--no-marketplace**
> 禁用对远程市场（marketplace）的访问

**--stealth**
> 禁用框架自身发起的所有被动网络请求

**--accessible**
> 在可用时使用无障碍输出

**-h**, **--help**
> 显示帮助信息

# CONSOLE COMMANDS

**workspaces list**
> 列出可用的工作区

**workspaces create** _name_
> 创建新工作区

**marketplace search** [_term_]
> 在市场中搜索可用模块

**marketplace install** _module_
> 从市场安装模块

**modules load** _module_
> 加载已安装的模块

**options set** _option_ _value_
> 设置模块选项

**options list**
> 显示当前模块选项

**run**
> 执行已加载的模块

**show** _table_
> 显示数据库表中的数据（hosts、contacts、domains 等）

**keys add** _name_ _value_
> 为外部服务添加 API 密钥

**keys list**
> 列出已配置的 API 密钥

# DESCRIPTION

**recon-ng** 是一个用于收集开源情报（OSINT）的模块化侦察框架。它采用类似 Metasploit 的界面设计，为安全专业人员在评估的信息收集阶段提供熟悉的工作流程。

该框架使用工作区来组织侦察项目，每个工作区维护自己收集到的数据数据库（域名、主机、联系人、凭据等）。模块可以查询这些数据并添加新的发现，从而构建完整的情报档案。

模块涵盖多种侦察类别：discovery（子域枚举、端口扫描）、recon（WHOIS、DNS 记录、社交媒体）、import（数据导入）和 reporting（HTML、JSON、Excel 导出）。许多模块需要 API 密钥才能集成外部 API（Shodan、VirusTotal、HaveIBeenPwned）。

# CONFIGURATION

**~/.recon-ng/workspaces/**
> 工作区目录，包含每个项目独立的 SQLite 数据库，存放收集到的主机、联系人、域名和凭据。

**keys add** _name_ _value_
> 外部服务（Shodan、VirusTotal、HaveIBeenPwned 等）的 API 密钥，存储在工作区数据库中，许多模块都需要用到。

# CAVEATS

**需要授权**：只能对你有权评估的目标执行侦察。未经授权的侦察可能违反法律和服务条款。

许多功能强大的模块需要外部服务的 API 密钥。使用这些模块前请先用 **keys add** 配置密钥。某些服务有速率限制或需要付费订阅。

安装基础集之外的模块必须访问市场。执行市场相关操作请确保网络连接正常。

模块结果的准确性参差不齐。请交叉比对多个来源的发现，并手动验证关键信息。

# HISTORY

Recon-ng 由当时任职于 Black Hills Information Security 的 **Tim Tomes** 开发，首次发布于约 **2012 年**，旨在将 Metasploit 的模块化、数据库驱动方法引入侦察阶段。该框架用 Python 编写，在社区贡献模块的支持下持续活跃开发。

# INSTALL

```apk: sudo apk add recon-ng```

```brew: brew install recon-ng```

```nix: nix profile install nixpkgs#recon-ng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[maltego](/man/maltego)(1), [amass](/man/amass)(1), [nmap](/man/nmap)(1)
