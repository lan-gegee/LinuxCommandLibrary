# TAGLINE

用于保存和调用命令片段的 CLI 命令管理器

# TLDR

**将新命令保存**到 hoard

```hoard new```

**列出并搜索已保存的命令**

```hoard list```

**编辑已保存的命令**

```hoard edit```

**删除已保存的命令**

```hoard remove```

**用占位符保存参数化命令**

```hoard new --name "[name]" --command "curl -X POST #url# -d #data#"```

# SYNOPSIS

**hoard** _command_ [_options_]

# DESCRIPTION

**hoard** 是一个 CLI 命令管理器，用来保存那些你经常使用、但过于复杂或冗长而记不住的命令。对于每个收藏的命令，它会以可自定义的分隔符（默认 **#**）将其参数化保存；当你选择某个命令时，hoard 会先询问所有缺失的参数，再把完整命令发送给你的 Shell。

当本地目录中存在 **trove.yml** 文件时，hoard 只加载该文件，从而支持项目专属的命令集合。它还可以安装为 Shell 插件，实现自动补全集成。

# CONFIGURATION

命令保存在 **trove.yml** 文件中。全局配置支持自定义参数分隔符、默认命名空间和 Shell 集成设置。

# CAVEATS

需要安装 Shell 插件才能使用完整的自动补全和内联执行功能。参数化命令采用简单的分隔符替换，不支持复杂的模板语法。

# HISTORY

**hoard** 由 **Hyde46** 创建，使用 **Rust** 编写。它旨在通过提供带参数替换的快速访问命令集合，解决记住复杂 CLI 命令的问题。

# INSTALL

```nix: nix profile install nixpkgs#hoard```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pet](/man/pet)(1), [navi](/man/navi)(1), [tldr](/man/tldr)(1)
