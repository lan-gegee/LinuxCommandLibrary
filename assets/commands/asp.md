# TAGLINE

获取 Arch Linux 软件包的构建文件

# TLDR

**从 Arch 软件仓库克隆一个软件包**

```asp checkout [package]```

**更新所有已检出的软件包**

```asp update```

**无需完整检出即可导出 PKGBUILD 文件**

```asp export [package]```

**列出包含某软件包的仓库**

```asp list-repos [package]```

**显示**某软件包的 PKGBUILD 内容

```asp show [package]```

**查看**某软件包的**修订历史**

```asp log [package]```

**列出所有本地跟踪的**软件包

```asp list-local```

# SYNOPSIS

**asp** _command_ [_options_] [_packages_]

# PARAMETERS

**checkout** _package_
> 为给定软件包创建一个包含完整源码和历史的 git 仓库。

**export** _package_
> 将构建源文件导出到当前目录下以该软件包命名的目录中。

**update** [_packages_]
> 跟踪新的软件包，或从远程刷新已有软件包。

**show** _package_ [_file_]
> 显示 PKGBUILD 内容；若给定具体文件则显示该文件。

**log** _package_
> 显示软件包的修订历史。

**difflog** _package_
> 显示带文件差异的修订历史。

**shortlog** _package_
> 显示精简的修订历史。

**list-repos** _package_
> 列出包含给定软件包的仓库。

**list-arches** _package_
> 列出给定软件包可用的架构。

**list-all**
> 列出所有可用软件包。

**list-local**
> 列出所有本地跟踪的软件包。

**ls-files** _package_
> 列出给定软件包的源文件。

**untrack** _package_
> 从本地仓库移除远程跟踪分支。

**disk-usage**
> 报告本地跟踪软件包的大致磁盘占用。

**gc**
> 执行清理维护，优化并压缩本地仓库。

**set-git-protocol** _protocol_
> 设置通信协议（git、http 或 https）。

**-a** _arch_
> 使用非默认架构。

**-h**
> 显示帮助文本。

**-V**
> 显示版本信息。

# DESCRIPTION

**asp**（Arch Build Source Management Tool）管理用于构建 Arch Linux 软件包的构建脚本的版本控制源码。它是对 svntogit 仓库的一层轻封装，用来替代较旧的 **abs** 工具。

与手动下载 PKGBUILD 不同，asp 使用基于 Git 并配合稀疏检出的后端，可以高效地跟踪变更、查看提交历史以及更新单个软件包。

常见用途包括：研究官方软件包的构建方式、以自定义选项修改软件包、向后移植补丁，以及从官方示例学习 PKGBUILD 的最佳实践。

# CAVEATS

asp 只提供官方 Arch 仓库中的构建文件，不提供 AUR 的。检出的文件需要用 **makepkg** 才能真正构建软件包。底层 VCS 操作需要安装 Git。软件包元数据存储在 **$ASPROOT** 中（默认为 **$XDG_CACHE_HOME/asp** 或 **~/.cache/asp**）。

# HISTORY

**asp** 工具的诞生是为了取代较旧的 **abs**（Arch Build System）工具，后者会下载所有 PKGBUILD 的完整副本。asp 于 **2015** 年前后推出，利用 Git 提供更高效的单包增量访问。随着 Arch 软件包仓库转向基于 Git 的工作流，asp 成为获取官方 PKGBUILD 的推荐方法。

# INSTALL

```aur: yay -S asp```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[makepkg](/man/makepkg)(8), [pacman](/man/pacman)(8), [yay](/man/yay)(1), [paru](/man/paru)(1), [pkgctl](/man/pkgctl)(1), [git](/man/git)(1)
