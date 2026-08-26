# TAGLINE

分析 Go 编译二进制文件的体积构成

# TLDR

二进制文件的**文本报告**

```gsa [path/to/binary]```

**交互式终端 UI**

```gsa --tui [path/to/binary]```

本地服务器上的 **Web UI**

```gsa --web [path/to/binary]```

**JSON 输出**

```gsa -f json [path/to/binary]```

**比较两个二进制文件**

```gsa --diff [old-binary] [new-binary]```

# SYNOPSIS

**gsa** [*options*] *binary*...

# DESCRIPTION

**gsa**（**go-size-analyzer**）分析 Go 编译的二进制文件的体积构成。它支持 ELF、Mach-O、PE 以及实验性的 WebAssembly，可按包和节进行分解。输出格式包括 text、JSON、HTML 和 SVG。可通过 **--tui** 和 **--web** 进行交互式探索。

可以从 GitHub releases、Homebrew（**brew install go-size-analyzer**）、Scoop 安装，或：

```
GOEXPERIMENT=jsonv2 go install github.com/Zxilly/go-size-analyzer/cmd/gsa@latest
```

从源码构建需要较新的 Go 工具链并启用 **jsonv2** 实验（如上游文档所述）。

# PARAMETERS

*binary*

> 编译后的 Go 二进制文件路径（在支持的模式下可以是多个）。

**--tui**

> 打开终端 UI 浏览器。

**--web**

> 启动 Web UI（默认端口见 **--help** 文档，通常为 8080）。

**-f**, **--format** text|json|html|svg

> 非交互运行时的输出格式。

**--diff**

> 比较二进制文件（json/text）。

详细标志、隐藏选项和服务器绑定地址请参见 **gsa --help**。

# CAVEATS

对带有符号/包信息的 Go 二进制文件效果最佳；剥离符号的二进制文件只能得到较粗略的报告。WebAssembly 分析是实验性的。浏览器/WASM 分析比本地分析慢得多。从源码构建需要特定的 Go 版本特性。

# INSTALL

```apt: sudo apt install gwenhywfar-tools```

```dnf: sudo dnf install gwenhywfar```

```pacman: sudo pacman -S gwenhywfar```

```apk: sudo apk add gwenhywfar```

```zypper: sudo zypper install gwenhywfar-tools```

```brew: brew install gwenhywfar```

```nix: nix profile install nixpkgs#gwenhywfar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [nm](/man/nm)(1), [size](/man/size)(1), [binsider](/man/binsider)(1)

# RESOURCES

```[Source code](https://github.com/Zxilly/go-size-analyzer)```

```[Homepage](https://gsa.zxilly.dev)```

<!-- verified: 2026-07-19 -->
