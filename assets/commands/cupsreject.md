# TAGLINE

阻止打印机接受新任务

# TLDR

让打印机**拒绝新的打印任务**

```cupsreject [printer_name]```

**附带原因信息拒绝**

```cupsreject -r "[printer offline]" [printer_name]```

# SYNOPSIS

**cupsreject** [_options_] _destination(s)_

# PARAMETERS

**-r** _reason_
> 设置拒绝的原因信息。

**-h** _server[:port]_
> 连接到指定的服务器。

# DESCRIPTION

**cupsreject** 指示打印系统拒绝指定目标的新打印任务。队列中已有的任务不受影响。

用 **cupsaccept** 可重新开始接受任务。需要管理员权限。

# INSTALL

```apt: sudo apt install cups-client```

```dnf: sudo dnf install cups-client```

```pacman: sudo pacman -S cups```

```apk: sudo apk add cups```

```zypper: sudo zypper install cups-client```

```brew: brew install cups```

```nix: nix profile install nixpkgs#cups```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cupsaccept](/man/cupsaccept)(1), [cupsdisable](/man/cupsdisable)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/cups)```

```[Homepage](https://www.cups.org)```

```[Documentation](https://openprinting.github.io/cups/)```

<!-- verified: 2026-06-26 -->
