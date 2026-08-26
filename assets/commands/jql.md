# TAGLINE

用 Rust 编写的 JSON 查询语言工具

# TLDR

**查询顶层字段**

```cat [data.json] | jql '"name"'```

**提取嵌套字段**

```cat [data.json] | jql '"users".[0]."name"'```

**选择多个字段**

```cat [data.json] | jql '"name" "age"'```

**原始字符串输出**（不带 JSON 引号）

```cat [data.json] | jql -r '"name"'```

**从文件读取**而非 stdin

```jql '"name"' [data.json]```

# SYNOPSIS

**jql** [_options_] _selectors_

# PARAMETERS

_SELECTORS_
> JQL 查询表达式（键名必须使用双引号）。

**-r**, **--raw-output**
> 输出不带 JSON 双引号的原始字符串。

**-s**, **--stream**
> 读取 JSON 行流（每行一个 JSON 对象）。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**jql** 是一个用 Rust 编写的 JSON 查询语言 CLI 工具。它提供简单的语法来提取和处理 JSON 数据。为符合 JSON 规范，键选择器必须使用双引号括起。

相比 jq 的复杂语法，该工具更注重简洁。它支持点号表示法访问嵌套结构、带范围的数组索引、用 **..** 展平数据，以及在单条查询中使用多个选择器。输入可来自 stdin 或文件参数。

# CAVEATS

语法与 jq 不同，两者不可互换使用。键选择器必须始终加双引号。该工具读取 JSON 并输出 JSON；需要原始字符串请用 **-r**。

# HISTORY

jql 的开发初衷是提供一个比 jq 更简单的替代方案，针对常见 JSON 操作提供更直观的查询语法。

# INSTALL

```dnf: sudo dnf install jql```

```apk: sudo apk add jql```

```brew: brew install jql```

```nix: nix profile install nixpkgs#jql```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [gron](/man/gron)(1), [fx](/man/fx)(1)
