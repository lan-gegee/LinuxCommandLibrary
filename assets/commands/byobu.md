# TAGLINE

带有增强状态栏和快捷键的终端复用器

# TLDR

**启动** byobu 会话

```byobu```

**创建**新窗口

```Ctrl-A c```

**切换**窗口

```Ctrl-A n```

**分离**会话

```Ctrl-A d```

**列出**会话

```byobu-select-session```

# SYNOPSIS

**byobu** [_options_]

# DESCRIPTION

**byobu** 是一个基于文本的窗口管理器和终端复用器。它是 tmux 或 screen 的封装，增加了状态栏、快捷键和配置，让终端会话管理更加轻松。

该工具在 Ubuntu 上颇受欢迎，为管理多个终端会话提供了易用的界面。

# PARAMETERS

**-S** _name_
> 创建命名会话

**-ls**
> 列出会话

**-r**
> 重新连接到会话

**-d**
> 分离会话

# KEYBINDINGS

**F2** - 新建窗口
**F3/F4** - 上一个/下一个窗口
**F6** - 分离
**F7** - 回滚模式
**F8** - 重命名窗口
**F9** - 配置菜单
**Shift-F2** - 水平分割
**Ctrl-F2** - 垂直分割

**Ctrl-A** 前缀：
- **c** - 创建窗口
- **n/p** - 下一个/上一个窗口
- **d** - 分离
- **[** - 复制模式

# FEATURES

- 预配置的 tmux/screen
- 信息丰富的状态栏
- F 键绑定
- 会话管理
- UTF-8 支持
- 配色方案
- 通知系统

# STATUS BAR

显示：
- 主机名
- 负载平均值
- 内存使用
- CPU 使用
- 磁盘空间
- 网络活动
- 日期/时间

# WORKFLOW

```bash
# Start session
byobu

# Create windows (F2)
# Switch windows (F3/F4)
# Split panes (Shift-F2, Ctrl-F2)

# Detach (F6)
# Reattach
byobu attach
```

# CAVEATS

F 键可能与终端模拟器冲突。后端（tmux 或 screen）会影响功能特性。状态栏占用一些资源。高级功能有学习曲线。默认快捷键与纯 tmux 不同。

# HISTORY

**Byobu** 由 Dustin Kirkland 在 **2008 年**前后创建，旨在为 GNU screen 提供更友好的界面，后来加入了对 tmux 的支持。

# CONFIGURATION

**~/.byobu/**
> 用户配置目录，包含快捷键、状态栏设置和配置偏好

**~/.byobu/keybindings**
> 自定义快捷键定义

**~/.byobu/status**
> 状态栏配置（显示哪些元素）

**~/.byobu/statusrc**
> 状态栏刷新频率和显示选项

**~/.byobu/.tmux.conf**
> Byobu 特定的 tmux 配置覆盖

# INSTALL

```dnf: sudo dnf install byobu```

```apk: sudo apk add byobu```

```zypper: sudo zypper install byobu```

```brew: brew install byobu```

```nix: nix profile install nixpkgs#byobu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [zellij](/man/zellij)(1)

# RESOURCES

```[Source code](https://github.com/dustinkirkland/byobu)```

```[Homepage](https://www.byobu.org)```

<!-- verified: 2026-06-22 -->
