# TAGLINE

Go 编程语言工具链

# TLDR

**运行程序**

```go run [main.go]```

**构建可执行文件**

```go build```

**运行测试**

```go test```

**下载依赖**

```go mod download```

**格式化代码**

```go fmt ./...```

# SYNOPSIS

**go** _command_ [_arguments_]

# PARAMETERS

**build**
> 编译包及其依赖。

**run**
> 编译并运行程序。

**test**
> 运行测试。

**mod**
> 模块维护。

**get**
> 下载并安装包。

**fmt**
> 格式化源码。

**vet**
> 报告疑似错误。

**doc**
> 显示文档。

**install**
> 编译并安装包。

**generate**
> 运行代码生成器。

**clean**
> 移除构建缓存和二进制文件。

**env**
> 打印 Go 环境变量。

**--help**
> 显示帮助信息。

# DESCRIPTION

**go** 是用于管理 Go 源码的工具。它提供建构、测试、运行和管理 Go 程序与模块的各种命令。

该工具负责编译、依赖管理、测试和代码质量。Go modules 提供带版本的依赖管理。工具链自成一体，默认生成静态链接的二进制文件。

# CONFIGURATION

**go.mod**
> 模块定义文件，指定模块路径、Go 版本和依赖。

**go.sum**
> 用于验证的模块依赖加密校验和。

**$GOPATH**
> 存放 Go 源码和二进制文件的工作区目录（默认：~/go）。

# CAVEATS

需要 GOPATH 或 modules。内置交叉编译支持。CGO 可能需要额外配置。

# HISTORY

Go 由 **Robert Griesemer、Rob Pike 和 Ken Thompson** 于 **2007 年**在 **Google** 创造，**2009 年**公开发布。

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

[go-build](/man/go-build)(1), [go-run](/man/go-run)(1), [go-mod](/man/go-mod)(1)
