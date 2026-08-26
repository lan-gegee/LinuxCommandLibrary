# TAGLINE

支持 XML 和 YAML 的可移植 jq 封装

# TLDR

**查询 JSON**（与 jq 相同）

```oq '.[0]' [file.json]```

**将 YAML 转换为 JSON**

```oq -i yaml '.' [file.yaml]```

**查询 XML 并输出为 YAML**

```oq -i xml -o yaml '.root.element' [file.xml]```

# SYNOPSIS

**oq** [_options_] _filter_ [_file_]

# PARAMETERS

**-i** _FORMAT_
> 输入格式（json、yaml、xml）。默认：json。

**-o** _FORMAT_
> 输出格式（json、yaml、xml）。默认：json。

**--xml-root** _NAME_
> 转码为 XML 时使用的根元素名称。默认：root。

**--indent** _N_
> 每个缩进级别的空格数（默认：2）。

**--tab**
> 使用制表符而非空格缩进。

**-h**, **--help**
> 显示帮助。所有其他参数都会传递给 jq。

# DESCRIPTION

**oq** 是一个高性能、可移植的 jq 封装，增加了对 JSON 之外格式的输入与输出支持，包括 XML 和 YAML。所有 jq 过滤器都能照常工作——oq 在输入和输出端透明地处理格式转换。

# CAVEATS

需要已安装 jq。XML 到 JSON 的转换遵循特定的映射规则，可能无法保留全部 XML 语义。

# HISTORY

**oq** 由 **Blacksmoke16** 创建，使用 **Crystal** 编写。

# INSTALL

```apk: sudo apk add oq```

```brew: brew install oq```

```nix: nix profile install nixpkgs#oq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [yq](/man/yq)(1), [xq](/man/xq)(1)
