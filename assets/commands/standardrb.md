# TAGLINE

零配置的 Ruby 风格检查器

# TLDR

**检查当前目录中的 Ruby 文件**

```standardrb```

**检查指定文件**

```standardrb [path/to/file.rb] [path/to/other.rb]```

**自动修复**代码风格问题

```standardrb --fix```

**修复时包括不安全的修正**

```standardrb --fix-unsafely```

**为现有违规生成 todo 文件**

```standardrb --generate-todo```

**以 progress 格式输出**

```standardrb --format progress```

**启动语言服务器**以便与 IDE 集成

```standardrb --lsp```

# SYNOPSIS

**standardrb** [_options_] [_files_...]

# PARAMETERS

**--fix**
> 在可能的情况下自动修复代码风格问题。

**--fix-unsafely**
> 应用修复，包括被标记为不安全的修正。

**--generate-todo**
> 创建 **.standard_todo.yml** 以忽略现有违规。

**--format** _format_
> 输出格式：progress、simple、json 等。

**--lsp**
> 作为 Language Server Protocol 服务器运行，以便与 IDE 集成。

**--no-fix**
> 禁用自动修复（默认行为）。

**--parallel**
> 以并行模式运行以加快检查速度。

**--config** _file_
> 使用指定的配置文件。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**standardrb** 是 Ruby 生态中带有明确主张的检查器和格式化工具，将 StandardJS 的理念带到了 Ruby。它通过在 RuboCop 外层封装一组固定规则来提供零配置的代码风格方案，消除关于代码格式的争论。

该工具无需配置文件，也无需团队讨论风格偏好，即可在整个 Ruby 项目中强制统一风格。它包含 RuboCop 内置 cops 和 rubocop-performance 的规则。

Standard Ruby 通过 LSP 支持与编辑器集成，并可用于 CI 流水线。**--generate-todo** 选项为现有项目采用 Standard 提供便利：它会创建一个忽略文件来记录当前违规，便于逐步解决。

# CAVEATS

Standard 有意不可配置；如果需要自定义规则，请直接使用 RuboCop。**--fix-unsafely** 选项在极少数情况下可能改变代码行为。Standard 会将大多数 CLI 参数转发给 RuboCop，因此 RuboCop 的标志通常可用。需要 Ruby 2.6 或更高版本。

# HISTORY

**Standard Ruby** 的目标是将 StandardJS 的"零配置"哲学带入 Ruby 生态系统。它构建于 RuboCop 之上，利用其庞大的规则集，同时提供带有明确主张的零配置体验。该项目已在 Ruby 社区获得广泛采用，成为避免代码风格"自行车棚效应"争论的一种方式。

# SEE ALSO

[rubocop](/man/rubocop)(1), [ruby](/man/ruby)(1), [bundle](/man/bundle)(1)
