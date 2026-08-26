# TAGLINE

Snakemake 工作流文件的强约束代码格式化工具

# TLDR

**格式化 Snakefile**

```snakefmt [Snakefile]```

**检查格式**

```snakefmt --check [Snakefile]```

**格式化目录**

```snakefmt [workflow/]```

**显示差异**

```snakefmt --diff [Snakefile]```

**设置行长度**

```snakefmt -l [100] [Snakefile]```

**格式化标准输入**

```cat [Snakefile] | snakefmt -```

**详细输出**

```snakefmt -v [Snakefile]```

# SYNOPSIS

**snakefmt** [_--check_] [_--diff_] [_-l length_] [_options_] _files_

# PARAMETERS

**--check**
> 仅检查，不做更改。

**--diff**
> 显示更改内容。

**-l**, **--line-length** _N_
> 最大行长度。

**-v**, **--verbose**
> 详细输出。

**--include** _PATTERN_
> 格式化目录时用于筛选要包含文件的正则表达式。

**--exclude** _PATTERN_
> 格式化目录时用于排除文件的正则表达式。

**--config** _FILE_
> 从 pyproject.toml 或 .editorconfig 文件读取配置。

**-**
> 从标准输入读取。

# DESCRIPTION

**snakefmt** 是面向 Snakemake 工作流文件的强约束代码格式化工具。它在 Snakefile 及相关 rules 文件之间强制统一的代码风格，既能处理标准 Python 语法，也能处理 Snakemake 特有的扩展，例如 **rule**、**checkpoint** 和 **module** 块。

该格式化工具构建在 Python 的 **black** 格式化器之上，采用相同的默认行长度（88 字符）和相近的格式化理念。它理解 Snakemake 的领域专用语法，能正确格式化 **input**、**output**、**params** 和 **shell** 等规则参数，同时保留语义。

检查模式（**--check**）在不修改文件的前提下验证格式，若需要更改则返回非零退出码，非常适合 CI 流水线。差异模式（**--diff**）可在实际应用之前预览将要发生的具体改动。

# CAVEATS

Snakemake 专属，不适用于一般 Python 文件。使用与 black 相同的默认行长度（88）。配置可写在 pyproject.toml 中。可能无法优雅地处理所有自定义 Snakemake wrapper 或大量使用模板的 rule。

# HISTORY

**snakefmt** 为 **Snakemake** 工作流管理系统而创建，为生物信息学流水线带来一致的代码格式。

# INSTALL

```brew: brew install snakefmt```

```nix: nix profile install nixpkgs#snakefmt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snakemake](/man/snakemake)(1), [black](/man/black)(1), [python](/man/python)(1), [ruff](/man/ruff)(1), [yapf](/man/yapf)(1)
