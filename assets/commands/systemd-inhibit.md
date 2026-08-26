# TAGLINE

阻止系统休眠或关机

# TLDR

**列出**所有活动的抑制锁

```systemd-inhibit --list```

在运行命令期间**阻止**系统关机

```systemd-inhibit --what shutdown [command]```

**防止**系统休眠或空闲

```systemd-inhibit --what sleep:idle wget [https://example.com/file]```

在脚本退出前**忽略**合上笔记本盖子的动作

```systemd-inhibit --what sleep:handle-lid-switch [path/to/script]```

在命令运行期间**忽略**电源键按下

```systemd-inhibit --what handle-power-key [command]```

**说明**是谁、为何创建了抑制器

```systemd-inhibit --who [$USER] --why [reason] --what [operation] [command]```

# SYNOPSIS

**systemd-inhibit** [_options_] [_command_] [_arguments_]

# PARAMETERS

**--list**
> 列出所有活动的抑制锁

**--what _operation_**
> 要抑制的操作（shutdown、sleep、idle、handle-power-key、handle-suspend-key、handle-hibernate-key、handle-lid-switch）

**--who _name_**
> 持锁者的描述性名称

**--why _reason_**
> 持锁原因的描述性说明

**--mode _mode_**
> 可为 "block" 或 "delay"

# DESCRIPTION

**systemd-inhibit** 创建抑制锁，可以在命令运行期间阻止或延迟系统休眠、关机以及硬件按键处理。锁会持续到命令执行结束为止。

多个操作之间用冒号分隔即可同时指定。**--list** 选项显示来自所有来源的活动抑制器，而不仅仅是本工具创建的那些。

# CAVEATS

抑制锁应谨慎使用，以免妨碍系统正常运行。"delay" 模式只能短暂推迟操作。某些操作需要相应的权限。本命令是 systemd 套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [loginctl](/man/loginctl)(1)
