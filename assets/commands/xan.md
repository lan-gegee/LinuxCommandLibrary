# TAGLINE

用于终端数据处理的 CSV 魔术师

# TLDR

**在终端中预览 CSV 文件**

```xan view [data.csv]```

**在某一列中搜索记录**

```xan search -s [name] "[pattern]" [data.csv]```

**根据频率数据绘制柱状图**

```xan frequency -s [column] [data.csv] | xan plot bar```

# SYNOPSIS

**xan** _command_ [_options_] [_input_]

# DESCRIPTION

**xan** 是一款从 xsv 分叉而来的强大 CSV 处理器，可直接在终端中读取、处理和可视化 CSV 数据。它支持过滤、排序、聚合、去重、并行处理，并能渲染散点图、直方图和热力图。可处理 GB 级别的文件。

# HISTORY

**xan** 由 **Guillaume Plique** 和 **medialab Sciences Po**（巴黎政治学院实验室）创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S xan```

```brew: brew install xan```

```nix: nix profile install nixpkgs#xan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xsv](/man/xsv)(1), [csvkit](/man/csvkit)(1), [miller](/man/miller)(1)
