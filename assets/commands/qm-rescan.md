# TAGLINE

重新扫描 Proxmox 虚拟机的存储卷

# TLDR

**重新扫描所有存储**并更新所有虚拟机的磁盘大小

```qm rescan```

**针对特定虚拟机重新扫描存储**

```qm rescan --vmid [100]```

**执行试运行**而不写入更改

```qm rescan --dryrun 1```

此命令是 **qm disk rescan** 的别名

查看原始命令的文档

```tldr qm disk```

# SYNOPSIS

**qm rescan** [_options_]

# PARAMETERS

**--dryrun** _boolean_
> 执行测试运行，不向虚拟机配置写入更改（默认：**0**）。

**--vmid** _integer_
> 虚拟机的唯一 ID（100-999999999）。省略时对所有虚拟机进行重新扫描。

# DESCRIPTION

**qm rescan** 是 **qm disk rescan** 的别名，用于重新扫描所有存储，并更新虚拟机的磁盘大小和未使用的磁盘镜像。不带 **--vmid** 运行时，会对节点上所有虚拟机的存储进行重新扫描。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-disk](/man/qm-disk)(1), [pvesm](/man/pvesm)(1)
