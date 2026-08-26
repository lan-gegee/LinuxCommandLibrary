# TAGLINE

基于 Clang 的 C++ 代码检查与静态分析工具

# TLDR

**对文件运行检查**

```clang-tidy [file.cpp] -- -I[include/path]```

**列出已启用的检查**

```clang-tidy --list-checks```

**列出所有可用的检查**

```clang-tidy --list-checks -checks='*'```

**运行指定的检查**

```clang-tidy -checks='-*,modernize-*' [file.cpp]```

**应用自动修复**

```clang-tidy --fix [file.cpp]```

**将修复导出到文件**

```clang-tidy --export-fixes=[fixes.yaml] [file.cpp]```

**导出配置**

```clang-tidy --dump-config```

# SYNOPSIS

**clang-tidy** [_options_] _file_ [_-- compile_options_]

# DESCRIPTION

**clang-tidy** 是一个基于 clang 的 C++ 代码检查工具，用于诊断和修复典型的编程错误，包括风格违规、接口误用以及可通过静态分析发现的 bug。它是 LLVM/Clang 额外工具的一部分。

该工具提供数百项检查，按 bugprone、modernize、performance、readability、cppcoreguidelines 等类别组织。许多检查可以自动向源码应用修复，因此非常适合大规模的代码现代化（例如迁移到现代 C++ 惯用法）。

clang-tidy 使用 **.clang-tidy** 配置文件进行项目级设置，并支持用 NOLINT 注释进行行内抑制。对于大型项目，**run-clang-tidy.py** 可跨多个文件并行执行。

# PARAMETERS

**-checks**=_list_
> 以逗号分隔的检查列表（带 +/- 前缀的通配模式）

**--list-checks**
> 列出已启用的检查

**--fix**
> 应用建议的修复

**--fix-errors**
> 即使出现错误也应用修复

**--export-fixes**=_file_
> 将修复写入 YAML 文件

**--dump-config**
> 将配置导出到 stdout

**--warnings-as-errors**=_list_
> 将指定的警告视为错误

**-p** _path_
> 编译数据库的路径

**--config-file**=_file_
> .clang-tidy 配置文件的路径

**--format-style**=_style_
> 应用修复时使用的格式风格（none、file、llvm、google、webkit、mozilla）

**--extra-arg**=_arg_
> 追加到编译器命令行的附加参数

**--fix-notes**
> 应用来自诊断备注（notes）的修复（隐含 --fix）

**--allow-no-checks**
> 允许启用的检查为空而不报错

# CHECK CATEGORIES

**bugprone-***
> 易引发 bug 的模式

**modernize-***
> C++ 现代化

**performance-***
> 性能问题

**readability-***
> 代码可读性

**cppcoreguidelines-***
> C++ Core Guidelines

**clang-analyzer-***
> Clang 静态分析器检查

**misc-***
> 杂项检查

**cert-***
> CERT 安全编码标准

# CONFIGURATION

在项目根目录创建 **.clang-tidy**：

```yaml
Checks: '-*,modernize-*,bugprone-*'
WarningsAsErrors: '*'
```

# SUPPRESSION

使用注释：NOLINT、NOLINTNEXTLINE、NOLINTBEGIN/NOLINTEND

# CAVEATS

复杂项目需要编译数据库。并行执行请使用 run-clang-tidy.py。

# INSTALL

```apt: sudo apt install clang-tidy```

```apk: sudo apk add clang22-extra-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang](/man/clang)(1), [clang-format](/man/clang-format)(1)
