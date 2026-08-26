# TAGLINE

自由的 RDP 远程桌面客户端

# TLDR

**连接**服务器

```xfreerdp /u:[username] /p:[password] /v:[ip_address]```

连接并启用**音频**

```xfreerdp /u:[username] /p:[password] /v:[ip_address] /sound:sys:alsa```

连接并启用**动态**分辨率

```xfreerdp /v:[ip_address] /u:[username] /p:[password] /dynamic-resolution```

连接并启用**剪贴板**

```xfreerdp /v:[ip_address] /u:[username] /p:[password] +clipboard```

**忽略**证书

```xfreerdp /v:[ip_address] /u:[username] /p:[password] /cert:ignore```

连接并启用**共享**目录

```xfreerdp /v:[ip_address] /u:[username] /p:[password] /drive:[path/to/directory],[share_name]```

# SYNOPSIS

**xfreerdp** [_OPTIONS_]

# PARAMETERS

**/v:** _HOST_
> 服务器主机名或 IP 地址

**/u:** _USERNAME_
> 用于身份验证的用户名

**/p:** _PASSWORD_
> 用于身份验证的密码

**/sound:** _DEVICE_
> 启用音频重定向

**/dynamic-resolution**
> 启用动态分辨率更新

**+clipboard**
> 启用剪贴板重定向

**/cert:ignore**
> 忽略证书警告

**/drive:** _PATH_,_NAME_
> 共享本地目录

**/f**
> 全屏模式

# DESCRIPTION

**xfreerdp** 是一个免费的远程桌面协议（RDP）客户端。它可以连接 Windows 远程桌面服务器以及其他兼容 RDP 的系统。

它是 FreeRDP 项目的一部分，提供开源的 RDP 实现。

# CAVEATS

在生产环境中不应忽略证书警告。如果在命令行中指定密码，密码会在进程列表中可见。

# INSTALL

```apk: sudo apk add freerdp2```

```zypper: sudo zypper install freerdp2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rdesktop](/man/rdesktop)(1), [vinagre](/man/vinagre)(1), [vncviewer](/man/vncviewer)(1)
