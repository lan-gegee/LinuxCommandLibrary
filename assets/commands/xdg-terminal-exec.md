# TAGLINE

启动用户首选的终端模拟器

# TLDR

**打开默认终端**而不运行命令

```xdg-terminal-exec```

**在首选终端中运行命令**

```xdg-terminal-exec [command] [args...]```

为启动的终端**设置窗口标题**

```xdg-terminal-exec --title=[My Shell] [command]```

执行命令前**设置工作目录**

```xdg-terminal-exec --dir=[path/to/dir] [command]```

命令退出后**保持终端打开**

```xdg-terminal-exec --hold [command]```

**打印所选的 Desktop Entry ID**而不启动它

```xdg-terminal-exec --print-id```

**显示将要执行的完整命令行**

```xdg-terminal-exec --print-cmd [command]```

# SYNOPSIS

**xdg-terminal-exec** [_options_] [**--**] [_command_ [_arguments_ ...]]

# PARAMETERS

**--app-id=**_app_id_
> 设置所生成窗口的 Wayland app-id（或 X11 class）。

**--title=**_title_
> 设置终端窗口标题。

**--dir=**_workdir_
> 运行命令前切换到 _workdir_。

**--hold**
> 命令终止后保持终端窗口打开。

**--print-id**
> 打印被选中的 Desktop Entry ID。

**--print-path**
> 打印所选 Desktop Entry 的文件系统路径。

**--print-content**
> 打印所选 Desktop Entry 的完整内容。

**--print-cmd**[=_printf_seq_]
> 打印将要执行的最终命令行，而不是实际运行。

**--print-delimiter=**_printf_seq_
> 设置多个打印输出之间使用的分隔符。

**--**
> 将其后的所有参数视为要执行的命令。

# DESCRIPTION

**xdg-terminal-exec** 启动用户首选的终端模拟器，并可在其中选择性地执行一条命令。它是 freedesktop.org 拟议中的 XDG Default Terminal Execution Specification 的参考实现。

候选终端从系统中已安装、声明了 **TerminalEmulator** 类别并提供 **X-TerminalArgExec** 键的 Desktop Entry 中发现。用户可以在配置文件中列出 Desktop Entry ID 来指定偏好哪个条目。

这与 **xdg-open** 等工具的做法一致：脚本、桌面启动器或应用程序不必硬编码终端，而是调用 **xdg-terminal-exec**，由系统在运行时解析用户的选择。

# CONFIGURATION

首选终端列在以下文件中，按 XDG 配置/数据优先级顺序搜索：

```
${desktop}-xdg-terminals.list
xdg-terminals.list
```

其中 _${desktop}_ 是 **XDG_CURRENT_DESKTOP** 中某项的小写形式。每一行是一个 Desktop Entry ID，可以带动作后缀：

```
foot.desktop
kitty.desktop
org.gnome.Terminal.desktop:new-window
```

以 **#** 开头的行是注释。特殊指令包括 **/enable_cache**、**/disable_cache**、**/execarg_compat**、**/execarg_strict** 和 **/execarg_default:entry.desktop:arg**。

# ENVIRONMENT

**XTE_CACHE_ENABLED**
> 启用或禁用对已解析终端的缓存。

**XTE_DEBUG**, **DEBUG**
> 向 stderr 打印调试信息。

**XDG_CURRENT_DESKTOP**, **XDG_CONFIG_HOME**, **XDG_CONFIG_DIRS**, **XDG_DATA_DIRS**
> 用于桌面检测和配置查找的标准 XDG 变量。

# CAVEATS

该规范在 freedesktop.org 的 **terminal-wg** 议题库中仍是**提案**状态；仅以尽力而为的方式保持向后兼容。并非每个终端模拟器都已提供 **X-TerminalArgExec** 键，因此在相应 Desktop Entry 修复之前，某些已安装的终端可能不会被选择器发现。

# HISTORY

**xdg-terminal-exec** 由 **Vladimir Kudrya**（Vladimir-csp）创建，是一个基于 shell 的参考实现，伴随针对 freedesktop.org terminal-wg 规范仓库的一个合并请求提交。它已被多个发行版（Debian、Arch、Fedora）打包，作为需要通用方式启动终端的现代桌面启动器的依赖项。

# INSTALL

```dnf: sudo dnf install xdg-terminal-exec```

```zypper: sudo zypper install xdg-terminal-exec```

```nix: nix profile install nixpkgs#xdg-terminal-exec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-open](/man/xdg-open)(1), [xdg-mime](/man/xdg-mime)(1), [xdg-settings](/man/xdg-settings)(1)
