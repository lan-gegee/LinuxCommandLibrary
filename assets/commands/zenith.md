# TAGLINE

带历史数据的终端系统监控器

# TLDR

**启动 zenith**

```zenith```

**以自定义间隔刷新**

```zenith --refresh-rate [500]```

**以指定数据库启动**

```zenith --db [/path/to/zenith.db]```

**禁用 GPU 监控**

```zenith --disable-gpu```

**使用指定的图形模式**

```zenith --graphics-mode [plain]```

# SYNOPSIS

**zenith** [_options_]

# PARAMETERS

**-d**, **--db** _path_
> 历史数据库路径。

**-r**, **--refresh-rate** _ms_
> 刷新率（毫秒）（默认：2000）。

**--disable-gpu**
> 禁用 GPU 监控。

**--disable-history**
> 禁用历史数据收集。

**--graphics-mode** _mode_
> 图形模式：unicode（默认）、plain。

**-p**, **--process** _mode_
> 进程显示方式：cpu、mem、top。

**--cpu-height** _rows_
> CPU 图表高度。

**--net-height** _rows_
> 网络图表高度。

**--disk-height** _rows_
> 磁盘图表高度。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# KEYBOARD COMMANDS

**q**
> 退出。

**Tab**
> 在各区块之间切换焦点。

**Up**/**Down** 或 **j**/**k**
> 浏览进程列表。

**/**
> 过滤进程。

**+**/**-**
> 缩放图表。

**g**/**G**
> 跳到进程列表顶部/底部。

**e**
> 展开/折叠磁盘区块。

**p**
> 暂停更新。

**c**
> 切换 CPU 视图模式。

**m**
> 切换内存视图模式。

**dd**
> 向选中的进程发送 SIGTERM。

**dk**
> 向选中的进程发送 SIGKILL。

# DESCRIPTION

**zenith** 是一款专注于历史数据可视化的终端系统监控器。它将指标存储在 SQLite 中，便于回顾过去的系统状态。

界面以迷你图形式显示 CPU、内存、网络、磁盘和 GPU 指标。进程列表展示当前系统活动，支持排序和过滤。

存储在 SQLite 数据库中的历史数据可用于查看过去的系统行为。通过缩放控件在时间轴上浏览。默认位置为 **~/.zenith.db**。

GPU 监控支持 NVIDIA（nvidia-smi）和 AMD（amdgpu）。需在编译时启用或检查构建特性。不可用时请使用 **--disable-gpu**。

刷新率控制指标更新的频率。数值越低动画越流畅，但 CPU 占用越高。

# CAVEATS

GPU 支持取决于驱动和硬件。数据库会随时间增长。部分指标可能是平台特定的。Unicode 图形需要兼容的终端。

# HISTORY

zenith 由 **Benjamin Vaisvil** 创建，首次发布于 **2019 年**前后。它使用 Rust 编写，旨在将实时监控与历史分析相结合。该项目通过存储并可视化历史指标与其他监控工具形成差异。

# INSTALL

```pacman: sudo pacman -S zenith```

```apk: sudo apk add zenith```

```zypper: sudo zypper install zenith```

```brew: brew install zenith```

```nix: nix profile install nixpkgs#zenith```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[htop](/man/htop)(1), [top](/man/top)(1), [btm](/man/btm)(1), [gtop](/man/gtop)(1), [glances](/man/glances)(1)
