# TAGLINE

将人生目标转化为任务的离线命令行工具

# TLDR

**初始化**本地存储

```earth init```

编辑**角色**的价值观和使命

```earth character edit```

**添加**并**开始**一个任务（quest）

```earth quest add
earth quest list
earth quest start [1]```

显示**今日**重点（当前任务、下一步行动、待关闭事项）

```earth today```

**关闭**待办事项并进行**复盘**

```earth loop add --text "[task]"
earth review
earth export [path.json]```

启动**本地 Web UI**（仅限回环地址）

```earth web```

# SYNOPSIS

**earth** _command_ [_options_]

**earth-game** _command_ [_options_]

# DESCRIPTION

**earth-game**（安装后以 **earth** 或 **earth-game** 调用）是一个私密的离线个人任务追踪器。它只使用 Python 标准库和本地 SQLite——没有账号、出站网络、打分或 AI 建议。

你维护一个角色档案（价值观、优势、使命）、带唯一当前焦点和下一步行动的任务（quest）、待关闭的事项（loop），以及定期复盘。数据默认存放在 **${XDG_DATA_HOME:-$HOME/.local/share}/earth-game/earth.db**，可通过 **EARTH_GAME_DB** 覆盖。**earth web** 仅在 **127.0.0.1** 上提供同一数据库的服务。

# PARAMETERS

**init**
> 创建本地存储，不覆盖已有数据库

**character** **show**|**edit**
> 查看或编辑个人档案字段

**quest** **add**|**list**|**start**|**done**|**drop**
> 管理任务；同一时刻只有一个任务为当前任务

**loop** **add**|**list**|**close**
> 记录并解决待办事项

**today**
> 当前任务、下一步行动和复盘状态的摘要

**review**
> 记录简短反思（**--update-quest** 可设置下一步行动）

**export** [_path_]
> 将所有数据导出为 JSON（绝不覆盖已有文件）

**web**
> 本地浏览器 UI（**--port**、**--no-open**）

# CONFIGURATION

将 **EARTH_GAME_DB** 设置为指向另一个 SQLite 文件。在 Arch Linux 上，可从 AUR 安装 **earth-game** 包。

# INSTALL

```aur: yay -S earth-game```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[taskwarrior](/man/task)(1)

# RESOURCES

```[Source code](https://github.com/skorotkiewicz/earth-game)```

<!-- verified: 2026-07-14 -->
