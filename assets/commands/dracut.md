# TAGLINE

initramfs 镜像生成器

# TLDR

为**当前内核**生成 initramfs

```dracut```

生成并**覆盖**已有镜像

```dracut -f```

为**指定内核**生成

```dracut --kver [kernel_version]```

**列出**可用模块

```dracut --list-modules```

为所有已安装内核**重建** initramfs

```dracut --regenerate-all -f```

构建可在任何硬件上启动的**通用**镜像

```dracut -f --no-hostonly [/boot/initramfs-rescue.img]```

显示镜像期望的**内核命令行**

```dracut --print-cmdline```

添加额外的**模块与驱动**

```dracut -f --add [crypt] --add-drivers [nvme]```

# SYNOPSIS

**dracut** [_options_] [_image_] [_kernel-version_]

# DESCRIPTION

**dracut** 用于构建 initramfs：这是内核解包进内存并在真正的根文件系统可用之前运行的小型根文件系统。它的任务是加载查找并挂载真正根文件系统所需的一切，这可能意味着组装 LVM 卷组、解锁 LUKS 设备、启动 RAID 阵列，或为 NFS/iSCSI 根建立网络连接。

较老的生成器使用手写脚本，而 dracut 是事件驱动的：它在镜像中填充 **udev** 规则和 systemd 单元，启动过程随设备出现而推进，而不是按固定顺序轮询。镜像内容来自 **dracut 模块**，即位于 `/usr/lib/dracut/modules.d/` 下的一组脚本及其依赖的小集合；模块根据运行系统的需要自动选择，也可用 **--add** 和 **--omit** 强制启用或排除。

最重要的选择是 **host-only** 模式。使用 **-H** 时，镜像只包含这台特定机器启动所需的驱动和模块，体积小且速度快；多数发行版默认采用此模式。**--no-hostonly** 镜像包含的内容多得多，能在构建它的机器之外的其他硬件上启动——救援镜像或在容器/chroot 内构建的镜像正需要这种方式。

# PARAMETERS

**-f**, **--force**
> 覆盖已有的镜像。

**--kver** _VERSION_
> 为指定的内核版本而非当前运行的内核构建。

**--regenerate-all**
> 为每个已安装内核重建 initramfs。

**-a**, **--add** _MODULES_
> 在自动选择的集合之上追加 dracut 模块。

**-o**, **--omit** _MODULES_
> 排除指定的 dracut 模块。

**--force-add** _MODULES_
> 即使模块本会被排除，也强制加入。

**-m**, **--modules** _MODULES_
> 只使用这些 dracut 模块，不用其他任何模块。

**--add-drivers** _MODULES_ / **--omit-drivers** _MODULES_
> 添加或排除特定的*内核*模块（驱动）。

**-d**, **--drivers** _MODULES_
> 只包含这些内核模块。

**-H**, **--hostonly** / **-N**, **--no-hostonly**
> 构建针对本机的镜像，或可在其他硬件上启动的通用镜像。

**--list-modules** / **-M**, **--show-modules**
> 列出可用的 dracut 模块，或打印构建过程中将要包含的模块。

**--print-cmdline**
> 打印本系统根文件系统配置所需的内核命令行参数。

**--kernel-cmdline** _PARAMS_
> 在镜像中嵌入默认的内核命令行参数。

**-I**, **--install** _FILES_
> 将额外文件安装进镜像，并解析其库依赖。

**--include** _SRC_ _TARGET_
> 将文件或目录复制到镜像内的指定路径。

**--fstab**
> 使用 `/etc/fstab` 而非 `/proc/self/mountinfo` 来确定挂载。

**--uefi**
> 生成结合内核、initramfs 和命令行的 UEFI 可执行文件。

**--gzip** / **--xz** / **--zstd** / **--no-compress**
> 选择压缩算法，或完全不压缩。

**--sysroot** _DIR_
> 基于另一个根目录构建，用于交叉构建或安装器场景。

**-v**, **--verbose** / **-q**, **--quiet**
> 提高或降低输出详细程度。

# CONFIGURATION

**/etc/dracut.conf**
> dracut 行为与模块选择的主配置文件。

**/etc/dracut.conf.d/**
> 存放附加配置文件的目录。

**/usr/lib/dracut/dracut.conf.d/**
> 全系统范围的 dracut 配置目录。

# CAVEATS

损坏的 initramfs 会让机器无法启动，而且直到下次重启你才会发现问题。请始终保留上一个内核及其镜像，使引导菜单中仍有进入系统的途径；并且宁可把 `dracut -f` 用在备用镜像名上，也不要覆盖你正在运行的镜像。

**Host-only 镜像不可移植。**在一台机器上、容器内或 chroot 中用 **-H** 构建的镜像可能缺少目标硬件所需的驱动，导致你落入 emergency shell。只要镜像要在构建它的机器之外的硬件上启动，就应使用 **--no-hostonly** 构建。

切换引导程序配置前值得先运行 `--print-cmdline`：只有当内核命令行告诉镜像去哪里找根文件系统时，它才能找到；缺少 `rd.luks.uuid` 或 `rd.lvm.lv` 时，失败恰好发生在最难调试的地方。

历史上，dracut 是 Fedora/RHEL/SUSE 的生成器，而 Debian 和 Ubuntu 使用 **initramfs-tools**；但如今 Debian 和 Ubuntu 也打包了 dracut 作为替代方案，它不再是 Red Hat 独有的工具。

# HISTORY

dracut 由 Red Hat 的 Harald Hoyer 等人于 **2008 年**前后启动，用来取代 `mkinitrd`——后者生成的镜像是发行版专属 shell 脚本的纠缠体，难以维护。其设计目标是让 initramfs 自身只保留尽可能少的逻辑，由 udev 事件驱动启动过程，这样一个生成器就能服务于所有发行版，而不是各发行版各自造轮子。Fedora、RHEL 和 SUSE 相继采用，使其成为事实上的标准。

**2024 年 3 月**，由于原仓库停滞，开发工作迁移到了 **dracut-ng**——这是一个由前任维护者联合多个发行版共同参与的协作分支。现在的发布都来自 dracut-ng，各发行版也已跟进。

# INSTALL

```apt: sudo apt install dracut-core```

```dnf: sudo dnf install dracut```

```pacman: sudo pacman -S dracut```

```apk: sudo apk add dracut-core```

```zypper: sudo zypper install dracut```

```nix: nix profile install nixpkgs#dracut```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkinitramfs](/man/mkinitramfs)(8), [lsinitrd](/man/lsinitrd)(1), [update-initramfs](/man/update-initramfs)(8), [mkinitcpio](/man/mkinitcpio)(8)

# RESOURCES

```[Source code](https://github.com/dracut-ng/dracut-ng)```

```[Homepage](https://dracut-ng.github.io/)```

<!-- verified: 2026-07-14 -->
