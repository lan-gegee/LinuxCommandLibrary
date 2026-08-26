# TAGLINE

显示 Go 软件包和符号的文档

# TLDR

**显示包文档**

```go doc [fmt]```

**显示函数文档**

```go doc [fmt.Println]```

**显示全部文档**

```go doc -all [package]```

**显示未导出的符号**

```go doc -u [package]```

**显示源代码**

```go doc -src [fmt.Println]```

# SYNOPSIS

**go doc** [_options_] [_package_] [_symbol_]

# PARAMETERS

_PACKAGE_
> 要查看文档的软件包。

_SYMBOL_
> 要查找的符号。

**-all**
> 显示全部文档。

**-u**
> 包含未导出的符号。

**-src**
> 显示源代码。

**-c**
> 匹配时区分大小写。

**-cmd**
> 将命令（main 包）当作普通软件包对待，显示其导出的符号。

**-short**
> 为每个符号打印一行简要描述。

**-http**
> 通过 HTTP 提供 HTML 文档，而不是打印到 stdout。

**--help**
> 显示帮助信息。

# DESCRIPTION

**go doc** 显示 Go 软件包和符号的文档。它遵循 Go 文档约定，从源代码注释中提取文档。

该命令显示包、类型、函数和方法的文档。它可以显示源代码和未导出符号供开发参考。

# CAVEATS

从源码读取，而非已安装的文档。标准库始终可用。自定义软件包需要有源码。

# HISTORY

go doc 是 **Go** 工具链的一部分，遵循 Go"文档写在源代码中"的惯例提供文档访问。

# INSTALL

```zypper: sudo zypper install go-doc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [godoc](/man/godoc)(1)

# RESOURCES

```[Documentation](https://pkg.go.dev/cmd/doc)```

```[Source code](https://github.com/golang/go)```

<!-- verified: 2026-07-17 -->
