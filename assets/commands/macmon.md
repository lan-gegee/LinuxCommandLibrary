# TAGLINE

无需 sudo 的 Apple Silicon 处理器性能监控工具

# TLDR

**启动系统监视器**

```macmon```

**以 JSON 格式输出指标**

```macmon pipe```

**设置刷新间隔**（毫秒）

```macmon -i [ms]```

# SYNOPSIS

**macmon** [_command_] [_options_]

# PARAMETERS

**-i**, **--interval** _MS_
> 更新间隔，单位毫秒（默认：1000）。

**pipe**
> 以 JSON 格式输出指标，便于管道传给其他工具。

**debug**
> 打印调试信息。

# DESCRIPTION

**macmon** 是一款面向 Apple Silicon 处理器的免 sudo 性能监控工具。它实时显示 CPU、GPU 和 Apple Neural Engine（ANE）的功耗、每个集群的 CPU 利用率、RAM/Swap 使用情况、温度，以及带有平均值和最大值的历史图表。

它使用一个未公开的 Apple API（与 powermetrics 所用的相同）来访问系统指标，因此无需 sudo。该工具内置 6 个可切换的颜色主题。

# CAVEATS

仅适用于 Apple Silicon Mac（M1 及之后机型）。使用了可能在 macOS 版本间变化的未公开 API。

# HISTORY

**macmon** 由 **vladkens** 创建，用 **Rust** 编写。

# INSTALL

```brew: brew install macmon```

```nix: nix profile install nixpkgs#macmon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[htop](/man/htop)(1), [btop](/man/btop)(1)
