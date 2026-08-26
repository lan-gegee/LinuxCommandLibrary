# TAGLINE

用于浏览 crates.io Rust 软件包的终端界面（TUI）

# TLDR

**启动** TUI 浏览 crates.io

```crates-tui```

**搜索**特定的 crate

```crates-tui [search_term]```

在 TUI 内将 crate 信息**复制**到剪贴板

```crates-tui```
> 按 `c` 复制所选 crate 的信息

# SYNOPSIS

**crates-tui** [_search_term_]

# DESCRIPTION

**crates-tui** 是一个终端用户界面应用，用于浏览和探索来自 crates.io 的 Rust 软件包。它提供一种交互式方式，让你无需离开终端即可搜索 crate、查看软件包详情以及把信息复制到剪贴板。

该界面允许用户在搜索结果中导航，查看 crate 的元数据（包括版本、描述和下载统计），并快速复制相关信息，以便用于 Cargo.toml 文件或文档。

# KEYBINDINGS

**↑/↓** 或 **k/j**
> 在 crate 列表中上下移动

**Enter**
> 查看所选 crate 的详细信息

**c**
> 将所选 crate 的信息复制到剪贴板

**q**
> 退出程序

**/**
> 进入搜索模式

# CAVEATS

需要稳定的网络连接才能从 crates.io 获取数据。剪贴板功能依赖于系统的剪贴板提供程序。某些终端模拟器对剪贴板的支持可能有限。

# HISTORY

**crates-tui** 作为一款 Rust 社区工具而开发，旨在提供基于终端的快速途径，替代通过网页浏览器浏览 crates.io。它借助 Rust 的生态系统和现代 TUI 库，打造出一款高效的软件包发现工具。

# INSTALL

```brew: brew install crates-tui```

```nix: nix profile install nixpkgs#crates-tui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-search](/man/cargo-search)(1), [rustc](/man/rustc)(1)
