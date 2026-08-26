# TAGLINE

基于终端的图形化活动监视器

# TLDR

**启动 gotop**

```gotop```

**使用指定的配色方案**

```gotop -c [monokai]```

**显示每个 CPU 的使用率**

```gotop -p```

**使用极简布局**

```gotop -m```

**显示电池组件**

```gotop -b```

**设置刷新间隔**

```gotop -r [500ms]```

**禁用 CPU 图表**

```gotop --no-cpu```

**使用指定的网络接口**

```gotop -i [eth0]```

# SYNOPSIS

**gotop** [_options_]

# PARAMETERS

**-c**, **--color** _scheme_
> 配色方案：default、monokai、solarized、vice 等。

**-p**, **--percpu**
> 分别显示每个 CPU 核心。

**-a**, **--averagecpu**
> 显示 CPU 平均使用率。

**-m**, **--minimal**
> 极简终端界面。

**-b**, **--battery**
> 显示电池组件。

**-r**, **--rate** _duration_
> 刷新间隔。默认：1s。

**-i**, **--interface** _name_
> 网络接口过滤器。

**-l**, **--layout** _name_
> 命名布局或自定义布局（例如 minimal、battery、kitchensink）。

**--nvidia**
> 启用 NVIDIA GPU 统计信息（需要 nvidia-smi）。

**--list** _keys|colorschemes_
> 打印可用的按键绑定或内置配色方案，然后退出。

**--write-config**
> 将当前命令行选项持久化到配置文件。

**--no-cpu**
> 禁用 CPU 组件。

**--no-disk**
> 禁用磁盘组件。

**--no-mem**
> 禁用内存组件。

**--no-net**
> 禁用网络组件。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# KEYBOARD COMMANDS

**q**, **Ctrl+c**
> 退出。

**Tab**
> 移动到下一个组件。

**j**/**k** 或 **Down**/**Up**
> 滚动进程列表。

**g**/**G**
> 跳到列表顶部/底部。

**d**
> 终止选中的进程。

**/**
> 过滤进程。

**h**
> 切换帮助显示。

**c**
> 按 CPU 排序。

**m**
> 按内存排序。

**p**
> 按 PID 排序。

# DESCRIPTION

**gotop** 是一个基于终端的图形化活动监视器，灵感来自 gtop 和 vtop。它通过 ASCII 图表在实时的组件面板中显示 CPU、内存、磁盘、网络和进程信息。

monokai、solarized、vice 等配色方案可以改变外观。配合 **-l** 使用的自定义布局允许以 YAML 格式重新排列和调整组件大小。进程排序支持 CPU、内存和 PID 列，并带有过滤和终止进程的功能。

# CONFIGURATION

**~/.config/gotop/layout**
> 以 YAML 格式定义组件位置的自定义布局文件。

**~/.config/gotop/colorscheme**
> 自定义配色方案定义。

# CAVEATS

NVIDIA GPU 监控需要系统中有 **nvidia-smi** 二进制文件；不支持 AMD GPU。部分指标可能与平台相关（与 Linux/FreeBSD/macOS 相比，Windows 支持有限）。电池组件需要受支持的硬件。过高的刷新频率会增加 CPU 占用。

# HISTORY

gotop 最初由 **Caleb Bassi**（cjbassi）于 **2018 年**创建，是 gtop 的 Go 语言重写版。原项目于 **2020 年**归档。由 **xxxserxxx** 维护的社区分支继续开发，并添加了新功能与修复。gotop 将可视化监视器风格带入 Go 生态，并提供跨平台支持。

# INSTALL

```apk: sudo apk add gotop```

```brew: brew install gotop```

```nix: nix profile install nixpkgs#gotop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[htop](/man/htop)(1), [btm](/man/btm)(1), [gtop](/man/gtop)(1), [zenith](/man/zenith)(1)

# RESOURCES

```[Source code](https://github.com/xxxserxxx/gotop)```

<!-- verified: 2026-07-17 -->
