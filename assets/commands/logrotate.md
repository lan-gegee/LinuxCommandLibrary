# TAGLINE

通过轮转、压缩、删除和邮寄来管理日志文件

# TLDR

手动**强制**轮转

```sudo logrotate --force [/etc/logrotate.conf]```

**调试模式**——只显示将要执行的操作而不实际更改

```logrotate --debug [/etc/logrotate.conf]```

**详细**轮转

```sudo logrotate --verbose [/etc/logrotate.conf]```

使用**自定义状态**文件

```sudo logrotate --state [/var/lib/logrotate/status] [/etc/logrotate.conf]```

将**详细日志**输出到文件

```sudo logrotate --verbose --log [/var/log/logrotate.log] [/etc/logrotate.conf]```

# SYNOPSIS

**logrotate** [_options_] _config_file_

# DESCRIPTION

**logrotate** 通过轮转、压缩、删除和邮寄来管理日志文件。它可以防止日志占用过多磁盘空间，通常通过 cron 每天运行一次。

# PARAMETERS

**-f**, **--force**
> 即使条件不满足也强制轮转

**-d**, **--debug**
> 调试模式；只显示将要执行的操作而不实际更改

**-v**, **--verbose**
> 详细输出

**-s**, **--state** _FILE_
> 使用替代的状态文件（默认：/var/lib/logrotate/status）

**-l**, **--log** _FILE_
> 将详细日志输出到文件

**--mail** _COMMAND_
> 使用指定命令邮寄日志

# CAVEATS

/etc/logrotate.d/ 中的配置文件会被主配置包含。状态文件记录每个日志上次轮转的时间。通常通过 cron 或 systemd 定时器每天运行。

# INSTALL

```apt: sudo apt install logrotate```

```dnf: sudo dnf install logrotate```

```pacman: sudo pacman -S logrotate```

```apk: sudo apk add logrotate```

```zypper: sudo zypper install logrotate```

```brew: brew install logrotate```

```nix: nix profile install nixpkgs#logrotate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[logger](/man/logger)(1), [journalctl](/man/journalctl)(1)
