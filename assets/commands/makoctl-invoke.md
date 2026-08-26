# TAGLINE

对 mako 通知守护进程显示的通知触发动作

# TLDR

对最近一条通知 Invoke（调用）**默认动作**

```makoctl invoke```

对通知 Invoke 一个**指定动作**

```makoctl invoke -n [notification_id] [action_name]```

# SYNOPSIS

**makoctl invoke** [_-n id_] [_action_]

# PARAMETERS

**-n _id_**
> 指定要操作的通知 ID

**_action_**
> 要调用的动作名称（未指定时使用默认动作）

# DESCRIPTION

**makoctl invoke** 对 mako 通知守护进程显示的通知触发动作。通知可以定义多个动作（如"回复"、"标记已读"、"打开"），此命令可以编程方式调用这些动作。

不带参数时，它会对最近一条通知调用默认动作——通常等同于点击该通知。使用 **-n** 可以按 ID 定位特定通知。

这适用于以键盘为主的工作流，避免用鼠标操作通知，也适用于以脚本方式响应通知。

# CAVEATS

通知必须仍然可见，其动作才能被调用。通知 ID 可通过 **makoctl list** 获取。可用动作取决于发送应用的定义；并非所有通知都有关闭以外的动作。

# INSTALL

```apt: sudo apt install mako-notifier```

```dnf: sudo dnf install mako```

```pacman: sudo pacman -S mako```

```apk: sudo apk add mako```

```zypper: sudo zypper install mako```

```brew: brew install mako```

```nix: nix profile install nixpkgs#mako```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[makoctl](/man/makoctl)(1), [makoctl-mode](/man/makoctl-mode)(1), [mako](/man/mako)(1)
