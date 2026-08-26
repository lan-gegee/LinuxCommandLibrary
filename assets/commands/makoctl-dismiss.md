# TAGLINE

从 mako 通知守护进程中移除通知

# TLDR

关闭**最近一条**通知

```makoctl dismiss```

**按 ID 关闭**

```makoctl dismiss -n [notification_id]```

关闭**所有**通知

```makoctl dismiss --all```

关闭**第一组**通知

```makoctl dismiss --group```

关闭且**不保留历史**

```makoctl dismiss --no-history```

# SYNOPSIS

**makoctl dismiss** [_options_]

# DESCRIPTION

**makoctl dismiss** 从 mako 通知守护进程中移除通知。它可以关闭单条、分组或全部通知，并可选择不将其加入历史记录。

# PARAMETERS

**-n ID**
> 按 ID 关闭指定通知

**-a, --all**
> 关闭所有通知

**-g, --group**
> 关闭第一组中的所有通知

**--no-history**
> 不将被关闭的通知加入历史记录

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

[makoctl](/man/makoctl)(1), [mako](/man/mako)(1)
