# TAGLINE

使用 Frida 列出本地与远程设备上的进程

# TLDR

**列出**本机上的所有进程

```frida-ps```

**列出****USB 连接的**设备上的进程

```frida-ps -U```

在 USB 设备上仅**列出正在运行的****应用**

```frida-ps -Ua```

在 USB 设备上**列出所有已安装的**应用（无论是否在运行）

```frida-ps -Uai```

按 ID **列出特定设备上**的进程

```frida-ps -D [device_id]```

**连接**到特定**主机**上的远程 frida-server

```frida-ps -H [192.168.1.100]```

# SYNOPSIS

**frida-ps** [_options_]

# PARAMETERS

**-a**, **--applications**
> 仅列出应用，而非全部系统进程。

**-i**, **--installed**
> 包括所有已安装的应用（需配合 **-a**）。

**-U**, **--usb**
> 连接到 USB 设备。

**-R**, **--remote**
> 连接到远程 frida-server。

**-H** _HOST_, **--host** _HOST_
> 连接到 HOST 上的远程 frida-server。

**-D** _ID_, **--device** _ID_
> 连接到具有给定 ID 的设备。

**--certificate** _CERTIFICATE_
> 与 HOST 进行 TLS 通信，并期望对方证书为 CERTIFICATE。

**--origin** _ORIGIN_
> 连接远程服务器时将 Origin 头设置为 ORIGIN。

**--token** _TOKEN_
> 使用 TOKEN 向 HOST 认证。

**--keepalive-interval** _INTERVAL_
> 设置保活间隔（秒），设为 0 表示禁用。

**-O** _FILE_, **--options-file** _FILE_
> 包含额外命令行选项的文本文件。

# DESCRIPTION

**frida-ps** 是一个用于列出进程的命令行工具，属于 Frida 动态插桩工具集。它的功能类似于 Unix 的 **ps** 命令，但设计上同时支持本地和远程设备（USB 连接的手机、远程 frida-server 实例）。它可以列出所有正在运行的进程，也可以只筛选应用，包括已安装但未运行的应用。

# CAVEATS

要列出远程或 USB 连接设备上的进程，该设备上必须以适当权限运行 **frida-server**。**-i** 标志需要配合 **-a**；单独使用 **--installed** 而不带 **--applications** 会报错。在本机上，列出其他用户的进程可能需要提升权限。

# HISTORY

**frida-ps** 包含在 **frida-tools** 软件包中，可通过 **pip install frida-tools** 安装。Frida 由 **Ole Andre Vadla Ravnas** 创建，于 **2014** 年公开发布。

# SEE ALSO

[frida](/man/frida)(1), [frida-trace](/man/frida-trace)(1), [ps](/man/ps)(1)
