# TAGLINE

以银行对账单格式显示单个账户的交易和滚动余额

# TLDR

**显示账户流水**

```hledger aregister [checking]```

**使用指定账簿文件显示**

```hledger aregister -f [journal.ledger] [assets:bank]```

**显示月度汇总**

```hledger aregister [checking] --monthly```

**包含报告期之前的历史余额**

```hledger aregister [checking] -H```

**限制输出宽度**

```hledger aregister [checking] -w [80]```

**包含净变动为零的交易**

```hledger aregister [checking] -E```

**输出为 CSV**

```hledger aregister [checking] -O csv```

# SYNOPSIS

**hledger** **aregister** | **areg** [_options_] _account_

# PARAMETERS

**-f**, **--file** _file_
> 使用指定的账簿文件。

**--daily**
> 显示每日汇总。

**--weekly**
> 显示每周汇总。

**--monthly**
> 显示每月汇总。

**-H**, **--historical**
> 包含报告期之前的余额。

**-E**, **--empty**
> 显示净变动为零的交易。

**--txn-dates**
> 按交易日期而非分录日期过滤。

**--depth** _n_
> 限制账户层级深度。

**-w**, **--width** _n_
> 设置输出宽度。

**-O**, **--output-format** _fmt_
> 输出格式：txt、csv、tsv、html、fods、json。

**--quarterly**
> 显示每季度汇总。

**--yearly**
> 显示每年汇总。

# DESCRIPTION

**hledger aregister**（别名 **areg**）以银行对账单格式显示单个账户的交易和滚动余额。每笔交易占一行，包含日期、描述、涉及的其他账户、金额和滚动余额。与每个分录显示一行的 **register** 不同，aregister 会把同一交易的各条分录归为一行。账户可以用完整名称指定，也可以用一个不区分大小写的正则表达式匹配（按字母序取第一个匹配账户）。

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

[hledger](/man/hledger)(1), [hledger-balance](/man/hledger-balance)(1), [hledger-print](/man/hledger-print)(1)
