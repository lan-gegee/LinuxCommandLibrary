# TAGLINE

创建和管理 QEMU 磁盘镜像

# TLDR

**创建磁盘镜像**

```qemu-img create -f [qcow2] [disk.qcow2] [20G]```

**转换镜像格式**

```qemu-img convert -f [raw] -O [qcow2] [input.img] [output.qcow2]```

**显示镜像信息**

```qemu-img info [disk.qcow2]```

**调整镜像大小**

```qemu-img resize [disk.qcow2] +[10G]```

**创建快照**

```qemu-img snapshot -c [snapshot1] [disk.qcow2]```

**检查镜像**的一致性错误

```qemu-img check [disk.qcow2]```

**列出镜像中的快照**

```qemu-img snapshot -l [disk.qcow2]```

# SYNOPSIS

**qemu-img** _command_ [_options_]

# PARAMETERS

**create**
> 创建新镜像。

**convert**
> 转换格式。

**info**
> 显示镜像信息。

**resize**
> 调整镜像大小。

**snapshot**
> 管理快照（-c 创建，-a 应用，-d 删除，-l 列出）。

**check**
> 执行一致性检查（仅限 qcow2、qed、vdi）。

**commit**
> 将 overlay 镜像中的更改提交到其后备文件。

**compare**
> 比较两个磁盘镜像。

**rebase**
> 更改镜像的后备文件。

**map**
> 显示镜像的分配映射。

**-f** _FORMAT_
> 输入镜像格式（raw、qcow2、vmdk、vdi、vhd 等）。

**-O** _FORMAT_
> convert 的输出格式。

**-p**
> 显示进度条。

**-q**
> 安静模式；抑制非错误输出。

# DESCRIPTION

**qemu-img** 是 QEMU 的磁盘镜像工具，用于创建、转换、调整大小和检查虚拟机磁盘镜像。它支持多种格式，包括 qcow2、raw、vmdk、vdi 和 vhd，是管理虚拟机存储以及在 hypervisor 之间迁移的关键工具。

**create** 命令以可选的精简配置方式构建新镜像，而 **convert** 在不同格式间转换，并可对输出进行压缩或加密。**info** 命令显示镜像元数据，包括格式、虚拟大小和快照详情。qcow2 镜像内部的快照可以创建和管理，用于时间点恢复。

# CAVEATS

属于 QEMU 套件的一部分（qemu-utils 软件包）。使用 resize 缩小镜像前需要先缩小客户机文件系统。只有 qcow2、qed 和 vdi 格式支持一致性检查。

# INSTALL

```apt: sudo apt install qemu-utils```

```dnf: sudo dnf install qemu-img```

```pacman: sudo pacman -S qemu-img```

```apk: sudo apk add qemu-img```

```zypper: sudo zypper install qemu-img```

```nix: nix profile install nixpkgs#qemu-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qemu](/man/qemu)(1), [virt-sparsify](/man/virt-sparsify)(1)
