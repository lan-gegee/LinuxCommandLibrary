# TAGLINE

列出 Go 包和模块信息

# TLDR

**列出当前包**

```go list```

**列出所有包**

```go list ./...```

**以 JSON 格式列出**

```go list -json [package]```

**连同依赖一起列出**

```go list -deps [package]```

**列出模块而非包**

```go list -m all```

**检查模块更新**

```go list -m -u all```

**自定义格式输出**

```go list -f '{{.ImportPath}}: {{.Dir}}'```

**列出模块的可用版本**

```go list -m -versions [module]```

# SYNOPSIS

**go** **list** [**-f** _format_] [**-json**] [**-m**] [_flags_] [_packages_]

# PARAMETERS

**-f** _format_
> 使用 Go 模板语法的自定义输出格式。默认为 **{{.ImportPath}}**。

**-json**
> 以 JSON 格式输出。可选地接受以逗号分隔的字段名来限制输出内容。

**-m**
> 列出模块而非包。

**-deps**
> 以深度优先后序遍历的方式包含所有依赖。

**-e**
> 包含有错误的包，且不向标准错误打印错误信息。

**-u**
> 显示可用更新（配合 **-m** 使用）。同时显示弃用（deprecation）和撤回（retraction）信息。

**-find**
> 只识别包而不解析依赖。Imports 和 Deps 列表将为空。

**-compiled**
> 将 CompiledGoFiles 设置为呈现给编译器的 Go 源文件，包括由 CgoFiles 和 SwigFiles 生成的代码。

**-export**
> 将 Export 字段设置为一个包含最新导出信息的文件，并设置 BuildID 字段。

**-test**
> 报告指定包的测试二进制文件及其重新编译的依赖。

**-versions**
> 将 Module 的 Versions 字段设置为所有已知版本（配合 **-m** 使用）。

**-retracted**
> 报告有关已撤回模块版本的信息（配合 **-m** 使用）。

# DESCRIPTION

**go list** 显示 Go 包和模块的相关信息。它会枚举包及其源码目录、导入路径和依赖。使用 **-m** 时，它列出的是模块而非包。**-f** 标志支持用 Go 模板语法进行自定义格式化，可访问 ImportPath、Dir、Deps、GoFiles 等包结构体字段。

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

[go](/man/go)(1), [go-mod](/man/go-mod)(1), [go-build](/man/go-build)(1), [go-get](/man/go-get)(1)
