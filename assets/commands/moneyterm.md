# TAGLINE

TUI 支出与预算跟踪器

# TLDR

**启动预算跟踪器**

```moneyterm```

# SYNOPSIS

**moneyterm** [_options_]

# DESCRIPTION

**moneyterm** 是一个基于 TUI 的支出与预算跟踪器，提供 Overview、Transactions、Labeler、Trends 和 Budget 管理等标签页。

功能包括从 QFX/OFX 银行导出文件导入交易（自动检测重复项）、按标签创建带月度金额的预算、在交互式数据表中查看交易详情、将交易拆分到多个标签，以及趋势分析。

# CAVEATS

交易导入仅支持 QFX/OFX 格式。数据保存在本地。

# HISTORY

**moneyterm** 由 **ChrisBuilds** 创建，使用 **Python** 编写，基于 Textual 和 Rich 框架。

# SEE ALSO

[ledger](/man/ledger)(1), [hledger](/man/hledger)(1)
