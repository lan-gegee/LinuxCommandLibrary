# TAGLINE

EGL 图形库信息展示

# TLDR

显示**完整**的平台 EGL 信息

```eglinfo```

显示**简要**的平台信息

```eglinfo -B```

显示**特定平台**的信息

```eglinfo -p [x11|wayland|gbm|surfaceless]```

显示**帮助**

```eglinfo -h```

# SYNOPSIS

**eglinfo** [_options_]

# DESCRIPTION

**eglinfo** 显示系统上 EGL（Embedded-System Graphics Library，嵌入式系统图形库）实现的信息。它展示可用的显示器、配置、扩展和渲染 API。

可用于调试图形问题和验证 GPU 驱动配置。

# PARAMETERS

**-B**
> 简要输出，只显示基本信息。

**-s**
> 每行打印一个扩展。

**-v**
> 以详细形式打印配置细节。

**-l**
> 显示 OpenGL 上限（需要 EGL 1.2+）。

**-a** _api_
> 显示特定 API 的信息（gl、glcore、gles）。

**-p** _platform_
> 显示特定平台的信息（x11、wayland、gbm、surfaceless、android）。

**-h**
> 显示帮助信息。

# CAVEATS

需要可正常工作的 EGL 实现。输出取决于已安装的图形驱动。在没有显示器的无头环境中可能无法工作。

# INSTALL

```apt: sudo apt install mesa-utils```

```pacman: sudo pacman -S mesa-utils```

```apk: sudo apk add mesa-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glxinfo](/man/glxinfo)(1), [vulkaninfo](/man/vulkaninfo)(1)
