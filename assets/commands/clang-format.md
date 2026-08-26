# TAGLINE

C 语言家族的自动源代码格式化工具

# TLDR

**格式化文件并输出到 stdout**

```clang-format [file.cpp]```

**原地格式化文件**

```clang-format -i [file.cpp]```

**以指定风格格式化**

```clang-format --style=[Google] [file.cpp]```

**使用项目配置文件格式化**

```clang-format --style=file [file.cpp]```

**格式化来自 stdin 的代码**

```echo "int main(){}" | clang-format```

**生成风格配置文件**

```clang-format --style=[LLVM] --dump-config > [.clang-format]```

**仅格式化指定的行**

```clang-format --lines=[10:20] [file.cpp]```

**检查文件是否已格式化**

```clang-format --dry-run --Werror [file.cpp]```

# SYNOPSIS

**clang-format** [_options_] [_file_...]

# DESCRIPTION

**clang-format** 是面向 C、C++、Java、JavaScript、JSON、Objective-C、Protobuf 和 C# 源文件的自动代码格式化工具。它是 LLVM/Clang 项目的一部分，根据可配置的风格规则对代码进行格式化。

该工具自带多种预定义风格（LLVM、Google、Chromium、Mozilla、WebKit、Microsoft、GNU），并支持通过 **.clang-format** 配置文件进行深度定制。使用 **--style=file** 时，它会向上级目录搜索最近的配置文件。

clang-format 与大多数主流编辑器和 CI/CD 流水线集成。结合 **--dry-run** 与 **--Werror** 可以在自动化检查中强制执行格式标准，而无需修改文件。

# PARAMETERS

**-i**
> 原地编辑文件

**--style**=_style_
> 代码风格（LLVM、Google、Chromium、Mozilla、WebKit、Microsoft、file）

**--dump-config**
> 将配置导出到 stdout

**--assume-filename**=_name_
> 从 stdin 读取时用于语言检测的文件名

**--lines**=_start:end_
> 只格式化指定的行范围

**--dry-run**
> 不写入更改；若需要更改则以错误退出

**--Werror**
> 将格式问题视为错误

**--fallback-style**=_style_
> 找不到 .clang-format 时使用的风格

**--verbose**
> 显示正在处理的文件

# CONFIGURATION

在项目根目录创建 **.clang-format** 或 **_clang-format**：

```yaml
BasedOnStyle: Google
IndentWidth: 4
ColumnLimit: 100
```

# PREDEFINED STYLES

LLVM、Google、Chromium、Mozilla、WebKit、Microsoft、GNU

# EDITOR INTEGRATION

提供 VS Code、CLion、Vim、Emacs、Sublime Text 及大多数主流编辑器的集成。

# CAVEATS

风格 "file" 使用父目录中最近的 .clang-format。某些格式化选择较为武断，可能需要调整配置。

# INSTALL

```apt: sudo apt install clang-format```

```apk: sudo apk add clang22-extra-tools```

```brew: brew install clang-format```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang](/man/clang)(1), [clang-tidy](/man/clang-tidy)(1)

# RESOURCES

```[Source code](https://github.com/llvm/llvm-project)```

```[Documentation](https://clang.llvm.org/docs/ClangFormat.html)```

<!-- verified: 2026-06-22 -->
