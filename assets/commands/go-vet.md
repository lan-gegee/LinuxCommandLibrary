# TAGLINE

对 Go 源码进行静态分析

# TLDR

**检查当前包**

```go vet```

**检查指定的包**

```go vet [package]```

**检查所有包**

```go vet ./...```

**运行特定分析器**

```go vet -[analyzer] [package]```

**列出分析器**

```go vet -help```

# SYNOPSIS

**go vet** [_options_] [_packages_]

# PARAMETERS

_PACKAGES_
> 要检查的包。

**-json**
> 以 JSON 格式输出。

**-c** _N_
> 显示问题所在行及其 N 行上下文。

**-v**
> 详细输出。

**-n**
> 打印命令但不运行。

**-x**
> 在命令执行时打印它们。

**-vettool** _prog_
> 选择其他分析工具。

**-tags** _TAGS_
> 构建标签。

# DESCRIPTION

**go vet** 检查 Go 源码，报告编译器无法捕获的可疑代码结构。它能发现 printf 格式字符串错误、不可达代码以及 sync 原语误用等 bug。

该工具运行多个分析器来检查常见错误。它与测试、格式化一起构成标准的质量保证工作流。

# CAVEATS

并非面面俱到；可能出现误报。请配合测试和代码审查使用。运行 `go help vet` 查看完整文档。额外的分析器（如 shadow）需要通过 `-vettool` 启用。

# HISTORY

go vet 是 **Go** 工具链的一部分，通过静态分析捕捉常见的编程错误。

# INSTALL

```apt: sudo apt install gccgo-go```

```dnf: sudo dnf install gcc-go```

```pacman: sudo pacman -S gcc-go```

```apk: sudo apk add gcc-go```

```zypper: sudo zypper install gcc-go```

```brew: brew install go```

```nix: nix profile install nixpkgs#go```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [staticcheck](/man/staticcheck)(1), [golint](/man/golint)(1)
