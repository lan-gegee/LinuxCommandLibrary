# TAGLINE

功能强大的极速 ls 替代品

# TLDR

在当前目录**列出文件**

```lla```

**以长格式列出文件**

```lla -l```

**以树状结构列出文件**

```lla -t```

**以表格布局列出文件**

```lla -T```

**以网格布局列出文件**

```lla -g```

# SYNOPSIS

**lla** [_options_] [_path_...]

# PARAMETERS

**-l**, **--long**
> 以长格式显示详细信息。

**-t**, **--tree**
> 以树状结构显示。

**-T**, **--table**
> 以表格布局显示。

**-g**, **--grid**
> 以网格布局显示。

**-s**, **--sort** _CRITERIA_
> 按条件排序（name、size、date）。

# DESCRIPTION

**lla** 是一个用 Rust 构建的现代 **ls** 替代品，具有多种视图模式（默认、长格式、树状、表格、网格）、带状态可视化的 Git 集成，以及支持复杂过滤模式（OR、AND、NOT、XOR）的智能搜索、正则表达式支持和内容搜索。

其他特性包括用于目录或文件比较的 diff 命令、时间线视图、存储分析、带书签和历史的交互式目录导航、支持人类可读单位的大小过滤器，以及支持 ISO 日期和相对时长的时间过滤器。

# CAVEATS

Git 集成等部分功能需要 Git 仓库。插件生态可扩展功能，但会增加复杂性。

# HISTORY

**lla** 由 **chaqchase** 创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install lla```

```nix: nix profile install nixpkgs#lla```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [eza](/man/eza)(1), [lsd](/man/lsd)(1)
