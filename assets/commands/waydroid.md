# TAGLINE

在 Linux 上的容器中运行 Android

# TLDR

以完整 UI **启动** Waydroid

```waydroid show-full-ui```

**初始化** Waydroid（首次运行时必须）

```sudo waydroid init```

从 APK 文件**安装** Android 应用

```waydroid app install [path/to/file.apk]```

按包名**启动** Android 应用

```waydroid app launch [com.example.app]```

**启动**或停止 Waydroid 会话

```waydroid session start|stop```

**管理** Waydroid 容器

```sudo waydroid container start|stop|restart|freeze|unfreeze```

**打开** Waydroid shell

```sudo waydroid shell```

**调整** Waydroid 窗口尺寸

```waydroid prop set persist.waydroid.width|height [number]```

# SYNOPSIS

**waydroid** [_command_] [_arguments_]

# PARAMETERS

**show-full-ui**
> 以完整 Android UI 启动 Waydroid

**init**
> 初始化 Waydroid（首次运行设置）

**app install _apk_**
> 安装 APK 文件

**app launch _package_**
> 按包名启动应用

**session start|stop**
> 启动或停止会话

**container start|stop|restart|freeze|unfreeze**
> 容器管理命令

**shell**
> 打开 Android shell

**prop set _key_ _value_**
> 设置 Android 系统属性

**log**
> 显示 Waydroid 日志

# DESCRIPTION

**waydroid** 在 Linux 上的容器中运行完整的 Android 系统。它利用 Linux 命名空间创建一个隔离的 Android 环境，并与宿主机的 Wayland 合成器集成。

Waydroid 通过与宿主机共享 Linux 内核，提供接近原生的 Android 性能。它支持 Android 应用、Google Play 服务（需额外设置）以及硬件加速。

# CAVEATS

需要 Wayland 合成器（不支持 X11）。需要 binder 和 ashmem 内核模块。由于硬件或架构差异，某些 Android 应用可能无法运行。x86 主机需要 ARM 转译层才能运行仅支持 ARM 的应用。

# INSTALL

```dnf: sudo dnf install waydroid```

```pacman: sudo pacman -S waydroid```

```apk: sudo apk add waydroid```

```nix: nix profile install nixpkgs#waydroid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[anbox](/man/anbox)(1), [lxc](/man/lxc)(1)
