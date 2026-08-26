# TAGLINE

用于任务管理的终端看板

# TLDR

**启动**看板

```basilk```

**显示版本**号

```basilk --version```

# SYNOPSIS

**basilk** [**--version**]

# PARAMETERS

**--version**
> 显示版本号并退出

# DESCRIPTION

**basilk** 是一款以极简看板逻辑管理任务的终端用户界面（TUI）应用。它按项目组织工作，每个项目包含若干任务，任务在三个状态列之间流转：**Up Next**、**On Going** 和 **Done**。任务还可以指定 1（最高）到 3（最低）的优先级，或 0 表示无优先级。当任务标记为 Done 时，其优先级会自动重置。

basilk 使用 Rust 和 ratatui 库编写，全程提供 vim 风格导航。在项目视图中，使用 **j**/**k** 或方向键导航，**n** 创建项目，**r** 重命名，**d** 删除，**Enter** 打开项目。在任务视图中，**n** 创建任务，**r** 重命名，**d** 删除，**Enter** 更改任务状态，**p** 更改优先级。按 **Esc** 或 **h** 返回项目视图，按 **q** 退出。

项目会根据已完成任务的占比显示彩色编码的完成指示器：0% 为深灰色，最高 50% 为品红色，最高 99% 为黄色，100% 为绿色。所有数据存储在一个带版本号的 JSON 文件中，并在不同版本间自动进行结构迁移。

# CONFIGURATION

配置以 TOML 文件形式存储，名为 **config.toml**，位于应用数据目录中。若该文件不存在，会自动以默认值创建。

**[ui]**
> **show_help** = true -- 切换界面中显示的帮助文本

数据存储在特定平台的目录中：Linux 上为 **~/.config/basilk**，macOS 上为 **~/Library/Application Support/basilk**，Windows 上为 **AppData\Roaming\basilk**。

# CAVEATS

该项目处于 beta 阶段，可能存在 bug。CLI 只接受 **--version** 标志；所有其他交互都在 TUI 内完成。除内部 JSON 存储外，没有导入或导出功能。

# HISTORY

**basilk** 由 **GabAlpha** 创建，是一个开源 Rust 项目，采用 MIT 与 Apache 2.0 双许可证。0.2.1 版发布于 2025 年 3 月。可通过 cargo、Homebrew、AUR 和 x-cmd 获取。

# INSTALL

```aur: yay -S basilk```

```nix: nix profile install nixpkgs#basilk```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[taskwarrior](/man/taskwarrior)(1), [todo.sh](/man/todo.sh)(1), [jira](/man/jira)(1), [task](/man/task)(1)
