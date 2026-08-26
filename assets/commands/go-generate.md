# TAGLINE

运行 Go 源文件中的代码生成指令

# TLDR

**在当前包中运行生成器**

```go generate```

**在所有包中运行生成器**

```go generate ./...```

**按模式运行特定生成器**

```go generate -run [pattern]```

**预览命令而不执行**

```go generate -n```

**以详细输出运行**

```go generate -v```

**跳过匹配模式的生成器**

```go generate -skip [pattern]```

# SYNOPSIS

**go** **generate** [**-run** _regexp_] [**-skip** _regexp_] [**-n**] [**-v**] [**-x**] [_packages_]

# PARAMETERS

**-run** _regexp_
> 只运行匹配正则表达式的指令。

**-skip** _regexp_
> 跳过匹配正则表达式的指令。

**-n**
> 打印命令但不执行。

**-v**
> 在处理过程中打印包名。

**-x**
> 在命令执行时打印它们。

# DESCRIPTION

**go generate** 会扫描 Go 源文件中以 **//go:generate command** 形式书写的特殊指令，并执行其中指定的命令。它在编译前自动完成代码生成，常用于创建字符串方法、mock 实现、protocol buffers 以及其他生成的代码。指令必须位于行首，且 // 与 go:generate 之间不能有空格。

# CAVEATS

执行期间会设置环境变量 $GOARCH、$GOOS、$GOFILE、$GOLINE、$GOPACKAGE、$GOROOT、$DOLLAR 和 $PATH。生成的文件应在非注释内容之前包含一行符合 **^// Code generated .* DO NOT EDIT\.$** 的注释。**go build** 或 **go test** 绝不会自动运行 **go generate**；必须显式调用它。

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

```[Documentation](https://pkg.go.dev/cmd/go#hdr-Generate_Go_files_by_processing_source)```

```[Source code](https://github.com/golang/go)```

<!-- verified: 2026-07-17 -->
