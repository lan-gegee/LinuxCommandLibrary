# TAGLINE

用于试验 jq 的 TUI 演练场

# TLDR

**打开 JSON 文件**进行演练

```jqp -f [path/to/file.json]```

**通过 stdin 管道传入 JSON**

```cat [path/to/file.json] | jqp```

**以初始查询启动**

```jqp -f [path/to/file.json] -q '.[0]'```

**使用指定主题**

```jqp -f [path/to/file.json] -t [monokai]```

**使用自定义配置文件**

```jqp -f [path/to/file.json] --config [path/to/.jqp.yaml]```

# SYNOPSIS

**jqp** [_query_] [_flags_]

# PARAMETERS

**-f**, **--file** _FILE_
> JSON 或 NDJSON 输入文件的路径。

**-q**, **--query** _QUERY_
> 启动时执行的初始 jq 查询。

**-t**, **--theme** _THEME_
> 配色主题名称。浅色主题适合浅色终端背景，深色主题适合深色背景。

**--config** _FILE_
> 配置文件路径（默认：**$HOME/.jqp.yaml**）。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**jqp** 是一个用于探索和试验 **jq** 查询的 TUI 演练场。它提供交互式界面，你可以输入 jq 过滤器并实时看到对 JSON 数据应用的结果。该工具内部使用 **gojq**（jq 的 Go 实现），支持 JSON 和**换行分隔的 JSON**（NDJSON）输入。

特性包括查询历史、自动补全、可定制的主题（明暗两种），以及以预定义查询启动的能力。配置可通过 **$HOME/.jqp.yaml** 或 **--config** 标志提供；命令行选项优先于配置文件。

# CAVEATS

大型 JSON 文件可能影响实时预览更新的响应速度。输入必须是合法的 JSON 或 NDJSON。

# HISTORY

**jqp** 由 **Noah Gorstein** 开发，使用 **Go** 编写。它的目标是成为网页版 jq 演练场的终端原生替代品。

# INSTALL

```apt: sudo apt install jqp```

```brew: brew install jqp```

```nix: nix profile install nixpkgs#jqp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [jnv](/man/jnv)(1), [fx](/man/fx)(1)
