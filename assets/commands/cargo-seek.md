# TAGLINE

用于搜索、添加和安装 cargo crate 的 TUI 工具

# TLDR

**启动 TUI**

```cargo seek```

**以搜索词启动**

```cargo seek -s [query]```

**在指定的项目目录内搜索**

```cargo seek [path/to/project]```

# SYNOPSIS

**cargo seek** [_options_] [_project_dir_]

# PARAMETERS

**-s**, **--search** _term_
> 启动时自动开始一次搜索

**-f**, **--fps** _float_
> 设置帧率（每秒帧数，默认：30）

**-t**, **--tps** _float_
> 设置逻辑帧率（每秒 tick 数，默认：4）

# DESCRIPTION

**cargo-seek** 是一个 Cargo 子命令，提供终端用户界面，用于从 crates.io 注册表搜索、添加和安装 crate。它支持在 Online、Project、Installed 或 All 等范围内搜索，可视化标注项目依赖和已安装的二进制文件，并支持添加/移除 crate、安装/卸载二进制以及打开文档。结果可按相关性、名称、下载量或更新时间排序。

# INSTALL

```apk: sudo apk add cargo-seek```

```nix: nix profile install nixpkgs#cargo-seek```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-search](/man/cargo-search)(1)
