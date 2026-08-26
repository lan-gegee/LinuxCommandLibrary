# TAGLINE

OpenCL 平台与设备信息工具

# TLDR

**显示所有 OpenCL 信息**

```clinfo```

**只显示平台与设备列表**

```clinfo -l```

**以原始格式显示**

```clinfo --raw```

**显示离线设备**

```clinfo --offline```

**以 JSON 格式输出**

```clinfo --json```

# SYNOPSIS

**clinfo** [_options_]

# PARAMETERS

**-l**, **--list**
> 仅列出平台和设备。

**--raw**
> 原始输出格式。

**-a**, **--all-props**
> 尝试获取所有属性，包括官方未支持的属性。

**-A**, **--always-all-props**
> 与 -a 类似，但也会为不支持的属性显示错误。

**--offline**
> 显示离线设备。

**--json**
> 以 JSON 格式输出原始数据（实验性）。

**-h**, **--human**
> 人类可读格式（默认）。

**-v**, **--version**
> 显示程序版本。

# DESCRIPTION

**clinfo** 显示系统上可用 OpenCL 平台和设备的详细信息。它查询 OpenCL 运行时，报告能力、内存大小、支持的特性和扩展。

输出内容包括每个 OpenCL 平台（厂商实现）及其设备（GPU、CPU、加速器）的信息。细节涵盖设备类型、计算单元、内存大小、支持的 OpenCL 版本以及可用的扩展。

这些信息对开发和调试 OpenCL 应用程序、验证驱动安装以及了解 GPU 计算任务的硬件能力至关重要。

# OUTPUT INCLUDES

**Platform**: Vendor, version, profile, extensions
**Device**: Type, vendor, compute units, frequencies
**Memory**: Global, local, constant memory sizes
**Workgroup**: Maximum sizes and dimensions
**Image**: Supported image formats and sizes
**Extensions**: Available OpenCL extensions

# CAVEATS

需要安装 OpenCL 运行时和 ICD（Installable Client Driver）加载器。输出内容因已安装的驱动而异；驱动缺失或过时可能显示不完整的信息。clinfo 只显示 OpenCL 设备，不包括 CUDA 或其他计算 API。

# HISTORY

clinfo 是为 OpenCL 生态系统开发的诊断工具。OpenCL（Open Computing Language）由 **Apple** 发布并于 **2009 年**由 **Khronos Group** 标准化，是一个跨异构平台并行编程的框架。clinfo 成为开发者和用户验证 OpenCL 环境配置、了解可用计算能力的重要实用工具。

# INSTALL

```apt: sudo apt install clinfo```

```dnf: sudo dnf install clinfo```

```pacman: sudo pacman -S clinfo```

```apk: sudo apk add opencl```

```zypper: sudo zypper install clinfo```

```brew: brew install clinfo```

```nix: nix profile install nixpkgs#clinfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [glxinfo](/man/glxinfo)(1), [vulkaninfo](/man/vulkaninfo)(1)
