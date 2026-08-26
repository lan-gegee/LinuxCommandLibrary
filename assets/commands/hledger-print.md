# TAGLINE

输出日志中的交易

# TLDR

**打印所有交易**

```hledger print```

**打印特定账户**

```hledger print [account-pattern]```

**打印日期范围**

```hledger print -b [2024-01-01] -e [2024-12-31]```

**按成本打印**

```hledger print --cost```

**以 CSV 输出**

```hledger print -O csv```

# SYNOPSIS

**hledger print** [_options_] [_patterns_]

# PARAMETERS

_PATTERNS_
> 账户或描述匹配模式。

**-b** _DATE_
> 起始日期。

**-e** _DATE_
> 结束日期。

**--cost**
> 转换为成本基准。

**--explicit**
> 使金额显式化。

**-O** _FORMAT_
> 输出格式（txt、csv）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hledger print** 输出日志中的交易。它会重现交易记录，可按需过滤或转换。

该命令适合提取交易的子集或在格式之间转换。输出为合法的 journal 语法。

# CAVEATS

默认以 journal 格式输出。过滤会减少输出内容。本命令属于 hledger 套件。

# HISTORY

Print 是 **hledger** 中用于显示和从日志中提取交易的核心命令。

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

[hledger](/man/hledger)(1), [hledger-import](/man/hledger-import)(1)
