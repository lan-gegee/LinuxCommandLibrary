# TAGLINE

交互式录入新交易并将其追加到账簿文件

# TLDR

**交互式添加交易**

```hledger add```

**添加到指定文件**

```hledger add -f [journal.ledger]```

**不允许创建新账户**

```hledger add --no-new-accounts```

**从命令行预填最初的提示项**（日期、描述、账户、金额）

```hledger add [today] ["best buy"] [expenses:supplies] [$20]```

**录入期间忽略余额断言**

```hledger add -I```

# SYNOPSIS

**hledger** **add** [_options_] [_entry-fields_]

# PARAMETERS

**-f**, **--file** _file_
> 使用指定的账簿文件（条目会追加到给出的第一个文件中）。

**--no-new-accounts**
> 不允许创建新账户；只能输入账簿中已使用过的账户。

**--layout=hledger1|**_COL_
> 分录金额的对齐方式：像 hledger 1 那样右对齐（默认），或将小数点对齐到第 COL 列。

**-I**, **--ignore-assertions**
> 录入金额时禁用余额断言检查。

# DESCRIPTION

**hledger add** 交互式提示录入新交易，并将它们追加到账簿文件。它会依次引导你输入日期（默认今天，可接受 "yesterday"/"today"/"tomorrow" 等词）、可选的交易代码、描述、账户名称和金额，并提供基于已有条目的 Tab 补全。

它尽量提供有用的默认值，会以描述最相似且日期最近的既有交易作为模板。前几个提示项的初始值也可以作为命令行参数给出。录入过程中可以使用 Readline 风格的编辑按键；在任何提示处输入 **<** 可回退一步。金额可以包含余额断言（**AMOUNT = BALANCE**）或余额赋值（**= BALANCEAMOUNT**），hledger 在每次输入金额后会重新校验账簿的余额断言，拒绝会导致失败的断言。完成录入后输入 **.**，或按下 Control-d 或 Control-c 结束。

# CAVEATS

这是少数几个会写入账簿文件的 hledger 命令之一（另见 **import**）；已有的交易永远不会被修改。它只适用于 journal 格式的文件，不适用于 timeclock 或 timedot 文件。**add** 不允许记录日期早于该账户现有余额赋值的分录；遇到这种情况可加 **-I** 运行来绕过。

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

[hledger](/man/hledger)(1), [hledger-import](/man/hledger-import)(1), [hledger-accounts](/man/hledger-accounts)(1)
