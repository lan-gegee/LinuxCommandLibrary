# TAGLINE

Void Linux 包管理器的 TUI 前端

# TLDR

**启动包管理器 TUI**

```xbps-tui```

**以 dry-run 模式启动**（预览操作而不执行）

```xbps-tui --dry-run```

# SYNOPSIS

**xbps-tui** [_options_]

# PARAMETERS

**--dry-run**
> 预览安装/移除操作而不实际执行。

# DESCRIPTION

**xbps-tui** 是 Void Linux 所用 xbps 包管理器的交互式终端前端。它支持按名称和描述模糊搜索软件包，按已安装、可更新或已标记进行过滤，并可通过 root 执行来标记软件包以便安装或移除。

按 **/** 或 **Ctrl+f** 进入模糊搜索模式。使用 **h**/**k** 或方向键在全部软件包、已安装、可更新、已标记安装和已标记移除之间切换过滤。设置 **XBPS_TUI_DATA** 环境变量可指定自定义数据目录。

# HISTORY

**xbps-tui** 由 **lukeflo** 创建，使用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#xbps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xbps-install](/man/xbps-install)(1), [xbps-query](/man/xbps-query)(1), [xbps-remove](/man/xbps-remove)(1)
