# TAGLINE

纯文本记账工具

# TLDR

**显示账户余额**

```hledger balance```

**显示交易账簿**

```hledger register```

**显示利润表**

```hledger incomestatement```

**显示资产负债表**

```hledger balancesheet```

**交互式添加交易**

```hledger add```

**使用指定的日志文件**

```hledger -f [ledger.journal] balance```

**显示日期范围内的余额**

```hledger balance -b [2024-01-01] -e [2024-12-31]```

**显示按月的余额变动**

```hledger balance --monthly```

**显示现金流量报告**

```hledger cashflow```

# SYNOPSIS

**hledger** [_options_] _command_ [_args_]

# PARAMETERS

**balance**, **bal**
> 显示账户余额。

**register**, **reg**
> 显示带累计总额的交易账簿。

**print**
> 以标准格式打印日志条目。

**add**
> 交互式添加交易。

**incomestatement**, **is**
> 显示利润表（收入与支出）。

**balancesheet**, **bs**
> 显示资产负债表（资产、负债、权益）。

**cashflow**, **cf**
> 显示现金流量表。

**accounts**
> 列出账户名。

**stats**
> 显示日志统计信息。

**import**
> 从 CSV 或其他文件导入新交易。

**-f** _FILE_
> 读取指定的日志文件，而非默认文件（$LEDGER_FILE 或 ~/.hledger.journal）。

**-b** _DATE_
> 起始日期（包含此日期及之后的交易）。

**-e** _DATE_
> 结束日期（包含此日期之前的交易）。

**-p** _PERIOD_
> 期间表达式（例如 "monthly"、"quarterly"、"2024"）。

**--monthly**, **--quarterly**, **--yearly**
> 按时间段显示金额。

**--depth** _N_
> 限制账户显示深度。

**--cost**, **-B**
> 使用交易价格转换为成本。

**--market**, **-V**
> 使用市场价格转换为市值。

**--output-format** _FMT_
> 输出格式：txt、csv、json、html。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hledger** 是一个纯文本记账工具，读取日志文件并生成财务报表。它实现复式记账，每笔交易必须平衡（借方等于贷方）。

默认的日志文件是 **~/.hledger.journal**，或由 **LEDGER_FILE** 环境变量指定的文件。日志条目由日期、描述和两条及以上分录（账户名和金额）组成。该工具支持多种货币、商品价格、周期性交易以及 CSV 导入规则。

报告可以按日期范围、账户名模式和描述查询进行过滤。多期间报表（**--monthly**、**--quarterly**）展示随时间变化的情况，便于趋势分析。

# CAVEATS

复式记账要求每笔交易平衡，这对初学者可能有些困惑。日志文件语法对空白敏感：账户名和金额之间必须至少隔两个空格。默认日志文件必须已存在，或通过 **-f** 或 **LEDGER_FILE** 指定。

# HISTORY

**hledger** 由 **Simon Michael** 于 **2007 年**创建，是受 John Wiegley 的 Ledger 启发而做的 Haskell 重实现。它致力于成为可靠、可移植的纯文本记账工具，注重易用性和文档。

# INSTALL

```apt: sudo apt install hledger```

```dnf: sudo dnf install hledger```

```pacman: sudo pacman -S hledger```

```apk: sudo apk add hledger```

```zypper: sudo zypper install hledger```

```brew: brew install hledger```

```nix: nix profile install nixpkgs#hledger```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ledger](/man/ledger)(1), [hledger-ui](/man/hledger-ui)(1), [hledger-web](/man/hledger-web)(1)
