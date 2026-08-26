# TAGLINE

通过二维码在设备间传输文件

# TLDR

**发送**文件或目录

```qrcp send [path/to/files...]```

**接收**文件

```qrcp receive```

以**压缩**方式发送

```qrcp send --zip [path/to/directory]```

使用指定**端口**

```qrcp send -p [8080]```

使用指定**网络接口**

```qrcp send -i [eth0]```

**保持服务器**运行

```qrcp send --keep-alive```

接收文件到指定**目录**

```qrcp receive --output [path/to/directory]```

在**浏览器**中打开二维码

```qrcp send --browser [path/to/file]```

# SYNOPSIS

**qrcp** [**send**|**receive**|**config**] [**-p** _port_] [**-i** _interface_] [**--zip**] [**--keep-alive**] [_files_...]

# PARAMETERS

**-p**, **--port** _port_
> 使用指定的端口号

**-i**, **--interface** _iface_
> 使用指定的网络接口

**-z**, **--zip**
> 传输前压缩文件

**-k**, **--keep-alive**
> 传输完成后保持服务器运行

**-q**, **--quiet**
> 只输出错误信息

**--browser**
> 在默认浏览器窗口中打开二维码

**--output** _dir_
> 接收文件的存放目录

**--secure**
> 使用 HTTPS 连接

**--path** _path_
> 要使用的 URL 路径（默认：随机字符串）

**-c**, **--config** _file_
> 配置文件的路径

**-d**, **--fqdn** _domain_
> 用于生成 URL 的完全限定域名

# DESCRIPTION

**qrcp** 使用二维码在设备间传输文件。它会启动一个临时的 Web 服务器并显示一个二维码，其他设备扫描该码即可下载或上传文件。

当搭建网络共享并不现实时，该工具适合用于快速传输文件。只要设备处于同一网络，它就能跨不同操作系统工作。

# CAVEATS

设备必须位于同一网络。传输速度取决于网络状况。通过 WiFi 传输大文件可能较慢。防火墙可能需要开放端口。

# HISTORY

**qrcp** 由 **Claudio d'Angelis** 创建，旨在简化设备间的文件传输。对于快速的本地传输，它免去了数据线、邮件附件或云服务的需要。

# INSTALL

```brew: brew install qrcp```

```nix: nix profile install nixpkgs#qrcp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wormhole](/man/wormhole)(1), [croc](/man/croc)(1), [rsync](/man/rsync)(1)
