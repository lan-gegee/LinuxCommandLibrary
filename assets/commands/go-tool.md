# TAGLINE

运行 Go 工具链程序

# TLDR

**列出可用工具**

```go tool```

**运行 pprof**

```go tool pprof [profile.pb.gz]```

**运行 trace**

```go tool trace [trace.out]```

**运行 compile**

```go tool compile [file.go]```

**运行 objdump**

```go tool objdump [binary]```

# SYNOPSIS

**go tool** [_tool_] [_arguments_]

# PARAMETERS

_TOOL_
> 要运行的工具名称。

_ARGUMENTS_
> 特定于工具的参数。

**pprof**
> 性能剖析查看器。

**trace**
> 执行跟踪器。

**compile**
> Go 编译器。

**link**
> Go 链接器。

**objdump**
> 目标文件反汇编器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**go tool** 运行作为标准 go 命令底层实现的 Go 工具链程序。它提供了对编译器、链接器、性能剖析器和跟踪器等底层工具的访问。

该命令用于高级调试、性能剖析以及理解编译器行为。每个工具都有各自的选项和用法。

# CAVEATS

属于底层工具。可能随版本更迭而变化。面向高级用户。

# HISTORY

go tool 提供对 **Go** 工具链内部组件的访问，支撑调试与优化工作流。

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

[go](/man/go)(1), [go-build](/man/go-build)(1)

# RESOURCES

```[Documentation](https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool)```

<!-- verified: 2026-07-17 -->
