# TAGLINE

在 KDE Plasma 上创建可通过 VNC 访问的虚拟显示器

# TLDR

创建带 VNC 访问的**虚拟显示器**

```krfb-virtualmonitor --resolution 1920x1080 --name [monitor_name] --password [password] --port 5900```

在自定义端口上创建**较低分辨率**的虚拟显示器

```krfb-virtualmonitor --resolution 1280x720 --name [monitor_name] --password [password] --port [5901]```

# SYNOPSIS

**krfb-virtualmonitor** **--resolution** _WxH_ **--name** _name_ **--password** _password_ **--port** _port_

# DESCRIPTION

**krfb-virtualmonitor** 在 KDE Plasma 上创建一个可以通过 VNC 访问的虚拟显示器。这对无头系统很有用，也可以用来创建可远程共享的额外虚拟显示。

# PARAMETERS

**--resolution WxH**
> 设置虚拟显示器分辨率（如 1920x1080）

**--name NAME**
> 为虚拟显示器指定名称

**--password PASSWORD**
> 设置用于远程访问的 VNC 密码

**--port PORT**
> VNC 端口号（默认：5900）

# CAVEATS

需要 KDE Plasma 桌面环境。VNC 密码通过命令行传递，可能会在进程列表中可见。

# INSTALL

```apt: sudo apt install krfb```

```dnf: sudo dnf install krfb```

```pacman: sudo pacman -S krfb```

```apk: sudo apk add krfb```

```zypper: sudo zypper install krfb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[x11vnc](/man/x11vnc)(1), [vncviewer](/man/vncviewer)(1)
