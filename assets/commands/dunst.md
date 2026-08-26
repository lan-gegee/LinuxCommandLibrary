# TAGLINE

轻量级桌面通知守护进程

# TLDR

**启动 dunst** 通知守护进程

```dunst```

**使用自定义配置文件启动**

```dunst -config [path/to/dunstrc]```

**将通知打印到标准输出**并同时显示

```dunst -print```

**用一条示例通知测试 dunst**

```notify-send "Title" "Message body"```

**再次显示最近一条**通知

```dunstctl history-pop```

**切换勿扰模式**

```dunstctl set-paused toggle```

**以详细输出启动**

```dunst -verbosity debug```

**打印版本信息**

```dunst -v```

# SYNOPSIS

**dunst** [_-config file_] [_-print_] [_-verbosity level_] [_-startup_notification_]

# PARAMETERS

**-config** _file_
> 使用指定的配置文件。

**-print**
> 将通知打印到标准输出而不显示。

**-verbosity** _level_
> 设置详细程度：crit、warn、mesg、info、debug。

**-startup_notification**
> 启动时显示一条通知。

**-v**, **-version**
> 打印版本信息。

**-h**, **-help**
> 显示帮助信息。

# CONFIGURATION

**~/.config/dunst/dunstrc**
> 主配置文件，控制外观、行为、紧急度样式和通知规则。

# DESCRIPTION

**dunst** 是一个面向 X11 和 Wayland 的轻量级通知守护进程，按照 freedesktop.org 通知规范显示桌面通知。它可以通过配置文件高度定制，在平铺式窗口管理器环境中颇受欢迎。

通知以样式化的弹出框形式出现，其位置、大小、颜色、字体、图标和行为均可配置。Dunst 支持通知动作和紧急级别（low、normal、critical），并且可以基于规则在通知到达时执行脚本。

配置通过 **~/.config/dunst/dunstrc** 完成。该文件定义全局设置、按紧急度区分的样式，以及按应用名、摘要、正文或其他条件匹配通知的规则。规则可以修改通知外观或触发动作。

主要特性包括通知历史（通过 **dunstctl history-pop** 访问）、勿扰模式、用于与通知交互的键盘导航，以及通知动作支持。critical 级别的通知可以配置为持续显示直到确认。

Dunst 与 **dunstctl** 集成实现运行时控制，与 **dunstify** 集成发送具备通知替换和进度条等高级特性的通知。

# CAVEATS

通知守护进程由 **D-Bus 激活**，而 `org.freedesktop.Notifications` 名称同一时间只能由一个进程持有。如果桌面环境已经自带一个（GNOME 和 KDE 都是如此），dunst 要么拒绝启动，要么启动了却永远收不到任何通知，取决于谁先占用了该名称。这正是 dunst 多见于平铺式窗口管理器（它们不自带通知守护进程）旁的原因。

由此推论，通常情况下根本不需要手动启动 dunst：D-Bus 会在第一条通知到来时启动它。既把它加入自启脚本*又*依赖 D-Bus 激活，是最终出现两个实例的常见原因。

注意这些标志用的是**单个短横线**，长选项也不例外：`-config`、`-verbosity`，而非 `--config`。

新版本支持通过 SIGUSR2 重载配置，但仍有许多设置只在启动时读取，而且无效的 `dunstrc` 会让 dunst 完全无法启动——在没有完整桌面的窗口管理器上，这意味着通知悄然失效且没有任何可见错误。遇到这种情况时，请在终端里用 `dunst -verbosity debug` 排查。

# HISTORY

**dunst** 由 **Sascha Kruse** 于 **2012 年**前后创建，面向那些运行平铺式窗口管理器、却发现现成的通知守护进程要么绑定整个桌面环境、要么弹出无法重设样式的提示框的用户。它的配置文件可以把任意通知按应用名、摘要、正文或紧急度匹配后重新设计样式或触发动作，这一能力使它与众不同，至今仍是人们选择它的理由。Wayland 支持后来才加入，如今 **mako** 在想要 Wayland 原生守护进程的用户中扮演着类似角色。

# INSTALL

```apt: sudo apt install dunst```

```dnf: sudo dnf install dunst```

```pacman: sudo pacman -S dunst```

```apk: sudo apk add dunst```

```zypper: sudo zypper install dunst```

```nix: nix profile install nixpkgs#dunst```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dunstctl](/man/dunstctl)(1), [dunstify](/man/dunstify)(1), [notify-send](/man/notify-send)(1), [mako](/man/mako)(1)

# RESOURCES

```[Source code](https://github.com/dunst-project/dunst)```

```[Homepage](https://dunst-project.org)```

<!-- verified: 2026-07-14 -->
