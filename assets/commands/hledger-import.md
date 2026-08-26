# TAGLINE

将来自 CSV 或其他数据文件的新交易添加到日志中

# TLDR

**从一个或多个 CSV 文件导入交易**

```hledger import [bank.csv]```

**预览将要导入的内容，而不修改日志**

```hledger import --dry-run [bank.csv]```

**导入到指定的日志文件**

```hledger import -f [ledger.journal] [bank.csv]```

**使用指定的 CSV 规则文件**

```hledger import --rules [bank.rules] [bank.csv]```

**从日志 rules/ 目录下的每个 .rules 文件导入**

```hledger import```

**将已有交易标记为已导入，但不实际导入它们**

```hledger import --catchup [bank.csv]```

# SYNOPSIS

**hledger import** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要从中导入的数据文件（CSV/SSV/TSV 或任何 hledger 可读取的格式）。若省略，则从日志 **rules/** 目录下找到的每个 **.rules** 文件导入。

**-f**, **--file** _[FMT:]FILE_
> 用于追加所导入交易的日志文件。默认为 $LEDGER_FILE 或 ~/.hledger.journal。

**--rules** _RULESFILE_
> 使用该文件中定义的规则来转换 CSV/SSV/TSV 输入。若未指定，hledger 会在每个 FILE.csv 旁边查找 **FILE.csv.rules**。

**-g**, **--get**
> 先通过运行 **get** 命令（任何 **data/getdata** 和 **prices/getprices** 脚本）获取新数据。

**--catchup**
> 不导入任何内容；只把当前所有交易记录为已导入，使以后的导入跳过它们。

**--dry-run**
> 以日志格式显示将被导入的交易，但不实际写入。

**--layout=hledger1|**_COL_
> 分录金额如何对齐：像 hledger 1 那样右对齐（默认），或让小数点在第 _COL_ 列对齐。

# DESCRIPTION

**hledger import** 在一个或多个 CSV（或其他受支持格式的）数据文件中检测新交易，并将它们追加到主日志（应采用 journal 格式）。它最常用于处理从银行下载的 CSV 文件，转换时使用与 hledger 文件读取器通常相同的 CSV 规则。

与通过管道将 CSV 文件传给 **hledger print** 不同，**import** 会避免重复导入已见过的交易：对于每个输入文件，它会将已处理的最新记录日期保存在旁边的隐藏文件 **.latest.FILE** 中，下次运行时跳过该日期及更早的内容。首次从某个文件导入前，建议先使用 **--dry-run** 预览将要添加的内容。

若不带文件参数运行，**import** 会查看主日志旁的 **rules/** 目录并读取其中找到的每个 **.rules** 文件（跳过名称以 **.** 或 **_** 开头的文件），将每条规则应用到对应的数据文件。

# CAVEATS

正确的字段映射通常需要配套的 CSV 规则文件；没有规则文件时，hledger 会退回到"每列一个字段"的通用读取方式，很少能产生有用的账户名。重叠检测依赖跨下载稳定的文件名、日期和行序；如果经常导入，偶发的违规通常无害。本命令属于 hledger 套件。

# HISTORY

**import** 加入 **hledger** 的目的，是将银行/CSV 对账单下载自动记录到纯文本日志中，免去手动复制粘贴和重复条目。

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

[hledger](/man/hledger)(1), [hledger-add](/man/hledger-add)(1), [hledger-print](/man/hledger-print)(1)
