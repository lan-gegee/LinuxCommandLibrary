# TAGLINE

虚拟帧缓冲 X 服务器

# TLDR

**启动虚拟显示**

```Xvfb :99```

**以指定屏幕尺寸启动**

```Xvfb :99 -screen 0 [1920x1080x24]```

**以多屏幕方式启动**

```Xvfb :1 -screen 0 [1280x1024x24] -screen 1 [800x600x16]```

**使用共享内存**

```Xvfb :99 -shmem -screen 0 [1024x768x24]```

**将帧缓冲存储到目录**

```Xvfb :99 -fbdir [/tmp/xvfb]```

**用 xvfb-run 运行应用程序**

```xvfb-run -a [application]```

**xvfb-run 配合自定义屏幕**

```xvfb-run -s "-screen 0 1280x1024x24" [application]```

# SYNOPSIS

**Xvfb** [:_display_] [_options_]

# PARAMETERS

**:display**
> 显示号（默认：0）。

**-screen** _num_ _WxHxD_
> 配置屏幕：编号、宽 x 高 x 色深。

**-pixdepths** _list_
> 要支持的额外像素图深度。

**-fbdir** _dir_
> 存放内存映射帧缓冲文件的目录。

**-shmem**
> 为帧缓冲使用共享内存。

**-linebias** _n_
> 调整线条的像素化处理。

**-blackpixel** _value_
> 设置黑色像素值。

**-whitepixel** _value_
> 设置白色像素值。

# XVFB-RUN OPTIONS

**-a**, **--auto-servernum**
> 自动寻找可用的显示号。

**-s** _args_
> 传给 Xvfb 的参数。

**-e** _file_
> 存储 Xvfb 错误输出的文件。

**-f** _file_
> 要使用的授权文件。

**-n** _num_
> 要使用的服务器编号。

# DESCRIPTION

**Xvfb**（X Virtual FrameBuffer）是一种 X 服务器，它在内存中完成所有图形操作，不需要任何物理显示设备。它实现了 X11 协议，使 X 应用程序能够在没有可见输出的情况下运行。

常见用途包括：在无头服务器上运行 GUI 应用、对图形应用进行自动化测试、为 Web 服务渲染图形，以及需要 X 应用的 CI/CD 流水线。

**xvfb-run** 包装脚本可简化使用：它会自动选择一个显示号并处理认证。

默认屏幕配置为 1280x1024x24（宽 x 高 x 位深）。

# CAVEATS

没有 GPU 加速。缺少真实显示器时，某些应用的行为可能不同。内存占用随屏幕尺寸和色深增加。期望特定显示特性的应用可能无法正常工作。

# HISTORY

**Xvfb** 自 X11R5 发布起就是 X.Org 服务器发行版的一部分。它的开发目的是让 X 应用能够运行在没有显示硬件的系统上，早在无头浏览器技术出现之前就支撑着服务端渲染和自动化测试。

# INSTALL

```apt: sudo apt install xvfb```

```apk: sudo apk add xvfb```

```nix: nix profile install nixpkgs#xvfb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xvfb-run](/man/xvfb-run)(1), [xdpyinfo](/man/xdpyinfo)(1)
