# TAGLINE

显示账簿中的账户余额

# TLDR

**显示所有余额**

```hledger balance```

**只显示资产**

```hledger balance assets```

**以层级结构显示**

```hledger balance --tree```

**以扁平列表显示**

```hledger balance --flat```

**按月分解**

```hledger balance -M```

**显示百分比**

```hledger balance --percent```

# SYNOPSIS

**hledger balance** [_options_] [_patterns_]

# PARAMETERS

_PATTERNS_
> 账户名称模式。

**--tree**
> 层级显示。

**--flat**
> 扁平账户列表。

**-M**, **--monthly**
> 按月分解。

**-Q**, **--quarterly**
> 按季度分解。

**-Y**, **--yearly**
> 按年分解。

**--percent**
> 显示百分比。

**--depth** _N_
> 限制账户层级深度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hledger balance** 显示账簿中的账户余额。它汇总所有匹配账户的借方和贷方。

该命令支持按账户模式、时间段和显示格式过滤。它是检查财务状况的主要工具。

# CAVEATS

零余额默认隐藏。需要有效的账簿。属于 hledger 工具套件。

# HISTORY

balance 是 **hledger** 中用于在纯文本记账中显示账户汇总的核心命令。

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

[hledger](/man/hledger)(1), [hledger-incomestatement](/man/hledger-incomestatement)(1)
