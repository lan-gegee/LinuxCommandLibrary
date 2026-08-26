# TAGLINE

跨平台终端系统监视器

# TLDR

**启动**资源监视器

```btm```

**基础**模式（功能较少）

```btm -b```

**指定**刷新率

```btm -r [2000]```

# SYNOPSIS

**btm** [_options_]

# DESCRIPTION

**btm**（bottom）是一个跨平台的终端图形化进程/系统监视器。它以可自定义的界面提供 CPU、内存、磁盘、网络和进程信息。

该工具凭借现代化的特性与外观，可作为 htop 和 top 的替代品。

# PARAMETERS

**-b**, **--basic**
> 基础模式（禁用图表）

**-r**, **--rate** _ms_
> 刷新率（毫秒，默认：1000）

**-a**, **--hide_avg_cpu**
> 隐藏平均 CPU 使用率

**-m**, **--hide_time**
> 隐藏时间图

**-t**, **--default_time_value** _ms_
> 默认时间范围

**-c**, **--config** _path_
> 配置文件

# FEATURES

- 每个 CPU 核心的使用率
- 内存与交换空间监控
- 磁盘 I/O 与使用情况
- 网络 I/O
- 可排序的进程列表
- 进程树视图
- 电池监控
- 温度传感器
- 可自定义的组件
- 支持鼠标

# KEYBINDINGS

- **q/Ctrl+C** - 退出
- **/** - 过滤
- **dd** - 杀死进程
- **e** - 展开组件
- **+/-** - 缩放时间图
- **Tab** - 切换组件
- **?** - 帮助

# CONFIGURATION

**~/.config/bottom/bottom.toml**
> 主配置文件，包含标志、颜色、布局和组件设置。

# CAVEATS

需要支持 Unicode 的现代终端。部分功能与平台相关。资源占用比极简工具更高。配置可能比较复杂。

# HISTORY

**bottom** 由 Clement Tsang 于 **2019 年**前后创建，是一个用 Rust 编写的现代化、可自定义的系统监视器。

# INSTALL

```apt: sudo apt install btm```

```pacman: sudo pacman -S bottom```

```apk: sudo apk add bottom```

```zypper: sudo zypper install bottom```

```brew: brew install bottom```

```nix: nix profile install nixpkgs#bottom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[htop](/man/htop)(1), [btop](/man/btop)(1), [top](/man/top)(1)

# RESOURCES

```[Source code](https://github.com/ClementTsang/bottom)```

```[Documentation](https://clementtsang.github.io/bottom/)```

<!-- verified: 2026-06-22 -->
