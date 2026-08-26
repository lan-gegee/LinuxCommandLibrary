# TAGLINE

基于 Debian 系统的交换文件管理工具

# TLDR

**停用**交换文件

```sudo dphys-swapfile swapoff```

**启用**交换文件

```sudo dphys-swapfile swapon```

**创建或调整**交换文件使其与配置一致

```sudo dphys-swapfile setup```

**彻底移除**交换文件

```sudo dphys-swapfile uninstall```

**调整交换空间大小**（标准的三步流程）

```sudo dphys-swapfile swapoff && sudo dphys-swapfile setup && sudo dphys-swapfile swapon```

**检查结果**

```swapon --show```

# SYNOPSIS

**dphys-swapfile** _command_

# DESCRIPTION

**dphys-swapfile** 创建并管理交换*文件*，而非交换分区。它存在的原因是文件可以在事后调整大小而分区不行，这对从固定磁盘镜像安装的系统至关重要；它最广为人知的身份是 **Raspberry Pi OS** 上的交换机制。

默认情况下它根据已安装内存容量计算交换大小，并以 `CONF_MAXSWAP` 为上限，因此无需任何人挑选数字就能得到合理的交换空间。设置 `CONF_SWAPSIZE` 可覆盖这一行为，将大小固定为指定兆字节数。

它通常在启动时由 init 脚本或 systemd 单元驱动，而不是手动运行。手动调用的意义在于改变大小时：文件必须先停用才能重建，所以顺序应为 **swapoff**、**setup**、**swapon**。

# PARAMETERS

**setup**
> 创建交换文件，或在配置的大小变化时调整其大小。不会激活它。

**swapon**
> 激活交换文件，不存在时会先创建。

**swapoff**
> 停用交换文件，但保留在磁盘上。

**uninstall**
> 停用交换文件并将其删除。

# CONFIGURATION

**/etc/dphys-swapfile**
> Shell 风格的配置文件，被每个子命令读取。

**CONF_SWAPFILE**
> 交换文件的路径。默认为 `/var/swap`。

**CONF_SWAPSIZE**
> 固定大小（兆字节）。留空则根据内存计算大小。Raspberry Pi OS 自带较小的默认值（通常为 100 或 200）。

**CONF_MAXSWAP**
> 计算所得大小的上限（兆字节）。默认 2048，同时也会限制 `CONF_SWAPSIZE`，因此想把交换空间提升到 2 GB 以上就必须同步提高此项。

# CAVEATS

`CONF_MAXSWAP` 会悄悄限制 `CONF_SWAPSIZE`。只设置 `CONF_SWAPSIZE=4096` 而不同时提高 `CONF_MAXSWAP`，你只会得到一个 2 GB 的交换文件且没有任何警告，这是一个常见的困惑来源。

只编辑配置不会有任何效果：文件只有靠 **setup** 才会重建，而在使用中无法重建，所以才需要 swapoff/setup/swapon 这个顺序。

在树莓派上，交换文件位于 SD 卡中，而换页会对闪存进行大量写入——这种闪存擦写次数有限，也谈不上磨损均衡。重度使用交换是搞坏 SD 卡的著名途径，而且还非常慢。如果工作负载确实需要交换，把它放到 USB SSD 上，或者改用 **zram** 在内存中压缩页面——大多数人发现后者才是小板子上的更好答案。

# SEE ALSO

[swapon](/man/swapon)(8), [swapoff](/man/swapoff)(8), [mkswap](/man/mkswap)(8), [free](/man/free)(1), [zramctl](/man/zramctl)(8)
