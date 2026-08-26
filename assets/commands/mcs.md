# TAGLINE

Mono C# 编译器

# TLDR

**编译 C# 文件**

```mcs [program.cs]```

**输出可执行文件**

```mcs -out:[program.exe] [program.cs]```

**构建类库**

```mcs -target:library [library.cs]```

**引用程序集**

```mcs -r:[System.dll] [program.cs]```

**调试构建**

```mcs -debug [program.cs]```

**编译多个文件**

```mcs [file1.cs] [file2.cs] -out:[program.exe]```

# SYNOPSIS

**mcs** [_options_] _files_

# PARAMETERS

_FILES_
> 要编译的 C# 源文件。

**-out:**_FILE_
> 输出文件名。

**-target:**_TYPE_
> 输出类型：**exe**（控制台应用，默认）、**library**（DLL）、**module** 或 **winexe**（GUI 应用）。

**-r:**_ASSEMBLY_
> 引用外部程序集。

**-debug**
> 生成调试信息。

**-optimize**
> 启用编译器优化。

**-define:**_SYMBOL_
> 定义预处理器符号。

**-pkg:**_PACKAGE_
> 引用通过 pkg-config 注册的软件包。

**-recurse:**_PATTERN_
> 递归编译匹配该模式的所有文件。

**-warn:**_LEVEL_
> 设置警告级别（0-4，默认 4）。

**-warnaserror**
> 将警告视为错误。

**-nowarn:**_NUMBERS_
> 抑制指定的警告编号。

**-unsafe**
> 允许编译 unsafe 代码。

**-checked**
> 启用溢出检查。

**-main:**_CLASS_
> 指定包含 Main 入口的类。

**-lib:**_PATHLIST_
> 用于搜索程序集的目录列表（逗号分隔）。

**-sdk:**_VERSION_
> 指定基类库版本（2 或 4，默认 4）。

**-noconfig**
> 禁用加载默认编译器配置。

**-langversion:**_VERSION_
> 指定 C# 语言版本（如 default、latest、ISO-1、ISO-2、3-7）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mcs** 是 Mono 的 C# 编译器。它将 C# 源代码编译成可在 Mono 或 .NET 运行时上执行的公共中间语言（CIL）程序集。它支持的 C# 语言版本最高至 C# 7。

选项采用冒号分隔符（如 `-out:file.exe`、`-target:library`），遵循 Microsoft csc 的约定，不过许多情况下也接受以空格分隔的替代语法。

# CAVEATS

属于 Mono 框架的一部分。Mono 项目已在很大程度上被 .NET（Core/.NET 5+）和基于 Roslyn 的 **csc** 编译器取代。新项目应优先选择 **dotnet build** 或 **csc**。语言支持止于 C# 7；更新的 C# 特性需要 Roslyn。

# HISTORY

**mcs** 是 **Mono** 项目的 C# 编译器，最初由 **Miguel de Icaza** 和 Mono 团队编写。它是最早的开源 C# 编译器实现之一，在 Microsoft 开源 .NET 之前就让 Linux 和 macOS 上的 .NET 开发成为可能。

# INSTALL

```pacman: sudo pacman -S mono```

```apk: sudo apk add mono```

```brew: brew install mono```

```nix: nix profile install nixpkgs#mono```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mono](/man/mono)(1), [csc](/man/csc)(1), [dotnet](/man/dotnet)(1)
