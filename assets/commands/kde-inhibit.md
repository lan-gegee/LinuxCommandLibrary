# TAGLINE

在指定命令运行期间暂时抑制各种 KDE Plasma 桌面功能

# TLDR

命令运行期间抑制**电源管理**

```kde-inhibit --power [command] [arguments]```

抑制**屏幕保护程序**

```kde-inhibit --screenSaver [command] [arguments]```

抑制**色彩校正**（夜间模式）

```kde-inhibit --colorCorrect [command]```

# SYNOPSIS

**kde-inhibit** [_options_] _command_ [_arguments_]

# PARAMETERS

**--power**
> 抑制电源管理（阻止睡眠/挂起）

**--screenSaver**
> 抑制屏幕保护程序激活

**--colorCorrect**
> 抑制色彩校正（夜间光/夜间模式）

# DESCRIPTION

**kde-inhibit** 在指定命令运行期间暂时抑制各种 KDE Plasma 桌面功能。这可以防止桌面干扰长时间运行的任务或媒体播放。

当命令退出时，抑制会自动结束。可以通过指定多个选项来组合多种抑制类型。

# CAVEATS

只在 KDE Plasma 桌面环境中有效。需要命令保持运行；命令退出后抑制即结束。对立即转入后台的命令无效。

# HISTORY

kde-inhibit 是 KDE 命令行工具的一部分，让脚本和应用程序无需直接进行 DBus 交互即可控制桌面行为。

# INSTALL

```apt: sudo apt install kde-cli-tools```

```dnf: sudo dnf install kde-cli-tools```

```pacman: sudo pacman -S kde-cli-tools```

```apk: sudo apk add kde-cli-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-inhibit](/man/systemd-inhibit)(1), [caffeine](/man/caffeine)(1)
