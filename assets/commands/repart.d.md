# TAGLINE

声明式磁盘分区定义

# TLDR

**应用分区定义**

```sudo systemd-repart --dry-run```

**运行 repart**

```sudo systemd-repart```

**只显示更改而不应用**

```systemd-repart --dry-run --no-pager```

# SYNOPSIS

**/etc/repart.d/*.conf** configuration files

# DESCRIPTION

**repart.d** 存放 systemd-repart 的配置文件，后者以声明方式管理 GPT 分区表。它可以增长、创建或修改磁盘上的分区。

# CONFIGURATION

```ini
# /etc/repart.d/50-root.conf
[Partition]
Type=root
Format=ext4
Label=root
SizeMinBytes=10G
SizeMaxBytes=50G
```

# PARTITION TYPES

```
root          - Root partition
home          - Home partition
srv           - Server data
var           - Variable data
tmp           - Temporary files
swap          - Swap space
esp           - EFI System Partition
```

# EXAMPLES

```bash
# Dry run
systemd-repart --dry-run

# Apply changes
systemd-repart

# Create partition config
cat > /etc/repart.d/50-home.conf << EOF
[Partition]
Type=home
Format=ext4
Label=home
SizeMinBytes=20G
EOF
```

# OPTIONS

```ini
[Partition]
Type=home
Format=ext4
Label=home
SizeMinBytes=1G
SizeMaxBytes=50G
Weight=1000
CopyFiles=/source:/dest
MakeDirectories=/home
Verity=off
FactoryReset=no
Flags=
```

**Type=**
> GPT 分区类型（root、home、srv、var、tmp、swap、esp 等）。

**Format=**
> 要创建的文件系统（ext4、btrfs、xfs、vfat、swap 等）。

**SizeMinBytes=**, **SizeMaxBytes=**
> 分区大小的最小和最大限制。

**Weight=**
> 分配剩余空闲空间的相对权重（默认 1000）。

**CopyFiles=**
> 以 source:destination 格式将文件从宿主机复制进该分区。

**MakeDirectories=**
> 在新文件系统中以 0755 权限创建目录。

**Verity=**
> dm-verity 模式：off、data、hash 或 signature。

**FactoryReset=**
> 将分区标记为在恢复出厂设置时移除。

# CAVEATS

需要 systemd 245 及以上版本。需要仔细规划。务必先用 --dry-run。主要为基于镜像的部署和 A/B 更新方案设计。

# HISTORY

systemd-repart 于 **systemd 245** 中引入，用于基于镜像的 Linux 系统的声明式分区管理。

# SEE ALSO

[systemd-repart](/man/systemd-repart)(8), [parted](/man/parted)(8), [gdisk](/man/gdisk)(8), [fdisk](/man/fdisk)(8), [lsblk](/man/lsblk)(8)
