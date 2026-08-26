# TAGLINE

从 OVF 清单将虚拟机导入 Proxmox VE

# TLDR

从 **OVF** 包在指定存储上创建虚拟机

```qm importovf [vmid] [path/to/manifest.ovf] [storage]```

# SYNOPSIS

**qm importovf** _vmid_ _manifest_ _storage_ [_OPTIONS_]

# PARAMETERS

**vmid**
> 新虚拟机的数字 ID

**manifest**
> `.ovf` 开放虚拟化格式（OVF）清单的路径

**storage**
> 存放磁盘的目标 Proxmox 存储

# DESCRIPTION

**qm importovf** 将由开放虚拟化格式（OVF）包描述的虚拟机导入 Proxmox VE。OVF 包通常包含一个 `.ovf` 描述文件以及一个或多个磁盘镜像（通常是 `.vmdk`）。该命令以给定的 ID 创建新虚拟机，并将磁盘放置在指定存储上。

OVF 常用于从 VMware 及其他导出 OVA/OVF 设备的平台迁移。导入完成后，请在 `qm config` 或 Web 界面中检查网络、CPU 和磁盘总线设置。

# CAVEATS

所有被引用的磁盘文件必须与清单位于同一目录（或在 OVF 中声明的路径下）。某些客户机硬件选项无法一一对应到 QEMU，需要手动调整。请确保目标 `vmid` 未被占用。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具（`qm`）。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-28 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-import](/man/qm-import)(1), [qm-importdisk](/man/qm-importdisk)(1)

# RESOURCES

```[Homepage](https://www.proxmox.com)```

```[Documentation](https://pve.proxmox.com/pve-docs/qm.1.html)```

<!-- verified: 2026-07-28 -->
