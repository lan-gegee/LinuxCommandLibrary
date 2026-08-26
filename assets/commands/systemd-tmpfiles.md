# TAGLINE

管理临时文件和目录

# TLDR

按配置**创建**文件和目录

```systemd-tmpfiles --create```

按老化参数**清理**文件和目录

```systemd-tmpfiles --clean```

按配置**移除**文件和目录

```systemd-tmpfiles --remove```

对用户级配置**应用**操作

```systemd-tmpfiles --create --user```

**执行**标记为早期启动的行

```systemd-tmpfiles --create --boot```

仅对特定前缀下的路径**应用**

```systemd-tmpfiles --create --prefix=[/tmp]```

一次调用中完成**创建、清理和移除**

```systemd-tmpfiles --create --clean --remove```

# SYNOPSIS

**systemd-tmpfiles** [_options_] [_configfile_...]

# PARAMETERS

**--create**
> 按配置创建文件和目录

**--clean**
> 清理超过配置时长的文件

**--remove**
> 移除文件和目录

**--user**
> 应用用户配置

**--boot**
> 执行启动时的条目

**--purge**
> 删除由指定配置文件创建的所有文件和目录

**--prefix** _path_
> 只应用路径以指定前缀开头的规则（可重复）

**--exclude-prefix** _path_
> 忽略路径以指定前缀开头的规则（可重复）

**-E**
> 排除 /dev、/proc、/run 和 /sys 层级的快捷方式

**--root** _path_
> 为所有路径加上给定的备用根目录前缀

**--replace** _path_
> 用命令行参数替代指定的配置文件

**--cat-config**
> 将配置文件的内容打印到标准输出

**--no-pager**
> 不将输出通过分页器显示

**-h**, **--help**
> 打印帮助文本并退出

# DESCRIPTION

**systemd-tmpfiles** 创建、删除和清理易失性的临时文件和目录。**/etc/tmpfiles.d/**、**/usr/lib/tmpfiles.d/** 及相关目录中的配置文件定义了要采取的操作。

该工具在系统启动期间由 systemd 服务自动调用。通常只有在测试配置或进行一次性清理时才需要手动执行。

# CAVEATS

由于 systemd 会自动处理，通常无需手动运行。可以在一次调用中组合使用 --create、--clean 和 --remove。配置中的语法错误可能导致清理无法正常进行。基于时长的清理需要正确配置的时间值。本命令是 systemd 套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1)
