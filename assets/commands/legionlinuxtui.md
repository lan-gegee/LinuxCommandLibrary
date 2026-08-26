# TAGLINE

在 Linux 上控制联想 Legion 笔记本的终端 UI

# TLDR

**运行** TUI（sysfs/驱动 I/O 需要 root）

```sudo legionlinuxtui```

从源码**构建**并运行

```go build -o build/```

```sudo ./build/legionlinuxtui```

无需安装直接**运行**（在源码检出目录中）

```sudo go run .```

# SYNOPSIS

**legionlinuxtui**

# DESCRIPTION

**legionlinuxtui** 是一个面向 Linux 上联想 **Legion** 笔记本的终端用户界面。它读取传感器数据，并通过全屏 TUI 提供多种能力开关（如保守模式和电源模式），大约每 100 ms 刷新一次传感器信息。

它依赖社区开发的 **Lenovo Legion Linux** 内核驱动（sysfs 接口），并且要求机器上已正确配置 **lm_sensors**。进程需要提升的权限才能与驱动通信并写入 sysfs 值——请使用 **sudo**（或等效方式）调用。

使用 Go 编写。可通过 Nix 获取软件包（作者提供的 NUR / flake 包）；否则需要用 Go ≥ 1.24.4 从仓库构建。

# PARAMETERS

不需要任何命令行选项。直接启动二进制即可；所有交互完全通过 TUI 完成。

# CAVEATS

需要 [LenovoLegionLinux](https://github.com/johnfanv2/LenovoLegionLinux) 驱动所支持的联想 Legion 硬件，且 **sensors** 必须可用。必须以足以进行驱动/sysfs I/O 的权限运行。并非面向非 Legion 机型的通用笔记本控制工具。

# HISTORY

**legionlinuxtui** 是一个开源 Go TUI 项目，维护于 **github.com/nooneknowspeter/legionlinuxtui**，采用 MIT 许可证。

# SEE ALSO

[sensors](/man/sensors)(1), [sensors-detect](/man/sensors-detect)(8), [amdgpu_top](/man/amdgpu_top)(1), [nvtop](/man/nvtop)(1)

# RESOURCES

```[Source code](https://github.com/nooneknowspeter/legionlinuxtui)```

<!-- verified: 2026-08-02 -->
