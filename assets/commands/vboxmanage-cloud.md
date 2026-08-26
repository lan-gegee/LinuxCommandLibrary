# TAGLINE

从 VirtualBox 管理云实例

# TLDR

**列出云实例**

```vboxmanage cloud --provider=[provider] --profile=[profile] instance list```

**创建云实例**

```vboxmanage cloud --provider=[provider] --profile=[profile] instance create```

**终止云实例**

```vboxmanage cloud --provider=[provider] --profile=[profile] instance terminate --id=[id]```

# SYNOPSIS

**vboxmanage** **cloud** **--provider**=_provider_ **--profile**=_profile_ _command_

# PARAMETERS

**--provider** _name_
> 云服务提供商（例如 OCI）。

**--profile** _name_
> 云配置文件名。

**instance** _cmd_
> 实例操作。

**image** _cmd_
> 镜像操作。

**network** _cmd_
> 网络操作。

# DESCRIPTION

**vboxmanage cloud** 用于在 VirtualBox 中管理云实例。它与 Oracle Cloud Infrastructure（OCI）集成，可在管理本地虚拟机的同时管理云虚拟机。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1)
