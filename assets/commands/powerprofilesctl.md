# TAGLINE

切换系统电源配置文件

# TLDR

**列出**可用的电源配置文件

```powerprofilesctl list```

**设置**电源配置文件

```powerprofilesctl set [performance|balanced|power-saver]```

# SYNOPSIS

**powerprofilesctl** [**list**|**set** _profile_|**get**]

# COMMANDS

**list**
> 列出所有可用的电源配置文件

**get**
> 获取当前活动的配置文件

**set _profile_**
> 设置活动的电源配置文件

# PARAMETERS

**profile**
> 配置文件名称：performance、balanced 或 power-saver

# DESCRIPTION

**powerprofilesctl** 通过 power-profiles-daemon 管理系统电源配置文件。它允许在性能模式与省电模式之间切换，以平衡能耗与系统响应速度。

配置文件会影响 CPU 调频策略、GPU 电源管理和其他硬件电源设置。守护进程通过 D-Bus 暴露配置文件，便于桌面环境集成。

# CAVEATS

需要 power-profiles-daemon 正在运行。可用配置取决于硬件支持。可能与其他电源管理工具（TLP 等）冲突。GNOME/KDE 通过图形设置界面集成了此功能。

# HISTORY

**power-profiles-daemon** 由 **Bastien Nocera** 为 freedesktop.org 开发。它为桌面环境提供了一个简单、标准化的电源管理接口。

# INSTALL

```apt: sudo apt install power-profiles-daemon```

```dnf: sudo dnf install power-profiles-daemon```

```pacman: sudo pacman -S power-profiles-daemon```

```apk: sudo apk add power-profiles-daemon```

```zypper: sudo zypper install power-profiles-daemon```

```nix: nix profile install nixpkgs#power-profiles-daemon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tlp](/man/tlp)(1), [cpupower](/man/cpupower)(1), [tuned-adm](/man/tuned-adm)(8)
