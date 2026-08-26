# 系统恢复

## 恢复策略
当机器无法启动或行为异常时，由外向内排查：拿到 Shell，看清磁盘状况，然后修复最小的故障点。大多数恢复都遵循同样的路径：启动救援介质，挂载或 `chroot` 进入已安装的系统，修复引导加载程序、文件系统或配置，然后重启。

| 症状 | 可选工具 |
|-----|-------------|
| **没有引导加载程序** | `[grub-install](/man/grub-install)` |
| **内核找不到根设备** | `[update-initramfs](/man/update-initramfs)` |
| **启动落入紧急模式** | `[findmnt](/man/findmnt)` |
| **忘记 root 密码** | `[passwd](/man/passwd)` |
| **脏文件系统** | `[fsck](/man/fsck)` |
| **软件包损坏** | `[dpkg](/man/dpkg)` |
| **磁盘濒临故障** | `[smartctl](/man/smartctl)` |
| **文件已被删除** | `[testdisk](/man/testdisk)` |

**在对故障磁盘动手改动之前，先给它做镜像。**`ddrescue` 和 `dd` 的用法参见 **备份与镜像**基础页面。

## 从救援介质启动
几乎每一次修复都从一个第二环境开始，这样你修理时损坏的系统并未运行。启动 live USB（任何发行版的安装介质都行）或发行版专用的救援镜像，然后进入终端。

在另一台机器上把 live 镜像写入 U 盘。
```[dd](/man/dd) if=linux.iso of=/dev/sdc bs=4M status=progress conv=fsync```

许多发行版还在 GRUB 里带有 **rescue** 条目，systemd 也内置了可在启动菜单中请求的恢复 Shell（见下文 *救援模式与紧急模式*）。引导加载程序本身没了的时候，就用 live USB。

live 系统的架构要与损坏的系统一致，工具集最好也一致：Arch 的 live USB 自带 `mkinitcpio`，Debian 的则自带 `update-initramfs`。

## 查看磁盘
挂载任何东西之前，先弄清楚有哪些分区。`lsblk` 显示块设备树，`blkid` 打印文件系统类型和 UUID，帮你挂载正确的对象。
```[lsblk](/man/lsblk) -f```
```[blkid](/man/blkid)```
```[fdisk](/man/fdisk) -l```

`findmnt` 显示当前已经挂载了什么，当 live 系统自动挂载磁盘时很有用。
```[findmnt](/man/findmnt)```

| 命令 | 显示内容 |
|-----|-------------|
| **lsblk -f** | 设备、文件系统、标签、挂载点 |
| **blkid** | 每个分区的 UUID 和类型 |
| **fdisk -l** | 分区表和大小 |
| **findmnt** | 当前挂载树 |

## 激活 LVM 与加密卷
如果根文件系统位于 LVM 或 LUKS 上，不激活它 live 系统就看不见。先解锁加密分区，再扫描卷组。
```[cryptsetup](/man/cryptsetup) open /dev/sda2 cryptroot```
```[vgscan](/man/vgscan)```
```[vgchange](/man/vgchange) -ay```
```[lvscan](/man/lvscan)```

此后逻辑卷会出现在 `/dev/mapper/` 下，解锁后的 LUKS 设备位于 `/dev/mapper/cryptroot`，随时可以挂载。

## 挂载损坏的系统
先把根分区挂载到某个位置，再把 `/boot`（以及 EFI 分区）叠加挂上去，使路径与真实系统一致。
```[mount](/man/mount) /dev/sda2 /mnt```
```[mount](/man/mount) /dev/sda1 /mnt/boot/efi```

如果你只是想把数据拷出来，到这里取走文件即可。如果根文件系统不肯干净地挂载，先对它做一次检查（见 *文件系统修复*）。

只想从状况可疑的磁盘抢救数据时，用 `mount -o ro` 以只读方式挂载，免得越弄越糟。

## chroot 进入系统
要使用损坏系统自己的工具（它自己的 `grub`、软件包管理器和 `passwd`），需要 `chroot` 进去。先绑定挂载内核的伪文件系统，这些工具才能工作，其中包括修复 UEFI 引导加载程序所需的 EFI 变量。
```[mount](/man/mount) --rbind /dev /mnt/dev```
```[mount](/man/mount) --rbind /proc /mnt/proc```
```[mount](/man/mount) --rbind /sys /mnt/sys```
```[mount](/man/mount) --rbind /run /mnt/run```
```[chroot](/man/chroot) /mnt /bin/bash```

在 Arch 及其衍生版上，`arch-chroot` 一步完成以上所有事情。
```[arch-chroot](/man/arch-chroot) /mnt```

结束时，`exit` 退出 chroot，然后按相反顺序递归卸载一切。
```[umount](/man/umount) -R /mnt```

