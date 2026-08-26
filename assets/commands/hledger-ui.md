# TAGLINE

hledger 的终端界面

# TLDR

**启动 TUI**

```hledger-ui```

**打开指定日志**

```hledger-ui -f [ledger.journal]```

**从指定日期开始**

```hledger-ui --begin [2024-01-01]```

**显示特定账户**

```hledger-ui [assets:bank]```

**监视文件变化**

```hledger-ui --watch```

**在资产负债表界面启动**

```hledger-ui --bs```

**使用指定的显示主题**

```hledger-ui --theme [dark]```

# SYNOPSIS

**hledger-ui** [_options_] [_patterns_]

# PARAMETERS

_PATTERNS_
> 要显示的账户匹配模式。

**-f**, **--file** _[FMT:]FILE_
> 要使用的日志文件。默认为 $LEDGER_FILE 或 ~/.hledger.journal。

**-w**, **--watch**
> 当日志文件发生变化时自动重新加载并更新显示。

**-b**, **--begin** _DATE_
> 只显示此日期及之后的分录/交易。

**-e**, **--end** _DATE_
> 只显示此日期之前的分录/交易。

**-t**, **--tree**
> 以层级树状结构显示账户。

**-l**, **--flat**
> 以扁平列表显示账户（默认）。

**--theme** _THEME_
> 使用的显示主题：light、dark、terminal 或 greenterm。

**--cash**, **--bs**, **--is**, **--all**
> 启动时进入现金账户、资产负债表、利润表或全部账户界面，而不是默认的账户界面。

**--register** _ACCTREGEX_
> 在第一个匹配账户的账簿（register）界面启动。

**--change**
> 启动时显示期间余额变动，而不是历史（期末）余额。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hledger-ui** 是 hledger 的终端（基于 curses）界面。它提供一种高效的全窗口方式，可交互地浏览账户、交易和报表，并具备有限的数据录入能力。

该 TUI 支持键盘和鼠标导航，可以从账户界面下钻到账簿和单笔交易，随时键入查询进行过滤，并在账户/账簿/交易界面之间切换。配合 **-w/--watch**，只要底层日志文件在磁盘上发生变化，它就会自动重新加载。

# KEY BINDINGS

**?**
> 显示帮助对话框，列出当前界面的所有按键。

**arrows**, **j**/**k**/**h**/**l**, **CTRL-n**/**p**/**f**/**b**
> 上/下/左/右移动（vi 和 emacs 风格的等价按键均可用）。

**/**
> 打开查询过滤器编辑器。

**a**
> 运行 hledger 的 **add** 命令记录一笔新交易。

**g**
> 从磁盘重新加载日志文件。

**t**
> 切换树状/扁平账户显示。

**B** / **V**
> 切换成本 / 市值转换。

**H**
> 在期间余额与历史余额之间切换。

**F**
> 切换预测模式，显示带未来日期的交易。

**E**
> 在 $EDITOR 中打开日志文件。

**q**, **ESCAPE**
> 退出，或返回上一层/顶层界面。

# CAVEATS

需要至少支持基本颜色的终端才能获得良好体验。部分界面和按键假定日志为 journal 格式；其他格式的支持有限。本命令属于 hledger 套件。

# HISTORY

hledger-ui 作为 hledger 命令行与 Web（**hledger-web**）界面的补充而开发，基于 **brick** TUI 库构建。

# INSTALL

```apt: sudo apt install hledger-ui```

```dnf: sudo dnf install hledger-ui```

```pacman: sudo pacman -S hledger-ui```

```apk: sudo apk add hledger-ui```

```zypper: sudo zypper install hledger-ui```

```nix: nix profile install nixpkgs#hledger-ui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hledger](/man/hledger)(1), [hledger-web](/man/hledger-web)(1), [ledger](/man/ledger)(1)
