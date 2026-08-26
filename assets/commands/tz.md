# TAGLINE

交互式的终端时区助手

# TLDR

**显示已配置的时区**

```tz```

**带标签显示指定时区**

```TZ_LIST="Europe/Paris,EMEA;US/Central,US" tz```

**显示特定时区**

```tz "[America/New_York]"```

# SYNOPSIS

**tz** [_options_] [_zones..._]

# DESCRIPTION

**tz** 是一个交互式 TUI 程序，可同时显示你选定的多个时区的时间。它使用标准的 tz 数据库名称，可以通过 **TZ_LIST** 环境变量、配置文件或命令参数进行配置。对于跨分布式团队安排会议非常有用。

# CONFIGURATION

**~/.config/tz/conf.toml**
> 配置文件，支持自定义时区别名。

**TZ_LIST**
> 以分号分隔的时区列表，可选地用逗号设置别名（例如 `Europe/Paris,EMEA;US/Central,US`）。

# HISTORY

**tz** 由 **Arnaud Berthomier**（oz）开发，使用 **Go** 编写。

# INSTALL

```apk: sudo apk add tz```

```brew: brew install tz```

```nix: nix profile install nixpkgs#tz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timedatectl](/man/timedatectl)(1), [date](/man/date)(1), [tzupdate](/man/tzupdate)(1)
