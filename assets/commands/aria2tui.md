# TAGLINE

aria2 下载管理器的 TUI 客户端

# TLDR

**启动 aria2tui**（连接到已配置的 aria2c 守护进程）

```aria2tui```

**显示帮助**及可用按键绑定

```Press ? inside aria2tui```

# SYNOPSIS

**aria2tui**

# DESCRIPTION

**aria2tui** 是 **aria2c** 下载工具的终端用户界面（TUI）客户端。它通过 RPC 与 aria2c 守护进程通信，提供交互式界面来管理下载、种子和队列，无需离开终端。

功能包括批量下载和种子管理、队列控制与下载优先级调整、下载选项的精细调节（如分片长度、user-agent、最大速度和代理设置），以及对活跃任务的实时监控。界面支持多个 aria2c 守护进程实例，可用 **{** 和 **}** 切换。

首次启动时，aria2tui 会显示配置表单，用户在其中填写 aria2c 守护进程的 URL、端口和身份验证令牌。这会在 **~/.config/aria2tui/config.toml** 创建配置文件。

按键导航包括：**?** 查看所有按键绑定，**'** 切换右侧边栏，**"** 循环切换边栏视图，**Ctrl-L** 重绘屏幕。固定光标模式（先按反引号再输入 **pc** 切换）可在下载重新排序时保持光标位置不变。可通过设置菜单（**~**）禁用自动刷新，以便在批量操作期间保留选中状态。

# CONFIGURATION

**~/.config/aria2tui/config.toml**
> 首次启动时创建的主配置文件。存储 aria2c 守护进程 URL、端口和 RPC 身份验证令牌。

# CAVEATS

需要运行中的 **aria2c** 守护进程且已启用 RPC。更改活跃或暂停任务中的下载选项很可能导致该下载重启。完整功能需要外部工具配合：**yazi** 用于选择种子文件，**neovim** 用于编辑下载选项和添加 URI，**plotille** 用于图形可视化，**pyperclip** 用于剪贴板集成。仅能在 Unix 系操作系统上运行。

# HISTORY

**aria2tui** 由 **Grim**（grimandgreedy）开发，使用 Python 和 curses 库编写。可从 PyPI 获取并通过 **pip** 安装。项目采用 MIT 许可证。

# INSTALL

```aur: yay -S aria2tui```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aria2c](/man/aria2c)(1), [wget](/man/wget)(1), [curl](/man/curl)(1)
