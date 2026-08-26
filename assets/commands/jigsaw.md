# TAGLINE

XScreenSaver 屏保程序，动画演示拼图自行复原的过程

# TLDR

作为屏保在根窗口上运行

```jigsaw -root```

在窗口中运行以便测试

```jigsaw -window```

设置动画速度

```jigsaw -root -speed [1.0]```

设置拼图复杂度

```jigsaw -root -complexity [1.0]```

# SYNOPSIS

**jigsaw** [**-root** | **-window**] [_options_]

# PARAMETERS

**-root**
> 在根窗口上绘制（由 xscreensaver 本身使用）。

**-window**
> 在新建的顶级窗口中绘制。

**-window-id** _id_
> 在具有给定 X11 ID 的现有窗口中绘制。

**-speed** _float_
> 动画速度倍率。

**-complexity** _float_
> 拼图复杂度（控制拼块数量）。

**-delay** _usecs_
> 帧间延迟，单位为微秒。

**-fps**
> 显示每秒帧数计数器。

# DESCRIPTION

**jigsaw** 是 **xscreensaver**（以及 **xscreensaver-gl**）自带的 OpenGL 屏保程序之一。它加载一张图像，将其切成拼图碎片，散布在 3D 空间中，然后以动画方式让碎片飞回原位重新拼合成图片，之后再次打乱。

图像来源由 xscreensaver 标准的图像获取设置控制，因此该屏保可以使用磁盘上的随机图片、网络摄像头画面或桌面截图。

# CAVEATS

需要 OpenGL 和可用的 X11 显示。没有 3D 加速的旧系统性能会有所下降。图像来源是通过 **xscreensaver-settings** 全局配置的，无法按单个屏保程序单独设置。

# SEE ALSO

[xscreensaver](/man/xscreensaver)(1), [xscreensaver-settings](/man/xscreensaver-settings)(1)
