# TAGLINE

发送桌面通知

# TLDR

**发送通知**

```notify-send "[Title]" "[Message body]"```

**设置紧急程度**

```notify-send -u [critical] "[Alert]" "[System error]"```

**设置过期时间**

```notify-send -t [5000] "[Title]" "[Message]"```

**添加图标**

```notify-send -i [dialog-information] "[Info]" "[Details]"```

**设置类别**

```notify-send -c [email] "[New Email]" "[Subject]"```

**设置应用名称**

```notify-send -a "[MyApp]" "[Title]" "[Message]"```

# SYNOPSIS

**notify-send** [_options_] _summary_ [_body_]

# PARAMETERS

_SUMMARY_
> 通知标题。

_BODY_
> 通知消息。

**-u** _LEVEL_
> 紧急程度（low、normal、critical）。

**-t** _MS_
> 以毫秒计的超时时间。

**-i** _ICON_
> 图标名称或路径。

**-c** _CATEGORY_
> 通知类别。

**--help**
> 显示帮助信息。

# DESCRIPTION

**notify-send** 用于发送桌面通知，使用的是桌面通知系统。

该工具显示弹窗消息，是 libnotify 的一部分，适用于 GNOME 及其他桌面环境。

# CAVEATS

需要通知守护进程。依赖桌面环境。属于 libnotify 的一部分。

# HISTORY

notify-send 是 **libnotify** 的一部分，实现了 freedesktop.org 的桌面通知规范。

# INSTALL

```apt: sudo apt install libnotify-bin```

```dnf: sudo dnf install libnotify```

```pacman: sudo pacman -S libnotify```

```apk: sudo apk add libnotify```

```brew: brew install libnotify```

```nix: nix profile install nixpkgs#libnotify```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[noti](/man/noti)(1), [dunst](/man/dunst)(1), [zenity](/man/zenity)(1)
