# TAGLINE

.NET SDK 提供的 C# 编译器

# TLDR

将 C# 文件**编译为可执行文件**

```csc [Program.cs]```

**编译多个文件**

```csc [File1.cs] [File2.cs] [File3.cs]```

**指定输出文件名**

```csc -out:[MyApp.exe] [Program.cs]```

**创建类库**（DLL）

```csc -target:library -out:[MyLib.dll] [Library.cs]```

**引用外部程序集**

```csc -reference:[System.Data.dll] [Program.cs]```

**开启优化编译**

```csc -optimize [Program.cs]```

**启用所有警告**

```csc -warn:4 [Program.cs]```

# SYNOPSIS

**csc** [_options_] _source-files_

# PARAMETERS

**-out:**_FILE_
> 指定输出文件名。

**-target:**_TYPE_
> 输出类型：exe、winexe、library、module。

**-reference:**_FILE_
> 引用程序集文件（可重复使用）。

**-lib:**_PATH_
> 程序集引用的附加查找目录。

**-optimize**[**+**|**-**]
> 启用或禁用优化。

**-debug**[**+**|**-**]
> 生成调试信息。

**-warn:**_LEVEL_
> 警告级别（0-4）。

**-nowarn:**_WARNINGS_
> 禁用特定警告。

**-define:**_SYMBOLS_
> 定义条件编译符号。

**-doc:**_FILE_
> 生成 XML 文档文件。

**-?**, **-help**
> 显示帮助信息。

# DESCRIPTION

**csc** 是 .NET SDK 提供的 C# 编译器。它把 C# 源文件编译成能在 .NET 运行时上运行的程序集（可执行文件或库）。编译器支持所有 C# 语言特性，生成 MSIL（Microsoft 中间语言）代码。

现代 C# 开发通常使用内部调用 csc 的 **dotnet** CLI，但直接使用 csc 对理解编译过程、编写构建脚本或维护旧项目仍然很有价值。

编译器负责语法检查、类型验证、代码生成和优化。它支持增量编译，并能生成供 Visual Studio 或其他调试器使用的调试符号。

# CAVEATS

现代 .NET 开发更推荐使用 **dotnet build** 而不是直接调用 csc。与使用项目文件不同，程序集引用必须显式指定。跨平台的 .NET Core/5+ 使用 Roslyn 编译器，需通过 dotnet CLI 访问。

# HISTORY

csc 自 **2002 年的 C# 1.0** 起就是 C# 编译器。它最初是 .NET Framework 的一部分，自 **2014** 年起以 C# 语言本身重写为 Roslyn 编译器。现代 csc 是 .NET SDK 的组成部分，跟随最新语言版本演进（随 .NET 10 提供 C# 14，并将继续更新）。

# INSTALL

```apt: sudo apt install chicken-bin```

```dnf: sudo dnf install chicken```

```pacman: sudo pacman -S chicken```

```apk: sudo apk add chicken```

```brew: brew install chicken```

```nix: nix profile install nixpkgs#chicken```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotnet](/man/dotnet)(1), [msbuild](/man/msbuild)(1), [mono](/man/mono)(1), [mcs](/man/mcs)(1)

# RESOURCES

```[Source code](https://github.com/dotnet/roslyn)```

```[Documentation](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/)```

<!-- verified: 2026-06-26 -->
