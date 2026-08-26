# TAGLINE

Clear Linux 的软件更新与 bundle 管理器

# TLDR

**更新**到最新版本

```sudo swupd update```

检查**可用更新**

```swupd check-update```

**列出**已安装的 bundle

```swupd bundle-list```

**搜索**软件包

```swupd search -b [package]```

**安装**一个 bundle

```sudo swupd bundle-add [bundle]```

**移除**一个 bundle

```sudo swupd bundle-remove [bundle]```

**校验**并修复系统文件

```sudo swupd verify```

显示**系统信息**

```swupd info```

# SYNOPSIS

**swupd** _command_ [_OPTIONS_]

# COMMANDS

**update** [_version_]
> 更新到最新或指定版本

**check-update**
> 检查可用更新

**bundle-list** [**--all**]
> 列出已安装（或全部可用）的 bundle

**bundle-add** _bundle_
> 安装一个 bundle

**bundle-remove** _bundle_
> 移除一个 bundle

**search** _term_
> 查找包含搜索词的 bundle

**info**
> 显示版本和更新服务器信息

**diagnose**
> 对照清单校验系统文件

**repair**
> 修复检测到的文件不一致

**autoupdate**
> 启用/禁用自动更新

**clean**
> 清除缓存的文件

# PARAMETERS

**-b**
> 搜索 bundle（与 search 配合）

**--all**
> 显示所有可用 bundle（与 bundle-list 配合）

**--force**
> 强制执行操作

**--no-scripts**
> 跳过更新后脚本

**-h, --help**
> 显示帮助

# DESCRIPTION

**swupd** 是 Clear Linux 的软件更新和 bundle 管理工具。与传统软件包管理器不同，swupd 管理 bundle（相关软件包的集合），并采用类似 git 的文件级版本控制，每个 OS 版本代表一个完整、一致的快照。

更新效率极高，只通过二进制差量下载发生变化的文件。该工具可以校验系统完整性、修复损坏的文件，并管理自动更新。

# CAVEATS

需要连接更新服务器的网络。bundle 包含全部依赖，无法单独安装某个软件包。OS 版本号不遵循语义化版本，每个版本号代表一个完整的系统状态。部分 bundle 体积较大。

# HISTORY

**swupd** 由 **Intel** 为 **Clear Linux** 开发。Clear Linux 是一个针对性能优化的 Linux 发行版，于 **2015 年**首次发布，率先倡导无状态计算和高效更新机制。swupd 工具以原子更新和文件级校验体现了 Clear Linux 的软件管理理念。

# SEE ALSO

[flatpak](/man/flatpak)(1), [dnf](/man/dnf)(8), [apt](/man/apt)(8)
