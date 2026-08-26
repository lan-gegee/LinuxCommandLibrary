# TAGLINE

读取 KDE Plasma 5 配置文件中的值

# TLDR

从**全局配置**读取键值

```kreadconfig5 --group [group_name] --key [key_name]```

从**指定文件**读取键值

```kreadconfig5 --file [path/to/file] --group [group_name] --key [key_name]```

检查 **systemd 启动**设置

```kreadconfig5 --file startkderc --group General --key systemdBoot```

# SYNOPSIS

**kreadconfig5** [_options_]

# PARAMETERS

**--file** _FILE_
> 要读取的配置文件

**--group** _GROUP_
> 配置组（节）

**--key** _KEY_
> 要读取的键名

**--default** _VALUE_
> 键不存在时使用的默认值

# DESCRIPTION

**kreadconfig5** 从 KDE Plasma 5 配置文件中读取值。KConfig 是 KDE 的配置系统，将设置以 INI 风格的文件存储，其中包含组和键值对。

配置文件通常存储在 ~/.config/ 中，文件名如 kdeglobals、kwinrc、plasmarc 等。该工具适合编写涉及 KDE 设置的脚本和自动化任务。

# CAVEATS

仅适用于 KDE 5；KDE 6 使用 kreadconfig6。文件路径可以是相对于 ~/.config 的路径或绝对路径。组和键名区分大小写。

# HISTORY

kreadconfig5 是 KDE Frameworks 的一部分，提供对 KDE 配置系统的命令行访问。它与 kwriteconfig5 互补，方便在脚本中读取设置。

# INSTALL

```apt: sudo apt install libkf5config-bin```

```pacman: sudo pacman -S kconfig5```

```apk: sudo apk add kconfig5```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kwriteconfig5](/man/kwriteconfig5)(1), [dconf](/man/dconf)(1)
