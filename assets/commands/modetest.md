# TAGLINE

用于测试和调试内核模式设置（KMS）功能的诊断工具

# TLDR

**列出连接器**及其针对指定驱动程序的可用模式

```modetest -M [driver] -c```

**列出所有 DRM 对象**（连接器、编码器、CRTC、平面）

```modetest -M [i915]```

**设置连接器的分辨率**

```sudo modetest -M [driver] -s [connector_id]:[1920x1080]```

**用指定格式测试平面**

```sudo modetest -M [driver] -P [plane_id]@[crtc_id]:[WxH]+[X]+[Y]@[format]```

**在对象上设置 DRM 属性**

```sudo modetest -M [driver] -w [obj_id]:[prop_name]:[value]```

**对连接器使用原子模式设置**

```sudo modetest -M [driver] -a -s [connector_id]:[1920x1080]```

# SYNOPSIS

**modetest** [**-M** _module_] [**-D** _device_] [**-c**] [**-e**] [**-f**] [**-p**] [**-s** _connector:mode_] [**-P** _plane_] [**-a**] [**-C**] [**-w** _prop_] [**-v**] [**-d**]

# PARAMETERS

**-M _module_**
> 使用给定的 DRM 驱动模块（如 i915、amdgpu、nouveau）

**-D _device_**
> 使用给定的 DRM 设备节点

**-c**
> 列出连接器及其可用模式

**-e**
> 列出编码器

**-f**
> 列出帧缓冲

**-p**
> 列出 CRTC 和平面

**-s _connector_id[,connector_id][@crtc_id]:mode[-vrefresh][@format]_**
> 在一个或多个连接器上设置显示模式

**-P _plane_id@crtc_id:WxH[+X+Y][*scale][@format]_**
> 以指定配置测试平面

**-C**
> 测试硬件光标

**-v**
> 测试垂直同步的页面翻转

**-w _obj_id:prop_name:value_**
> 在 DRM 对象上设置属性

**-a**
> 使用原子模式设置 API

**-F _pattern1,pattern2_**
> 指定测试图像的填充图案

**-d**
> 设置模式后放弃 DRM master 身份

# DESCRIPTION

**modetest** 是一个诊断工具，用于测试和调试直接渲染管理器（DRM）驱动程序的内核模式设置（KMS）功能。它枚举包括连接器、编码器、CRTC 和平面在内的 DRM 对象，并可直接设置显示模式。

该工具属于 **libdrm**，提供对图形子系统的底层访问，可用于测试显示配置、像素格式和平面叠加。未给定查询或测试选项时，它会转储所有可用的 DRM 信息。设置模式时会显示 SMPTE 彩条测试图案。

# CAVEATS

需要 root 权限或 render/video 组成员身份才能访问 DRM 设备。在正在使用的显示器上运行 modetest 可能干扰当前桌面环境（Xorg、Wayland），可能导致黑屏或画面错乱。它主要面向开发者和诊断用途。

# HISTORY

**modetest** 是 **libdrm** 项目的一部分，该项目提供与 Linux 内核直接渲染管理器交互的用户态库。KMS 在 Linux 内核 2.6.29（2009 年）中引入，目的是把显示模式设置从用户态 X 服务器移入内核。

# INSTALL

```apt: sudo apt install libdrm-tests```

```apk: sudo apk add libdrm-tests```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xrandr](/man/xrandr)(1)
