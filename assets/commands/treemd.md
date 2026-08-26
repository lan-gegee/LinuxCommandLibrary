# TAGLINE

生成 Markdown 格式的目录树

# TLDR

生成 Markdown 树

```treemd```

针对特定目录

```treemd [path/to/directory]```

排除匹配的模式

```treemd -e "[node_modules,*.log]"```

限制深度

```treemd -d [2]```

输出到文件

```treemd > [tree.md]```

# SYNOPSIS

**treemd** [_-e patterns_] [_-d depth_] [_options_] [_path_]

# PARAMETERS

**-e** _PATTERNS_
> 排除模式。

**-d** _DEPTH_
> 最大深度。

**-f**
> 包含文件。

**--help**
> 显示帮助。

# DESCRIPTION

**treemd** 生成 Markdown 格式的目录树，便于在 README 文件和其他 Markdown 文档中加入项目结构说明。其输出采用与 Markdown 兼容的缩进和格式，能在 GitHub 等平台上正确渲染。

可以通过模式排除 node_modules 或构建产物之类会让树状输出变得杂乱的目录。深度限制控制树的显示层级，使文档聚焦于相关的结构。

输出可以重定向到文件，或通过管道传入其他命令，融入文档工作流。

# CAVEATS

存在多种实现。输出格式各异。请确认版本。

# HISTORY

**treemd** 类工具将目录结构生成为 Markdown，适用于文档和 README 文件。

# INSTALL

```pacman: sudo pacman -S treemd```

```brew: brew install treemd```

```nix: nix profile install nixpkgs#treemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tree](/man/tree)(1), [tre](/man/tre)(1), [find](/man/find)(1)
