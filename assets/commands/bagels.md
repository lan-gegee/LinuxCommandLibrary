# TAGLINE

基于终端的记账工具，支持预算管理与消费洞察

# TLDR

**启动应用**

```bagels```

以指定目录存储数据并**启动**

```bagels --at [path/to/directory]```

**定位数据库**文件

```bagels locate database```

**定位配置**文件

```bagels locate config```

从 Actual Budget **迁移数据**

```bagels --migrate actualbudget --source [path/to/source.db]```

# SYNOPSIS

**bagels** [**--at** _path_] [**--migrate** _type_ **--source** _path_]

**bagels** **locate** {**config** | **database**}

# PARAMETERS

**--at** _path_
> 指定存储数据库和配置文件的自定义目录。默认使用 XDG 基础目录。

**--migrate** _type_
> 从其他应用执行数据迁移。目前支持 **actualbudget**。

**--source** _path_
> 使用 **--migrate** 时源数据库文件的路径。

**locate config**
> 显示配置 YAML 文件的路径。

**locate database**
> 显示 SQLite 数据库文件的路径。

# CONTROLS

**a**
> 添加新记录、账户或类别（取决于上下文）

**e**
> 编辑选中项

**d**
> 删除选中项

**v**
> 切换跳转模式，在 UI 各面板间快速导航

**c**
> 在 Home 和 Manager 标签页之间切换

**t**
> 创建账户间的新转账

**b**
> 打开预算视图

**s**
> 切换交易拆分显示

**q** / **w**
> 按日期 / 按人员显示记录

**f**
> 打开高级筛选

**.**
> 循环切换时间偏移类型（日、周、月、年）

**/**
> 在收入与支出模式之间切换

**[** / **]**
> 选择上一个 / 下一个账户

**\\**
> 切换基于账户的记录过滤

**Left** / **Right**
> 导航到上一个 / 下一个时间段

**1-9**
> 按编号快速应用交易模板

**ctrl+a**
> 为记录添加新拆分（在记录弹窗中）

**ctrl+d**
> 删除最后一个拆分（在记录弹窗中）

**ctrl+t**
> 提交并保存为模板（在记录弹窗中）

**ctrl+q**
> 退出应用

# DESCRIPTION

**bagels** 是一款用于记录个人收支的终端用户界面（TUI）应用。它将所有财务数据存储在本地的 SQLite 数据库中，并提供基于 Textual 框架构建的交互式界面。

应用分为两个主视图：Home 和 Manager。Home 视图显示交易记录、账户余额、带图表的消费洞察、收入/支出模式切换以及快速访问模板。Manager 视图提供管理账户、含子类别的类别、预算以及用于拆分记录的人员的工具。

主要功能包括跨多个类别的拆分交易、被跟踪账户与外部账户之间的转账、可通过数字键访问的周期性交易模板，以及在 UI 各面板之间进行键盘导航的跳转模式系统。洞察模块通过可视化图表提供消费分析、预估趋势以及针对可配置上限的预算跟踪。

Bagels 支持预算管理，可配置收入评估政策、储蓄百分比目标以及"想要与必需"支出比例。记录可以按标签、金额、类别和时间段（日、周、月或年）过滤。

所有数据都保存在用户本机上，文件存储遵循 XDG 基础目录规范。可以使用 **--at** 标志将数据库和配置放置在自定义目录中。

# CONFIGURATION

配置存储在 XDG 配置目录下的 **config.yaml** 文件中（通常为 **~/.config/bagels/config.yaml**）。该文件在首次运行时自动生成，采用 YAML 格式。

**defaults.period**
> Home 视图的默认时间段。可选值：**day**、**week**、**month**、**year**。默认：**week**。

**defaults.first_day_of_week**
> 每周的第一天（0 = 周一，6 = 周日）。默认：**6**。

**defaults.date_format**
> 日期显示格式字符串。默认：**%d/%m**。

**defaults.round_decimals**
> 金额的小数位数。默认：**2**。

**defaults.plot_marker**
> 图表绘制标记样式。可选值：**braille**、**fhd**、**hd**、**dot**。默认：**braille**。

**state.theme**
> 配色主题。可用主题包括 **tokyo-night**、**nord**、**gruvbox**、**catppuccin-mocha**、**dracula**、**galaxy**、**alpine**、**cobalt**、**hacker**、**flexoki** 和 **dark**。默认：**tokyo-night**。

**state.check_for_updates**
> 启动时检查 PyPI 是否有新版本。默认：**true**。

**state.budgeting**
> 预算参数，包括收入评估政策、储蓄百分比和"想要"支出比例。

**hotkeys**
> 所有键盘快捷键均可在 **hotkeys** 区段下完全自定义。

**symbols**
> 可自定义的显示符号，包括线条、拆分指示符、类别标记和金额符号。

# CAVEATS

需要 Python 3.13 或更高版本。为获得最佳渲染效果，请使用现代终端模拟器；macOS 用户建议使用 Ghostty，Windows 用户应使用 Windows Terminal。

**--migrate** 选项目前仅支持从 Actual Budget 导入。使用迁移时必须提供 **--source** 标志。

所有数据均本地存储，没有云同步。请备份数据库文件（通过 **bagels locate database** 定位）以防数据丢失。

# HISTORY

**Bagels** 由 **Jax (EnhancedJax)** 创建，于 **2024** 年首次发布，是一款开源的终端记账工具。该项目基于 **Textual** TUI 框架构建，灵感来自 **Posting** 终端应用。它在终端工具社区颇受欢迎，累计获得超过 2,700 个 GitHub 星标。项目采用 **GPL-3.0** 许可证。

# INSTALL

```aur: yay -S bagels```

```brew: brew install bagels```

```nix: nix profile install nixpkgs#bagels```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ledger](/man/ledger)(1), [hledger](/man/hledger)(1), [awk](/man/awk)(1)
