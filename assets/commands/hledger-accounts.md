# TAGLINE

列出账簿中的账户名称

# TLDR

**列出所有账户**

```hledger accounts```

**从指定文件列出账户**

```hledger accounts -f [journal.ledger]```

**列出匹配模式的账户**

```hledger accounts [expenses]```

**限制层级深度列出**

```hledger accounts --depth [2]```

**显示账户树**

```hledger accounts --tree```

**仅列出使用过的账户**

```hledger accounts --used```

**仅列出已声明的账户**

```hledger accounts --declared```

**连同账户类型一起显示**

```hledger accounts --types```

**去掉账户名的前 N 个组成部分**

```hledger accounts --drop [1]```

# SYNOPSIS

**hledger** **accounts** [_options_] [_query_]

# PARAMETERS

**-f**, **--file** _file_
> 使用指定的账簿文件。

**--depth** _n_
> 限制显示的账户层级深度。

**--tree**
> 以树形结构显示账户。

**--used**
> 仅显示有交易记录的账户。

**--declared**
> 仅显示用 account 指令声明的账户。

**--flat**
> 以完整名称的扁平列表形式显示账户（默认）。

**--drop** _n_
> 扁平模式下省略账户名的前 n 个组成部分。

**--types**
> 显示每个账户的类型（如果已知）。

# DESCRIPTION

**hledger accounts** 列出账簿中的账户名称。它是 hledger 纯文本记账工具的一部分。它显示已声明（通过 account 指令）、有分录过账或两者兼有的账户（默认行为）。账户可以按查询模式过滤、按深度限制，并以扁平列表或树形方式显示。

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

[hledger](/man/hledger)(1), [hledger-balance](/man/hledger-balance)(1), [hledger-print](/man/hledger-print)(1), [ledger](/man/ledger)(1)
