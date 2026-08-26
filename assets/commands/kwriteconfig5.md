# TAGLINE

向 KDE Plasma 5 配置文件写入值

# TLDR

设置**全局配置**键

```kwriteconfig5 --group [group_name] --key [key] [value]```

在**特定文件**中设置键

```kwriteconfig5 --file [path/to/file] --group [group_name] --key [key] [value]```

**删除**某个键

```kwriteconfig5 --group [group_name] --key [key] --delete```

为 Plasma 会话启用 **systemd 引导**

```kwriteconfig5 --file startkderc --group General --key systemdBoot true```

**窗口最大化时**隐藏标题栏

```kwriteconfig5 --file ~/.config/kwinrc --group Windows --key BorderlessMaximizedWindows true```

# SYNOPSIS

**kwriteconfig5** [_options_]

# PARAMETERS

**--file** _FILE_
> 要写入的配置文件

**--group** _GROUP_
> 配置组（节）

**--key** _KEY_
> 要设置的键名

**--delete**
> 删除该键而不是设置它

**--type** _TYPE_
> 值类型（bool、string、int 等）

# DESCRIPTION

**kwriteconfig5** 用于向 KDE Plasma 5 配置文件写入值。它支持以脚本方式修改 KDE 设置，无需手动编辑配置文件。

配置文件存放在 ~/.config/ 目录下，名称如 kdeglobals、kwinrc、plasmarc。更改可能需要重启相关应用程序或 Plasma 会话才能生效。

# CAVEATS

仅适用于 KDE 5；KDE 6 使用 kwriteconfig6。某些更改需要重启 Plasma 或注销登录才能生效。组名和键名区分大小写。

# HISTORY

kwriteconfig5 是 KDE Frameworks 5 的一部分，与负责读取设置的 kreadconfig5 相辅相成。它使 KDE 配置能够在脚本和 dotfile 管理中实现自动化。

# INSTALL

```apt: sudo apt install libkf5config-bin```

```pacman: sudo pacman -S kconfig5```

```apk: sudo apk add kconfig5```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kreadconfig5](/man/kreadconfig5)(1), [dconf](/man/dconf)(1)
