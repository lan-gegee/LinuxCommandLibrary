# TAGLINE

可配置的 Unix TUI 剪贴板管理器

# TLDR

**打开**剪贴板历史 TUI

```clipse```

**启动**后台剪贴板监听器

```clipse -listen```

通过管道将文本**复制**到系统剪贴板

```echo "hello" | clipse -c```

**添加文本**到剪贴板历史，但不复制到系统剪贴板

```echo "some data" | clipse -a```

将当前剪贴板内容**打印**到 stdout

```clipse -p```

**清空**除置顶项以外的剪贴板历史

```clipse -clear```

**暂停**剪贴板监控 5 分钟

```clipse -pause 5m```

# SYNOPSIS

**clipse** [_flags_] [_command_]

# PARAMETERS

**-listen**
> 运行监控剪贴板变化的后台监听进程。

**--listen-shell**
> 在当前终端中运行监听器以便调试。

**-a** _string_
> 将字符串添加到剪贴板历史，但不复制到系统剪贴板。接受 stdin。

**-c** _string_
> 将字符串复制到系统剪贴板。接受 stdin。

**-p**
> 将当前剪贴板内容打印到控制台。

**-output-all**
> 将整个剪贴板历史打印到 stdout。

**-clear**
> 清空所有剪贴板历史，但保留置顶项。

**-clear-all**
> 清空整个剪贴板历史，包括置顶项。

**-clear-images**
> 从剪贴板历史中清除所有图像。

**-clear-text**
> 从剪贴板历史中清除所有文本条目。

**-clean**
> 清理现有文本条目并移除孤立的图像条目。

**-kill**
> 终止所有已存在的后台监听进程。

**-pause** _duration_
> 在指定时长内暂停剪贴板监控（如 5m、1h）。

**-v**
> 打印版本号。

**keep**
> 选择条目复制后保持 TUI 打开。

**-help**
> 显示帮助信息。

# DESCRIPTION

**clipse** 是一个用 Go 编写的剪贴板管理器，提供用于浏览、搜索和管理剪贴板历史的终端用户界面。它同时支持文本和图像，可在 Wayland、X11 和 macOS 上运行，基于 BubbleTea TUI 框架构建。

主要功能包括模糊搜索与过滤、支持批量操作的多选、通过置顶重要条目使其在清空时得以保留、重复内容过滤、可配置的历史上限（默认 100 条）、自动粘贴支持，以及将特定应用排除在监控之外的能力。TUI 外观和按键绑定均可完全自定义。

# CONFIGURATION

配置存储在 **~/.config/clipse/configuration.json**。主题单独存放在同一目录下的 **custom_theme.json**。选项包括 **maxHistory**、重复过滤、自动粘贴按键、被排除的应用/窗口以及自定义主题颜色。

# CAVEATS

在 **Wayland** 上，需要安装 **wl-clipboard** 才能访问文本和图像剪贴板。Wayland 上的自动粘贴需要访问 **/dev/uinput**。在 **X11** 上，从源码构建可能需要 xlib API 头文件。必须在登录/启动时启动后台监听器（**clipse -listen**）才能捕获剪贴板历史。

# HISTORY

**clipse** 由 GitHub 用户 **savedra1** 创建。首个稳定版本（v1.0.0）于 **2023 年 7 月**发布，带有多选、自定义主题支持和图像/文本预览。1.1.0 版本（2023 年 10 月）增加了自定义按键绑定；v1.2.0（2024 年 12 月）带来了一次重大性能重构，集成了用于 X11/Darwin 的 C API、自动粘贴和排除应用支持。

# INSTALL

```nix: nix profile install nixpkgs#clipse```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xclip](/man/xclip)(1), [xsel](/man/xsel)(1), [wl-copy](/man/wl-copy)(1), [pbcopy](/man/pbcopy)(1)
