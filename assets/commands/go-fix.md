# TAGLINE

将 Go 代码更新到较新的 API 版本

# TLDR

**修复当前模块中的所有包**

```go fix ./...```

**修复指定的包**

```go fix [package]```

**以统一 diff 预览更改而不修改文件**

```go fix -diff [package]```

**以 JSON 输出修复结果而不是直接应用**

```go fix -json [package]```

**使用自定义修复工具**

```go fix -fixtool=[prog] [package]```

# SYNOPSIS

**go fix** [_-diff_] [_-json_] [_-fixtool=prog_] [_packages_]

# PARAMETERS

_PACKAGES_
> 要修复的包。使用 ./... 表示当前模块中的所有包。

**-diff**
> 以统一 diff 打印更改而不是直接应用。适用于 CI 流水线。

**-json**
> 以 JSON 形式输出修复结果而不是直接应用。

**-fixtool** _prog_
> 选择其他分析工具，以使用替代或额外的修复器。默认为 go tool fix。

**-v**
> 详细输出。

**-n**
> 打印将要执行的命令但不实际运行。

**-x**
> 在命令执行时打印它们。

# DESCRIPTION

**go fix** 将 Go 代码更新到较新的 Go 版本。它应用针对 API 变更和已弃用模式的转换，帮助代码在各 Go 版本之间保持可维护性。

该工具运行特定的修复器（分析器）来处理 Go 版本间的已知变化。从 Go 1.24 起，go fix 使用与 go vet 相同的分析框架，并支持按名称选择特定的分析器。

可用的分析器包括以下修复：将 interface{} 替换为 any、使用 min/max 内置函数、现代化字符串操作、更新 fmt.Appendf 模式、range-over-int 等。

默认情况下文件会被就地修改，因此建议在运行前使用版本控制。

# CAVEATS

除非使用 -diff，否则会就地修改文件。请务必使用版本控制。可能需要人工复查。仅限于已知的修复项。每次运行只分析一种构建配置；对于多平台项目，请分别用不同的 GOARCH/GOOS 值运行。

# HISTORY

go fix 是 **Go** 工具链的一部分。它最初用于处理 Go 1.x 开发期间的破坏性 API 变更，并在 **Go 1.24** 中得到显著增强：改用分析框架，获得了对自定义分析器和现代化修复的支持。

# SEE ALSO

[go](/man/go)(1), [go-vet](/man/go-vet)(1), [go-fmt](/man/go-fmt)(1)
