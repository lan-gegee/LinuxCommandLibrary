# TAGLINE

为 Linux 桌面配置输入法框架

# TLDR

**配置输入法**

```im-config```

**列出可用的方法**

```im-config -l```

**设置输入法**

```im-config -n [ibus]```

**显示当前方法**

```im-config -c```

**重置为自动**

```im-config -a```

# SYNOPSIS

**im-config** [_options_]

# PARAMETERS

**-l**
> 列出可用的方法。

**-n** _METHOD_
> 设置输入法。

**-c**
> 显示当前设置。

**-a**
> 自动检测方法。

**-x**
> X 模式（GUI）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**im-config** 为 Linux 桌面配置输入法框架。它在 IBus、Fcitx、SCIM 等输入系统之间进行选择。

该工具管理用于激活输入法的 X 启动脚本。它常用于设置多语言输入。

# CAVEATS

Debian/Ubuntu 工具。需要重启会话。行为因桌面环境而异。

# HISTORY

im-config 是一个用于管理输入法配置的 Debian 工具。

# SEE ALSO

[ibus](/man/ibus)(1), [fcitx](/man/fcitx)(1), [im-launch](/man/im-launch)(1)
