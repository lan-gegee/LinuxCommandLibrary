# TAGLINE

创建并安装 libvirt 虚拟机

# TLDR

**创建**一台 1GB 内存、12GB 存储的虚拟机，并启动 Debian 安装

```virt-install -n [vm_name] --memory [1024] --vcpus [2] --disk path=[path/to/image.qcow2],size=[12] --cdrom [path/to/debian.iso] --osinfo [debian12]```

**创建**一台基于 UEFI、Q35 芯片组、4GB 内存的虚拟机

```virt-install -n [vm_name] --arch x86_64 --virt-type kvm --machine q35 --boot uefi --memory [4096] --vcpus [4] --disk path=[path/to/image.raw],size=[16] --cdrom [path/to/fedora.iso] --osinfo [fedora40]```

**导入**现有磁盘镜像作为虚拟机（不执行安装）

```virt-install -n [vm_name] --memory [2048] --vcpus [2] --disk path=[path/to/image.qcow2] --import --osinfo [detect=on]```

**创建**具有特定 CPU 拓扑和 host-model CPU 的虚拟机

```virt-install -n [vm_name] --cpu host-model,topology.sockets=1,topology.cores=4,topology.threads=2 --memory [16384] --disk path=[path/to/image.qcow2],size=[250] --cdrom [path/to/os.iso]```

**从远程安装树执行**自动化的 kickstart 安装

```virt-install -n [vm_name] --memory [2048] --disk path=[path/to/image.qcow2],size=[20] --location [https://download.fedoraproject.org/...] --extra-args "inst.ks=[https://path/to/kickstart]"```

**通过 PXE 和桥接网络启动**虚拟机

```virt-install -n [vm_name] --memory [2048] --disk path=[path/to/image.qcow2],size=[20] --network bridge=[br0] --pxe --osinfo [linux2022]```

# SYNOPSIS

**virt-install** [_options_]

# PARAMETERS

**-n**, **--name** _NAME_
> 新虚拟机的唯一名称。

**--memory** _SIZE_
> 客户机内存（MiB），也可使用子选项（如 memory=2048,currentMemory=1024）。

**--vcpus** _N_
> 虚拟 CPU 数量；支持 sockets/cores/threads 及热插拔上限等子选项。

**--cpu** _MODEL_
> CPU 型号与特性（例如 host-model、host-passthrough、topology.sockets=...）。

**--disk** _SPEC_
> 存储规格（path=、size=、format=、bus=、cache= 等）。无盘虚拟机使用 `--disk none`。

**-c**, **--cdrom** _PATH_
> 用作安装介质的 ISO 文件或 CDROM 设备。

**-l**, **--location** _URL_|_PATH_
> 网络安装的安装树位置（HTTP/FTP/NFS URL 或本地目录）。

**--pxe**
> 从网络（PXE）启动以进行安装。

**--import**
> 跳过操作系统安装，围绕现有磁盘镜像构建客户机。

**--boot** _OPTIONS_
> 安装后的启动配置（uefi、bios、启动顺序、loader 路径）。

**--osinfo** _ID_
> 针对特定操作系统优化客户机（libosinfo short-id，如 fedora40、debian12、win11）。取代旧的 --os-variant。

**--network** _SPEC_
> 网络接口（例如 bridge=br0、network=default、type=direct）。可重复指定。

**--graphics** _TYPE_
> 图形显示：vnc、spice 或 none。

**--virt-type** _TYPE_
> Hypervisor 类型（kvm、qemu、xen）。

**--machine** _TYPE_
> 机型类型（q35、pc 等）。

**-x**, **--extra-args** _ARGS_
> 传递给 --location 安装的额外内核命令行参数。

**--unattended**
> 使用 libosinfo 安装脚本执行自动化安装。

**--autoconsole** _TYPE_
> 控制台自动连接行为（graphical、text、none）。取代 --noautoconsole。

**--noreboot**
> 安装程序完成后不自动重启客户机。

**--wait** _MINUTES_
> 等待安装完成的时长（-1 表示无限等待，0 表示不等待）。

**--dry-run**
> 校验选项并显示生成的 XML，但不创建虚拟机。

# DESCRIPTION

**virt-install** 使用 libvirt 创建新的虚拟机。它会配置虚拟机的配置与存储，并从 ISO 镜像、网络位置或 PXE 启动等多种来源发起操作系统安装。

该工具支持高级配置，包括 UEFI 启动、CPU 绑定、NUMA 拓扑以及各种设备直通选项。它与 QEMU/KVM、Xen 及其他 libvirt 支持的 hypervisor 集成。

# CAVEATS

需要 libvirt 守护进程正在运行以及适当的虚拟化后端。KVM 需要硬件虚拟化支持。UEFI 启动需要 OVMF 固件软件包。网络安装需要能够连接到安装源。

# INSTALL

```dnf: sudo dnf install virt-install```

```pacman: sudo pacman -S virt-install```

```apk: sudo apk add virt-install```

```zypper: sudo zypper install virt-install```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virt-clone](/man/virt-clone)(1), [virsh](/man/virsh)(1), [virt-manager](/man/virt-manager)(1), [qemu-img](/man/qemu-img)(1)
