# TAGLINE

从 Wayland 剪贴板粘贴数据

# TLDR

**粘贴**剪贴板内容

```wl-paste```

从 **primary** 选择区粘贴（高亮选中的文本）

```wl-paste --primary```

将剪贴板内容**写入**文件

```wl-paste > [path/to/file]```

粘贴时不带末尾**换行符**

```wl-paste --no-newline```

列出剪贴板中可用的 **MIME 类型**

```wl-paste --list-types```

以特定 **MIME 类型**粘贴剪贴板内容（如图片）

```wl-paste --type image/png > [path/to/image.png]```

将剪贴板内容通过管道传给命令

```wl-paste | [command]```

每次**剪贴板变化**时运行一条命令

```wl-paste --watch [command]```

# SYNOPSIS

**wl-paste** [_options_]

# PARAMETERS

**-p**, **--primary**
> 使用 primary 选择区而不是剪贴板

**-n**, **--no-newline**
> 不追加换行符

**-t**, **--type** _mime-type_
> 请求特定的 MIME 类型

**-l**, **--list-types**
> 列出可用的 MIME 类型

**-s**, **--seat** _seat_
> 选择要使用的 seat

**-w**, **--watch** _command_ [_args_...]
> 每次剪贴板变化时运行命令

**-v**, **--version**
> 显示版本信息

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**wl-paste** 从 Wayland 剪贴板获取数据并写入标准输出。它可以请求特定 MIME 类型的剪贴板数据，既支持文本，也支持图片等二进制内容。

primary 选择区（用鼠标选中的文本）可通过 **--primary** 访问，实现中键粘贴功能。监视模式可用于跟踪剪贴板变化。

# CAVEATS

只能在 Wayland 下工作；X11 请使用 **xclip** 或 **xsel**。可用 MIME 类型取决于复制方应用程序提供的内容。有些应用可能不会填充 primary 选择区。

# HISTORY

属于 **wl-clipboard** 项目，由 Sergey Bugaev 编写，用于以 Wayland 原生方式访问剪贴板。它是 wl-copy 的粘贴端对应工具，实现了用于读取剪贴板的 Wayland data-device 协议。

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

[wl-copy](/man/wl-copy)(1), [xclip](/man/xclip)(1), [xsel](/man/xsel)(1)
