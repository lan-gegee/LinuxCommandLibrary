# TAGLINE

将 Go 源码格式化为标准风格

# TLDR

**格式化一个 Go 文件**

```go fmt [file.go]```

**格式化当前包中的所有文件**

```go fmt```

**递归格式化所有包**

```go fmt ./...```

**显示将被更改的文件**

```gofmt -l [file.go]```

**显示更改的差异**

```gofmt -d [file.go]```

**简化代码**

```gofmt -s [file.go]```

# SYNOPSIS

**go** **fmt** [**-n**] [**-x**] [_packages_]

**gofmt** [_flags_] [_path_ ...]

# PARAMETERS

**-n**
> 打印将要执行的命令。

**-x**
> 在命令执行时打印它们。

**-l**
> 列出格式与标准不一致的文件（gofmt）。

**-w**
> 将结果写回源文件（gofmt）。

**-d**
> 显示差异而不重写文件（gofmt）。

**-s**
> 简化代码（gofmt）。

**-r** _rule_
> 在格式化之前应用重写规则（gofmt）。

# DESCRIPTION

**go fmt** 按照 Go 标准风格约定格式化 Go 源码。对于导入路径所指定的包，它相当于运行 **gofmt -l -w**。**gofmt** 工具还可以通过 **-s** 简化代码，并通过 **-r** 应用重写规则来进行重构。

# CAVEATS

**go fmt** 与 **gofmt** 接受的参数不同。需要使用 **-s**、**-d**、**-l** 和 **-r** 选项时，请直接调用 **gofmt**。

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

[go](/man/go)(1), [goimports](/man/goimports)(1)

# RESOURCES

```[Documentation](https://pkg.go.dev/cmd/gofmt)```

```[Source code](https://github.com/golang/go)```

<!-- verified: 2026-07-17 -->
