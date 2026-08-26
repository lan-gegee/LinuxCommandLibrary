# TAGLINE

面向专业用户的更美观强大的 ls

# TLDR

**列出当前目录**

```pls```

**显示详细元数据列出内容**

```pls -d```

**列出特定文件或目录**

```pls [path/to/directory] [path/to/file]```

# SYNOPSIS

**pls** [_options_] [_paths_...]

# PARAMETERS

**-d**, **--det** _COLS_
> 显示详细的文件元数据。各列可按规范自由排序。

# DESCRIPTION

**pls** 是一个比 **ls** 更美观、更强大的替代品，设计目标是供人类阅读而非脚本使用。pls 中的 "p" 代表 pretty、powerful、performant、practical、petite、pliable 和 personable。它具有 Nerd Font 图标、丰富的格式化、灵活的列排序和可配置的显示方式。文件和目录可以作为位置参数传入。

# CAVEATS

图标渲染需要 Nerd Font。不适合脚本使用——机器可读输出请用 **ls**。

# HISTORY

**pls** 由 **pls-rs** 组织维护，使用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#pls```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [eza](/man/eza)(1), [lsd](/man/lsd)(1), [lla](/man/lla)(1)
