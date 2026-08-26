# TAGLINE

以输入法支持启动应用程序

# TLDR

**带输入法启动**

```im-launch [application]```

**以指定输入法（如 ibus、fcitx）启动应用**

```im-launch -n [ibus] [application]```

只显示将使用的输入法而不实际启动

```im-launch -v [application]```

# SYNOPSIS

**im-launch** [_options_] _command_

# PARAMETERS

_COMMAND_
> 要启动的应用程序。

**-n** _METHOD_
> 指定输入法。

**-v**
> 详细模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**im-launch** 以输入法支持启动应用程序。它会为所选的输入框架设置环境变量。

该工具确保应用程序能够使用 IBus、Fcitx 或其他输入法。适合启动需要国际化输入的应用。

# CAVEATS

属于 im-config 软件包。通过设置环境变量实现。Debian/Ubuntu 特有。

# HISTORY

im-launch 是 **im-config** 的一部分，用于以输入法支持启动应用程序。

# SEE ALSO

[im-config](/man/im-config)(1), [ibus](/man/ibus)(1), [fcitx](/man/fcitx)(1)
