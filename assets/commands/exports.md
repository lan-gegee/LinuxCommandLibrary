# TAGLINE

NFS 共享目录配置与管理

# TLDR

**查看当前导出项**

```exportfs -v```

**重载导出配置**

```sudo exportfs -ra```

**临时导出目录**

```sudo exportfs -o [rw,sync] [client:/path]```

**取消导出目录**

```sudo exportfs -u [client:/path]```

# SYNOPSIS

**/etc/exports** - NFS 导出配置文件

**exportfs** [_options_] [_client:/path_]

# PARAMETERS

**exportfs -r**
> 重新导出所有目录。

**exportfs -a**
> 导出 /etc/exports 中的所有条目。

**exportfs -u** _client:/path_
> 取消导出目录。

**exportfs -v**
> 详细输出；显示当前导出项。

# EXPORTS FILE FORMAT

```
/path      client(options)
/home      192.168.1.0/24(rw,sync)
/data      *(ro,async)
/shared    @group(rw,no_root_squash)
```

# OPTIONS

**rw** / **ro**
> 读写或只读访问。

**sync** / **async**
> 同步或异步写入。

**no_root_squash**
> 不将 root 映射为匿名用户。

**root_squash**
> 将 root 映射为匿名用户（默认）。

**all_squash**
> 将所有用户映射为匿名用户。

**subtree_check** / **no_subtree_check**
> 子树检查。

**secure** / **insecure**
> 要求端口小于 1024。

# DESCRIPTION

**/etc/exports** 定义哪些目录通过 NFS（网络文件系统）共享。每一行指定一个路径，以及哪些客户端可以用什么选项访问它。

**exportfs** 命令在运行时管理导出表，从 /etc/exports 读取配置并更新内核的导出表，无需重启 NFS 服务。

# CAVEATS

修改 /etc/exports 后需要执行 `exportfs -ra` 才能生效。默认安全性依赖基于 IP 的访问控制。如需经过身份验证的 NFS，可考虑 Kerberos。客户端与服务器之间的权限映射也需要考虑。

# SEE ALSO

[nfsd](/man/nfsd)(8)
