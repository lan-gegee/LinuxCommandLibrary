# TAGLINE

启动 PlatformIO Home Web 界面

# TLDR

**打开 PlatformIO Home**

```pio home```

**在指定端口打开**

```pio home --port [8008]```

**打开但不启动浏览器**

```pio home --no-open```

# SYNOPSIS

**pio home** [_options_]

# PARAMETERS

**--port** _port_
> HTTP 服务器端口。

**--host** _host_
> HTTP 服务器主机。

**--no-open**
> 不打开浏览器。

**--session-id** _id_
> 会话 ID。

# DESCRIPTION

**pio home** 启动 PlatformIO Home Web 界面。提供图形化项目管理、库浏览器、开发板浏览和平台更新功能。运行本地 Web 服务器。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-init](/man/pio-init)(1), [pio-boards](/man/pio-boards)(1)
