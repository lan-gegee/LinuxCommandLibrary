# TAGLINE

轻量级 YAML 与 JSON 处理器

# TLDR

从 YAML 文件**读取值**

```yq '.[key]' [file.yaml]```

**读取嵌套值**

```yq '.[parent].[child]' [file.yaml]```

**将 YAML 转换为 JSON**

```yq -o=json [file.yaml]```

**将 JSON 转换为 YAML**

```yq -p=json [file.json]```

**原地编辑文件**

```yq -i '.[key] = "value"' [file.yaml]```

**合并多个 YAML 文件**

```yq eval-all 'select(fileIndex == 0) * select(fileIndex == 1)' [file1.yaml] [file2.yaml]```

**从数组中选择元素**

```yq '.items[] | select(.name == "foo")' [file.yaml]```

**统计数组元素个数**

```yq '.items | length' [file.yaml]```

# SYNOPSIS

**yq** [_options_] _expression_ [_file ..._]

# PARAMETERS

**-i**, **--inplace**
> 原地编辑文件。

**-p**, **--input-format** _format_
> 输入格式：yaml、json、xml、props、csv、tsv、toml。

**-o**, **--output-format** _format_
> 输出格式：yaml、json、xml、props、csv、tsv。

**-I**, **--indent** _n_
> 设置缩进级别（默认 2）。

**-C**, **--colors**
> 强制彩色输出。

**-M**, **--no-colors**
> 禁用彩色输出。

**-N**, **--no-doc**
> 不打印文档分隔符。

**-e**, **--exit-status**
> 根据表达式结果设置退出状态。

**--from-file** _file_
> 从文件加载表达式。

**-n**, **--null-input**
> 不读取输入；适合创建新文档。

**-s**, **--split-exp** _expression_
> 将输出拆分为多个文件。

**-v**, **--verbose**
> 启用详细输出。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**yq** 是一款轻量级的命令行 YAML、JSON、XML、CSV、TOML 和 properties 处理器。它使用类似 jq 的语法查询和操作结构化数据，方便提取值、修改文档以及在不同格式间转换。

该工具支持从文件或标准输入读取，可输出到标准输出或原地编辑文件。表达式遵循与 jq 类似的基于路径的语法，支持复杂的查询和转换。

存在两种实现：**mikefarah/yq**（基于 Go 的独立二进制文件）和 **kislyuk/yq**（jq 的 Python 封装）。包管理器安装的通常是 Go 版本。

# CAVEATS

两个 yq 实现的语法和能力不同。Go 版本（mikefarah/yq）使用自己的表达式语言，而 Python 版本（kislyuk/yq）直接使用 jq 语法。可用 **yq --version** 检查安装的是哪个版本。

# HISTORY

Python 版 yq 封装由 **Andrey Kislyuk** 创建，于 **2017 年**发布，是针对 YAML 的轻量 jq 封装。基于 Go 的 yq 由 **Mike Farah** 在同一时期创建，是一款独立工具。由于 Go 版本是零依赖的单个二进制文件，且支持 YAML 以外的多种格式，因此更受欢迎。

# INSTALL

```dnf: sudo dnf install yq```

```pacman: sudo pacman -S yq```

```apk: sudo apk add yq-go```

```zypper: sudo zypper install yq```

```brew: brew install yq```

```nix: nix profile install nixpkgs#yq-go```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [xmlstarlet](/man/xmlstarlet)(1), [dasel](/man/dasel)(1), [fx](/man/fx)(1)
