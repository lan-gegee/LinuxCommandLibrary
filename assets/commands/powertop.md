# TAGLINE

分析并优化电源消耗

# TLDR

**校准**功耗测量

```sudo powertop --calibrate```

生成 **HTML 报告**

```sudo powertop --html=[report.html]```

**自动调优**以获得最佳功耗表现

```sudo powertop --auto-tune```

测量特定的**时长**

```sudo powertop --time=[60]```

# SYNOPSIS

**powertop** [**--calibrate**] [**--html** _file_] [**--auto-tune**] [**--time** _seconds_]

# PARAMETERS

**--calibrate**
> 校准功耗测量（循环切换显示状态）

**--html _file_**
> 生成 HTML 报告

**--auto-tune**
> 应用所有建议的电源优化

**--time _seconds_**
> 测量时长（默认：20）

**--csv _file_**
> 生成 CSV 报告

**--iteration _num_**
> 迭代次数

# DESCRIPTION

**powertop** 分析系统功耗并给出优化建议。它能找出耗电的进程、设备和内核设置，并提供可操作的改进建议。

交互模式实时显示功耗明细。报告可以定位在笔记本电脑上造成过度耗电的具体软件或硬件。

# CAVEATS

校准需要不间断运行，可能耗时数分钟。自动调优所做的更改在重启后不会保留。某些优化可能影响性能或稳定性。大多数功能需要 root 权限。

# HISTORY

**powertop** 由 **Intel** 开发，用于帮助 Linux 用户优化电池续航。它已成为笔记本电源管理的标准工具，并包含在大多数发行版中。

# INSTALL

```apt: sudo apt install powertop```

```dnf: sudo dnf install powertop```

```pacman: sudo pacman -S powertop```

```apk: sudo apk add powertop```

```zypper: sudo zypper install powertop```

```nix: nix profile install nixpkgs#powertop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[powerstat](/man/powerstat)(8), [tlp](/man/tlp)(1), [tuned](/man/tuned)(8)
