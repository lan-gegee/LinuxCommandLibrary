# TAGLINE

显示软件包更新日志

# TLDR

查看软件包的**全部更新日志**

```dnf changelog [package]```

查看**某日期之后**的更新日志

```dnf changelog --since [date] [package]```

查看**最近 n 条**更新日志

```dnf changelog --count [number] [package]```

显示可升级软件包的**新增条目**

```dnf changelog --upgrades [package]```

# SYNOPSIS

**dnf changelog** [_options_] _package_

# DESCRIPTION

**dnf changelog** 显示软件包的更新日志（changelog），其中记录了各软件包版本包含的变更、bug 修复和安全更新。它是 dnf-plugins-core 的一部分，需要安装该插件。

更新日志由软件包维护者编写，可帮助了解版本之间的变化。在升级前查看安全修复、新功能或 bug 修正时特别有用。可以按日期或条数过滤更新日志以聚焦最近的变更，或使用 --upgrades 只查看可用更新相对于已装版本的新增内容。

# PARAMETERS

**--since** _date_
> 显示指定日期之后的条目

**--count** _n_
> 显示最近 n 条条目

**--upgrades**
> 仅显示可用升级的新增条目

**--help-cmd**
> 显示帮助

# CAVEATS

需要 dnf-plugins-core。更新日志是否可用取决于软件包维护者是否将其写入 RPM。

# SEE ALSO

[dnf](/man/dnf)(8), [rpm](/man/rpm)(8)

# RESOURCES

```[Source code](https://github.com/rpm-software-management/dnf-plugins-core)```

```[Documentation](https://dnf-plugins-core.readthedocs.io/en/latest/changelog.html)```

<!-- verified: 2026-07-11 -->
