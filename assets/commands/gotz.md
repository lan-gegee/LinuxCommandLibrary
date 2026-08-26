# TAGLINE

面向跨时区团队的命令行时区信息工具

# TLDR

**显示**多个时区的当前时间

```gotz```

**显示**特定城市的时间

```gotz [city-name]```

**在不同时区间转换**时间

```gotz "[time]" [from-zone] [to-zone]```

**列出**所有支持的时区

```gotz --list```

# SYNOPSIS

**gotz** [_options_] [_timezone-or-query_]

# PARAMETERS

**-l, --list**
> 列出所有支持的时区

**-c, --config** _FILE_
> 配置文件路径

**-f, --format** _FORMAT_
> 时间格式字符串

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**gotz** 是一个用于处理时区的命令行工具。它可以显示不同地点的当前时间并在各时区之间转换时间，非常适合跨多个地区协作的团队使用。

该工具可以同时显示多个时区，并支持对城市名称进行模糊匹配。

# EXAMPLES

显示已配置的时区：
```gotz```

显示东京的时间：
```gotz tokyo```

将纽约下午 3 点转换为东京时间：
```gotz "3pm" America/New_York Asia/Tokyo```

# CONFIGURATION

配置文件（~/.config/gotz/config.toml）：

```toml
[zones]
default = ["America/New_York", "Europe/London", "Asia/Tokyo"]
```

# CAVEATS

时区名称必须遵循 IANA 数据库。模糊匹配可能返回意料之外的结果。夏令时切换可能造成混淆。

# HISTORY

**gotz** 的创建目的是为分布式团队简化时区转换，提供一种替代在线工具的快速 CLI 方案。

# INSTALL

```brew: brew install gotz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[date](/man/date)(1), [tzselect](/man/tzselect)(1), [timedatectl](/man/timedatectl)(1)
