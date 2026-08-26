# TAGLINE

开源 Smalltalk 虚拟机

# TLDR

**以默认镜像启动 Squeak**

```squeak```

**运行特定的镜像文件**

```squeak [path/to/image.image]```

**以无头模式运行**（无 GUI）

```squeak -headless [image.image]```

**以指定内存大小运行**

```squeak -memory [512m] [image.image]```

**以指定的 sources 文件运行**

```squeak -pathenc utf8 [image.image]```

**带 VM 选项运行**

```squeak -vm-sound-null [image.image]```

# SYNOPSIS

**squeak** [_vm-options_] [_image_] [_script-arguments_]

# PARAMETERS

**-headless**
> 不使用图形显示运行。适用于服务器和 CI 环境。

**-memory** _size_
> 设置初始内存大小（例如 256m、1g）。

**-vm-sound-null**
> 禁用声音输出。

**-vm-display-null**
> 使用空显示驱动。

**-encoding** _enc_
> 设置文件操作使用的字符编码。

**-pathenc** _enc_
> 设置路径编码（utf8、latin1）。

**-plugins** _path_
> 包含 VM 插件的目录。

**-version**
> 显示 VM 版本信息。

**-help**
> 显示帮助信息。

# ENVIRONMENT

**SQUEAK_IMAGE**
> 命令行未指定时默认使用的镜像文件。

**SQUEAK_PLUGINS**
> 包含 VM 插件的目录。

# DESCRIPTION

**squeak** 是 Squeak 的虚拟机启动器。Squeak 是一个开源的 Smalltalk 编程环境，其镜像（image）文件包含 Smalltalk 系统的完整状态，包括所有对象、类和开发环境。

该 VM 提供跨平台的可移植执行环境。不带参数启动时，它会在 **~/squeak** 和 **/usr/share/squeak** 中查找镜像，或使用 **SQUEAK_IMAGE** 环境变量中指定的镜像。

Squeak 自带完整的 IDE，包括代码浏览器、调试器和 GUI 工具集。无头模式让 Squeak 应用可以作为服务器或在 CI 流水线中运行，而无需图形输出。CommandShell 在 Squeak 环境内提供 Unix Shell 集成。

# CAVEATS

在 64 位 Linux 系统上运行 32 位 Squeak 镜像需要 32 位兼容库。图形模式必须安装 X11。镜像文件在差异较大的 VM 版本之间不可移植。大型项目可能需要调整内存设置。

# HISTORY

**Squeak** 由 Alan Kay、Dan Ingalls 等人于 **1996 年**在 Apple 创建，是 Smalltalk-80 的开源实现。名字来源于老鼠吉祥物。它源自最初的 Xerox PARC Smalltalk，并由国际社区持续开发。Squeak 衍生出了 Pharo 等项目，同时也是 Scratch（其最初实现）等教育编程工具的载体平台。

# INSTALL

```nix: nix profile install nixpkgs#squeak```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pharo](/man/pharo)(1), [smalltalkci](/man/smalltalkci)(1)
