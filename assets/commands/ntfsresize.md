# TAGLINE

无数据丢失地调整 NTFS 文件系统大小

# TLDR

**显示当前大小和可缩小的最小尺寸**

```sudo ntfsresize --info /dev/[sda1]```

**调整到指定大小的试运行**

```sudo ntfsresize --no-action --size [50G] /dev/[sda1]```

**调整到指定大小**

```sudo ntfsresize --size [50G] /dev/[sda1]```

**扩展文件系统以填满当前分区**

```sudo ntfsresize --expand /dev/[sda1]```

**检查设备是否已准备好**进行调整

```sudo ntfsresize --check /dev/[sda1]```

**强制调整大小**，跳过一致性检查提示

```sudo ntfsresize --force --size [50G] /dev/[sda1]```

# SYNOPSIS

**ntfsresize** [_options_] **--info**(**-mb-only**) _device_
**ntfsresize** [_options_] [**--size** _size_[**k**|**M**|**G**]] _device_

# PARAMETERS

**-i**, **--info**
> 显示卷大小及支持的最小缩小尺寸。

**-m**, **--info-mb-only**
> 类似 --info，但只输出以 MB 为单位的可缩小尺寸。

**-s**, **--size** _SIZE_[**k**|**M**|**G**]
> 将文件系统调整为 SIZE。修饰符：k（10^3）、M（10^6）、G（10^9）。

**-x**, **--expand**
> 将文件系统扩展到当前分区大小。

**-c**, **--check**
> 检查设备是否已准备好调整大小，不做更改。

**-n**, **--no-action**
> 执行测试运行而不做更改（只读）。

**-f**, **--force**
> 即使文件系统被标记为需要一致性检查也强制操作。使用两次（-ff）可跳过所有安全检查。

**-b**, **--bad-sectors**
> 支持含有坏扇区的磁盘（否则会被拒绝）。

**-P**, **--no-progress-bar**
> 禁用进度条。

**-v**, **--verbose**
> 增加输出详细程度。

**-V**, **--version**
> 显示版本号并退出。

**-h**, **--help**
> 显示帮助信息并退出。

# DESCRIPTION

**ntfsresize** 安全地调整 NTFS 文件系统的大小，不会丢失数据，也无需事先碎片整理。它可以在未挂载的设备上缩小或扩展卷。

**缩小流程：**先用 ntfsresize 调整文件系统，再用 fdisk 或 parted 缩小分区。

**扩大流程：**先扩展分区，再用 ntfsresize 扩大文件系统（或使用 --expand）。

# TYPICAL WORKFLOW

```bash
# 1. Check filesystem
ntfsfix /dev/sda1

# 2. Get info
ntfsresize --info /dev/sda1

# 3. Resize filesystem
ntfsresize --size 50G /dev/sda1

# 4. Resize partition (separate step)
parted /dev/sda resizepart 1 50G
```

# CAVEATS

调整大小前必须卸载卷。请先备份重要数据。分区大小调整是单独的步骤。调整后 Windows 会在下次启动时安排一致性检查（chkdsk）。建议从 Live USB 运行。

# HISTORY

ntfsresize 属于 **ntfs-3g**，由 **Szabolcs Szakacsits** 等人开发，在 Linux 上提供安全的 NTFS 大小调整。

# INSTALL

```apt: sudo apt install ntfs-3g```

```dnf: sudo dnf install ntfs-3g```

```pacman: sudo pacman -S ntfs-3g```

```apk: sudo apk add ntfs-3g-progs```

```zypper: sudo zypper install ntfs-3g```

```brew: brew install ntfs-3g```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntfs-3g](/man/ntfs-3g)(8), [ntfsfix](/man/ntfsfix)(8), [parted](/man/parted)(8), [fdisk](/man/fdisk)(8)
