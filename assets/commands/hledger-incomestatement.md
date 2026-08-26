# TAGLINE

显示利润表，列出报告期内的收入与支出

# TLDR

**显示利润表**

```hledger incomestatement```

**从指定文件显示**

```hledger incomestatement -f [journal.ledger]```

**显示特定期间**

```hledger incomestatement -p "[this month]"```

**按月细分显示**

```hledger incomestatement --monthly```

**限制账户深度**

```hledger incomestatement --depth [2]```

# SYNOPSIS

**hledger** **incomestatement** | **is** [_options_]

# PARAMETERS

**-f**, **--file** _file_
> 使用指定的日志文件。

**-p**, **--period** _expr_
> 报告期间（例如 "this month"、"2024"）。

**--monthly**
> 显示按月分列。

**--quarterly**
> 显示按季度分列。

**--yearly**
> 显示按年分列。

**--depth** _n_
> 限制账户深度。

**--tree**
> 以树状结构显示账户。

**--flat**
> 以扁平列表显示账户（默认）。

**--average**
> 显示行平均值列。

**--row-total**
> 显示行合计列。

**--no-total**
> 省略最后的总计行。

**--sort-amount**
> 按金额而非账户名排序。

**--output-format** _fmt_
> 输出格式（txt、html、csv、tsv、json）。

# DESCRIPTION

**hledger incomestatement**（别名 **is**）显示一份利润表（损益报告），列出报告期内的收入与支出，并将二者的差额作为净收入展示。它是 hledger 标准财务报表之一，与资产负债表和现金流量表并列。

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

[hledger](/man/hledger)(1), [hledger-balancesheet](/man/hledger-balancesheet)(1)
