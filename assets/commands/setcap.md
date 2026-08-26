# TAGLINE

为文件设置能力以实现细粒度特权

# TLDR

设置**能力**

```setcap 'cap_net_raw' path/to/file```

设置**多个**能力

```setcap 'cap_dac_read_search,cap_sys_tty_config+ep' path/to/file```

**移除**所有能力

```setcap -r path/to/file```

**校验**能力

```setcap -v 'cap_net_raw' path/to/file```

为**命名空间**设置

```setcap -n root_uid 'cap_net_admin' path/to/file```

# SYNOPSIS

**setcap** [_OPTIONS_] _capabilities_ _file_

# DESCRIPTION

**setcap** 为文件设置能力，使进程无需完整 root 权限即可获得特定的提升特权。这提供了细粒度的安全控制，可作为 setuid 可执行文件的替代方案。

# PARAMETERS

**-r**
> 移除文件的所有能力

**-v**
> 校验指定的能力是否与文件匹配

**-n** _rootuid_
> 为特定用户命名空间设置能力

**+e**
> 有效标志——能力处于激活状态

**+p**
> 允许标志——能力可被使用

**+i**
> 可继承标志——传递给子进程

# CAVEATS

修改能力需要 root 权限。文件被修改后其能力会被清除。常见能力包括 cap_net_raw（原始套接字）、cap_net_admin（网络管理）和 cap_sys_admin（各类系统管理任务）。

# HISTORY

**setcap** 是 **libcap** 的一部分，在 Linux 上实现 POSIX 1003.1e 能力机制。

# INSTALL

```apt: sudo apt install libcap2-bin```

```apk: sudo apk add libcap-setcap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[getcap](/man/getcap)(8), [capabilities](/man/capabilities)(7)
