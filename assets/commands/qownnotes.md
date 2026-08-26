# TAGLINE

支持云同步的纯文本 Markdown 笔记工具

# TLDR

**启动 QOwnNotes**

```QOwnNotes```

**以便携模式启动**（设置与可执行文件存放在一起）

```QOwnNotes --portable```

**使用不同的会话**上下文存储设置

```QOwnNotes --session [session_name]```

**以 Markdown 格式导出当前设置**和环境信息

```QOwnNotes --dump-settings```

**清除设置**并重新开始

```QOwnNotes --clear-settings```

**启动后触发菜单动作**

```QOwnNotes --action [actionShow_Todo_List]```

即使设置中不允许，也**允许多实例运行**

```QOwnNotes --allow-multiple-instances```

# SYNOPSIS

**QOwnNotes** [_options_]

# PARAMETERS

**--portable**
> 以便携模式运行，将设置与可执行文件存放在一起。

**--session** _name_
> 使用不同的上下文来保存设置和内部文件。便于在不丢失当前设置的情况下排查问题。

**--clear-settings**
> 在启动应用程序前清除所有设置。

**--dump-settings**
> 以 GitHub Markdown 格式输出当前设置和环境的完整信息，然后退出。

**--action** _name_
> 启动后触发一个菜单动作。脚本自定义动作请使用 **customAction_**_identifier_ 形式。

**--allow-multiple-instances**
> 即使设置中不允许，也允许运行多个 QOwnNotes 实例。

**--completion** _shell_
> 生成 Shell 补全代码。支持 **fish** 和 **bash**。

**--version**
> 输出版本号并退出。

**--help**
> 显示可用的命令行选项。

# DESCRIPTION

**QOwnNotes** 是一款纯文本笔记应用，将笔记以标准 Markdown 文件的形式保存在磁盘上。笔记完全可移植，可以用任何文本编辑器编辑；同时 QOwnNotes 提供了丰富的界面，包括语法高亮、预览面板、标签、笔记搜索和层级文件夹组织功能。

可选的 ownCloud 或 Nextcloud 集成可实现跨设备的云端同步，包括服务器端加密和版本管理。该应用还支持通过脚本实现自定义工作流、Vim 键位绑定，以及从可移动介质运行的便携模式。

# CAVEATS

基于 Qt 的应用程序，需要显示服务器。二进制文件名因平台而异：Linux 原生版本为 **QOwnNotes**，Snap 版本为 **qownnotes**。云同步需要单独的 ownCloud 或 Nextcloud 服务器。当只允许单实例运行（默认）时，用 **--action** 启动第二个实例会在已运行的实例中触发该动作。

# HISTORY

QOwnNotes 由 **Patrizio Bekerle** 创建，是一款开源、跨平台的纯文本 Markdown 笔记应用。它基于 Qt/C++ 构建，专注于让笔记保持为标准 Markdown 文件，从而在应用之外依然可移植、可编辑。可选的 Nextcloud/ownCloud 集成提供带服务器端版本管理和加密的云同步。

# INSTALL

```dnf: sudo dnf install qownnotes```

```nix: nix profile install nixpkgs#qownnotes```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[joplin](/man/joplin)(1), [notable](/man/notable)(1)
