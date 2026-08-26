# TAGLINE

OpenStack 云服务的统一 CLI

# TLDR

**列出服务器**

```openstack server list```

**创建服务器**

```openstack server create --flavor [m1.small] --image [ubuntu] --network [net] [name]```

**列出镜像**

```openstack image list```

**列出规格**

```openstack flavor list```

**查看服务器详情**

```openstack server show [server_name]```

**删除服务器**

```openstack server delete [server_name]```

# SYNOPSIS

**openstack** [_options_] _command_ [_args_]

# PARAMETERS

**server**
> 计算实例相关命令。

**image**
> 镜像相关命令。

**network**
> 网络相关命令。

**volume**
> 块存储相关命令。

**flavor**
> 规格相关命令。

**--os-cloud** _name_
> 使用指定的云配置。

**-f** _format_
> 输出格式。

# DESCRIPTION

**openstack** 是 OpenStack 云服务的统一 CLI。它提供单一接口来管理计算、存储、网络和身份服务。

配置通常位于 clouds.yaml 或环境变量中。

# CONFIGURATION

```yaml
# ~/.config/openstack/clouds.yaml
clouds:
  mycloud:
    auth:
      auth_url: https://cloud.example.com:5000
      username: user
      password: pass
      project_name: myproject
```

# COMMON COMMANDS

```bash
openstack server list
openstack image list
openstack network list
openstack volume list
openstack flavor list
```

# CAVEATS

需要 OpenStack 凭据。API 版本因部署而异。大规模操作可能超时。

# HISTORY

统一的 OpenStack 客户端旨在取代各服务专用的 CLI（nova、neutron、cinder），从而在各服务之间提供一致的界面。

# SEE ALSO

[nova](/man/nova)(1), [neutron](/man/neutron)(1), [glance](/man/glance)(1)
