# TAGLINE

管理 pkgctl 服务身份验证

# TLDR

登录 Arch GitLab 以执行 **pkgctl** 操作

```pkgctl auth login```

显示**凭据**是否已配置

```pkgctl auth status```

# SYNOPSIS

**pkgctl auth** _command_

# PARAMETERS

**login**
> 向 GitLab 实例进行身份验证

**status**
> 显示当前的身份验证状态

# DESCRIPTION

**pkgctl auth** 管理 pkgctl 与 GitLab 等服务之间的身份验证。它处理软件仓库操作和源码控制集成所需的登录凭据。

与 Arch Linux 基础设施交互的操作（如发布软件包和管理仓库访问权限）需要进行身份验证。

# CAVEATS

凭据存储在本地。请确保凭据文件的权限设置正确，以防止未经授权的访问。

# HISTORY

属于 **pkgctl** 的一部分，后者是面向官方仓库维护者的 Arch Linux 软件包控制工具。

# SEE ALSO

[pkgctl](/man/pkgctl)(1), [pkgctl-release](/man/pkgctl-release)(1)
