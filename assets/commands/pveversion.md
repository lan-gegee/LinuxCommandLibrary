# TAGLINE

显示 Proxmox 系统版本信息

# TLDR

输出**系统版本**

```pveversion```

输出 Proxmox **子软件包版本**

```pveversion -v```

# SYNOPSIS

**pveversion** [_options_]

# PARAMETERS

**-v**, **--verbose**
> 显示所有 Proxmox 相关软件包的版本

# DESCRIPTION

**pveversion** 显示 Proxmox VE 安装的版本信息。不带选项时，它显示主要的 Proxmox VE 版本。使用 **--verbose** 时，它会列出所有 Proxmox 子软件包的版本，包括 pve-manager、pve-kernel、qemu-server 等。

这对支持请求、验证更新状态以及检查组件兼容性非常有用。

# SEE ALSO

[pvesh](/man/pvesh)(1), [pveam](/man/pveam)(1), [pvecm](/man/pvecm)(1)
