# TAGLINE

点击强制关闭 X11 窗口

# TLDR

**点击关闭窗口**

```xkill```

**关闭指定窗口 ID**

```xkill -id [window_id]```

**关闭所有匹配名称的窗口**

```xkill -frame```

**显示可用的按钮**

```xkill -button any```

# SYNOPSIS

**xkill** [_-id window_id_] [_-button button_] [_-frame_] [_options_]

# PARAMETERS

**-id** _WINDOWID_
> 按 ID 关闭特定窗口。

**-button** _BUTTON_
> 要使用的按钮（any、1、2、3）。

**-frame**
> 包含窗口边框。

**-all**
> 关闭所有匹配的客户端。

**-display** _DISPLAY_
> X server 显示器。

# DESCRIPTION

**xkill** 强制关闭 X11 窗口。运行后光标会发生变化，下一个被点击的窗口将被杀死。

该工具向 X server 发送终止请求。这比请求窗口正常关闭更为强硬。

可以针对窗口管理器的边框。使用 -frame 后，即使点击的是窗口装饰而非内容，也会杀死该窗口。

任何鼠标按钮都可以触发终止。默认只有按钮 1（左键）有效。-button 选项可以改变这一点。

按下任意按键会取消 xkill 而不关闭窗口。这样即使误启动也能退出。

当应用失去响应且正常关闭方法失效时，该工具非常有用。

# CAVEATS

仅支持 X11——在 Wayland 上无效。可能丢失未保存的数据。不会优雅地关闭应用程序。某些窗口可能会抵抗终止。

# HISTORY

**xkill** 自 X11 早期起就是 **X.Org** 工具的一部分。它为应对行为异常的 X 应用提供了简单的手段。

# INSTALL

```apt: sudo apt install x11-utils```

```dnf: sudo dnf install xkill```

```apk: sudo apk add xkill```

```zypper: sudo zypper install xkill```

```nix: nix profile install nixpkgs#xkill```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kill](/man/kill)(1), [killall](/man/killall)(1), [xwininfo](/man/xwininfo)(1), [xdotool](/man/xdotool)(1)
