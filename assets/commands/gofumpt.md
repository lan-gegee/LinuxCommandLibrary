# TAGLINE

更严格的 Go 代码格式化工具

# TLDR

**格式化 Go 文件并将结果打印到标准输出**

```gofumpt [file.go]```

**就地格式化文件**

```gofumpt -w [file.go]```

**递归格式化当前目录中的所有 Go 文件**

```gofumpt -w .```

**显示格式化更改的差异而不实际应用**

```gofumpt -d [file.go]```

**启用额外的强制性规则进行格式化**

```gofumpt -extra [file.go]```

**从标准输入读取并格式化**

```cat [file.go] | gofumpt```

# SYNOPSIS

**gofumpt** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要格式化的 Go 文件。

**-w**
> 将结果写回源文件而不是标准输出。

**-d**
> 显示差异而不重写文件。

**-e**
> 报告所有错误（而不是每个文件只报前 10 个）。

**-extra**
> 启用额外的格式化规则（例如强制把简短的 case 体写在同一行）。

**-l**
> 列出格式与 gofumpt 输出不一致的文件。

**-version**
> 打印版本并退出。

# DESCRIPTION

**gofumpt** 是比 gofmt 更严格的替代品，它在标准 Go 风格之外应用更多格式化规则。它会移除不必要的空行、强制一致的分组，并施加其他风格要求，同时仍然是 gofmt 的超集。

**-extra** 标志可启用更加严苛的规则，得到更紧凑的代码格式。

# CAVEATS

比 gofmt 更严格——经 gofumpt 格式化的代码必然是合法的 gofmt 输出，反之则不然。可能与项目既有约定冲突。大多数编辑器都支持通过设置把 gofumpt 配置为 gofmt 的直接替代品。

# HISTORY

gofumpt 由 **Daniel Marti** 创建，旨在提供比标准 gofmt 更严格的格式化。

# INSTALL

```pacman: sudo pacman -S gofumpt```

```brew: brew install gofumpt```

```nix: nix profile install nixpkgs#gofumpt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gofmt](/man/gofmt)(1), [go-fmt](/man/go-fmt)(1)
