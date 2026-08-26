# TAGLINE

面向微控制器、WebAssembly 和小型二进制文件的 Go 编译器

# TLDR

向 Arduino Uno **烧录** blink 示例

```tinygo flash -target [arduino-uno] examples/blinky1```

**构建** WASI WebAssembly 模块

```tinygo build -o [out.wasm] -target=wasip1 [program.go]```

针对特定开发板目标**构建**

```tinygo build -o [firmware.elf] -target [board] [main.go]```

**列出**编译器相关信息

```tinygo version```

**运行**当前包的测试（主机或目标）

```tinygo test```

# SYNOPSIS

**tinygo** *command* [*options*] [*packages*]

# DESCRIPTION

**tinygo** 是一款基于 LLVM 的 Go 编译器，面向各种"小地方"：微控制器、WebAssembly（WASM/WASI）以及紧凑的命令行程序。它支持 Go 的一个较大子集，重点是更小的二进制体积和良好的 CGo 互操作性，而不是在高度并发的服务器负载上完全对标标准 **gc** 工具链的性能表现。

常见工作流包括：用 **tinygo flash** 编译固件并写入开发板，用 **tinygo build** 生成二进制或 **.wasm** 模块，以及指定开发板专属的 **-target** 值（支持 150 多种开发板）。借助 TinyGo 的 OS 目标，程序也可以构建到 Linux、macOS 和 Windows 上。

# PARAMETERS

**flash**

> 编译程序并烧录到已连接的微控制器。

**build**

> 将包编译为二进制文件、库或 WebAssembly 模块。

**run**

> 在受支持的宿主或目标上编译并运行。

**test**

> 运行包测试。

**version**

> 打印 TinyGo 与 LLVM 的版本信息。

**targets**

> 列出或检查可用目标（完整列表见上游文档）。

**-target** *name*

> 编译目标（开发板名称、**wasip1**、**wasm**、OS 目标等）。

**-o** *file*

> 输出路径。

**-buildmode** *mode*

> 构建模式（例如 WASM 库使用 **c-shared**）。

**-size** *level*

> 体积报告 / 优化相关选项（见 **tinygo help**）。

**-opt** *level*

> 优化级别。

# CAVEATS

并非所有 Go 程序或标准库包都受支持；详见 TinyGo 语言支持文档。工具链安装（编译器、库、开发板工具链）因平台而异——请参考 https://tinygo.org/getting-started/。二进制体积和性能上的取舍也与标准 Go 编译器不同。

# INSTALL

```dnf: sudo dnf install tinygo```

```pacman: sudo pacman -S tinygo```

```zypper: sudo zypper install tinygo```

```nix: nix profile install nixpkgs#tinygo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [wasm-ld](/man/wasm-ld)(1)

# RESOURCES

```[Source code](https://github.com/tinygo-org/tinygo)```

```[Homepage](https://tinygo.org)```

```[Documentation](https://tinygo.org/docs/)```

<!-- verified: 2026-07-19 -->
