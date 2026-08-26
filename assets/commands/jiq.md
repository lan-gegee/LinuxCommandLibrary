# TAGLINE

使用 jq 表达式的交互式 JSON 查询工具

# TLDR

从 stdin 查询 JSON

```echo '[1, 2, 3]' | jiq```

查询 JSON 文件

```cat [path/to/file.json] | jiq```

从 curl 响应中查询

```curl -s [https://api.example.com/data] | jiq```

# SYNOPSIS

**jiq** < _json_input_

# DESCRIPTION

**jiq** 是一个使用 **jq** 过滤器表达式的交互式 JSON 查询工具。它从 stdin 读取 JSON，并提供一个终端界面，你可以在其中输入 jq 查询，结果会随输入实时更新。这让你可以逐步探索并深入复杂的 JSON 结构。

jiq 需要已安装 **jq** 并可在 PATH 中找到，因为它将查询执行委托给 jq 完成。

# CAVEATS

需要单独安装 **jq**。只能从 stdin 读取；无法直接打开文件。整个 JSON 输入会被加载进内存。

# HISTORY

**jiq** 由 **fiatjaf** 创建，用 **Go** 编写。它受 **jid**（JSON incremental digger）启发，但采用 jq 的查询语法而非自定义语法。

# INSTALL

```nix: nix profile install nixpkgs#jiq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [fx](/man/fx)(1), [jaq](/man/jaq)(1)
