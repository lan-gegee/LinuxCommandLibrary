# TAGLINE

Intel Core i3、i5 和 i7 处理器的实时报告工具

# TLDR

**启动** i7z 监控（需要 root）

```sudo i7z```

# SYNOPSIS

**i7z** [_options_]

# DESCRIPTION

**i7z** 是一款面向 Intel Core i3、i5 和 i7 处理器的实时报告工具。它在基于控制台的界面中显示 CPU 频率、温度、睿频加速状态和电源管理信息。

该工具读取 CPU 特有的 MSR（Model Specific Register，型号专用寄存器），提供关于处理器性能状态的准确信息，包括每核心频率和 C-state 驻留情况。

# CAVEATS

仅适用于 Intel Core i3、i5 和 i7 处理器（Sandy Bridge 及之后）。访问 CPU MSR 需要 root 权限。对非常新的处理器代际可能无法正常工作。已被 turbostat 等更现代的工具取代。

# HISTORY

i7z 的开发初衷是在现有工具缺乏对 Turbo Boost 等 Intel 处理器新特性支持的情况下，提供详细的 Intel 处理器监控。开发始于 **2009 年**前后，正值 Intel Core i7 处理器家族发布之际。

# INSTALL

```apt: sudo apt install i7z```

```nix: nix profile install nixpkgs#i7z```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[turbostat](/man/turbostat)(8), [cpupower](/man/cpupower)(1), [sensors](/man/sensors)(1)
