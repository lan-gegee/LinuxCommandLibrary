# TAGLINE

Go 静态分析工具

# TLDR

**检查当前软件包**

```go vet```

**递归检查所有软件包**

```go vet ./...```

**检查特定软件包**

```go vet [package/path]```

**以 JSON 格式输出诊断信息**

```go vet -json ./...```

**打印命令但不执行**

```go vet -n ./...```

**使用自定义分析工具**

```go vet -vettool=[path/to/analyzer] ./...```

# SYNOPSIS

**go vet** [_-n_] [_-x_] [_-json_] [_-vettool prog_] [_packages_]

# PARAMETERS

**-n**
> 打印将要执行的命令，但不实际运行。

**-x**
> 在命令执行时将其打印出来。

**-json**
> 以 JSON 格式输出诊断信息。

**-vettool** _prog_
> 选择其他分析工具，提供替代或额外的检查项。

**-c** _int_
> 显示问题行及其上下若干行代码。

**./...**
> 通配符，递归匹配当前模块中的所有软件包。

# DESCRIPTION

**go vet** 检查 Go 源码，报告编译器无法捕获的可疑结构。它使用的启发式方法不保证所有报告都是真实问题。它可检查的问题包括：printf 格式字符串错误、不可达代码、可疑的函数调用、sync 原语的误用以及不正确的 struct 标签。

该工具是标准 Go 工具链的一部分，无需执行代码即可运行。通常与测试和 linter 一起作为持续集成工作流的一部分使用。各个分析器可以单独启用或禁用（例如 `-printf=false`）。运行 `go tool vet help` 可查看可用的分析器及其选项。

# CAVEATS

仅适用于 Go。无法找出所有 bug。请与测试配合使用。

# HISTORY

**go vet** 是 Go 工具链的一部分，通过静态分析发现常见的编程错误。

# INSTALL

```brew: brew install vet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [go-vet](/man/go-vet)(1), [go-build](/man/go-build)(1), [golint](/man/golint)(1), [staticcheck](/man/staticcheck)(1)
