# TAGLINE

修改 Proxmox LXC 容器的配置

# TLDR

启用开机**自启**

```pct set 100 --onboot```

设置**静态 IP**

```pct set 100 --net0 name=eth0,bridge=vmbr0,ip=10.0.0.100/24,gw=10.0.0.1```

设置 **memory** 和 CPU 限制

```pct set 100 --memory 8192 --cpulimit 4```

**挂载**宿主目录

```pct set 100 --mp0 /host/path,mp=/guest/mount```

设置 **tags**

```pct set 100 --tags tag1,tag2```

**删除**选项

```pct set 100 --delete net0,mp0```

# SYNOPSIS

**pct set** _vmid_ [_OPTIONS_]

# DESCRIPTION

**pct set** 修改 Proxmox LXC 容器的配置。某些更改可能需要重启容器才能生效。该命令可配置网络、资源、挂载点及其他容器属性。

# PARAMETERS

**vmid**
> 容器的数字 ID

**--onboot** _boolean_
> 主机启动时启动容器

**--memory** _megabytes_
> 内存限制（单位为 MB）

**--cpulimit** _number_
> CPU 时间限制（例如 4 表示相当于 4 个核心）

**--net**_N_ _config_
> 网络接口配置

**--mp**_N_ _config_
> 绑定挂载的挂载点配置

**--tags** _list_
> 以逗号分隔的标签列表

**--delete** _list_
> 移除指定的选项

# CAVEATS

某些更改需要先停止容器。网络更改可能导致运行中的会话断开。挂载点必须存在于宿主系统上。

# HISTORY

**pct set** 是用于管理 LXC 容器的 **Proxmox VE** 虚拟化平台的一部分。

# SEE ALSO

[pct](/man/pct)(1), [pct-config](/man/pct-config)(1)
