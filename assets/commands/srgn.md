# TAGLINE

语法感知的 grep 与代码编辑工具

# TLDR

**替换匹配的文本**

```echo 'Hello World!' | srgn '[wW]orld' -- 'there'```

**将管道输入转换为大写**

```echo 'hello' | srgn --upper '.*'```

**删除匹配的字符**

```echo 'Hello World!' | srgn --delete '[!]'```

**压缩重复字符**

```echo 'Helloooo Woooorld!!!' | srgn --squeeze '(o|!)'```

**在 Python 类定义内搜索**

```srgn --python 'class' '[age]'```

**仅在 Rust 字符串内转换为小写**

```srgn --rust 'string' --lower '.*'```

# SYNOPSIS

**srgn** [_options_] [_scope_] [**--** _replacement_]

# PARAMETERS

**--upper**
> 将匹配文本转为大写

**--lower**
> 将匹配文本转为小写

**--delete**
> 删除匹配文本

**--squeeze**
> 将连续重复字符压缩为单个

**--python** _QUERY_
> 限定作用于 Python 语法节点（例如 class、function、string）

**--rust** _QUERY_
> 限定作用于 Rust 语法节点

**--go** _QUERY_
> 限定作用于 Go 语法节点

**--typescript** _QUERY_
> 限定作用于 TypeScript 语法节点

**--c** _QUERY_
> 限定作用于 C 语法节点

**--csharp** _QUERY_
> 限定作用于 C# 语法节点

**--hcl** _QUERY_
> 限定作用于 HCL 语法节点

**--glob** _PATTERN_
> 处理匹配 glob 模式的文件

# DESCRIPTION

**srgn** 是一款类似 grep 的工具，它通过 tree-sitter 理解源代码语法，并在搜索之外还支持文本操作。它将 tr、sed 和 ripgrep 的能力与语言语法感知结合在一起，支持 Python、Rust、Go、TypeScript、C、C# 和 HCL。它可以执行批量文件编辑、大小写转换，以及限定于特定语法结构的正则替换。

各个操作可以组合使用，并按固定顺序应用，与标志的书写顺序无关。先应用替换（位于 **--** 之后的位置参数），再依次应用 **--upper**、**--lower**、**--delete** 和 **--squeeze** 等标志。

# HISTORY

**srgn** 由 **Alex Povel** 创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S srgn```

```brew: brew install srgn```

```nix: nix profile install nixpkgs#srgn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sed](/man/sed)(1), [tr](/man/tr)(1), [ripgrep](/man/ripgrep)(1), [ast-grep](/man/ast-grep)(1)
