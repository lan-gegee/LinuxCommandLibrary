# TAGLINE

针对文件路径过滤优化的模糊查找器

# TLDR

**交互式模糊查找文件**

```find . -type f | zf```

**在 vim 中打开选中的文件**

```vim $(find . -type f | zf)```

# SYNOPSIS

**zf** [_options_]

# DESCRIPTION

**zf** 是一个命令行模糊查找器，它优先匹配文件名而非完整路径。当查询内容类似文件路径时，它会应用路径感知启发式算法以获得更准确的结果。也可作为零分配的库使用。

# HISTORY

**zf** 由 **Nate Craddock**（natecraddock）创建，使用 **Zig** 编写。

# INSTALL

```brew: brew install zf```

```nix: nix profile install nixpkgs#zf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fzf](/man/fzf)(1)
