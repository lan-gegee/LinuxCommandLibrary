# TAGLINE

交互式 JSON 查询工具

# TLDR

交互式探索 JSON 文件

```jid < [file.json]```

探索命令输出的 JSON

```curl -s [https://api.example.com/data] | jid```

以初始查询启动

```jid -q ".[0].name" < [file.json]```

单色输出

```jid -M < [file.json]```

格式化输出 JSON

```jid -p < [file.json]```

# SYNOPSIS

**jid** [_options_]

# PARAMETERS

**-q** _query_
> 启动时使用的初始查询字符串。

**-M**
> 单色输出（无颜色）。

**-p**
> 格式化输出 JSON。

**-h**
> 显示帮助信息。

**-version**
> 显示版本信息。

# KEYBOARD COMMANDS

**Tab**
> 触发自动补全建议。

**Ctrl+w**
> 向后删除一个词。

**Ctrl+u**
> 清空整个查询行。

**Ctrl+f** / **Right**
> 光标前移。

**Ctrl+b** / **Left**
> 光标后移。

**Ctrl+a** / **Home**
> 跳到行首。

**Ctrl+e** / **End**
> 跳到行尾。

**Ctrl+n** / **Down**
> 下一条建议。

**Ctrl+p** / **Up**
> 上一条建议。

**Enter**
> 接受并输出结果。

**Ctrl+c**
> 不输出直接退出。

# QUERY SYNTAX

**.**
> 访问对象属性。

**.foo**
> 访问属性 "foo"。

**[0]**
> 访问数组索引 0。

**.[0:5]**
> 数组切片，从索引 0 到 5。

**.[]**
> 遍历所有数组元素。

**|**
> 将输出管道传给下一个过滤器。

# DESCRIPTION

**jid**（JSON Incremental Digger）是一个交互式 JSON 查询工具。它显示 JSON 数据，并在你输入查询的同时提供实时过滤与自动补全。

与非交互运行查询的 jq 不同，jid 会在你构建查询的过程中即时显示结果。Tab 补全会提示可用的键和索引，便于探索陌生的 JSON 结构。

查询语法遵循 jq 约定。输入 **.** 访问对象的键，**[n]** 访问数组索引，**.[]** 遍历数组。自动补全会在每一层级显示可用选项。

按下 Enter 时，jid 会将当前过滤结果输出到 stdout，可再通过管道传给其他命令。这使它非常适合交互式地构建 jq 查询。

# CAVEATS

会将整个 JSON 读入内存，因此非常大的文件可能较慢。查询语法是 jq 的子集；部分高级 jq 特性不受支持。输入必须是有效的 JSON。

# HISTORY

jid 由 **simeji** 创建，首次发布于 **2016 年**前后。它用 Go 编写，旨在让 JSON 探索变得交互化，而不需要预先构建完整查询。该项目在"探索未知 JSON 结构"与"为自动化构建 jq 查询"之间架起了桥梁。

# INSTALL

```apt: sudo apt install jid```

```dnf: sudo dnf install jid```

```brew: brew install jid```

```nix: nix profile install nixpkgs#jid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [gojq](/man/gojq)(1), [jless](/man/jless)(1), [fx](/man/fx)(1)
