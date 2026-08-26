# TAGLINE

编译并安装 Go 包和二进制文件

# TLDR

**从当前模块安装包**

```go install```

**安装指定的包**

```go install [package]```

**安装工具的最新版本**

```go install [example.com/tool]@latest```

**安装指定版本**

```go install [example.com/tool]@v1.2.3```

**以详细输出安装**

```go install -v [package]```

# SYNOPSIS

**go** **install** [_build flags_] [_packages_]

# PARAMETERS

**-v**
> 在编译时打印包名。

**-n**
> 打印命令但不执行。

**-x**
> 在命令执行时打印它们。

**@version**
> 安装指定版本（latest、v1.2.3 等）。

# DESCRIPTION

**go install** 用于编译并安装包及其依赖。可执行文件会被安装到 GOBIN 环境变量指定的目录，默认为 $GOPATH/bin 或 $HOME/go/bin。带上 @version 后缀使用时，无论当前目录位于何处，它都会以模块感知模式进行安装，并忽略任何已存在的 go.mod。

# CAVEATS

使用 **@latest** 或 **@version** 可以独立于当前模块安装工具。不带版本后缀时，go install 会使用当前模块 go.mod 中声明的依赖。

# HISTORY

自 **Go 1.16** 起，**go install** 成为在特定版本下构建和安装命令的推荐方式，接替了 **go get** 的这一角色；而 go get 自 **Go 1.18** 起已被完全禁止执行此类操作。

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

[go](/man/go)(1), [go-build](/man/go-build)(1), [go-get](/man/go-get)(1)

# RESOURCES

```[Documentation](https://go.dev/ref/mod#go-install)```

<!-- verified: 2026-07-17 -->
