# TAGLINE

纯文本记账工具

# TLDR

**显示余额**

```ledger -f [journal.ledger] balance```

**显示账目登记**

```ledger -f [journal.ledger] register```

**查看账户余额**

```ledger -f [journal.ledger] balance [Expenses]```

**按月汇总**

```ledger -f [journal.ledger] register --monthly```

**打印交易记录**

```ledger -f [journal.ledger] print```

**预算报告**

```ledger -f [journal.ledger] budget```

# SYNOPSIS

**ledger** [_options_] _command_ [_args_]

# PARAMETERS

**-f** _FILE_
> 账簿文件。

**balance**
> 显示账户余额。

**register**
> 显示交易登记表。

**print**
> 打印交易。

**--monthly**
> 按月分组。

**--period** _PERIOD_
> 时间段过滤。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ledger** 是一个纯文本记账工具。它处理复式记账账簿。

该工具从简单的文本文件生成报表。它支持多种货币和商品。

# CAVEATS

特定于文本文件格式。有一定学习曲线。查询语言十分强大。

# HISTORY

Ledger 由 **John Wiegley** 创建，是一个面向命令行用户的强大纯文本记账系统。

# INSTALL

```apt: sudo apt install ledger```

```dnf: sudo dnf install ledger```

```pacman: sudo pacman -S ledger```

```apk: sudo apk add ledger```

```zypper: sudo zypper install ledger```

```brew: brew install ledger```

```nix: nix profile install nixpkgs#ledger```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hledger](/man/hledger)(1)
