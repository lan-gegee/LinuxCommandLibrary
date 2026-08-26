# TAGLINE

修改 DVD booktype 以提升兼容性

# TLDR

**查询驱动器和已装载盘片的当前 booktype** 设置

```dvd+rw-booktype [/dev/dvd]```

将**当前装入的盘片**的 booktype 设为 DVD-ROM

```dvd+rw-booktype -dvd-rom-spec -media [/dev/dvd]```

让驱动器在之后的每次刻录时**默认使用 DVD-ROM booktype**

```dvd+rw-booktype -dvd-rom-spec -unit [/dev/dvd]```

**仅对 DVD+R** 刻录设置驱动器默认值

```dvd+rw-booktype -dvd-rom-spec -unit+r [/dev/dvd]```

恢复已装载 DVD+RW 盘片的**原生 booktype**

```dvd+rw-booktype -dvd+rw-spec -media [/dev/dvd]```

**打印驱动器 inquiry** 信息

```dvd+rw-booktype -inq [/dev/dvd]```

# SYNOPSIS

**dvd+rw-booktype** [**-dvd-rom-spec**|**-dvd+rw-spec**|**-dvd+r-spec**|**-inq**] [**-media**|**-unit**|**-unit+rw**|**-unit+r**] _device_

# PARAMETERS

_device_
> DVD 驱动器设备路径，例如 /dev/dvd 或 /dev/sr0。

**-dvd-rom-spec**
> 使用 DVD-ROM book type 规格。

**-dvd+rw-spec**
> 使用原生 DVD+RW book type 规格。

**-dvd+r-spec**
> 使用原生 DVD+R book type 规格。

**-inq**
> 打印驱动器 inquiry 信息并退出。

**-media**
> 将所选规格应用到当前装入的盘片。

**-unit**
> 将所选规格保存为驱动器的默认值，用于以后的刻录。

**-unit+rw**
> 仅对 DVD+RW 刻录保存驱动器默认值。

**-unit+r**
> 仅对 DVD+R 刻录保存驱动器默认值。

# DESCRIPTION

**dvd+rw-booktype** 更改记录在 DVD+R 和 DVD+RW 盘片上的 book type 字段。播放器通过读取 book type 来判断手中是哪种类型的盘片，因此它直接影响播放兼容性。

将 DVD+R 或 DVD+RW 盘片呈现为 DVD-ROM，可以让许多较老的外置播放机和机顶盒接受它，因为这些设备的出现早于 DVD+ 格式。规格标志选择要写入的身份；目标标志则决定它作用于当前盘片（**-media**），还是成为驱动器以后刻录的默认值（**-unit** 及其变体）。

只带设备参数运行该命令时，会打印当前驱动器和盘片设置而不做任何更改。

# CAVEATS

并非所有驱动器都支持修改 book type，且支持与否通常取决于固件。更改 DVD+R 盘片的 book type 是单向操作：该字段被写入盘片的控制数据后无法重写。DVD+RW 盘片则可以反复更改。此命令完全不影响 DVD-R/-RW 盘片。

# HISTORY

dvd+rw-booktype 是 **dvd+rw-tools** 软件包的一部分，用于在 Linux 上管理 DVD+R/RW 盘片。在 DVD+ 格式与 DVD- 竞争的年代，booktype 修改对兼容性变得十分重要。

# INSTALL

```apt: sudo apt install dvd+rw-tools```

```dnf: sudo dnf install dvd+rw-tools```

```pacman: sudo pacman -S dvd+rw-tools```

```apk: sudo apk add dvd+rw-tools```

```zypper: sudo zypper install dvd+rw-tools```

```brew: brew install dvd+rw-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[growisofs](/man/growisofs)(1), [dvd+rw-mediainfo](/man/dvd+rw-mediainfo)(1)
