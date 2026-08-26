# TAGLINE

Go 交叉编译工具

# TLDR

**为所有平台构建**

```gox```

**为特定平台构建**

```gox -osarch="linux/amd64 darwin/amd64"```

**构建特定的包**

```gox [./cmd/app]```

**设置输出路径**

```gox -output="dist/{{.Dir}}_{{.OS}}_{{.Arch}}"```

**并行构建**

```gox -parallel=[4]```

# SYNOPSIS

**gox** [_options_] [_packages_]

# PARAMETERS

_PACKAGES_
> 要构建的包。

**-osarch** _TARGETS_
> 操作系统/架构组合。

**-os** _OS_
> 目标操作系统。

**-arch** _ARCH_
> 目标架构。

**-output** _PATTERN_
> 输出路径模板——支持 `{{.Dir}}`、`{{.OS}}`、`{{.Arch}}`。

**-parallel** _N_
> 并发构建工作器的数量（默认：CPU 数量）。

**-osarch-list-json** _FILE_
> 覆盖受支持的操作系统/架构组合列表。

**-cgo**
> 启用 cgo（大多数交叉构建都需要安装合适的交叉编译器）。

**-rebuild**
> 为每个目标重新构建标准库。

**-ldflags** _FLAGS_
> 传递给 `go build` 的链接器标志。

**-tags** _TAGS_
> 传递给 `go build` 的构建标签。

**-mod** _MODE_
> 传递给 `go build` 的模块下载模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gox** 是一个简单的 Go 交叉编译工具，可以并行地为多个平台构建 Go 二进制文件。它在 `go build` 之上封装了便捷的交叉编译选项，并支持使用操作系统和架构变量模板化输出路径。

该工具让一条命令即可完成面向多个目标平台的发布构建。

# CAVEATS

CGO 可能使交叉编译复杂化。目标数量过多时速度较慢。发布场景可考虑 goreleaser。

# HISTORY

gox 由 **Mitchell Hashimoto**（HashiCorp）创建，用于简化面向多个平台的 Go 二进制文件构建。

# INSTALL

```apt: sudo apt install gox```

```pacman: sudo pacman -S gox```

```nix: nix profile install nixpkgs#gox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go-build](/man/go-build)(1), [goreload](/man/goreload)(1)
