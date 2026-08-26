# TAGLINE

Gentoo Linux 软件包管理器

# TLDR

**同步**所有软件包

```sudo emerge --sync```

**更新**所有软件包及其依赖

```sudo emerge [-avuDN|--ask --verbose --update --deep --newuse] @world```

**继续**失败的更新，跳过出错的软件包

```sudo emerge --resume --skipfirst```

**安装**新软件包并确认

```sudo emerge [-av|--ask --verbose] [package]```

**移除**软件包及其依赖

```sudo emerge [-avc|--ask --verbose --depclean] [package]```

移除**孤立的**软件包

```sudo emerge [-avc|--ask --verbose --depclean]```

**搜索**软件包数据库

```emerge [-S|--searchdesc] [keyword]```

# SYNOPSIS

**emerge** [_options_] [_atoms_]

# DESCRIPTION

**emerge** 是 Gentoo Linux 的软件包管理器。它根据 USE 标志和系统配置从源码编译软件包，从而完成安装、更新和移除。

它管理软件的整个生命周期，包括依赖解析和 slot 冲突处理。

# PARAMETERS

**--sync**
> 同步软件包数据库

**-a, --ask**
> 执行前询问

**-v, --verbose**
> 详细输出

**-u, --update**
> 更新软件包

**-D, --deep**
> 考虑整棵依赖树

**-N, --newuse**
> 因 USE 标志变更而重新构建

**--depclean**
> 移除不再需要的软件包

**-S, --searchdesc**
> 搜索软件包描述

**--resume**
> 继续被中断的操作

**--skipfirst**
> 恢复时跳过第一个软件包

# CONFIGURATION

**/etc/portage/make.conf**
> 全局 Portage 配置，包括 USE 标志、编译器标志和系统设置。

**/etc/portage/package.use**
> 针对单个软件包的 USE 标志覆盖。

**/etc/portage/package.accept_keywords**
> 接受不稳定版本或特定版本的软件包。

# CAVEATS

Gentoo Linux 专属。从源码编译，可能非常耗时。需要正确配置 /etc/portage。更新前先运行 `emerge --sync` 或 `emaint sync`。

# SEE ALSO

[emaint](/man/emaint)(1), [equery](/man/equery)(1), [eix](/man/eix)(1), [portageq](/man/portageq)(1)
