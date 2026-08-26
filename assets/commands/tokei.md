# TAGLINE

快速的源代码行数统计工具

# TLDR

**统计当前目录中的代码行数**

```tokei```

**统计特定目录**

```tokei [path/to/project]```

**统计多个目录**

```tokei [path/to/project] [path/to/other]```

**排除目录或模式**

```tokei -e [vendor] -e [node_modules]```

**单独显示每个文件**

```tokei --files```

**按特定列排序**

```tokei -s [code]```

**以 JSON 输出**

```tokei -o json```

**只统计特定语言**

```tokei -t [Rust,Python]```

**显示受支持的语言**

```tokei --languages```

**读取先前保存的 JSON 输出**

```tokei [path/to/project] -i [stats.json]```

# SYNOPSIS

**tokei** [_path_...] [_options_]

# PARAMETERS

**-e**, **--exclude** _PATTERN_
> 忽略所有匹配模式的文件和目录。使用 gitignore 语法。可多次指定。

**-t**, **--type** _TYPES_
> 按语言类型过滤输出，逗号分隔（例如 Rust,Markdown）。

**-s**, **--sort** _COLUMN_
> 按列对语言排序。可选值：files、lines、blanks、code、comments。默认：按语言名称字母顺序。

**-o**, **--output** _FORMAT_
> 以机器可读格式输出。可选值：json、yaml、cbor。

**-i**, **--input** _FILE_
> 读入上一次 tokei 运行的输出并与当前结果合并。传入文件路径或 "stdin" 从标准输入读取。

**-f**, **--files**
> 打印单个文件的统计信息，而不是按语言汇总。

**-l**, **--languages**
> 打印所有受支持语言及其文件扩展名的列表。

**--hidden**
> 统计隐藏文件和目录（以点开头的那些）。

**--no-ignore**
> 不遵循任何 ignore 文件（.gitignore、.ignore 等）。隐含 --no-ignore-parent、--no-ignore-dot 和 --no-ignore-vcs。

**--no-ignore-dot**
> 不遵循 .ignore 和 .tokeignore 文件，包括父目录中的那些。

**--no-ignore-parent**
> 不遵循父目录中的 ignore 文件。

**--no-ignore-vcs**
> 不遵循 VCS ignore 文件（.gitignore、.hgignore 等），包括父目录中的那些。

**-c**, **--columns** _NUM_
> 为终端输出设置严格的列宽。

**-v**, **--verbose**
> 提高日志输出级别。最多可使用三次（-vvv）以获得更多细节。

# DESCRIPTION

**tokei** 快速而准确地统计代码行数。它根据文件扩展名识别语言，将各行归类为代码、注释或空白，并按语言分组结果。

该工具用 Rust 编写并采用并行文件处理，能够在数秒内统计数百万行代码。结果显示各语言的明细及总计。

语言检测支持超过 150 种语言，能正确处理多行注释、嵌套注释以及包含类注释语法的字符串。

文件过滤默认遵循 .gitignore 和 .ignore 文件，从而排除生成的代码和依赖目录。可以用 **-e** 排除额外的模式，也可以使用与 .gitignore 语法相同的 .tokeignore 文件。

单文件模式（**--files**）显示每个文件的统计信息而非按语言汇总，有助于识别冗长或生成的文件。

机器可读输出（JSON、YAML、CBOR）便于与其他工具和 CI/CD 流水线集成。可将上一次运行的 JSON 输出通过 **--input** 反馈回来，合并不同目录树的结果。

# CAVEATS

代码行数并非完美的度量指标。生成的代码可能使结果产生偏差。多语言文件（例如内嵌代码块的 Markdown）只计入主语言，但嵌入子语言的总量会单独显示。基于扩展名的检测可能误判某些文件。二进制文件会被跳过。CBOR 和 YAML 输出要求 tokei 编译时启用相应的 feature 标志。

# HISTORY

**tokei** 由 **Erin Power**（XAMPPRocky）于 **2016 年**前后创建。其日文名（時計）意为“时钟”。它用 Rust 编写以保证性能，已成为 cloc 及其他代码行统计工具的热门替代品。

# INSTALL

```apt: sudo apt install tokei```

```dnf: sudo dnf install tokei```

```pacman: sudo pacman -S tokei```

```apk: sudo apk add tokei```

```zypper: sudo zypper install tokei```

```brew: brew install tokei```

```nix: nix profile install nixpkgs#tokei```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cloc](/man/cloc)(1), [scc](/man/scc)(1), [wc](/man/wc)(1), [loc](/man/loc)(1)
