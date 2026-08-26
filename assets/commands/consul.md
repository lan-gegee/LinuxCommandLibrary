# TAGLINE

服务发现与配置工具

# TLDR

**以开发模式启动代理**

```consul agent -dev```

**列出数据中心成员**

```consul members```

**注册服务**

```consul services register [service.json]```

**注销服务**

```consul services deregister -id=[service-id]```

**列出服务目录中的服务**

```consul catalog services```

**通过 DNS 查询服务**

```dig @127.0.0.1 -p 8600 [web.service.consul]```

**存储键值对**

```consul kv put [key] [value]```

**读取键值**

```consul kv get [key]```

**加入集群**

```consul join [192.168.1.100]```

**校验配置文件**

```consul validate [/etc/consul.d/]```

**重新加载代理配置**

```consul reload```

# SYNOPSIS

**consul** [_options_] _command_ [_arguments_]

# DESCRIPTION

**consul** 是 HashiCorp 出品的服务发现与配置工具。它提供服务网格、健康检查、键值存储、多数据中心支持以及安全的服务间通信。

# COMMANDS

**agent**
> 运行 Consul 代理

**members**
> 列出集群成员

**join**
> 通过代理地址加入集群

**leave**
> 优雅地退出集群

**catalog**
> 与服务目录交互

**services**
> 注册/注销服务

**kv**
> 键值存储操作

**connect**
> 服务网格功能

**acl**
> 访问控制列表管理

**watch**
> 监视数据视图的变化并调用进程

**event**
> 触发自定义用户事件

**exec**
> 在集群节点上远程执行

**operator**
> 集群级运维工具

**snapshot**
> 保存/恢复集群状态

**reload**
> 重新加载代理配置文件

**validate**
> 校验配置文件

**monitor**
> 流式输出运行中代理的日志

**debug**
> 创建调试归档

# PARAMETERS

**-dev**
> 开发模式（单节点，无持久化）

**-server**
> 以服务器模式运行代理

**-bind** _addr_
> 内部集群通信的地址（默认：0.0.0.0）

**-token** _token_
> 用于认证的 ACL 令牌

**-token-file** _file_
> 包含 ACL 令牌的文件

**-datacenter** _dc_
> 目标数据中心

**-http-addr** _addr_
> Consul HTTP API 地址

**-auto-reload-config**
> 文件变化时自动重新加载配置

# CONFIGURATION

**/etc/consul.d/**
> Consul 代理设置、服务和检查项的配置目录，支持 HCL 或 JSON 格式。

# ENVIRONMENT

**CONSUL_HTTP_ADDR**
> HTTP API 地址

**CONSUL_HTTP_TOKEN**
> ACL 令牌

**CONSUL_CACERT**
> CA 证书路径

**CONSUL_HTTP_SSL**
> 与 Consul 通信时使用 HTTPS

# DNS INTERFACE

默认 DNS 端口：8600

```dig @127.0.0.1 -p 8600 web.service.consul```

# CAVEATS

启用 ACL 系统后，大多数操作都需要令牌。开发模式将所有内容保存在内存中。生产环境需要正确的集群配置。

# INSTALL

```pacman: sudo pacman -S consul```

```nix: nix profile install nixpkgs#consul```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vault](/man/vault)(1), [nomad](/man/nomad)(1), [terraform](/man/terraform)(1)
