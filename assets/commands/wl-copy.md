# TAGLINE

将数据复制到 Wayland 剪贴板

# TLDR

**复制文本**到剪贴板

```wl-copy "[text]"```

将命令输出通过管道送入剪贴板

```ls | wl-copy```

只允许**粘贴一次**然后清空

```wl-copy --paste-once "[text]"```

复制**图片**

```wl-copy < [path/to/image]```

复制**敏感**数据（如密码），不进入剪贴板历史

```wl-copy --sensitive "[password]"```

指定特定 **MIME 类型**

```wl-copy --type text/html "[<b>bold</b>]"```

**清空**剪贴板

```wl-copy --clear```

# SYNOPSIS

**wl-copy** [_options_] [_text_]

# PARAMETERS

**-o**, **--paste-once**
> 只响应一次粘贴请求后退出

**-c**, **--clear**
> 清空剪贴板而不是复制内容

**-p**, **--primary**
> 使用 primary 选择区而不是剪贴板

**-n**, **--trim-newline**
> 不追加换行符

**-t**, **--type** _mime-type_
> 设置内容的 MIME 类型

**-s**, **--seat** _seat_
> 选择要使用的 seat

**-f**, **--foreground**
> 保持在前台运行而不 fork

**--sensitive**
> 提示内容是敏感信息（如密码）；剪贴板管理器可能会避免将其保存到历史记录中

**-v**, **--version**
> 显示版本信息

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**wl-copy** 将数据复制到 Wayland 剪贴板。它可以从参数复制文本，也可以从标准输入读取二进制数据，并自动处理 MIME 类型。该工具默认 fork 到后台运行，以保持剪贴板内容可用。

数据可以通过管道传入 wl-copy，用于复制命令输出或文件内容。它同时支持常规剪贴板和 primary 选择区（用于鼠标中键粘贴）。

# CAVEATS

只能在 Wayland 下工作；X11 请使用 **xclip** 或 **xsel**。进程必须保持运行（或 fork）才能响应粘贴请求。在前台模式下，wl-copy 退出后剪贴板内容会丢失。

# HISTORY

属于 **wl-clipboard** 项目，由 Sergey Bugaev 编写，用于以 Wayland 原生方式访问剪贴板。提供与 xclip、xsel 等 X11 工具等效的功能，但使用的是 Wayland 剪贴板协议。

# INSTALL

```apt: sudo apt install wl-clipboard```

```dnf: sudo dnf install wl-clipboard```

```pacman: sudo pacman -S wl-clipboard```

```apk: sudo apk add wl-clipboard```

```zypper: sudo zypper install wl-clipboard```

```brew: brew install wl-clipboard```

```nix: nix profile install nixpkgs#wl-clipboard```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wl-paste](/man/wl-paste)(1), [xclip](/man/xclip)(1), [xsel](/man/xsel)(1)
