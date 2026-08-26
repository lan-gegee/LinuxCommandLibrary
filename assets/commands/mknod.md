# TAGLINE

以特殊文件的形式创建块设备、字符设备或 FIFO

# TLDR

创建**块设备**特殊文件

```sudo mknod [path/to/device_file] b [major_device_number] [minor_device_number]```

创建**字符设备**特殊文件

```sudo mknod [path/to/device_file] c [major_device_number] [minor_device_number]```

创建 **FIFO**（命名管道）

```sudo mknod [path/to/device_file] p```

创建带**指定权限**的设备文件

```sudo mknod -m [0660] [path/to/device_file] c [major] [minor]```

创建带**默认 SELinux 上下文**的设备文件

```sudo mknod -Z [path/to/device_file] c [major] [minor]```

# SYNOPSIS

**mknod** [_OPTION_]... _NAME_ _TYPE_ [_MAJOR_ _MINOR_]

# PARAMETERS

**-m**, **--mode**=_MODE_
> 将文件权限位设为 MODE（符号或数字形式），而不是默认的 a=rw 减去 umask。

**-Z**
> 将 SELinux 安全上下文设为默认类型。

**--context**[=_CTX_]
> 类似 -Z；若指定了 CTX，则将 SELinux 或 SMACK 安全上下文设为 CTX。

**--help**
> 显示帮助并退出。

**--version**
> 输出版本信息并退出。

**b**
> 创建块（缓冲）特殊文件；MAJOR 和 MINOR 为必需。

**c**, **u**
> 创建字符（无缓冲）特殊文件；MAJOR 和 MINOR 为必需。

**p**
> 创建 FIFO（命名管道）；必须省略 MAJOR 和 MINOR。

# DESCRIPTION

**mknod** 以特殊文件的形式创建块设备、字符设备或 FIFO（命名管道）。设备文件为用户程序与内核中的设备驱动之间提供接口。

块设备以固定大小的块传输数据并支持缓冲（如硬盘）。字符设备逐字符传输数据且不缓冲（如终端、串口）。FIFO 通过命名文件实现进程间通信。

主设备号和次设备号标识设备驱动以及具体的设备实例。这些编号可用十进制、八进制（前缀 0）或十六进制（前缀 0x）表示。

# CAVEATS

现代 Linux 系统使用 udev 和 devtmpfs 动态创建设备节点，手动使用 mknod 的场景已很少见。创建设备节点需要 root 权限。错误的主/次设备号可能导致系统不稳定。/dev 目录通常以 devtmpfs 形式挂载并被自动管理。

# HISTORY

**mknod** 是可追溯到早期 Unix 系统的标准 Unix 命令。在 Linux 上它属于 **GNU coreutils**。该命令直接调用 mknod(2) 系统调用来创建特殊文件。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfifo](/man/mkfifo)(1), [stat](/man/stat)(2), [mknod](/man/mknod)(2)
