# TAGLINE

GNOME Shell 集成调试器与检查器

# TLDR

在 GNOME Shell 运行对话框中**打开 Looking Glass 调试器**

```> Alt+F2, type "lg", press Enter```

在隐藏了 Looking Glass 的系统上**启用它**

```gsettings set org.gnome.shell development-tools true```

**重新禁用 Looking Glass**

```gsettings set org.gnome.shell development-tools false```

在 Looking Glass 中**引用最近一次求值结果**

```> it```

在 Looking Glass 中**回溯某个较早的编号结果**

```> r([number])```

**放慢 GNOME Shell 动画**以便调试

```> St.set_slow_down_factor([factor])```

# SYNOPSIS

**lg** _（输入到 GNOME Shell 的运行对话框中）_

# DESCRIPTION

**Looking Glass** 是 **GNOME Shell** 内置的调试器、检查器和 JavaScript REPL。在正在运行的 GNOME 会话中按下 **Alt+F2** 并输入关键字 **lg** 即可打开。它面向 shell 本身的调试，也用于编写和排查 GNOME Shell 扩展。

界面提供四个窗格。**Evaluator** 是一个交互式 JavaScript 提示符，可完全访问 GNOME Shell 进程，包括 **St**、**Clutter**、**Meta** 和 **GLib** 等 API。**Windows** 窗格列出已打开的窗口。**Extensions** 窗格显示已安装的 shell 扩展并链接到它们的源码。**Errors** 窗格显示记录下来的错误（在较新版本中，这些错误通常被转交 **journalctl** 记录）。

左上角有一个**元素拾取工具**，点击屏幕上的 UI 元素即可在求值器中取得对应的 actor 以便检查。

在求值器窗格中按 **Esc** 可关闭 Looking Glass。

# EVALUATOR HELPERS

**it**
> 引用最近一次求值的表达式。

**r(_n_)**
> 引用索引为 _n_ 的结果。

**St.set_slow_down_factor(_f_)**
> 将动画时长乘以 _f_（大于 1 表示变慢）；调试过渡动画时非常有用。

# CONFIGURATION

Looking Glass 通过 **org.gnome.shell** GSettings schema 向 GNOME Shell 暴露。在默认隐藏它的发行版上，把 **development-tools** 设置为 **true** 即可启用。命令历史会持久化保存到 dconf 中。

# CAVEATS

并非独立 CLI 工具：**lg** 是由 GNOME Shell 运行对话框解释的关键字，而不是 **PATH** 中的可执行文件。仅在正在运行的 GNOME Shell 会话（X11 或 Wayland）中可用。它会直接在 shell 进程内部执行 JavaScript，因此一段有问题的代码就可能冻结甚至崩溃整个桌面会话。

# HISTORY

Looking Glass 随 **GNOME Shell 3.0** 于 **2011 年 4 月**问世，是一款受 Firebug 启发的自省工具，为扩展作者和 shell 开发者提供了一个直通运行中会话的实时 JavaScript 控制台。此后它一直保留在 GNOME Shell 的各个版本中。

# SEE ALSO

[gsettings](/man/gsettings)(1), [dconf](/man/dconf)(1)
