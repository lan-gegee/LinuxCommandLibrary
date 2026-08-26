# TAGLINE

面向 ledger 账本的 TUI 个人财务管理器

# TLDR

**以账本文件启动**

```cashd [path/to/journal.ledger]```

**以默认账本启动**

```cashd```

# SYNOPSIS

**cashd** [_options_] [_file_]

# DESCRIPTION

**cashd** 是一个用于个人财务管理的终端用户界面，配合 **ledger** 格式的纯文本记账账本使用。它提供交互式界面，用于查看以复式记账格式存储的账户、余额和交易。

该 TUI 显示账户层级、交易列表和余额汇总。用户可以在账户和时间周期之间导航来分析自己的财务数据。底层数据格式与 **ledger**、**hledger** 及其他纯文本记账工具兼容。

# CAVEATS

要求账本文件采用 ledger 兼容格式。不提供交易录入功能——请使用文本编辑器或 ledger CLI 添加新交易。自动交易或商品换算等复杂的 ledger 特性在 TUI 视图中可能不受完整支持。

# SEE ALSO

[ledger](/man/ledger)(1), [hledger](/man/hledger)(1)
