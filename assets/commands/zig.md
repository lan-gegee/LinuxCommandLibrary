# TAGLINE

系统编程语言与编译器

# TLDR

**编译并运行文件**

```zig run [file.zig]```

**构建项目**

```zig build```

**编译为可执行文件**

```zig build-exe [file.zig]```

**编译为目标文件**

```zig build-obj [file.zig]```

**格式化 Zig 代码**

```zig fmt [file.zig]```

**运行测试**

```zig test [file.zig]```

**启动 REPL（交互模式）**

```zig repl```

# SYNOPSIS

**zig** [_command_] [_options_] [_arguments_]

# SUBCOMMANDS

**build**
> 使用 build.zig 构建项目

**build-exe**
> 编译为可执行文件

**build-lib**
> 编译为库

**build-obj**
> 编译为目标文件

**run**
> 立即编译并运行

**test**
> 运行单元测试

**fmt**
> 格式化源代码

**cc**
> 将 Zig 用作 C 编译器

**c++**
> 将 Zig 用作 C++ 编译器

**translate-c**
> 将 C 代码翻译为 Zig

**init-exe**
> 初始化可执行项目

**init-lib**
> 初始化库项目

# PARAMETERS

**-O** _mode_
> 优化模式（Debug、ReleaseSafe、ReleaseFast、ReleaseSmall）

**-target** _triple_
> 交叉编译目标

**-I** _dir_
> 添加头文件包含目录

**-l** _lib_
> 链接库

**-femit-asm**
> 输出汇编代码

**-freference-trace**
> 显示编译错误的引用追踪

# DESCRIPTION

**Zig** 是一门专注于安全性、性能和可维护性的系统编程语言。zig 命令既是编译器也是构建系统。

主要特性包括编译期代码执行（comptime）、可选的安全检查、C 互操作性，以及对众多目标的内置交叉编译能力而无需外部工具链。

Zig 还可以作为即插即用的 C/C++ 编译器（**zig cc**、**zig c++**），提供一致的交叉编译能力，即使对非 Zig 项目也很有用。

构建系统使用 Zig 本身编写的 **build.zig** 文件，为构建配置提供了完整的语言能力。

# CAVEATS

Zig 仍处于 1.0 之前阶段，语言和标准库可能随版本变化。

Debug 构建包含能捕获 bug 的运行时安全检查，但有性能开销。

交叉编译功能强大，但某些特性仍可能需要目标平台特定的系统库。

# INSTALL

```dnf: sudo dnf install zig```

```pacman: sudo pacman -S zig```

```apk: sudo apk add zig```

```zypper: sudo zypper install zig```

```brew: brew install zig```

```nix: nix profile install nixpkgs#zig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [clang](/man/clang)(1), [rustc](/man/rustc)(1), [make](/man/make)(1)
