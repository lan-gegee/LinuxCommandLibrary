# TAGLINE

显示 Vulkan GPU 与驱动信息

# TLDR

**显示 Vulkan 信息摘要**

```vulkaninfo --summary```

**显示完整的 Vulkan 信息**（详细）

```vulkaninfo```

**输出到文件**

```vulkaninfo -o [vulkan_info.txt]```

**生成 JSON 输出**

```vulkaninfo --json```

**生成 HTML 报告**

```vulkaninfo --html```

**显示所有可用格式**

```vulkaninfo --show-formats```

在多 GPU 系统中**指定目标 GPU**

```vulkaninfo --json=[0]```

# SYNOPSIS

**vulkaninfo** [**--summary**] [**--json**[=_gpu_]] [**--html**] [**--text**] [**-o** _file_] [**--show-formats**]

# PARAMETERS

**--summary**
> 显示所有 GPU 的 Vulkan 信息简要摘要。

**--text**
> 向标准输出产生文本输出。这是默认格式。

**--html**
> 生成保存为 vulkaninfo.html 的 HTML 报告。

**-j**, **--json**[=_gpu_]
> 产生符合 Vulkan Profiles 模式的 JSON 输出。可选的 GPU 编号用于指定设备。

**-o** _file_, **--output** _file_
> 将输出保存到指定文件。

**--show-formats**
> 显示支持的图像格式的详细信息。

**--show-all**
> 显示所有可用信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**vulkaninfo** 显示系统上 Vulkan API 支持的详细信息，包括物理设备（GPU）、可用扩展、层、内存类型、队列族和支持的格式。

该工具查询 Vulkan 运行时，枚举所有支持 Vulkan 的设备及其能力。这包括设备属性（名称、类型、驱动版本、API 版本）、限制、支持的特性、内存堆和队列族属性。

在多 GPU 或驱动特性丰富的系统上，输出可能非常冗长。使用 **--summary** 可快速概览，或将输出重定向到文件以进行详细分析。该工具对于验证 Vulkan 安装、调试驱动问题以及确定应用开发的硬件能力至关重要。

vulkaninfo 是大多数 Linux 发行版上 vulkan-tools 软件包的一部分。

# CAVEATS

需要正常工作的 Vulkan 驱动和运行时。默认输出可能有数千行；简要输出请使用 **--summary**。某些功能需要特定的 Vulkan 扩展。除非过滤，多 GPU 系统会显示所有设备的信息。

# HISTORY

**vulkaninfo** 由 **Khronos Group** 开发，是 Vulkan SDK 工具的一部分，由 **LunarG** 维护。Vulkan 于 **2015 年**公布，**2016 年 2 月**发布，作为面向高性能图形的 OpenGL 后继者。vulkaninfo 自 Vulkan SDK 首次发布起就是其中一员，是 Vulkan 安装的主要诊断工具。

# INSTALL

```apt: sudo apt install vulkan-tools```

```dnf: sudo dnf install vulkan-tools```

```pacman: sudo pacman -S vulkan-tools```

```apk: sudo apk add vulkan-tools```

```zypper: sudo zypper install vulkan-tools```

```brew: brew install vulkan-tools```

```nix: nix profile install nixpkgs#vulkan-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glxinfo](/man/glxinfo)(1), [nvidia-smi](/man/nvidia-smi)(1), [lspci](/man/lspci)(8), [clinfo](/man/clinfo)(1)
