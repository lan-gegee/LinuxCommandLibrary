# TAGLINE

更新 Arch 二进制仓库数据库

# TLDR

将待发布的软件包更新推入**二进制仓库**（发布步骤）

```pkgctl db update```

# SYNOPSIS

**pkgctl db update** [_options_]

# DESCRIPTION

**pkgctl db update** 作为软件包发布流程的最后一步，更新已传输并暂存在 repos.archlinux.org 上的软件包的 pacman 数据库。此命令会触发仓库同步过程。

它通常在上传构建好的软件包之后使用，让用户能够通过官方 Arch Linux 仓库获取这些软件包。

# CAVEATS

需要正确的身份验证和维护者权限。只能在软件包妥善暂存并验证之后使用。

# HISTORY

属于 **pkgctl** 的一部分，后者是面向官方仓库维护者的 Arch Linux 软件包控制工具。它简化了软件包发布工作流。

# SEE ALSO

[pkgctl](/man/pkgctl)(1), [pkgctl-release](/man/pkgctl-release)(1), [pkgctl-auth](/man/pkgctl-auth)(1)
