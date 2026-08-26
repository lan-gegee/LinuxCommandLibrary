# TAGLINE

管理 OpenDNSSEC 各组件

# TLDR

**启动 ODS 服务**

```ods-control start```

**停止 ODS 服务**

```ods-control stop```

**检查状态**

```ods-control status```

**重新加载配置**

```ods-control reload```

**仅启动 enforcer**

```ods-control enforcer start```

# SYNOPSIS

**ods-control** [_component_] _command_

# PARAMETERS

**start**
> 启动服务。

**stop**
> 停止服务。

**status**
> 显示状态。

**reload**
> 重新加载配置。

**enforcer**
> 仅控制 enforcer。

**signer**
> 仅控制 signer。

# DESCRIPTION

**ods-control** 管理 OpenDNSSEC 的各组件。OpenDNSSEC 用于自动化 DNSSEC 密钥管理和区域签名。

该工具控制 enforcer（密钥管理）和 signer（区域签名）两个守护进程。

# COMPONENTS

```
enforcer - Key management daemon
signer   - Zone signing daemon
```

# TYPICAL WORKFLOW

```bash
# Start OpenDNSSEC
ods-control start

# Check status
ods-control status

# After config change
ods-control reload
```

# CAVEATS

需要已配置的 KASP。数据库必须先初始化。通常需要 root 权限。

# HISTORY

OpenDNSSEC 的开发目的是简化 DNSSEC 部署，提供自动化的密钥轮换和区域签名。

# SEE ALSO

[ods-enforcer](/man/ods-enforcer)(8)
