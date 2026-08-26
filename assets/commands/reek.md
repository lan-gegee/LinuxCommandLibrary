# TAGLINE

检测 Ruby 源文件中的代码异味

# TLDR

**检查 Ruby 代码中的异味**

```reek [file.rb]```

**检查整个项目**

```reek```

**以指定格式检查**

```reek --format [yaml] [file.rb]```

**显示可用的异味类型**

```reek --smell-types```

**排除特定异味**

```reek --except [TooManyStatements] [file.rb]```

# SYNOPSIS

**reek** [_options_] [_files_...]

# PARAMETERS

**-f**, **--format** _format_
> 输出格式（text、yaml、json、html）。

**--smell-types**
> 列出可用的异味。

**--except** _smells_
> 排除异味。

**--only** _smells_
> 只检查指定的异味。

**-c**, **--config** _file_
> 配置文件。

# DESCRIPTION

**Reek** 是一个静态分析工具，用于检测 Ruby 源文件中的代码异味，报告潜在的设计问题，例如过长的方法、依恋情结（feature envy）、数据泥团和过长的参数列表。它基于 Martin Fowler 重构目录中的原则，检查代码结构和命名模式，识别可能需要重构的部分。

输出可格式化为文本、YAML、JSON 或 HTML，便于集成到 CI 流水线和代码评审工作流。可用 **--only** 和 **--except** 包含或排除特定异味类型，而 **.reek.yml** 中的项目级配置允许调整阈值和排除路径。

# EXAMPLES

```bash
# Check file
reek app/models/user.rb

# Check directory
reek app/

# JSON output
reek --format json app/ > smells.json

# List smell types
reek --smell-types

# Specific smells only
reek --only "TooManyStatements,LongMethod" app/

# With configuration
reek -c .reek.yml
```

# SMELL TYPES

```
TooManyStatements  - Method too long
FeatureEnvy        - Wrong class responsibility
DataClump          - Data always together
LongParameterList  - Too many parameters
DuplicateMethodCall - Repeated calls
```

# CONFIGURATION (.reek.yml)

```yaml
detectors:
  TooManyStatements:
    max_statements: 10
  exclude_paths:
    - spec/
```

# CAVEATS

仅适用于 Ruby。某些异味可能是误报。请按项目进行配置。

# HISTORY

Reek 由 **Kevin Rutherford** 创建，是一款基于 Martin Fowler 重构理念的 Ruby 代码异味检测器。

# SEE ALSO

[rubocop](/man/rubocop)(1), [ruby](/man/ruby)(1)
