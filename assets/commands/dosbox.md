# TAGLINE

用于经典游戏和应用程序的 DOS 模拟器

# TLDR

挂载目录后**启动 DOSBox**

```dosbox -c "mount c [/path/to/games]"```

**直接运行 DOS 程序**

```dosbox [path/to/program.exe]```

**使用指定配置启动 DOSBox**

```dosbox -conf [path/to/dosbox.conf]```

**以全屏模式启动**

```dosbox -fullscreen```

**程序运行结束后退出**

```dosbox [program.exe] -exit```

**以指定 CPU 周期数启动**

```dosbox -c "cycles [max]"```

**挂载 CD-ROM 镜像**

```dosbox -c "imgmount d [path/to/image.iso] -t cdrom"```

**启动时运行批处理文件**

```dosbox -c "mount c ." -c "c:" -c "[autoexec.bat]"```

# SYNOPSIS

**dosbox** [_-conf config_] [_-c command_] [_-fullscreen_] [_-exit_] [_program_] [_arguments_]

# PARAMETERS

**-conf** _file_
> 加载指定的配置文件。

**-c** _command_
> 启动后执行一条 DOS 命令。可以多次指定。

**-fullscreen**
> 以全屏模式启动。

**-exit**
> 程序终止时退出 DOSBox。

**-machine** _type_
> 模拟特定的机器类型（hercules、cga、tandy、pcjr、ega、svga_s3）。

**-noconsole**
> 启动时不显示控制台窗口（仅限 Windows）。

**-startmapper**
> 立即启动按键映射器。

**-noautoexec**
> 跳过配置文件中的 [autoexec] 部分。

**-scaler** _scaler_
> 对图形输出使用指定的缩放器。

**-forcescaler** _scaler_
> 即使不是最优也强制使用指定的缩放器。

**-securemode**
> 以安全模式运行，禁用 mount 及其他可能有危险的命令。

**-userconf**
> 加载用户配置文件。

**-version**
> 打印版本信息。

**-lang** _file_
> 使用指定的语言文件。

**-printconf**
> 打印默认配置文件的位置。

**-editconf** _program_
> 用指定的编辑器打开配置文件。

**-resetconf**
> 删除默认配置文件。

**-resetmapper**
> 删除默认的映射器文件。

**-opencaptures** _program_
> 用指定的程序打开截图文件夹。

**-socket** _n_
> 向 nullmodem 模拟传递套接字编号。

# DESCRIPTION

**DOSBox** 是一款模拟器，可重现配备 DOS 的 IBM PC 兼容机。它通过模拟那个年代的 x86 CPU、图形、声音和输入硬件，让经典 DOS 游戏和应用程序能在现代操作系统上运行。

模拟器提供一个命令提示符，标准 DOS 命令在其中可用：**dir**、**cd**、**copy** 等。宿主机的目录通过挂载为虚拟驱动器来访问。命令 **mount c /path/to/folder** 可将一个文件夹显示为 DOSBox 内部的 C: 盘。

配置文件控制模拟设置，包括 CPU 速度（cycles）、图形渲染、声卡模拟（Sound Blaster、AdLib 等）以及内存分配。默认配置文件位于 Linux 的 **~/.dosbox/** 或 Windows 的用户配置目录中。

按键映射可以通过内置的 keymapper（Ctrl+F1）自定义。常用快捷键包括 Alt+Enter 切换全屏、Ctrl+F10 释放鼠标捕获，以及 Ctrl+F12/F11 调整 CPU 速度。DOSBox 还能挂载磁盘镜像（ISO、CUE/BIN），满足需要 CD-ROM 的游戏。

# CONFIGURATION

**~/.dosbox/dosbox-*.conf**
> 主配置文件，控制 CPU、图形、声音和 autoexec 设置。

**/etc/dosbox.conf**
> 系统级配置文件（Linux）。

# CAVEATS

并非所有 DOS 软件都兼容；非常古老或要求很高的程序可能无法正常运行。CPU 周期设置可能需要调整才能获得合适的游戏速度。某些防拷贝机制可能无效。DOSBox 为游戏而生，不适合把 DOS 当作主要操作系统来运行。

# HISTORY

**DOSBox** 由 Peter Veenstra 和 Sjoerd van der Berg 于 **2002 年**发起，目的是在现代系统上运行旧的 DOS 游戏。它成为最受欢迎的 DOS 模拟器之一，支持 Windows、Linux、macOS 等多种平台。开发在各版本中持续推进，DOSBox Staging 和 DOSBox-X 作为功能更丰富的增强分支相继出现。

# INSTALL

```apt: sudo apt install dosbox```

```dnf: sudo dnf install dosbox-staging```

```pacman: sudo pacman -S dosbox```

```apk: sudo apk add dosbox-staging```

```zypper: sudo zypper install dosbox```

```brew: brew install dosbox-staging```

```nix: nix profile install nixpkgs#dosbox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qemu](/man/qemu)(1), [wine](/man/wine)(1)
