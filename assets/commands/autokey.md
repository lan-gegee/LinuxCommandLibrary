# TAGLINE

桌面文本扩展与自动化工具

# TLDR

以 GTK 界面**启动 AutoKey**

```autokey-gtk```

以 Qt 界面**启动 AutoKey**

```autokey-qt```

以详细日志**启动**

```autokey-gtk --verbose```

启动时**显示配置**窗口

```autokey-gtk --configure```

同时**记录鼠标按键事件**

```autokey-gtk --mouse```

# SYNOPSIS

**autokey-gtk** [_options_]

**autokey-qt** [_options_]

# PARAMETERS

**-c**, **--configure**
> 启动时显示配置窗口，即使不是首次运行。

**-l**, **--verbose**
> 启用详细（调试）日志。

**-m**, **--mouse**
> 类似 --verbose，但还会记录鼠标按键事件。

**-V**, **--version**
> 显示版本信息并退出。

**-h**, **--help**
> 显示帮助消息并退出。

# DESCRIPTION

**AutoKey** 是一款 Linux 桌面自动化工具，提供文本扩展和热键触发的自动化功能。它既支持简单的短语替换，也支持用复杂 Python 脚本完成高级自动化任务。

**短语（Phrase）**是输入缩写时展开的文本片段。例如，输入 "addr" 可以展开为你的完整地址。短语支持宏，可实现日期、剪贴板内容或命令输出等动态内容。

**脚本（Script）**使用 Python 3 实现高级自动化，包括模拟鼠标点击、键盘模拟、窗口操作和系统命令。脚本的触发方式与短语相同，都可以由缩写或热键触发。

AutoKey 有两个变体：面向 GTK 桌面（GNOME、XFCE、MATE）的 **autokey-gtk** 和面向 Qt 桌面（KDE Plasma）的 **autokey-qt**。两者共享相同的配置和脚本能力。

# CONFIGURATION

**~/.config/autokey/**
> 配置目录，存放短语、脚本和应用设置。

# CAVEATS

仅支持 X11，目前不支持 Wayland。需要系统托盘或 appindicator 支持；GNOME Shell 用户可能需要安装 AppIndicator Support 扩展。必须保持后台运行才能执行自动化。短语触发词必须唯一，以免冲突。

# HISTORY

**AutoKey** 由 **Chris Olsen** 于 **2008 年**前后创建，旨在提供其他平台上文本扩展工具的 Linux 等价物。自 2018 年起由 autokey GitHub 组织进行社区维护。它为需要在 Linux 上进行文本扩展和键盘自动化的用户提供类似 TextExpander 的功能。

# INSTALL

```nix: nix profile install nixpkgs#autokey```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[xdotool](/man/xdotool)(1), [xclip](/man/xclip)(1), [espanso](/man/espanso)(1)

# RESOURCES

```[Source code](https://github.com/autokey/autokey)```

```[Documentation](https://autokey.github.io/)```

<!-- verified: 2026-06-17 -->
