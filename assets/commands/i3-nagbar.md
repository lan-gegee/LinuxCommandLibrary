# TAGLINE

为 i3 窗口管理器显示通知栏

# TLDR

**显示警告消息**

```i3-nagbar -t warning -m "[message]"```

**显示错误消息**

```i3-nagbar -t error -m "[message]"```

**添加在终端中执行动作的按钮**

```i3-nagbar -m "[message]" -b "[button text]" "[command]"```

**添加直接执行动作的按钮**

```i3-nagbar -m "[message]" -B "[button text]" "[command]"```

在主显示器上显示

```i3-nagbar -p -m "[message]"```

**指定字体**

```i3-nagbar -f "[pango:monospace 10]" -m "[message]"```

# SYNOPSIS

**i3-nagbar** [_options_]

# PARAMETERS

**-m** _message_
> 要显示的消息。

**-t** _type_
> 类型：warning 或 error。

**-b** _button_ _action_
> 在终端中运行动作的按钮。

**-B** _button_ _action_
> 直接运行动作的按钮。

**-f** _font_
> 字体规格。

**-p**
> 在主显示器上显示。

**-v**
> 详细模式。

# DESCRIPTION

**i3-nagbar** 为 i3 窗口管理器显示一条通知栏。i3 用它报告配置错误，也可用于用户自定义的警告或确认。它支持以按钮形式执行 shell 命令，可在终端中运行或直接运行。

# INSTALL

```apt: sudo apt install i3-wm```

```pacman: sudo pacman -S i3-wm```

```apk: sudo apk add i3wm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[i3](/man/i3)(1), [i3-msg](/man/i3-msg)(1)
