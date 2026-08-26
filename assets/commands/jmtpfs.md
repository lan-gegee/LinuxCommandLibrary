# TAGLINE

用于访问 Android 手机等 MTP 设备的 FUSE 文件系统

# TLDR

**挂载第一个可用的 MTP 设备**

```jmtpfs [mountpoint]```

**列出已连接的 MTP 设备**（显示总线、设备、厂商、产品信息）

```jmtpfs -l```

**按总线和设备号挂载指定设备**

```jmtpfs -device=[bus],[dev] [mountpoint]```

**以 allow-other 和指定 UID 挂载**

```jmtpfs -o allow_other,uid=[1000] [mountpoint]```

**以前台模式运行并输出调试信息**

```jmtpfs -f -d [mountpoint]```

**卸载设备**（请使用 fusermount，而非 jmtpfs）

```fusermount -u [mountpoint]```

# SYNOPSIS

**jmtpfs** [_options_] _mountpoint_

# PARAMETERS

**-l**
> 列出可用的 MTP 设备并退出。

**-device=**_bus_,_dev_
> 挂载位于指定 USB 总线和设备号上的设备。

**-o** _options_
> 传递 FUSE 挂载选项（如 `allow_other`、`uid=1000`、`gid=1000`、`fsname=phone`）。

**-f**
> 以前台模式运行（不守护进程化）。

**-d**
> 启用 FUSE 调试输出（隐含 `-f`）。

**-s**
> 禁用多线程操作。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**jmtpfs** 是一个 FUSE 文件系统，可将 MTP（Media Transfer Protocol，媒体传输协议）设备——Android 手机、平板电脑、相机和便携媒体播放器——暴露为普通目录。它构建于 **libmtp** 和 **libusb** 之上，无需 root 权限即可对设备存储进行读写访问。

同一时间只能有一个进程与 MTP 设备通信，因此挂载前请先解锁手机并关闭任何 "USB 模式" 弹窗。多个存储区域（内部存储、SD 卡）会在挂载点内显示为各自独立的顶层目录。

# CAVEATS

MTP 是基于会话的协议：文件大小、修改时间等元数据的更新可能滞后，且协议不支持对已有文件的随机写入（通常需要完整重写文件）。断开设备前务必先用 **fusermount -u** 卸载；如果设备失去响应，请重新插拔数据线。

# INSTALL

```apt: sudo apt install jmtpfs```

```dnf: sudo dnf install jmtpfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fusermount](/man/fusermount)(1), [fuser](/man/fuser)(1)
