# TAGLINE

Nim 编程语言编译器

# TLDR

**编译为可执行文件**

```nim c [program.nim]```

**编译并运行**

```nim c -r [program.nim]```

**发布版构建**

```nim c -d:release [program.nim]```

**只生成 C 源码而不链接**

```nim c --compileOnly [program.nim]```

**编译为 JavaScript**

```nim js [program.nim]```

**编译为 C++**

```nim cpp [program.nim]```

**检查语法和语义**

```nim check [program.nim]```

**生成 HTML 文档**

```nim doc [program.nim]```

# SYNOPSIS

**nim** [_command_] [_options_] _file_

# PARAMETERS

_COMMAND_
> 编译命令。

**c** / **compile**
> 编译为 C（默认后端）。

**cpp**
> 编译为 C++。

**js**
> 编译为 JavaScript。

**objc**
> 编译为 Objective-C。

**check**
> 校验语法和语义，但不生成代码。

**doc**
> 从源码生成 HTML 文档。

**-r**, **--run**
> 编译完成后运行程序。

**-c**, **--compileOnly**
> 只生成代码，不进行链接。

**-d:release**
> 启用发布优化。

**-d:danger**
> 关闭全部运行时检查以换取最高速度。

**-o:**_FILE_
> 设置输出文件名。

**--opt:**_speed|size|none_
> 优化目标。

**--mm:**_arc|orc|refc_
> 选择内存管理策略。

**--threads:on**
> 启用多线程支持。

**-f**, **--forceBuild**
> 强制完整重建所有模块。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nim** 是 Nim 编程语言的编译器，可编译到 C、JavaScript 等多种后端。

该工具生成高效的本地可执行文件。语法类似 Python，同时具备静态类型。

# CAVEATS

本地构建需要 C 编译器。默认使用垃圾回收。生态系统仍在成长中。

# HISTORY

Nim 由 **Andreas Rumpf** 自 2005 年开始开发，最初名为 Nimrod。

# INSTALL

```pacman: sudo pacman -S nim```

```apk: sudo apk add nim```

```zypper: sudo zypper install nim```

```brew: brew install nim```

```nix: nix profile install nixpkgs#nim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nimble](/man/nimble)(1), [gcc](/man/gcc)(1), [python](/man/python)(1)
