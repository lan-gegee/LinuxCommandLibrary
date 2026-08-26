# TAGLINE

允许使用键盘控制鼠标光标

# TLDR

**启动 keynav**

```keynav```

**以自定义配置启动**

```keynav "[loadconfig ~/.keynavrc]"```

**守护进程化**

```keynav daemonize```

# SYNOPSIS

**keynav** [_commands_]

# PARAMETERS

_commands_
> 要执行的 keynav 命令。

**daemonize**
> 在后台运行。

# DESCRIPTION

**keynav** 允许使用键盘控制鼠标光标。它将屏幕递归地划分为多个区域，让你可以用快捷键快速定位到任意位置。

默认绑定使用 Ctrl+分号激活 keynav，然后用 h/j/k/l 或方向键切割屏幕，逐步缩小范围到目标位置。

# DEFAULT BINDINGS

```
ctrl+semicolon  Start keynav
h, Left         Cut left
j, Down         Cut down
k, Up           Cut up
l, Right        Cut right
shift+h         Move left
shift+j         Move down
shift+k         Move up
shift+l         Move right
space, Enter    Click
semicolon       Click and end
Escape          Cancel
```

# CONFIGURATION

```
# ~/.keynavrc
clear
ctrl+semicolon start
h cut-left
l cut-right
k cut-up
j cut-down
space warp,click 1,end
```

# CAVEATS

仅支持 X11（不支持 Wayland）。需要练习才能高效使用。可能与其他快捷键冲突。

# HISTORY

keynav 由 **Jordan Sissel** 创建，旨在实现无鼠标操作。它遵循 Unix 哲学——把一件事做好，即通过键盘实现精确的光标定位。

# INSTALL

```apt: sudo apt install keynav```

```apk: sudo apk add keynav```

```nix: nix profile install nixpkgs#keynav```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdotool](/man/xdotool)(1), [xbindkeys](/man/xbindkeys)(1), [warpd](/man/warpd)(1)
