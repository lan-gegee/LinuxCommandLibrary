# TAGLINE

简化 Hyperledger Fabric 网络部署

# TLDR

**初始化 Hyperledger Fabric 网络**

```minifab up```

**关闭网络**

```minifab down```

**安装链码**

```minifab install -n [chaincode_name]```

**调用链码**

```minifab invoke -n [chaincode_name] -p '"[function]","[arg1]","[arg2]"'```

# SYNOPSIS

**minifab** _command_ [_options_]

# PARAMETERS

**up**
> 启动 Fabric 网络。

**down**
> 停止并移除网络。

**install**
> 安装链码。

**invoke**
> 调用链码函数。

**query**
> 查询链码。

**-n** _name_
> 链码名称。

**-p** _params_
> 函数参数。

**-c** _channel_
> 通道名称。

# DESCRIPTION

**minifab** 简化 Hyperledger Fabric 网络部署。以最少的配置创建开发网络。自动管理链码生命周期。

# SEE ALSO

[docker](/man/docker)(1)
