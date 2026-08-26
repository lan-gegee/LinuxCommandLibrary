# TAGLINE

显示标准资产负债表报告

# TLDR

**显示资产负债表**

```hledger balancesheet```

**按月对比**

```hledger balancesheet -M```

**按年对比**

```hledger balancesheet -Y```

**以百分比显示**

```hledger balancesheet --percent```

**树状视图**

```hledger balancesheet --tree```

# SYNOPSIS

**hledger balancesheet** [_options_]

# PARAMETERS

**-M**, **--monthly**
> 按月细分。

**-Q**, **--quarterly**
> 按季度细分。

**-Y**, **--yearly**
> 按年细分。

**--tree**
> 层级视图。

**--flat**
> 扁平列表视图。

**--percent**
> 以百分比显示。

**-H**, **--historical**
> 显示期末余额（累计）。默认显示期间变动余额。

**--cumulative**
> 显示自报告起始的累计余额，忽略任何期初余额。

**-T**, **--row-total**
> 为每行添加合计（Total）列。

**-A**, **--average**
> 为每行添加平均值（Average）列。

**--no-total**
> 省略最后的总计行。

**-d**, **--depth** _N_
> 将账户树中深度超过 _N_ 的层级聚合在一起。

**--pretty**
> 使用 Unicode 制表符（框线字符）。

**--transpose**
> 交换行与列。

**--invert**
> 将所有金额符号取反。

**-b** _DATE_
> 起始日期。

**-e** _DATE_
> 结束日期。

**-o**, **--output-file** _FILE_
> 将输出写入 _FILE_（根据扩展名推断格式）。

**-O**, **--output-format** _FMT_
> 强制指定输出格式：`txt`、`csv`、`tsv`、`html`、`json`、`fods`、`sql`。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hledger balancesheet** 显示一份标准资产负债表报告。它展示资产、负债，并计算净资产。

该报告遵循会计惯例，资产在一侧，负债在另一侧。净资产等于资产减去负债。

# CAVEATS

需要有匹配查询 `type:A`（资产）和 `type:L`（负债）的账户，或名为 `assets` / `liabilities` 的顶层账户。若存在权益类账户，请考虑使用 **hledger balancesheetequity** 获取完整的三段式报表。别名：**bs**。

# HISTORY

Balancesheet 是 **hledger** 中用于查看某一时点财务状况的标准报表。

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

[hledger](/man/hledger)(1), [hledger-balance](/man/hledger-balance)(1), [hledger-incomestatement](/man/hledger-incomestatement)(1)
