# TAGLINE

从 VirtualBox 注册表中移除虚拟机

# TLDR

**按名称取消注册虚拟机**

```vboxmanage unregistervm [vmname]```

**按 UUID 取消注册虚拟机**

```vboxmanage unregistervm [uuid]```

**取消注册并删除所有关联的虚拟机文件**

```vboxmanage unregistervm [vmname] --delete```

**取消注册并删除所有文件，包括挂接的 DVD 和软盘镜像**

```vboxmanage unregistervm [vmname] --delete-all```

# SYNOPSIS

**vboxmanage** **unregistervm** _uuid_ | _vmname_ [**--delete** | **--delete-all**]

# PARAMETERS

**--delete**
> 删除所有虚拟机文件，包括硬盘镜像（未与其他虚拟机共享的）、机器 XML 定义文件和快照文件。

**--delete-all**
> 删除 --delete 所述的所有文件，以及位于虚拟机文件夹内且仅挂接到该虚拟机的全部 DVD 和软盘镜像。

# DESCRIPTION

**vboxmanage unregistervm** 将虚拟机从 VirtualBox 注册表中移除。可以通过名称或 UUID 标识虚拟机。不带 --delete 时只移除注册信息，虚拟机的所有文件仍保留在磁盘上。使用 --delete 或 --delete-all 时，关联文件将被永久删除。

# CAVEATS

--delete 和 --delete-all 选项会永久删除虚拟机文件且无法撤销。被其他虚拟机使用的共享磁盘镜像不会被删除。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [vboxmanage-registervm](/man/vboxmanage-registervm)(1), [vboxmanage-list](/man/vboxmanage-list)(1), [vboxmanage-showvminfo](/man/vboxmanage-showvminfo)(1)
