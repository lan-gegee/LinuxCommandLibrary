# TAGLINE

实时监控 AMD GPU 利用率

# TLDR

**启动 TUI** 监控 AMD GPU 使用情况

```amdgpu_top```

**启动图形界面**模式

```amdgpu_top --gui```

**启动类似 nvidia-smi 的简易 TUI 模式**

```amdgpu_top --smi```

**导出 AMDGPU 信息**（规格、VRAM、PCI、VBIOS）

```amdgpu_top -d```

**输出 JSON 格式数据**供脚本使用

```amdgpu_top -d --json```

**显示 GPU 进程**及各进程的内存占用

```amdgpu_top -p```

按实例编号**选择特定 GPU**

```amdgpu_top -i [0]```

为所有 AMD GPU **导出 GPU 指标**

```amdgpu_top --gpu-metrics```

# SYNOPSIS

**amdgpu_top** [_options_]

# PARAMETERS

**-d**, **--dump**
> 导出 AMDGPU 信息，包括规格、VRAM、PCI、ResizableBAR、VBIOS 和视频能力。

**--list**
> 显示可用 AMDGPU 设备列表。

**-J**, **--json**
> 输出 JSON 格式数据。可与 -d 或 --gpu-metrics 选项组合使用。

**--gui**
> 启动图形界面模式。

**--smi**
> 启动类似 nvidia-smi 或 rocm-smi 的简易 TUI 模式。

**-p**, **--process**
> 导出所有 GPU 进程及各进程的内存占用。

**-i** _INDEX_
> 按索引编号选择 GPU 实例。

**--pci** _PATH_
> 以 domain:bus:dev.func 格式指定 PCI 路径。

**--apu**, **--select-apu**
> 选择 APU 实例。

**--single**, **--single-gpu**
> 仅显示选定的 APU/GPU。

**--no-pc**
> 禁用性能计数器读取（GRBM、GRBM2）。可用于避免关闭节能功能。

**-gm**, **--gpu_metrics**, **--gpu-metrics**
> 为所有 AMD GPU 导出 gpu_metrics。

**--pp_table**, **--pp-table**
> 从 sysfs 和 VBIOS 为所有 AMD GPU 导出功耗/性能表。

**--drm-info**
> 导出 DRM 信息。

**--json_fifo**, **--json-fifo** _PATH_
> 将 JSON 格式数据输出到 FIFO（命名管道），供其他应用程序和脚本使用。

**--decode-gm**, **--decode-gpu-metrics** _PATH_
> 解码指定的 gpu_metrics 文件。

**-s** _MS_
> 设置 JSON 模式的刷新间隔，单位为毫秒（默认：1000ms）。

**-n** _COUNT_
> 设置 JSON 模式的最大迭代次数（0 = 无限）。

**-u**, **--update-process-index** _SEC_
> fdinfo 的更新间隔，单位为秒（默认：5s）。

**--dark**, **--dark-mode**
> 为 TUI/GUI 启用深色模式。

**--light**, **--light-mode**
> 为 TUI/GUI 启用浅色模式。

**--gl**, **--opengl**
> GUI 后端使用 OpenGL API。

**--vk**, **--vulkan**
> GUI 后端使用 Vulkan API。

**-V**, **--version**
> 打印版本信息。

**-h**, **--help**
> 打印帮助信息。

# DESCRIPTION

**amdgpu_top** 是一款 AMD GPU 监控工具，以类似 htop 的方式显示实时利用率数据，但专门针对 AMD 图形硬件。它从性能计数器（GRBM、GRBM2）、传感器、fdinfo 和 AMDGPU 驱动收集信息，提供全面的 GPU 指标。

该工具提供三种显示模式：功能完整的 TUI（默认）、简化的 SMI 风格 TUI 以及图形界面。它可以监控 GPU 活动、VRAM 占用、温度、功耗、风扇转速以及每个进程的 GPU 利用率。

# TUI KEYBINDINGS

**g** - 切换 GRBM 性能计数器
**r** - 切换 GRBM2 性能计数器
**v** - 切换 VRAM/GTT 占用显示
**f** - 切换 fdinfo 显示
**n** - 切换传感器显示
**m** - 切换 GPU 指标显示
**h** - 更改更新间隔（high=100ms，low=1000ms）
**P** - 按 PID 对 fdinfo 排序
**M** - 按 VRAM 占用对 fdinfo 排序
**G** - 按 GFX 使用率对 fdinfo 排序
**R** - 反转排序顺序
**q** - 退出程序

# CAVEATS

在某些 APU 上，读取性能计数器（GRBM、GRBM2）可能阻止 GPU 进入节能状态。如果存在此问题，可使用 **--no-pc** 禁用性能计数器读取。需要 AMDGPU 内核驱动以及访问 GPU sysfs 条目的相应权限。

# HISTORY

**amdgpu_top** 由 Umio-Yasuno 创建，使用 **Rust** 编写，是 radeontop 的现代替代品。它提供了 radeontop 所缺少的功能，如温度监控、GPU 指标和图形界面。该项目在 GitHub 上持续活跃维护。

# INSTALL

```pacman: sudo pacman -S amdgpu_top```

```zypper: sudo zypper install amdgpu_top```

```nix: nix profile install nixpkgs#amdgpu_top```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[radeontop](/man/radeontop)(1), [nvtop](/man/nvtop)(1), [nvidia-smi](/man/nvidia-smi)(1), [htop](/man/htop)(1)
