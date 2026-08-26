# TAGLINE

C 和 C++ 类型声明翻译器

# TLDR

**进入交互模式**

```cdecl```

**解释一个 C 声明**

```cdecl explain "int *(*fp)(int)"```

**将英文转换为 C 声明**

```cdecl declare "x as pointer to function returning int"```

**解释一个复杂的函数声明**

```cdecl explain "void (*signal(int, void (*)(int)))(int)"```

**构造强制类型转换表达式**

```cdecl cast "x into pointer to function returning int"```

**通过管道用英文声明**

```echo "declare argv as array of pointer to char" | cdecl```

**定义一个 typedef**

```cdecl declare "str as typedef pointer to char"```

# SYNOPSIS

**cdecl** [_-ciV_] [_command ..._]

# PARAMETERS

**-+**
> 使用 C++ 语法而不是 C（同 -c）。

**-c**
> 使用 C++ 语法而不是 C。

**-i**
> 进入交互模式（未给出命令时默认）。

**-V**
> 显示版本信息。

**explain** _declaration_
> 将 C/C++ 声明翻译为英文。

**declare** _description_
> 将英文描述转换为 C/C++ 声明。

**cast** _expression_
> 生成强制类型转换表达式。

**typedef** _declaration_
> 从声明创建 typedef。

**set** _option_
> 设置选项（例如 cplusplus、preansi）。

**help**
> 在交互模式中显示帮助。

**quit**
> 退出交互模式。

# DESCRIPTION

**cdecl**（C declaration）在复杂 C 和 C++ 类型声明晦涩的语法与平实的英文之间进行互译。它帮助程序员理解和构建涉及指针、数组和函数的复杂声明。

该工具可以用易懂的措辞解释现有声明，如函数指针、指针数组或数组指针。反过来，它也能根据英文描述生成正确的 C 语法，帮助避免常见的声明错误。

在交互模式下，cdecl 提供一个提示符，你可以连续输入多条 explain 或 declare 命令。它能处理各种复杂场景，例如返回数组指针的函数指针、信号处理函数声明，以及其他出了名容易混淆的 C 构造。

C++ 模式增加了对引用和成员指针的支持。在处理遗留代码、信号处理函数、回调函数或任何包含深层嵌套类型声明的代码时，该工具尤其有价值。

# CAVEATS

某些非常复杂或不标准的声明可能无法正确解析。该工具专注于类型声明，不处理完整的 C/C++ 语法。较新的 C++ 特性（concepts、auto 等）可能不受支持。不同版本之间的英文措辞可能略有差异。

# HISTORY

**cdecl** 最初由 Graham Ross 编写，后来由 David Wolverton 等多位贡献者增强。它诞生于 20 世纪 80 年代，当时 C 的声明语法是困惑和 bug 的常见来源。"declare x as..." 这一短语成了理解 C 由内向外阅读声明规则的教学工具。如今该工具对复杂声明仍然很有用。

# INSTALL

```apt: sudo apt install cdecl```

```dnf: sudo dnf install cdecl```

```zypper: sudo zypper install cdecl```

```brew: brew install cdecl```

```nix: nix profile install nixpkgs#cdecl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [clang](/man/clang)(1), [make](/man/make)(1), [ctags](/man/ctags)(1)
