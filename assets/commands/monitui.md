# TAGLINE

管理 Hyprland 显示器布局的 TUI

# TLDR

**启动显示器管理器**

```monitui```

# SYNOPSIS

**monitui** [_options_]

# DESCRIPTION

**monitui** 是一个用于管理 Hyprland 显示器布局的终端工具，无需手动编辑配置文件。它让用户可以可视化地排列显示器、调整分辨率和旋转设置，并为不同场景（桌面、扩展坞、差旅）保存多套配置预设。

功能包括可用鼠标拖动的显示器定位、将工作区分配给指定显示器，以及防止产生问题布局的确认保护机制。

# CAVEATS

只能在 Linux 上配合 Hyprland 窗口管理器使用。需要正在运行的 Hyprland 会话。

# HISTORY

**monitui** 由 **Nathaniel Fargo** 创建，使用 **Rust** 编写。

# INSTALL

```aur: yay -S monitui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hyprctl](/man/hyprctl)(1)
