# TAGLINE

个人及小型企业财务记账软件

# TLDR

**启动 GnuCash**

```gnucash```

**打开指定文件**

```gnucash [file.gnucash]```

**启动时不加载上次的文件**

```gnucash --nofile```

**启用调试模式**

```gnucash --debug```

**显示版本**

```gnucash --version```

**启用额外功能**

```gnucash --extra```

# SYNOPSIS

**gnucash** [_options_] [_datafile_]

# PARAMETERS

**-h**, **--help**
> 显示帮助消息。

**-v**, **--version**
> 显示 GnuCash 版本。

**--nofile**
> 不加载上次打开的文件。

**--debug**
> 启用调试模式。

**--extra**
> 启用额外/开发功能。

**--log** _arg_
> 日志级别覆盖（如 "modulename=debug"）。

**--logto** _file_
> 日志写入的文件。

**--help-gtk**
> 显示 GTK 选项。

# DESCRIPTION

**GnuCash** 是一款面向个人和小型企业的财务记账应用。它支持复式记账、股票/债券/共同基金账户、定期交易和财务报表。**GnuCash** 可以导入 OFX、QIF 和 CSV 文件，并跟踪收入、支出、银行账户和投资。

# CONFIGURATION

**~/.local/share/gnucash/**
> 用户数据目录，包含保存的报表、自定义设置和元数据。

**~/.config/gnucash/**
> 用户配置目录，存放偏好设置和 UI 状态。

# INSTALL

```apt: sudo apt install gnucash```

```dnf: sudo dnf install gnucash```

```pacman: sudo pacman -S gnucash```

```apk: sudo apk add gnucash```

```zypper: sudo zypper install gnucash```

```nix: nix profile install nixpkgs#gnucash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnucash-cli](/man/gnucash-cli)(1), [ledger](/man/ledger)(1), [hledger](/man/hledger)(1)

# RESOURCES

```[Source code](https://github.com/Gnucash/gnucash)```

```[Homepage](https://www.gnucash.org/)```

<!-- verified: 2026-07-17 -->
