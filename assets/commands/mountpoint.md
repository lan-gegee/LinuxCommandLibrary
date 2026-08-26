# TAGLINE

检查给定目录或文件是否为文件系统挂载点

# TLDR

**检查**目录是否为挂载点

```mountpoint [path/to/directory]```

**静默**检查（无输出，仅返回退出码）

```mountpoint -q [path/to/directory]```

显示文件系统的**主/次设备号**

```mountpoint -d [path/to/directory]```

显示**块设备**的主/次设备号

```mountpoint -x [/dev/sda1]```

# SYNOPSIS

**mountpoint** [**-d**|**-q**] _directory_|_file_
**mountpoint** **-x** _device_

# PARAMETERS

**-d, --fs-devno**
> 显示已挂载文件系统的主/次设备号

**-q, --quiet**
> 抑制所有输出，仅使用退出码

**--nofollow**
> 不跟随路径最后一级组件中的符号链接

**-x, --devno**
> 输出块设备的主/次设备号

**-h, --help**
> 显示帮助并退出

**-V, --version**
> 显示版本并退出

# DESCRIPTION

**mountpoint** 通过检查 /proc/self/mountinfo 来判断给定目录或文件是否为文件系统挂载点。它常用于 shell 脚本中，在执行操作前验证挂载状态。

若路径是挂载点，命令返回退出码 0；否则返回退出码 32。退出码 1 表示用法错误或系统故障。

# CAVEATS

该命令检查的是 /proc/self/mountinfo，因此结果取决于调用进程的挂载命名空间。绑定挂载可能产生与预期不同的结果。设置 LIBMOUNT_DEBUG=all 可启用调试输出。

# HISTORY

**mountpoint** 最初是 **sysvinit** 的一部分，现在作为 **util-linux** 的一部分由 Karel Zak 维护。它为脚本提供了一种无需解析 mount 输出即可检查挂载状态的可靠方法。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [umount](/man/umount)(8), [findmnt](/man/findmnt)(8)
