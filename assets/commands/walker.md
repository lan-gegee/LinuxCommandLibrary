# TAGLINE

Wayland 应用启动器与命令运行器

# TLDR

**打开**启动器

```walker```

**将结果限制**为单一提供者

```walker -m [desktopapplications|calc|clipboard|runner|...]```

以 dmenu 模式**运行**，从 stdin 读取选项

```printf "Choice1\nChoice2\nChoice3" | walker -d```

**应用**命名主题

```walker -t [theme_name]```

**保持**后台服务运行以加快启动速度

```walker --gapplication-service```

# SYNOPSIS

**walker** [_options_]

# PARAMETERS

**-m**, **--provider** _name_
> 将启动器限制为单个 Elephant 提供者（例如 **desktopapplications**、**calc**、**clipboard**、**runner**）。

**-d**, **--dmenu**
> 从 **stdin** 读取条目，将选中的条目输出到 **stdout**（dmenu 兼容模式）。

**-t**, **--theme** _name_
> 从 **~/.config/walker/themes/** 加载名为 _name_ 的主题。

**--gapplication-service**
> 以 D-Bus/GApplication 后台服务方式运行 Walker，以减少冷启动延迟。

# DESCRIPTION

**walker** 是一款面向 Wayland 桌面的快速、可定制的应用启动器，使用 Rust 和 GTK4 编写。它依赖 **elephant** 提供者守护进程以及可插拔的 **elephant-*** 系列提供者作为搜索来源。

开箱即用，Walker 可以启动桌面应用、运行 shell 命令、计算算术表达式、浏览文件、搜索网页、显示剪贴板历史、挑选符号、管理书签和待办事项、查询 Arch 软件包，并与 Bitwarden、WirePlumber 以及 Niri 窗口管理器操作等工具集成。搜索框中的前缀字符用于切换提供者（例如 **=** 计算器、**/** 文件、**:** 剪贴板历史）。

配置位于 **~/.config/walker/** 目录下（**config.toml**、主题以及各提供者的条目布局）。主题继承内置默认值，可以针对每个提供者覆盖 CSS 和 GTK4 XML 条目模板。

要获得最低延迟，请在每个会话中运行一次 **walker --gapplication-service**（通常放在合成器的自启动中）。之后的 **walker** 调用会附加到该服务；当不需要额外参数时，位于 **/run/user/$UID/walker/walker.sock** 的 Unix 套接字可通过 **nc -U** 即时打开。

# CONFIGURATION

默认设置随上游的 **resources/config.toml** 提供。用户覆盖配置写入 **~/.config/walker/config.toml**：主题名称、占位文本、提供者前缀映射和按键绑定（修饰键 **ctrl**、**alt**、**shift**、**super** 加 GDK 键名）。主题是 **~/.config/walker/themes/** 下的目录，包含 **style.css** 和可选的 **layouts/** XML 片段。

# CAVEATS

仅支持 Wayland。在 Walker 显示结果之前，**elephant** 和至少一个提供者（例如 **elephant-desktopapplications**）必须正在运行。仅通过套接字激活时无法传递命令行参数。

# INSTALL

```nix: nix profile install nixpkgs#walker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fuzzel](/man/fuzzel)(1), [wofi](/man/wofi)(1), [rofi](/man/rofi)(1), [dmenu](/man/dmenu)(1)
