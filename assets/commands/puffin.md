# TAGLINE

基于 hledger 的个人理财管理终端仪表板

# TLDR

使用 **$LEDGER_FILE** 中的账本**启动理财仪表板**

```puffin```

**启动 v3 界面**

```puffin -v3```

# SYNOPSIS

**puffin** [_-v3_]

# DESCRIPTION

**puffin** 是一款个人理财管理终端仪表板，将 hledger 报表集成到 TUI 中。它显示利润表、资产负债表和账目登记数据，支持按账户、日期、期间和深度过滤，并支持多种商品（commodity）跟踪。

Puffin 不接受自己的 **--file**/**--config** 标志；它通过 **hledger** 自身的配置获取账本（**$LEDGER_FILE** 环境变量或 **~/.hledger.journal**）。可选的 **puffin.json** 文件用于配置自定义报表标签页（含 **name**、**cmd** 和 **locked** 字段）；v3 界面读取的配置更简单，只包含一个 **journalFile** 字段。在 TUI 内按 **?** 可显示按键绑定帮助。

# CAVEATS

需要安装并配置好带账本文件的 **hledger**。自定义报表命令中传入的所有过滤标志都必须是有效的 **hledger** 参数。

# HISTORY

**puffin** 由 **siddhantac** 创建，使用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#puffin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hledger](/man/hledger)(1), [ledger](/man/ledger)(1)
