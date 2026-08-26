# TAGLINE

Go 模块依赖管理

# TLDR

**初始化新模块**

```go mod init [module-name]```

**下载依赖**

```go mod download```

**整理依赖**

```go mod tidy```

**将依赖复制到 vendor 目录**

```go mod vendor```

**验证校验和**

```go mod verify```

# SYNOPSIS

**go mod** _command_ [_arguments_]

# PARAMETERS

**init** _NAME_
> 初始化新模块。

**download**
> 将模块下载到缓存。

**tidy**
> 添加缺失的依赖，移除未使用的依赖。

**vendor**
> 创建 vendor 目录。

**verify**
> 验证依赖。

**graph**
> 打印依赖图。

**why** _PACKAGE_
> 解释为什么需要该包。

**--help**
> 显示帮助信息。

# DESCRIPTION

**go mod** 管理 Go modules——Go 官方的依赖管理系统。模块是包的集合，其带版本的依赖关系定义在 go.mod 文件中。

该命令用于初始化模块、管理依赖并维持可重现的构建。它与模块代理及校验和数据库集成，以确保包的完整性和可用性。

# CONFIGURATION

**go.mod**
> 模块定义文件，包含模块路径、Go 版本和依赖要求。

**go.sum**
> 用于验证的模块依赖校验和。

**GOSUMDB**
> 用于验证已下载模块的校验和数据库名称；设为 **off** 可禁用验证。

**GONOSUMDB**
> 不参与校验和数据库验证的模块路径 glob 模式（未设置时默认取自 **GOPRIVATE**）。

**GOFLAGS**
> 应用于 go 命令的默认标志，包括 go mod 子命令。

# CAVEATS

需要 Go 1.11 及以上版本。go.sum 应提交到版本控制。离线构建可使用 vendor 模式。

# HISTORY

Go modules 在 **Go 1.11** 中引入，作为官方的依赖管理方案，取代了基于 GOPATH 的工作流程。

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

[go](/man/go)(1), [go-get](/man/go-get)(1)

# RESOURCES

```[Documentation](https://go.dev/ref/mod)```

<!-- verified: 2026-07-17 -->
