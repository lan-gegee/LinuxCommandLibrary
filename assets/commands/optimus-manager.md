# TAGLINE

管理搭载 Nvidia Optimus 技术笔记本上的 GPU 切换

# TLDR

在不同 GPU 模式间**切换**

```optimus-manager --switch [nvidia|integrated|hybrid]```

**清理**配置和状态

```optimus-manager --cleanup```

# SYNOPSIS

**optimus-manager** [_options_]

# PARAMETERS

**--switch _mode_**
> 切换到指定的 GPU 模式：nvidia、integrated 或 hybrid

**--cleanup**
> 清理之前会话遗留的配置

**--status**
> 显示当前 GPU 模式和配置

**--print-mode**
> 仅打印当前模式名称

**--print-startup**
> 打印配置中的启动模式

**--no-confirm**
> 切换前不请求确认

# DESCRIPTION

**optimus-manager** 管理搭载 Nvidia Optimus 技术（Intel/Nvidia 双显卡）笔记本上的 GPU 切换。它处理在集成 Intel GPU、独立 Nvidia GPU 或混合模式之间切换这一复杂任务。

可用模式包括：
- **integrated**：仅使用 Intel GPU（电池续航最佳）
- **nvidia**：仅使用 Nvidia GPU（性能最佳）
- **hybrid**：两个 GPU 同时启用，Nvidia 用于特定应用（通过 PRIME）

切换模式通常需要注销或重启。该工具负责管理 Xorg 配置、内核模块加载和显示管理器集成。

# CAVEATS

切换 GPU 需要注销桌面会话。混合模式需要正确配置 PRIME 渲染卸载。支持多种显示管理器，但可能需要额外配置。仅适用于配备 Nvidia Optimus 硬件的 Linux 笔记本。

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [prime-run](/man/prime-run)(1), [envycontrol](/man/envycontrol)(1)
