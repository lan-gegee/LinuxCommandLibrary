# TAGLINE

从 OCI 镜像创建 Proxmox VE microVM 模板

# TLDR

从 _debian:trixie-slim_ **创建默认的 microVM 模板**（VMID 9000）

```pve-microvm-template```

**将模板克隆**为新的 microVM

```qm clone [9000] [901] --name [my-sandbox] --full```

**启动克隆出的 microVM** 并打开串口控制台

```qm start [901] && qm terminal [901]```

不再需要时**移除模板**

```qm destroy [9000]```

# SYNOPSIS

**pve-microvm-template**

# DESCRIPTION

**pve-microvm-template** 是随 **pve-microvm** Debian 软件包附带的辅助脚本。该软件包是一个实验性插件，将 QEMU 的 **microvm** 机型引入 **Proxmox VE**。运行一次即可拉取最小化的 OCI 基础镜像（默认 _debian:trixie-slim_，约 28 MB），用 **pve-oci-import** 将其转换为可启动磁盘，注册为 Proxmox VM 9000，配置 microvm 机型和串口控制台，最后将该 VM 转换为模板。

模板创建后，就可以通过标准的 **qm clone** 流程即时创建新的 microVM。由于 microVM 的启动时间远小于一秒，且使用精简内核、不含固件和 PCI 仿真，生成的沙箱行为更像容器而非完整的 VM，同时保持 KVM 级别的隔离。

该命令有意设计为零参数：它是一个一次性的引导工具，之后的全部操作都使用 **qm clone** 和 **qm start** 完成。

# CAVEATS

整个 **pve-microvm** 项目被标记为**高度实验性**：microvm 是 Proxmox 官方不支持的 QEMU 机型，该软件包通过修补 **qemu-server** 来添加支持，且实时迁移、HA 以及一些备份边界情况均未经过测试。只应在非生产主机上使用。生成的模板以自定义的 **vmlinuz-microvm** 内核启动，仅带最小化 init——许多工具（systemd、SSH 等）在安装到客户机内之前并不存在。已在 **Proxmox VE 9.1** 和 **QEMU 10.1** 上测试。

# HISTORY

由 **Rui Carmo**（rcarmo）编写，于 **2025 年**作为 **pve-microvm** 软件包的一部分首次发布在 GitHub 上。它与同一软件包中的其他工具互为补充：**pve-oci-import**、**pve-microvm-run**、**pve-microvm-share**、**pve-microvm-ssh-agent** 和 **pve-microvm-bench**。

# SEE ALSO

[qm](/man/qm)(1), [pvesh](/man/pvesh)(1), [qemu-system-x86_64](/man/qemu-system-x86_64)(1)
