# TAGLINE

受 AUR 启发、面向 Ubuntu 及基于 Debian 发行版的软件包管理器

# TLDR

**搜索**软件包

```pacstall -S [query]```

**安装**软件包

```pacstall -I [package]```

**移除**软件包

```pacstall -R [package]```

**添加**仓库

```pacstall -A [repository_url]```

**更新** pacstall 的脚本

```pacstall -U```

**升级**所有已安装的软件包

```pacstall -Up```

显示已安装软件包的**信息**

```pacstall -Ci [package]```

**列出**所有已安装的软件包

```pacstall -L```

无提示地安装软件包并保留构建文件

```pacstall -P -K -I [package]```

# SYNOPSIS

**pacstall** [_command_] [_options_] [_package_...]

# PARAMETERS

**-I**, **--install** _package_
> 从仓库或 pacscript 安装软件包。

**-R**, **--remove** _package_
> 从系统中移除软件包。

**-S**, **--search** _query_
> 在所有可用仓库中搜索软件包。

**-Sd**, **--search-description** _query_
> 搜索软件包名称和描述。

**-Si**, **--search-info** _package_
> 显示远程软件包的元数据（SRCINFO）。

**-Ci**, **--cache-info** _package_
> 显示已安装软件包的元数据。

**-A**, **--add-repo** _url_
> 向 pacstall 添加一个仓库。

**-Rr**, **--remove-repo** _repo_
> 从 pacstall 移除一个仓库。

**-U**, **--update**
> 更新 pacstall 和所需的脚本。

**-Up**, **--upgrade**
> 升级有新版本的软件包。

**-L**, **--list**
> 列出已安装的软件包。

**-T**, **--tree** _package_
> 以树状图显示软件包的依赖。

**-D**, **--download** _package_
> 将 pacscript 下载到当前目录。

**-Qa**, **--quality-assurance** _package#number_
> 在合并前测试来自 pull request 的软件包。

**-V**, **--version**
> 显示版本信息。

**-P**, **--disable-prompts**
> 禁用交互提示并接受所有默认值。

**-K**, **--keep**
> 安装后保留构建文件。

**-B**, **--build-only**
> 只构建 deb 包而不安装。

**-Q**, **--quiet**
> 静默下载软件包条目。

**-Nc**, **--nocheck**
> 若 pacscript 中存在 check() 函数则跳过它。

**-Ns**, **--nosandbox**
> 不使用 bwrap 沙箱构建软件包。

# DESCRIPTION

**pacstall** 是面向 Ubuntu 及基于 Debian 发行版的软件包管理器，它通过允许用户从社区维护的构建脚本（称为 pacscript，类似于 Arch 的 PKGBUILD）安装软件包，带来了类似 AUR 的功能。

该工具维护自己的构建脚本仓库，独立于系统的 apt 仓库。用户可以添加托管在 GitHub 或 GitLab 上的自定义仓库，从而在官方渠道之外实现社区驱动的软件包分发。

# CAVEATS

软件包从源码构建，可能比较耗时。需要预先安装构建依赖。未经 Ubuntu/Debian 官方支持；软件包可能与系统软件包冲突。安装前务必审查 pacscript。

# HISTORY

该项目旨在将 AUR（Arch 用户仓库）体验带给 Ubuntu 用户。它是 PPA 和 Snap 的替代方案，面向偏好使用社区维护脚本从源码构建软件包的用户。项目致力于提供一种简单方式来安装官方仓库中没有的软件。

# SEE ALSO

[apt](/man/apt)(8), [dpkg](/man/dpkg)(1), [yay](/man/yay)(8), [makepkg](/man/makepkg)(8), [nala](/man/nala)(8)
