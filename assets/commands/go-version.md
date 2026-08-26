# TAGLINE

打印 Go 版本和二进制构建信息

# TLDR

**显示 Go 版本**

```go version```

**显示二进制文件使用的 Go 版本**

```go version [binary]```

**显示所有二进制文件的版本信息**

```go version -m [binary]```

# SYNOPSIS

**go version** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要检查的二进制文件。

**-m**
> 打印每个可执行文件内嵌的模块版本信息（Go 1.13 新增）。

**-v**
> 报告无法识别的文件（否则扫描目录时会静默跳过非 Go 文件）。

**--help**
> 显示帮助信息。

# DESCRIPTION

不带参数调用时，**go version** 会打印工具链自身的 Go 运行时版本。给定文件参数——可执行文件或存放可执行文件的目录——时，它会报告每个二进制文件构建时所用的 Go 版本；配合 **-m** 还会转储二进制文件中内嵌的构建期模块依赖图（相当于 `go.mod` 的信息）。

目录参数会被递归遍历；除非给出 **-v**，非 Go 可执行文件会被静默跳过。

# CAVEATS

只有 Go 1.13+ 构建的二进制文件才会内嵌模块信息。经过深度精简的二进制文件（例如先用 `-ldflags="-w -s"` 构建、再经移除 Go 构建信息段的外部工具处理）可能报告不出任何版本。

# HISTORY

go version 是 **Go** 工具链的一部分，后经扩展，可为调试输出二进制的构建信息。

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
