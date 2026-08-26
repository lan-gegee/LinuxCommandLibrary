# TAGLINE

控制 v4l2 回环设备

# TLDR

**创建新的回环设备**并指定名称

```sudo v4l2loopback-ctl add -n "[My Virtual Camera]"```

**列出所有** v4l2 回环设备

```v4l2loopback-ctl list```

**删除**回环设备

```sudo v4l2loopback-ctl delete /dev/video[0]```

**查询**设备的属性

```v4l2loopback-ctl query /dev/video[0]```

**设置设备的帧率**

```v4l2loopback-ctl set-fps /dev/video[0] [30]```

**设置设备的格式能力**

```v4l2loopback-ctl set-caps /dev/video[0] "[UYVY:1024x768@30/1]"```

**设置超时图像**，在没有生产者活动时显示

```v4l2loopback-ctl set-timeout-image -t [3000] /dev/video[0] [path/to/image.png]```

# SYNOPSIS

**v4l2loopback-ctl** [_options_]

**v4l2loopback-ctl** **add** [_options_] [_outputdevice_ [_capturedevice_]]

**v4l2loopback-ctl** **delete** _device_

**v4l2loopback-ctl** **list** [_options_]

**v4l2loopback-ctl** **query** [_options_] _device_

**v4l2loopback-ctl** **set-fps** _device_ _fps_

**v4l2loopback-ctl** **set-caps** _device_ _caps_

**v4l2loopback-ctl** **set-timeout-image** [_options_] _device_ _image_

# PARAMETERS

**-h**, **-?**, **--help**
> 显示帮助信息并退出。

**-v**, **--version**
> 显示版本并退出。

# ADD OPTIONS

**-b** _num_, **--buffers** _num_
> 队列中缓冲区的数量。

**-w** _w_, **--max-width** _w_
> 最大帧宽度。

**-h** _h_, **--max-height** _h_
> 最大帧高度。

**--min-width** _w_
> 最小帧宽度。

**--min-height** _h_
> 最小帧高度。

**-n** _name_, **--name** _name_
> 在应用程序中显示的设备名称。

**-o** _num_, **--max-openers** _num_
> 最大并发打开者数量。

**-x** _x_, **--exclusive-caps** _x_
> 声明独占能力（0 或 1）。

# SET-CAPS FORMAT

caps 参数使用 **'_fourcc_:_width_x_height_@_fps_'** 格式，例如 **'UYVY:1024x768@60/1'**。使用 **'any'** 可清除当前的 caps 设置。

# SET-TIMEOUT-IMAGE OPTIONS

**-t** _timeout_, **--timeout** _timeout_
> 显示后备图像前的超时时长（毫秒）。

# DESCRIPTION

**v4l2loopback-ctl** 是用于管理由 **v4l2loopback** 内核模块创建的虚拟视频回环设备的实用工具。这些虚拟设备充当管道：一个应用程序向设备写入视频帧（生产者），另一个应用程序从中读取（消费者），从而支持虚拟网络摄像头、向视频会议工具共享屏幕、视频处理流水线等用例。

该工具采用基于动词的接口，提供创建、删除、列出和查询回环设备的命令，还可配置其帧率、格式能力和后备超时图像。

# CAVEATS

需要已加载 **v4l2loopback** 内核模块。创建和删除设备通常需要 root 权限。set-caps 的格式字符串必须与 fourcc:WxH@fps 模式完全匹配。并非所有应用都能正确检测或使用回环设备，尤其是在未设置独占能力时。

# HISTORY

**v4l2loopback** 项目由 **IOhannes m zmölnig** 创建，目的是使用 Video4Linux2（V4L2）框架在 Linux 上提供虚拟视频设备。它作为创建虚拟网络摄像头的方式被广泛采用，在视频会议兴起期间尤为流行。**v4l2loopback-ctl** 实用程序后来被加入，提供了一个用户友好的接口来管理这些设备，而无需直接操作内核模块参数。

# INSTALL

```apt: sudo apt install v4l2loopback-utils```

```pacman: sudo pacman -S v4l2loopback-utils```

```zypper: sudo zypper install v4l2loopback-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[v4l2-ctl](/man/v4l2-ctl)(1), [ffmpeg](/man/ffmpeg)(1), [modprobe](/man/modprobe)(8)
