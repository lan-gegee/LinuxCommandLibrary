# TAGLINE

编译并运行 Go 程序

# TLDR

**运行 Go 文件**

```go run [main.go]```

**运行包**

```go run .```

**带参数运行**

```go run [main.go] [arg1] [arg2]```

**运行多个文件**

```go run [main.go] [helper.go]```

# SYNOPSIS

**go run** [_options_] _package_ [_arguments_]

# PARAMETERS

_PACKAGE_
> 要运行的 Go 文件或包。

_ARGUMENTS_
> 传递给程序的参数。

**-race**
> 启用竞态检测器。

**-exec** _CMD_
> 执行包装器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**go run** 用一步完成 Go 程序的编译和运行。它会把程序编译到临时位置并立即执行，因此非常适合快速开发和测试，而无需生成持久的二进制文件。

包名之后的任何参数都会传递给程序。支持 `-race` 和 `-ldflags` 等标准构建标志。

# CAVEATS

比直接运行已编译的二进制文件慢。临时二进制文件不会被保留。适合开发阶段使用。

# HISTORY

go run 是 **Go** 工具链的一部分，为开发过程中的快速迭代提供便利。

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

```[Documentation](https://pkg.go.dev/cmd/go#hdr-Compile_and_run_Go_program)```

<!-- verified: 2026-07-17 -->
