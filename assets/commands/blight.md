# TAGLINE

控制显示屏背光亮度

# TLDR

**将**屏幕亮度**设置**为百分比

```blight set [50]```

**显示**当前亮度状态

```blight status```

**增加**屏幕亮度百分比

```blight inc [5]```

**降低**屏幕亮度并带平滑过渡

```blight dec [10] -s```

**列出**可用的背光设备

```blight list```

**在指定设备上设置亮度**

```blight inc [2] -d [nvidia_0]```

**保存**当前亮度级别以便日后恢复

```blight save```

**恢复**之前保存的亮度级别

```blight restore```

**配置**权限和 udev 规则

```sudo blight setup```

# SYNOPSIS

**blight** _command_ [_value_] [_options_]

# DESCRIPTION

**blight** 是一个省心的 Linux 背光亮度管理命令行工具。它能很好地兼容混合 GPU 配置和专有驱动，智能检测当前活动的图形设备。

该工具优先选择集成显卡，其次为独立 Nvidia GPU 和 ACPI 内核模块，因此你无需手动指定哪个设备处于活动状态。

# SUBCOMMANDS

**set** _value_
> 将亮度设置为指定的百分比

**status**
> 显示当前亮度状态

**list**
> 显示所有可用的背光设备

**inc** _value_
> 按百分比增加亮度

**dec** _value_
> 按百分比降低亮度

**save**
> 保存当前亮度设置

**restore**
> 恢复之前保存的亮度

**setup**
> 配置写权限和 udev 规则（需要 sudo）

# PARAMETERS

**-d**, **--device** _device_
> 指定目标背光设备（如 nvidia_0、amdgpu_bl0）

**-s**, **--sweep**
> 启用平滑的亮度过渡而非瞬间变化

# CAVEATS

需要对 sysfs 背光文件的写权限。运行一次 `sudo blight setup` 来配置 udev 规则和权限，或手动将你的用户加入 video 组。仅适用于通过 sysfs 暴露背光控制的显示器。

# INSTALL

```apt: sudo apt install blight```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xbacklight](/man/xbacklight)(1), [brightnessctl](/man/brightnessctl)(1), [light](/man/light)(1)
