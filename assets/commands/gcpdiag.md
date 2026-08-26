# TAGLINE

Google Cloud Platform 诊断工具

# TLDR

**运行 lint 检查**

```gcpdiag lint --project [project_id]```

**使用特定规则运行**

```gcpdiag lint --project [project_id] --include [gke/ERR/2021_001]```

**排除某些规则运行**

```gcpdiag lint --project [project_id] --exclude [gke/*]```

**以 JSON 格式输出**

```gcpdiag lint --project [project_id] --output json```

**启用详细输出**

```gcpdiag lint --project [project_id] --verbose```

# SYNOPSIS

**gcpdiag** **lint** [_options_]

# SUBCOMMANDS

**lint**
> 运行诊断检查。

# PARAMETERS

**--project** _id_
> Google Cloud 项目 ID。

**--include** _pattern_
> 包含匹配模式的规则。

**--exclude** _pattern_
> 排除匹配模式的规则。

**--output** _format_
> 输出格式（text、json）。

**--verbose**
> 详细输出。

**--auth-adc**
> 使用 Application Default Credentials。

# DESCRIPTION

**gcpdiag** 是一款 Google Cloud Platform 命令行诊断工具，可对项目运行自动化检查以发现常见问题。它分析基础设施中的配置错误、配额问题、权限错误和违反最佳实践的情况。

该工具执行一组按服务（GKE、Compute Engine、Cloud SQL 等）组织的精选规则。每条规则都基于 Google 内部的故障排查经验来检查特定的已知问题。结果会标明检查是通过、失败还是跳过，并附有详细说明和修复建议。

gcpdiag 通过在问题引发故障之前主动发现它们来缩短故障排查时间。它特别适合验证新部署和调查生产环境问题。

# SEE ALSO

[gcloud](/man/gcloud)(1)

# RESOURCES

```[Source code](https://github.com/GoogleCloudPlatform/gcpdiag)```

```[Homepage](https://gcpdiag.dev/)```

<!-- verified: 2026-07-15 -->
