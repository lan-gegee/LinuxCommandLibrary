# TAGLINE

编译 Go 软件包及其依赖

# TLDR

**构建当前包**

```go build```

**构建指定文件**

```go build [main.go]```

**设置输出名称**

```go build -o [binary-name]```

**交叉编译**

```GOOS=[linux] GOARCH=[amd64] go build```

**启用竞态检测器构建**

```go build -race```

**裁剪路径构建**（用于可重现构建）

```go build -trimpath -o [binary-name]```

**基于剖析引导优化构建**

```go build -pgo=[profile.pprof] -o [binary-name]```

# SYNOPSIS

**go build** [_options_] [_packages_]

# PARAMETERS

_PACKAGES_
> 要构建的软件包。

**-o** _FILE_
> 输出文件名。

**-v**
> 详细输出。

**-race**
> 启用竞态检测器。

**-ldflags** _FLAGS_
> 链接器标志。

**-tags** _TAGS_
> 构建标签。

**-trimpath**
> 从生成的可执行文件中移除所有文件系统路径。

**-gcflags** _'[pattern=]arg list'_
> 传给 Go 编译器的参数。

**-mod** _MODE_
> 模块下载模式：readonly、vendor 或 mod。

**-pgo** _FILE_
> 剖析引导优化文件（默认：auto）。

**-cover**
> 启用代码覆盖率插桩。

**-a**
> 强制重新构建已是最新状态的软件包。

**-n**
> 打印命令但不执行。

**-x**
> 在命令执行时打印出来。

**-buildmode** _MODE_
> 构建模式（default、archive、c-archive、c-shared、shared、exe、pie、plugin）。

# DESCRIPTION

**go build** 编译 Go 软件包及其依赖。对于 main 包它会生成可执行二进制文件；对于库包则只检查能否编译通过。

该命令负责依赖解析、编译和链接。交叉编译内置于 GOOS 和 GOARCH 环境变量中，无需额外的工具链。

# CAVEATS

main 包生成可执行文件；库包只检查编译。CGO 需要 C 编译器。完整文档见 `go help build`。

# HISTORY

go build 是 **Go** 工具链的核心命令之一，自 Go 发布以来就提供快速的增量编译。

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

[go](/man/go)(1), [go-run](/man/go-run)(1), [go-install](/man/go-install)(1)
