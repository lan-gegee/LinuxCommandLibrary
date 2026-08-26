# TAGLINE

从摄像头视频扫描条形码

# TLDR

**扫描**条形码

```zbarcam```

扫描但**不显示画面**

```zbarcam --nodisplay```

打印**原始**输出

```zbarcam --raw```

指定**设备**

```zbarcam [/dev/video_device]```

# SYNOPSIS

**zbarcam** [_OPTIONS_] [_DEVICE_]

# PARAMETERS

**--nodisplay**
> 禁用视频窗口

**--raw**
> 打印条形码数据而不带类型

**--prescale** _WxH_
> 将视频预缩放到指定尺寸

**-v, --verbose**
> 提高详细程度

**-q, --quiet**
> 抑制输出

# DESCRIPTION

**zbarcam** 从视频设备（网络摄像头）扫描并解码条形码和二维码，解码的数据实时打印到标准输出。

属于 ZBar 条形码读取软件包的一部分。

# CAVEATS

需要网络摄像头或视频采集设备。条形码必须清晰可见且光照良好。可能需要 v4l2 权限。

# INSTALL

```apt: sudo apt install zbar-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zbarimg](/man/zbarimg)(1), [qrencode](/man/qrencode)(1)
