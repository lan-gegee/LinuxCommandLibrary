# TAGLINE

允许打印队列接受任务

# TLDR

允许打印机**接受打印任务**

```cupsaccept [printer_name]```

**附带原因信息**接受任务

```cupsaccept -r "[reason]" [printer_name]```

# SYNOPSIS

**cupsaccept** [_options_] _destination(s)_

# PARAMETERS

**-E**
> 加密与服务器的连接。

**-r** _reason_
> 设置接受任务的原因信息。

**-h** _server[:port]_
> 连接到指定的服务器。

# DESCRIPTION

**cupsaccept** 指示打印系统开始接受指定目标的打印任务。其效果与 **cupsreject** 相反。

该命令是 **accept** 的别名，需要管理员权限。

# INSTALL

```apt: sudo apt install cups-client```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cupsreject](/man/cupsreject)(1), [cupsenable](/man/cupsenable)(1), [cupsdisable](/man/cupsdisable)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/cups)```

```[Homepage](https://www.cups.org)```

```[Documentation](https://openprinting.github.io/cups/)```

<!-- verified: 2026-06-26 -->