**绑定挂载并非可有可无。**不挂载 `/dev`、`/proc` 和 `/sys`，`grub-install` 和 `update-initramfs` 这类工具就会以莫名其妙的方式失败。每次 `--rbind` 之后运行 `mount --make-rslave /mnt/dev`（其余同理），这样后面的 `umount -R /mnt` 才不会反向传播，把 live 系统自己的 `/dev` 和 `/sys` 也卸载掉。

## 修复引导加载程序
引导加载程序缺失或损坏会让你停在 `grub>` 提示符，或干脆没有任何菜单。在 chroot 内把 GRUB 重装到磁盘，然后重新生成它的配置。

传统 BIOS 系统要装到整块磁盘（而不是分区）。
```[grub-install](/man/grub-install) /dev/sda```

UEFI 系统要用 EFI 目标装到 EFI 分区。
```[grub-install](/man/grub-install) --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB```

然后重建菜单，让它列出已安装的内核。Debian 和 Ubuntu 把这一步封装成了 `update-grub`。
```[grub-mkconfig](/man/grub-mkconfig) -o /boot/grub/grub.cfg```
```[update-grub](/man/update-grub)```

固件启动了错误的东西时，用 `efibootmgr` 检查或清理 UEFI 启动项。
```[efibootmgr](/man/efibootmgr) -v```

## 重建 initramfs
如果内核更新被打断，或者早期启动镜像损坏（启动时报“找不到根设备”或内核恐慌），请在 chroot 内重新生成 initramfs。具体命令因发行版而异。

| 发行版 | 重建命令 |
|-----|-------------|
| **Debian / Ubuntu** | `update-initramfs -u -k all` |
| **Arch** | `mkinitcpio -P` |
| **Fedora / RHEL** | `dracut -f --regenerate-all` |

```[update-initramfs](/man/update-initramfs) -u -k all```
```[mkinitcpio](/man/mkinitcpio) -P```
```[dracut](/man/dracut) -f --regenerate-all```

## 救援模式与紧急模式
并非总是需要 live USB。systemd 自带两个可在 GRUB 菜单里请求的恢复目标：**rescue**（单用户模式，大部分服务已停止）和 **emergency**（一个光秃秃的 Shell，根以只读挂载，几乎什么都没有）。

在菜单里高亮该条目，按 `e` 编辑，把以下内容追加到 `linux` 行末，然后按 `Ctrl-X`（或 `F10`）启动：
```systemd.unit=rescue.target```
```systemd.unit=emergency.target```

想彻底绕过 init、直接拿到无需密码的 root Shell，就改为追加这一行，然后把根文件系统重新挂载为可写。
```init=/bin/bash```
```[mount](/man/mount) -o remount,rw /```

在已经运行的系统上，你可以直接切换进这些模式，问题修好后再恢复正常启动。
```[systemctl](/man/systemctl) rescue```
```[systemctl](/man/systemctl) emergency```
```[systemctl](/man/systemctl) default```

**注意：**进入 `init=/bin/bash` 后，正常的关机路径已经不存在。强制复位之前，先运行 `sync`，再用魔法 SysRq 键重启，或执行 `mount -o remount,ro /`，以免损坏文件系统。

## 重置遗忘的 root 密码
最简单的路子是从 chroot 入手：挂载系统，`chroot` 进去，直接设置密码。
```[chroot](/man/chroot) /mnt /bin/bash```
```[passwd](/man/passwd) root```

没有救援介质时，用上面的 `init=/bin/bash` 技巧，把根重新挂载为读写，改好密码，再重启。
```[mount](/man/mount) -o remount,rw /```
```[passwd](/man/passwd) root```
```[exec](/man/exec) /sbin/init```

**SELinux 系统（Fedora、RHEL）：**用这种方式改完密码后，运行 `touch /.autorelabel`。否则重写过的 `/etc/shadow` 会带着错误的安全标签，下次启动可能把你再次挡在门外。

## 文件系统修复
脏的或损坏的文件系统会卡住启动。**永远只检查未挂载的文件系统**，绝不检查正在使用的根。启动救援介质，让分区保持未挂载，然后运行合适的检查工具。

对 ext2/3/4，`fsck`（或 `e2fsck`）会重放日志并修复结构。`-f` 强制完整检查，`-y` 对每个提问都回答 yes。
```[fsck](/man/fsck) -f /dev/sda2```
```[e2fsck](/man/e2fsck) -fy /dev/sda2```

XFS 使用自己的修复工具，同样需要文件系统处于未挂载状态。
```[xfs_repair](/man/xfs_repair) /dev/sda2```

Btrfs 默认只读检查；`--repair` 是如假包换的最后手段，可能让损坏雪上加霜。
```[btrfs](/man/btrfs) check /dev/sda2```
```[btrfs](/man/btrfs) check --repair /dev/sda2```

| 文件系统 | 检查 / 修复 |
|-----|-------------|
| **ext2/3/4** | `fsck -f`, `e2fsck -fy` |
| **XFS** | `xfs_repair` |
| **Btrfs** | `btrfs check`, `--repair`（最后手段） |
| **FAT / exFAT** | `fsck.vfat -a`, `fsck.exfat` |

