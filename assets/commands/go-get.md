# TAGLINE

下载和管理 Go 包依赖

# TLDR

**下载包**

```go get [github.com/pkg/errors]```

**下载指定版本**

```go get [github.com/pkg/errors@v0.9.1]```

**更新包**

```go get -u [package]```

**下载所有依赖**

```go get ./...```

**安装二进制文件**

```go install [github.com/user/tool@latest]```

# SYNOPSIS

**go get** [_options_] [_packages_]

# PARAMETERS

_PACKAGES_
> 要下载的包。

**-u**
> 更新到最新版本。

**-d**
> 仅下载而不安装（自 Go 1.16 起为默认行为；该标志现已废弃，无实际作用）。

**-t**
> 包含测试依赖。

**@** _VERSION_
> 指定版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**go get** 用于下载并安装包及其依赖。在模块模式下，它会更新 go.mod 和 go.sum 文件以跟踪依赖。如需安装工具类二进制文件，请改用 **go install**。

该命令通过模块代理解析版本，支持语义化版本控制。它可以指定具体的版本、分支或提交。

# CAVEATS

自 **Go 1.18** 起，**go get** 不再构建或安装包；它只编辑 go.mod/go.sum 并填充模块缓存。在模块之外运行它，或试图用它安装命令时，都会失败并报错提示使用 **go install**。更新操作会修改 go.mod 和 go.sum，这些更改应当提交到版本控制中。

# HISTORY

go get 是 **Go** 工具链的一部分。作为模块化转型的一部分，其构建/安装功能在 **Go 1.17-1.18** 中被拆分给 **go install**，此后 go get 只专注于依赖解析。

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

[go](/man/go)(1), [go-mod](/man/go-mod)(1), [go-install](/man/go-install)(1)

# RESOURCES

```[Documentation](https://go.dev/ref/mod#go-get)```

<!-- verified: 2026-07-17 -->
