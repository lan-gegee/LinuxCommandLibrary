# TAGLINE

netExec NFS 模块

# TLDR

**枚举 NFS 共享**

```nxc nfs [target]```

**列出有访问权限的共享**

```nxc nfs [target] --shares```

**检查读取权限**

```nxc nfs [target] --enum-shares```

**扫描多个目标**

```nxc nfs [targets.txt]```

# SYNOPSIS

**nxc** **nfs** [_target_] [_options_]

# PARAMETERS

_TARGET_
> NFS 服务器地址。

**--shares**
> 枚举 NFS 导出。

**--enum-shares**
> 详细的共享枚举。

**-p** _PORT_
> NFS 端口（默认：2049）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nxc nfs** 是 NetExec 的 NFS 模块，用于枚举 NFS 服务器的导出。

该工具可识别可访问的共享，是 NetExec 套件的一部分。

# CAVEATS

安全工具。仅限授权使用。NetExec 的组成部分。

# HISTORY

nxc nfs 在 NetExec 框架内提供 **NFS 枚举**功能。

# SEE ALSO

[nxc](/man/nxc)(1), [showmount](/man/showmount)(1), [nfsstat](/man/nfsstat)(1)
