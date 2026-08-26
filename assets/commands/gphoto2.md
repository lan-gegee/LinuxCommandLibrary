# TAGLINE

通过 libgphoto2 控制数码相机的命令行客户端

# TLDR

**检测已连接的相机**及其所连接的端口

```gphoto2 --auto-detect```

**拍摄一张照片**并将其保留在相机上

```gphoto2 --capture-image```

**拍摄一张照片**并立即下载

```gphoto2 --capture-image-and-download```

**列出相机上存储的所有文件**

```gphoto2 --list-files```

按索引编号**下载特定文件**

```gphoto2 --get-file [number]```

**下载相机上的所有文件**

```gphoto2 --get-all-files```

以 30 秒间隔**延时拍摄** 10 帧

```gphoto2 --capture-image-and-download -F 10 -I 30```

将**实时预览流**输出到标准输出（可用作网络摄像头源）

```gphoto2 --stdout --capture-movie```

# SYNOPSIS

**gphoto2** [_options_] _action_

# PARAMETERS

**--auto-detect**
> 检测连接到系统的相机。

**--list-cameras**
> 打印所有受支持相机型号的列表。

**--list-ports**
> 打印受支持端口类型的列表。

**--port** _PATH_
> 选择特定端口（例如 _usb:_ 或 _serial:/dev/ttyS0_）。

**--camera** _MODEL_
> 强制使用特定的相机型号。

**-L**, **--list-files**
> 列出相机上当前文件夹中的文件。

**-f** _FOLDER_, **--folder** _FOLDER_
> 切换到相机上的指定文件夹。

**-p** _RANGE_, **--get-file** _RANGE_
> 按编号范围下载文件（例如 _1_、_1-4_、_1,3,5_）。

**--get-all-files**
> 下载当前文件夹中的所有文件。

**--get-thumbnail** _RANGE_
> 下载缩略图而不是完整文件。

**--get-raw-data** _RANGE_
> 下载原始传感器数据。

**-u** _FILE_, **--upload-file** _FILE_
> 将文件上传到相机。

**-d** _RANGE_, **--delete-file** _RANGE_
> 按编号删除文件。

**-D**, **--delete-all-files**
> 删除当前文件夹中的所有文件。

**--capture-image**
> 触发快门并将图像保留在相机上。

**--capture-image-and-download**
> 拍摄并立即下载生成的文件。

**--capture-movie** [_=COUNT_|_=SECONDSs_]
> 拍摄视频或预览帧流。

**-F** _N_, **--frames** _N_
> 延时拍摄的帧数。

**-I** _SECONDS_, **--interval** _SECONDS_
> 延时拍摄中帧与帧之间的秒数。

**--filename** _TEMPLATE_
> 指定输出文件名模板（支持 _%n_、_%C_、_%f_ 等）。

**--stdout**
> 将下载的数据写入标准输出而不是文件。

**--list-config**
> 列出所有相机配置项。

**--get-config** _NAME_
> 打印某个配置项的当前值。

**--set-config** _NAME=VALUE_
> 设置配置项（例如 _iso=400_、_shutterspeed=1/125_）。

**--summary**
> 打印相机功能的摘要。

**-q**, **--quiet**
> 降低输出详细程度。

**-h**, **--help**
> 显示用法信息。

# DESCRIPTION

**gphoto2** 是 **libgphoto2** 库的官方命令行前端，可通过 USB、串口、PTP/IP 等传输方式访问超过 **2500 款数码相机**。它让摄影师和开发者无需厂商软件即可拍摄图像、下载文件、触发快门、将相机联机到电脑以及调整设置。

该工具作用于相机存储的当前文件夹；用 **--folder** 切换文件夹，用 **--list-folders** 或 **--list-files** 查询结构。每个文件通过从 1 开始的索引来寻址。多个操作可以在一条命令行上组合，并按顺序执行。

在配置方面，gphoto2 通过 **--list-config**、**--get-config** 和 **--set-config** 暴露相机的属性树（曝光、ISO、白平衡、对焦模式等）。这使它成为远程拍摄工作室、天文台设备和 Linux 网络摄像头方案（例如把 **--capture-movie** 的输出通过管道传给 **ffmpeg** 和 **v4l2loopback**）的常用构件。

# CAVEATS

并非每台相机都支持所有功能；PTP 相机通常允许拍摄和配置，而较旧的不兼容 PTP 的相机仅提供文件传输。直接使用 gphoto2 前，请先停止任何自动挂载 MTP/PTP 相机的桌面服务（如 _gvfs-gphoto2-volume-monitor_）；否则 USB 设备会被其他进程占用。长时间联机会话可能需要显式设置电源选项，以防相机进入休眠。

# HISTORY

**gphoto** 项目由 **Scott Fritzinger** 于 **1997 年**发起，目的是为 Linux 用户提供一个访问消费级数码相机的通用接口。第二代库 **libgphoto2** 及其参考客户端 **gphoto2** 于 **2001 年**发布，围绕模块化的 camlib 驱动重构了架构。该项目由开源社区维护，是 GNOME 和 KDE 等桌面环境中相机支持的基石。

# INSTALL

```apt: sudo apt install gphoto2```

```dnf: sudo dnf install gphoto2```

```pacman: sudo pacman -S gphoto2```

```apk: sudo apk add gphoto2```

```brew: brew install gphoto2```

```nix: nix profile install nixpkgs#gphoto2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [v4l2-ctl](/man/v4l2-ctl)(1), [exiftool](/man/exiftool)(1)
