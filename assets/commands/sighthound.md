# TAGLINE

基于 Tree-sitter 的静态应用安全测试（SAST）扫描器

# TLDR

以自动检测的语言和内置规则**扫描**项目

```sighthound /path/to/project```

运行污点分析扫描并输出 JSON

```sighthound --taint-analysis --output-format json /path/to/project > findings.json```

为 GitHub Code Scanning 输出 SARIF

```sighthound --output-format sarif /path/to/project > results.sarif```

以显式语言和自定义规则路径**扫描**

```sighthound /path/to/project python rules/python```

从源码**构建**

```cargo build --release```

# SYNOPSIS

**sighthound** [options] <ROOT_DIR> [LANGUAGE] [RULES_PATH]

# DESCRIPTION

Sighthound 是一个快速、感知 AST 的静态漏洞扫描器。它借助 Tree-sitter 解析器在多种语言上支持模式匹配（"search" 模式）和污点追踪（"taint" 模式）。规则使用 RON 编写，默认内置常见语言（Python、JavaScript/TypeScript、Java、PHP、C#、Go、Ruby、HTML/Django 模板）的规则集。

它可以并行运行，输出 text/JSON/CSV/SARIF 格式的报告，并支持自定义规则包。

# PARAMETERS

**--taint-analysis**
> 在模式搜索之外或替代模式搜索启用污点（source → sink）分析。

**--output-format** text|json|csv|sarif
> 选择报告格式（默认 text）。SARIF 2.1.0 适合 GitHub Code Scanning 使用。

**--help**
> 显示完整的选项列表。

语言和自定义规则路径是根目录之后的可选位置参数。

# CAVEATS

- 部分仅在运行时出现或高度动态的问题会被漏检。
- 支持跨文件的污点分析，但在复杂代码库上可能需要调优。
- 目前不支持 C/C++ 和 Razor（`.cshtml`）。
- 最好作为更广泛的安全计划的一部分使用。

# SEE ALSO

[semgrep](/man/semgrep)(1)

# RESOURCES

```[Source code](https://github.com/Corgea/Sighthound)```

```[Homepage](https://corgea.com/sighthound)```

```[Documentation](https://github.com/Corgea/Sighthound#readme)```

<!-- verified: 2026-07-11 -->
