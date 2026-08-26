# TAGLINE

管理 SELinux 端口类型标签

# TLDR

**列出**所有端口标签规则

```sudo semanage port -l```

不带标题地**列出**所有用户自定义的端口标签规则

```sudo semanage port -l -C -n```

**添加**一条为端口分配标签的用户自定义规则

```sudo semanage port -a -t [ssh_port_t] -p [tcp] [22000]```

为端口范围**添加**用户自定义规则

```sudo semanage port -a -t [http_port_t] -p [tcp] [80-88]```

按协议和端口**删除**用户自定义规则

```sudo semanage port -d -p [udp] [11940]```

# SYNOPSIS

**semanage port** [**-l**|**-a**|**-d**|**-m**] [_options_] _port_

# PARAMETERS

**-l, --list**
> 列出所有端口标签规则

**-a, --add**
> 添加新的端口规则

**-d, --delete**
> 删除端口规则

**-m, --modify**
> 修改现有的端口规则

**-t, --type _type_**
> 分配给端口的 SELinux 类型

**-p, --proto _protocol_**
> 协议（tcp 或 udp）

**-C, --locallist**
> 仅显示本地自定义的规则

**-n, --noheading**
> 输出中省略列标题

# DESCRIPTION

**semanage port** 管理 SELinux 端口类型定义。端口标签控制哪些受限域可以绑定或连接到特定的网络端口。

在非标准端口上运行服务时，必须添加端口规则，SELinux 才允许服务使用该端口。例如，让 SSH 运行在 22000 端口需要将该端口加入 **ssh_port_t**。

# CAVEATS

需要 root 权限。端口范围的书写格式为 **start-end**（例如 8080-8090）。更改立即生效。使用 **semanage port -l | grep** 可以查找服务已有的端口类型。

# SEE ALSO

[semanage](/man/semanage)(8), [ss](/man/ss)(8), [netstat](/man/netstat)(8)
