# TAGLINE

执行沙箱化的 Flatpak 应用程序

# TLDR

**运行**已安装的 flatpak 应用

```flatpak run [com.example.app]```

从**特定分支**运行应用

```flatpak run --branch=[stable|beta|master] [com.example.app]```

在 flatpak 内运行**交互式 shell**

```flatpak run --command=sh [com.example.app]```

以**指定的运行时版本**运行

```flatpak run --runtime-version=[24.08] [com.example.app]```

以**另一个运行时**运行

```flatpak run --runtime=[org.freedesktop.Sdk] [com.example.app]```

以**额外的文件系统访问权限**运行

```flatpak run --filesystem=[home] [com.example.app]```

以**严格沙箱模式**运行（剥离额外权限）

```flatpak run --sandbox [com.example.app]```

# SYNOPSIS

**flatpak run** [_options_] _ref_ [_args..._]

# PARAMETERS

**--user**
> 使用按用户划分的安装

**--system**
> 使用系统级安装

**--arch** _arch_
> 针对特定架构

**--branch** _branch_
> 使用特定分支（stable、beta、master）

**--command** _command_
> 运行指定命令而非默认命令

**--runtime** _runtime_
> 使用另一个运行时

**--runtime-version** _version_
> 使用特定的运行时版本

**--sandbox**
> 以最小权限运行（剥离额外权限）

**--share** _subsystem_
> 与宿主机共享子系统（network、ipc）

**--unshare** _subsystem_
> 不与宿主机共享子系统

**--socket** _socket_
> 暴露众所周知的套接字（x11、wayland、pulseaudio）

**--nosocket** _socket_
> 不暴露套接字

**--filesystem** _path_
> 授予文件系统访问权限（home、host、/path）

**--nofilesystem** _path_
> 撤销文件系统访问权限

**--env** _var=value_
> 设置环境变量

**--device** _device_
> 向应用暴露设备（dri、input、usb、kvm、shm、all）

**--devel**
> 使用应用元数据中指定的 devel 运行时

**--die-with-parent**
> 当启动进程死亡时终止应用程序

# DESCRIPTION

**Flatpak run** 在 Flatpak 的沙箱环境中执行应用程序或打开 shell。沙箱提供隔离：运行时挂载于 **/usr**，应用位于 **/app**，并有一个可写的 **/var** 目录用于持久化数据。

运行应用程序时，额外的参数会透传给该应用。对于运行时，该命令会打开一个 shell 用于开发和测试。

沙箱会自动调整环境变量，包括 **PATH**、**LD_LIBRARY_PATH** 和图形相关变量，以确保适当的隔离并防止对沙箱运行的干扰。

# CAVEATS

沙箱权限由应用的清单控制，可以在运行时通过 **--share**、**--socket** 和 **--filesystem** 选项覆盖。使用 **--sandbox** 可提供最大程度的隔离，但可能破坏需要特定权限的应用。某些应用在使用修改后的运行时可能无法正常工作。

# HISTORY

本命令是 Red Hat 的 Alexander Larsson 所开发 **Flatpak** 项目的一部分。Flatpak 约于 **2015 年**从 xdg-app 项目演化而来，为 Linux 提供具有强隔离保证的沙箱化应用执行方式。

# INSTALL

```apt: sudo apt install flatpak```

```dnf: sudo dnf install flatpak```

```pacman: sudo pacman -S flatpak```

```apk: sudo apk add flatpak```

```zypper: sudo zypper install flatpak```

```nix: nix profile install nixpkgs#flatpak```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flatpak](/man/flatpak)(1), [flatpak-install](/man/flatpak-install)(1)
