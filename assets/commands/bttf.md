# TAGLINE

日期/时间运算、解析与格式化 CLI

# TLDR

**显示**当前时间辅助信息 / 默认输出

```bttf```

**获取子命令帮助**

```bttf --help```

**子命令的帮助**

```bttf [command] --help```

# SYNOPSIS

**bttf** [*command*] [*options*]

# DESCRIPTION

**bttf**（前身为 **biff**）是 BurntSushi 的命令行工具集，用于 datetime 解析、格式化、算术运算以及带时区的计算。当单用 **date** 不够顺手时，它是一个对脚本友好的补充。locale 配置技巧参见上游用户指南。

# PARAMETERS

命令涵盖 parse/format/add/duration 类操作——功能面有意做得较宽。请以 **bttf --help** 和各子命令的帮助信息作为你所用版本的权威参考。

# CAVEATS

在某些环境中可能需要显式配置 locale 支持。此工具曾名为 **biff**；重命名后请更新脚本。

# INSTALL

```brew: brew install bttf```

```nix: nix profile install nixpkgs#bttf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[date](/man/date)(1), [timedatectl](/man/timedatectl)(1)

# RESOURCES

```[Source code](https://github.com/BurntSushi/bttf)```

<!-- verified: 2026-07-19 -->
