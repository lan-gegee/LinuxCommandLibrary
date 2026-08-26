# TAGLINE

GnuCash 报表和报价的命令行界面

# TLDR

**更新所有证券的报价**

```gnucash-cli --quotes get [file.gnucash]```

**显示 Finance::Quote 的版本和数据源**

```gnucash-cli --quotes info```

**导出特定证券的报价**

```gnucash-cli --quotes dump [namespace] [symbol1] [symbol2]```

**列出可用的报表**

```gnucash-cli --report list```

**运行一个报表**

```gnucash-cli --report run --name "[Balance Sheet]" [file.gnucash]```

**将报表导出到文件**

```gnucash-cli --report run --name "[report]" --output-file [output.html] [file.gnucash]```

# SYNOPSIS

**gnucash-cli** [_options_] [_datafile_]

# PARAMETERS

**-h**, **--help**
> 显示帮助消息。

**-v**, **--version**
> 显示 GnuCash 版本。

**-Q**, **--quotes** _command_
> 报价模式：info、get、dump。

**--namespace** _regexp_
> 商品命名空间的正则表达式（用于 quotes dump）。

**-R**, **--report** _command_
> 报表模式：run、show、list。

**--name** _name_
> run 命令使用的报表名称。

**--output-file** _file_
> 报表的输出文件。

**--export-type** _type_
> 导出格式类型。

**--debug**
> 启用调试模式。

**--extra**
> 启用开发者/调试功能。

**--log** _arg_
> 日志级别覆盖（可多次指定）。

**--logto** _file_
> 日志写入的文件（可用 "stderr" 或 "stdout" 表示对应流）。

**-V**, **--verbose**
> 显示扩展的 Finance::Quote 参数（与 quotes dump 配合使用）。

# DESCRIPTION

**gnucash-cli** 是 GnuCash（一款个人及小型企业财务记账应用）的命令行界面。它有两种工作模式：用于获取和更新证券价格的报价模式，以及用于生成财务报表的报表模式。这样无需打开图形界面即可自动完成价格更新和报表生成。

# CAVEATS

报价功能需要正确配置 Finance::Quote。MySQL 和 PostgreSQL 后端支持数据库 URI。

# INSTALL

```apt: sudo apt install gnucash```

```dnf: sudo dnf install gnucash```

```pacman: sudo pacman -S gnucash```

```apk: sudo apk add gnucash```

```zypper: sudo zypper install gnucash```

```nix: nix profile install nixpkgs#gnucash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnucash](/man/gnucash)(1), [ledger](/man/ledger)(1)