**小心：**对已挂载且可写的文件系统运行 `fsck` 会把它弄坏。如果必须检查根设备，从救援介质进行，或在它被重新挂载为读写之前进行。

## 修复损坏的 /etc/fstab
`/etc/fstab` 里的一个笔误或缺失的设备会把启动拖进紧急模式。在紧急 Shell 里，把根重新挂载为可写，然后修正或注释掉出错的那一行。
```[mount](/man/mount) -o remount,rw /```

编辑 `/etc/fstab`，注释掉惹祸的挂载项，或者加上 `nofail` 选项，让设备缺失不再阻塞启动。
```UUID=... /data ext4 defaults,nofail 0 2```

重启前先验证这个文件能否正确解析；`mount -a` 会尝试每个条目并报告失败。
```[mount](/man/mount) -a```
```[findmnt](/man/findmnt) --verify```

**按 UUID 匹配设备**（用 `blkid` 查看），不要按 `/dev/sdX`——后者可能每次启动都变，是 fstab 启动失败的常见原因。

## 修复损坏的软件包状态
中断的升级会让软件包停在半配置状态，系统随之无法启动或无法使用。系统起不来就在 chroot 里运行这些命令；还能勉强进 Shell 就直接运行。

Debian 和 Ubuntu 上，完成待处理的配置并解决损坏的依赖关系。
```[dpkg](/man/dpkg) --configure -a```
```[apt](/man/apt) --fix-broken install```

Fedora 和 RHEL 上，检查并重新同步软件包集合。
```[dnf](/man/dnf) check```
```[dnf](/man/dnf) distro-sync```

`rpm` 本身报错的话，重建损坏的 RPM 数据库。
```[rpm](/man/rpm) --rebuilddb```

## 用日志诊断
与其瞎猜，不如先看看系统记录了什么。`journalctl` 显示启动日志；`-x` 附带解释，`-b` 选择某次启动，`-b -1` 则显示**上一次**（失败的）启动。
```[journalctl](/man/journalctl) -xb```
```[journalctl](/man/journalctl) -b -1 -p err```

在 live USB 上，让 `journalctl` 去读损坏系统的日志，而不是 live 系统自己的。
```[journalctl](/man/journalctl) -D /mnt/var/log/journal -xb```

内核环形缓冲区能捕获导致早期崩溃的硬件和驱动错误。
```[dmesg](/man/dmesg) --level=err,warn```

## 检查磁盘健康状况
同样的错误反复出现，这块盘可能正在死去。`smartctl` 读取磁盘自身的 SMART 数据，是确认硬件故障最快的途径。
```[smartctl](/man/smartctl) -H /dev/sda```
```[smartctl](/man/smartctl) -a /dev/sda```
```[smartctl](/man/smartctl) -t short /dev/sda```

`badblocks` 扫描盘面寻找不可读扇区。存有数据的磁盘请使用只读模式。
```[badblocks](/man/badblocks) -sv /dev/sda```

`smartctl -a` 里 **Reallocated_Sector_Ct** 或 **Current_Pending_Sector** 数值不佳意味着：停下来，用 `ddrescue` 给磁盘做镜像，然后换盘。在垂死的硬件上做修复只能换来几分钟。

## 恢复已删除的文件与分区
当问题是数据丢失而非启动失败时，要在磁盘的**副本**上操作，绝不要碰原始盘。`testdisk` 能重建受损的分区表并找回整个分区。
```[testdisk](/man/testdisk) /dev/sda```

`photorec` 不管文件系统，靠文件特征签名把文件抠回来，即使磁盘被重新格式化过也有效。
```[photorec](/man/photorec) /dev/sda```

对 ext3/ext4，`extundelete` 能借助日志找回最近删除的文件。
```[extundelete](/man/extundelete) /dev/sda2 --restore-all```

**一发现文件被删，立刻卸载文件系统或直接断电。**后续写入会覆盖你正想恢复的那些数据块。

## 最后手段：先救援，再重建
如果系统坏得没法修，能抢救多少抢救多少，然后从头再来。趁故障恶化之前给磁盘做镜像，之后挂载镜像，按自己的节奏提取文件。
```[ddrescue](/man/ddrescue) /dev/sda rescue.img rescue.map```

整盘镜像装的是分区表而非单个文件系统，所以要用 `losetup -P` 以只读方式关联，暴露出其中的分区，再挂载你需要的那一个。
```[losetup](/man/losetup) -rfP --show rescue.img```
```[mount](/man/mount) -o ro /dev/loop0p2 /mnt```

把需要的数据从镜像里拷出来，重装操作系统，再从备份恢复。面对烂到底子的系统，干净的重装往往更快更安全。

有了最新的备份和演练过的恢复，每一次恢复都会轻松得多。你在这里付出的一切，就是没有备份的代价：参见 **备份与镜像**页面。
