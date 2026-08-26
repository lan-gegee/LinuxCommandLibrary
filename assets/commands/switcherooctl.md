# TAGLINE

在特定 GPU 上启动命令

# TLDR

**列出**已知的 GPU（未给出命令时的默认行为）

```switcherooctl```

显式**列出** GPU

```switcherooctl list```

在**第一块独立 GPU** 上启动命令

```switcherooctl launch [glxgears]```

在**指定 GPU** 上启动命令（编号来自 **list**）

```switcherooctl launch [-g|--gpu] [1] [firefox]```

打印 **switcheroo-control** 版本

```switcherooctl version```

显示子命令的**帮助**

```switcherooctl help launch```

启动 **switcheroo-control** 守护进程

```sudo systemctl enable --now switcheroo-control.service```

# SYNOPSIS

**switcherooctl** **help** [_COMMAND_]

**switcherooctl** **version**

**switcherooctl** **list**

**switcherooctl** **launch** [**-g**|_**--gpu=**_GPU_] _COMMAND_...

# COMMANDS

**help** [_COMMAND_]
> 打印简短用法，或某个命令的详细帮助。

**version**
> 打印此 CLI 所属的 **switcheroo-control** 版本。

**list**
> 列出已知 GPU。每个条目包含一个设备编号，供 **launch --gpu** 使用。未给出命令时这是默认命令。

**launch** [_OPTION_] _COMMAND_...
> 在某块 GPU 上运行 _COMMAND_。不带 **-g** 时使用第一块独立（非默认）GPU；若系统没有独立 GPU 则使用默认 GPU。

# PARAMETERS

**-g**, **--gpu=**_GPU_
> 要在其上启动的 GPU（来自 **list** 的设备编号）。适用于 **launch**。

# DESCRIPTION

**switcherooctl** 是 **switcheroo-control** 的命令行客户端。后者是一个 D-Bus 服务，用于发现在混合显卡 Linux 系统上的 GPU，并告知桌面环境存在哪些适配器。GNOME 和 KDE 使用该 API 实现"使用独立显卡运行"之类的菜单操作。

**list** 会打印每个适配器及其设备编号、它是默认 GPU 还是独立 GPU，以及守护进程会为该设备设置的环境变量。**launch** 以这些变量启动进程，使应用在所选 GPU 上渲染（通常是 PRIME 渲染卸载：Mesa 的 **DRI_PRIME**，NVIDIA 上则是厂商的卸载变量）。它不会切换硬件复用器（mux）。

守护进程是 **switcheroo-control.service**。没有它，**switcherooctl** 无法枚举 GPU。软件包名为 **switcheroo-control**；你输入的命令是 **switcherooctl**。

# CAVEATS

需要 **switcheroo-control.service** 正在运行，且机器拥有不止一块 GPU。这是渲染卸载而非 mux 切换：显示器可以继续连接集成 GPU，而单个应用使用独立 GPU。在特殊硬件上检测可能错误标记适配器。Wayland 加专有 NVIDIA 驱动历来需要额外的合成器与驱动支持；某些程序可能仍需 **prime-run** 或厂商工具。

# HISTORY

**switcheroo-control** 由 **Bastien Nocera**（hadess）为 GNOME 编写，让桌面外壳无需用户手动设置环境变量即可提供独立 GPU 启动功能。源代码从 GitHub 迁移到 **gitlab.freedesktop.org**；旧的 GitHub 镜像于 **2020 年 6 月**归档。GNOME 3.36（2020 年）收紧了 D-Bus API。openSUSE 后来推荐用 **switcherooctl** 取代 **suse-prime** 和 Bumblebee 来支持混合显卡笔记本。

# INSTALL

```apt: sudo apt install switcheroo-control```

```dnf: sudo dnf install switcheroo-control```

```pacman: sudo pacman -S switcheroo-control```

```zypper: sudo zypper install switcheroo-control```

```nix: nix profile install nixpkgs#switcheroo-control```

<!-- packages: 2026-08-17 -->

# SEE ALSO

[prime-run](/man/prime-run)(1), [optirun](/man/optirun)(1), [envycontrol](/man/envycontrol)(1), [nvidia-smi](/man/nvidia-smi)(1), [glxinfo](/man/glxinfo)(1)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/hadess/switcheroo-control)```

<!-- verified: 2026-08-17 -->
