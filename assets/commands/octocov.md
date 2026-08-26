# TAGLINE

收集代码覆盖率和各项指标的工具包

# TLDR

**使用当前目录中的配置运行 octocov**

```octocov```

**生成覆盖率徽章**

```octocov badge```

**比较两份覆盖率报告**

```octocov diff [report_a] [report_b]```

**查看特定文件的文件级覆盖率**

```octocov view [file]```

**列出覆盖率报告中跟踪的所有文件**

```octocov ls-files```

**生成默认配置文件**

```octocov init```

# SYNOPSIS

**octocov** [_command_] [_options_]

# PARAMETERS

**init**
> 在当前目录生成默认的 `.octocov.yml` 配置文件。

**ls-files**
> 列出覆盖率报告中记录的所有源文件。

**view**, **cat**
> 显示给定源文件的文件级覆盖率详情。

**diff** [_report_a_] [_report_b_]
> 比较两份覆盖率报告并显示差异。

**badge**
> 基于当前报告生成覆盖率徽章图片。

# DESCRIPTION

**octocov** 是一个收集代码指标的工具包，涵盖代码覆盖率、代码与测试比以及测试执行时间。它既可以作为本地 CLI 工具使用，也可以作为集成 GitHub Actions 的 CI 工具使用。

其特性包括支持多种覆盖率报告格式（Go、Ruby、Python、Clover、LCOV 等）、徽章生成、拉取请求评论，以及将报告存储到 GitHub、S3 或 BigQuery。它可以聚合来自多个仓库的报告，实现集中监控。配置在 `.octocov.yml` 中定义。

# CAVEATS

覆盖率报告格式的支持情况取决于所用的语言和测试框架。拉取请求评论等 CI 功能需要在 GitHub Actions 中进行配置。

# HISTORY

**octocov** 由 **k1LoW** 创建，使用 **Go** 编写。可通过 GitHub Action `k1LoW/octocov-action` 使用。

# SEE ALSO

[go-test](/man/go-test)(1)
