# TAGLINE

基于 systemd 的系统更新控制器

# TLDR

**检查**更新

```updatectl check```

**更新**到最新版本

```updatectl update```

**列出**更新目标

```updatectl list```

显示**目标**数据

```updatectl list [target]```

以**离线**方式列出目标

```updatectl --offline list [target]```

更新后**重启**

```updatectl --reboot update [target]```

**清理**旧版本

```updatectl vacuum [target]```

# SYNOPSIS

**updatectl** [_OPTIONS_] _COMMAND_ [_TARGET_]

# COMMANDS

**check**
> 检查可用的更新

**update**
> 更新到最新版本

**list**
> 显示更新目标及版本

**vacuum**
> 清理旧版本

# PARAMETERS

**--offline**
> 使用本地数据，不从网络获取

**--reboot**
> 应用更新后重启

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**updatectl** 是一款基于 systemd 的系统更新工具。它负责管理系统更新，包括检查新版本、应用更新以及清理旧版本。

该工具围绕更新目标运作，每个目标代表一个可独立更新的系统组件。

# CAVEATS

仅限基于 systemd 的系统。部分操作需要 root 权限。某些更新可能需要重启才能生效。

# SEE ALSO

[systemctl](/man/systemctl)(1)
