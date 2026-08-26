# TAGLINE

LLVM 模式匹配测试工具

# TLDR

**对文件运行 FileCheck**

```FileCheck [check-file] < [input]```

**使用来自标准输入的模式检查**

```FileCheck --input-file=[input] [check-file]```

**启用详细输出**

```FileCheck -v [check-file] < [input]```

**要求整行匹配**

```FileCheck --match-full-lines [check-file] < [input]```

# SYNOPSIS

**FileCheck** [_options_] _check-file_

# PARAMETERS

_CHECK-FILE_
> 包含 CHECK 指令的文件。

**--input-file** _FILE_
> 要验证的输入文件。

**-v**, **--verbose**
> 打印成功匹配的内容。

**--match-full-lines**
> 要求整行匹配。

**--strict-whitespace**
> 严格匹配空白字符。

**--check-prefix** _PREFIX_
> 使用自定义检查前缀（默认：CHECK）。

**--check-prefixes** _PREFIXES_
> 以逗号分隔的检查前缀列表。

**-vv**
> 打印有助于诊断分析的信息。

**--dump-input** _MODE_
> 失败时转储带标注的输入（help、always、fail、never）。

**--allow-empty**
> 允许检查文件为空。

**--help**
> 显示帮助信息。

# DESCRIPTION

**FileCheck** 是 LLVM 的测试工具，用来验证文本输出是否匹配指定的模式。它读取一个包含 CHECK 指令的文件，然后核对这些指令与输入（通常是编译器输出）是否相符。

该工具支持多种检查类型：CHECK 用于顺序匹配，CHECK-NEXT 用于紧邻行，CHECK-NOT 用于断言不存在，CHECK-SAME 用于同行匹配，CHECK-DAG 用于无序匹配，CHECK-LABEL 用于划定作用域，CHECK-EMPTY 用于空行。

在 LLVM 与编译器测试中，FileCheck 是验证生成代码符合预期模式的必备工具。

# CAVEATS

其模式语法使用正则表达式的一个子集，并带有 LLVM 特有的扩展，比如变量捕获（`[[VAR:regex]]`）。空白默认会被规范化（多个连续空格视作一个）。它主要为 LLVM/编译器测试而设计，但同样可用于任何文本校验场合。

# HISTORY

FileCheck 是作为 **LLVM 测试基础设施**的一部分开发的。它提供灵活的模式匹配系统，用于在回归测试中校验编译器输出。

# INSTALL

```apk: sudo apk add filecheck```

```nix: nix profile install nixpkgs#filecheck```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grep](/man/grep)(1), [diff](/man/diff)(1)
