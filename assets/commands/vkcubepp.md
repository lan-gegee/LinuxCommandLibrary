# TAGLINE

C++ 版 Vulkan 立方体演示程序

# TLDR

**运行 Vulkan 立方体演示**

```vkcubepp```

**带校验层运行**

```vkcubepp --validate```

**在指定 GPU 上运行**

```vkcubepp --gpu_number [0]```

**全屏运行**

```vkcubepp --fullscreen```

**不显示帧数输出**

```vkcubepp --suppress_popups```

**显示帮助**

```vkcubepp --help```

# SYNOPSIS

**vkcubepp** [_options_]

# PARAMETERS

**--validate**
> 启用 Vulkan 校验层。

**--gpu_number** _n_
> 按索引选择 GPU。

**--fullscreen**
> 以全屏模式运行。

**--present_mode** _mode_
> 设置呈现模式。

**--suppress_popups**
> 不显示信息弹窗。

**--width** _n_
> 窗口宽度（像素）。

**--height** _n_
> 窗口高度（像素）。

**--help**, **-h**
> 显示帮助。

# DESCRIPTION

**vkcubepp** 显示一个使用 Vulkan 图形 API 渲染的旋转 3D 立方体。它是一个简单的测试程序，用于验证 Vulkan 驱动和库已正确安装并正常工作。

vkcubepp 属于 Khronos Group 的 Vulkan-Tools 软件包，使用 C++ 编写（vkcube 是 C 版本）。两者产生相同的视觉效果，但展示了不同的 API 使用方式。

以 --validate 运行会启用 Vulkan 校验层，这对调试 Vulkan 应用程序的开发者很有用。如果 Vulkan 工作正常，立方体应当平滑旋转。

# CAVEATS

需要支持 Vulkan 的 GPU 和驱动。若 Vulkan 配置有误，可能会静默失败。属于 vulkan-tools 软件包。窗口系统支持（X11/Wayland）取决于构建选项。

# HISTORY

**vkcubepp** 是 Khronos Group 维护的官方 Vulkan-Tools 仓库的一部分。Vulkan 于 2016 年发布，作为 OpenGL 的后继者，提供更低层的 GPU 访问。这个立方体演示是一个最小的 Vulkan 测试用例。

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

[vulkaninfo](/man/vulkaninfo)(1), [vkcube](/man/vkcube)(1), [glxinfo](/man/glxinfo)(1), [glxgears](/man/glxgears)(1)
