# TAGLINE

Nvidia Optimus 笔记本的 GPU 切换工具

# TLDR

在不同 GPU 模式间**切换**

```sudo envycontrol [-s|--switch] [nvidia|integrated|hybrid]```

手动指定**显示管理器**

```envycontrol --dm [gdm|gdm3|sddm|lightdm]```

**查看**当前 GPU 模式

```sudo envycontrol [-q|--query]```

**重置**设置

```sudo envycontrol --reset```

显示**帮助**

```envycontrol [-h|--help]```

显示**版本**

```envycontrol [-v|--version]```

# SYNOPSIS

**envycontrol** [_options_]

# DESCRIPTION

**envycontrol** 是专为运行 Linux 的 Nvidia Optimus 笔记本设计的 GPU 切换工具。它提供简化的界面，可在集成 Intel/AMD 显卡、混合模式（双 GPU 同时启用）和独立 Nvidia GPU 模式之间切换，无需手动编辑配置文件。

该工具通过处理 GPU 模式切换所需的各种复杂配置变更来简化双 GPU 系统的电源管理和性能调优，其中包括显示管理器设置和驱动配置。由于底层图形栈必须重新初始化，更改需要重启系统才能生效。

# PARAMETERS

**-s**, **--switch** _mode_
> 切换到 nvidia、integrated 或 hybrid 模式

**--dm** _manager_
> 指定显示管理器

**-q**, **--query**
> 显示当前 GPU 模式

**--reset**
> 重置为默认设置

**-h**, **--help**
> 显示帮助消息

**-v**, **--version**
> 显示版本

# CAVEATS

需要 Nvidia Optimus 笔记本。更改需重启后生效。必须正确指定显示管理器。可能与其他 GPU 切换方案冲突。

# INSTALL

```aur: yay -S envycontrol```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1)
