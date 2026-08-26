# TAGLINE

在专用 Nvidia GPU 上运行命令

# TLDR

在**专用 Nvidia GPU** 上运行命令

```prime-run [command]```

在 Nvidia GPU 上运行**游戏**

```prime-run steam```

**验证**是否使用了 Nvidia 显卡

```prime-run glxinfo | grep "OpenGL renderer"```

检查 **Vulkan** 渲染器

```prime-run vulkaninfo | grep "deviceName"```

# SYNOPSIS

**prime-run** _command_ [_arguments_...]

# DESCRIPTION

**prime-run** 在混合显卡系统（Optimus）上使用专用 Nvidia GPU 执行程序。它是一个轻量包装器，在执行给定命令前设置环境变量 **__NV_PRIME_RENDER_OFFLOAD=1**、**__NV_PRIME_RENDER_OFFLOAD_PROVIDER=NVIDIA-G0**、**__GLX_VENDOR_LIBRARY_NAME=nvidia** 和 **__VK_LAYER_NV_optimus=NVIDIA_only**。

该工具是 PRIME render offload 的一部分，允许特定应用选择性地使用性能更强的 GPU，而日常使用仍由集成显卡节省电量。

# CAVEATS

需要 nvidia-prime 软件包和正确的驱动配置。仅适用于 Nvidia 专有驱动。某些应用程序可能不遵循这些环境变量。Wayland 支持情况因合成器而异。

# HISTORY

**prime-run** 随 NVIDIA 驱动版本 435 的 PRIME render offload 支持一同推出。对于 Linux 笔记本上的混合显卡，它提供了比 Bumblebee 更简单的替代方案。

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [optirun](/man/optirun)(1), [switcherooctl](/man/switcherooctl)(1)
