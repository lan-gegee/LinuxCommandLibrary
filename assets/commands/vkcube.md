# TAGLINE

Vulkan 旋转立方体演示程序

# TLDR

**运行 Vulkan 演示**

```vkcube```

**指定帧数**

```vkcube --c [1000]```

**呈现模式**

```vkcube --present_mode [0]```

**选择 GPU**

```vkcube --gpu [0]```

# SYNOPSIS

**vkcube** [_--c frames_] [_--present_mode mode_] [_options_]

# PARAMETERS

**--c** _FRAMES_
> 帧数。

**--present_mode** _MODE_
> 呈现模式。

**--gpu** _INDEX_
> 选择 GPU。

**--width** _W_
> 窗口宽度。

**--height** _H_
> 窗口高度。

# DESCRIPTION

**vkcube** 是 Vulkan SDK 中的一个简单演示程序，显示一个使用 Vulkan 图形 API 渲染的旋转 3D 立方体。它可用作快速验证工具，确认 Vulkan 驱动和库已正确安装并在系统上正常工作。

该程序会打开一个窗口，显示一个持续旋转的带纹理立方体。如果立方体渲染并旋转流畅，说明 GPU、Vulkan 驱动和显示系统协同工作正常。其选项允许选择特定的 GPU、设置呈现模式以及限制渲染的帧数。

作为 Khronos Group 维护的官方 Vulkan-Tools 软件包的一部分，vkcube 是该演示的 C 实现（vkcubepp 是 C++ 版本）。在 Linux 系统上排查 Vulkan 支持问题时，它通常被用作第一步诊断手段。

# CAVEATS

需要 Vulkan 驱动。需要 GPU。需要显示设备。

# HISTORY

**vkcube** 是 **Vulkan SDK** 的一部分，提供一个简单的 Vulkan 功能测试程序。

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

[vulkaninfo](/man/vulkaninfo)(1), [glxgears](/man/glxgears)(1), [vkcubepp](/man/vkcubepp)(1)
