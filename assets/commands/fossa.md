# TAGLINE

依赖许可证与安全扫描器

# TLDR

**分析依赖项**

```fossa analyze```

**检测许可证问题**

```fossa test```

**为项目生成报告**

```fossa report attribution```

**初始化配置**

```fossa init```

**列出已分析的项目**

```fossa list-targets```

# SYNOPSIS

**fossa** _command_ [_options_]

# SUBCOMMANDS

**analyze**
> 分析项目依赖项。

**test**
> 检查许可证问题。

**report**
> 生成报告。

**init**
> 初始化配置。

**list-targets**
> 列出分析目标。

# PARAMETERS

**--project** _name_
> 项目名称。

**--revision** _rev_
> 项目修订版本。

**--config** _file_
> 配置文件路径。

# CONFIGURATION

**.fossa.yml**
> 项目配置，涵盖分析目标、依赖项和策略。

# DESCRIPTION

**fossa** 是一个依赖分析工具，扫描项目的许可证合规性和安全漏洞。它支持多种语言和包管理器，自动检测依赖项并根据组织策略分析它们的许可证。

该工具集成到 CI/CD 流水线中以强制执行许可证策略，阻止存在合规问题的构建。它生成用于开源合规的署名报告，并跟踪依赖项中的安全漏洞。

Fossa 维护着许可证元数据和漏洞信息数据库，提供关于项目依赖项的详细报告。它可以跨复杂构建系统检测直接与传递依赖。

# CAVEATS

需要 API 密钥并与 Fossa 服务在线连接。分析准确性取决于正确的构建配置。部分包管理器可能需要手动配置。

# HISTORY

**Fossa** 创建于 **2015** 年，旨在应对现代软件开发中的许可证合规挑战。该平台逐步支持多种语言，成为开源许可证管理的标准工具。

# SEE ALSO

[snyk](/man/snyk)(1), [npm-audit](/man/npm-audit)(1)

# RESOURCES

```[Source code](https://github.com/fossas/fossa-cli)```

```[Documentation](https://docs.fossa.com/)```

<!-- verified: 2026-07-15 -->
