# TAGLINE

面向本地安装的 AppImage 与便携应用管理器

# TLDR

**按名称搜索并安装**软件包

```appman -i [package_name]```

**更新所有**已安装的应用程序

```appman -u```

**移除**已安装的应用程序

```appman -r [package_name]```

**按关键字搜索**可用软件包

```appman -q [keyword]```

**列出所有已安装的**应用程序

```appman -f```

**查看**已安装应用程序的信息

```appman -a [package_name]```

# SYNOPSIS

**appman** [_option_] [_package_name_]

# PARAMETERS

**-i**, **install** _package_
> 在用户主目录中本地安装一个或多个应用程序

**-ia**, **install-appimage** _package_
> 专门安装 AppImage 软件包

**-r**, **remove** _package_
> 移除一个或多个已安装的应用程序

**-u**, **update**
> 更新所有已安装的应用程序以及 AppMan 本身。使用 **--apps** 可仅更新程序

**-l**, **list**
> 列出数据库中所有可用的应用程序

**-q**, **query** _keyword_
> 按关键字搜索可用的应用程序

**-f**, **files**
> 显示所有本地已安装的应用程序

**-a**, **about** _package_
> 查看某个应用程序的描述与来源信息

**-d**, **download** _package_
> 下载并阅读安装脚本，但不进行安装

**-b**, **backup** _package_
> 为已安装的应用程序创建快照以便回滚

**-o**, **overwrite** _package_
> 用全新的副本覆盖现有安装

**-e**, **extra** _url_
> 从外部 GitHub 仓库安装应用程序

**-c**, **clean**
> 删除临时文件和缓存文件

**-s**, **sync**
> 更新 AppMan 的模块和核心脚本

**--rollback** _package_
> 将应用程序恢复到先前的版本

**--sandbox** _package_
> 通过 Aisap 为 AppImage 启用 Bubblewrap 沙箱

**--disable-sandbox** _package_
> 移除 AppImage 的沙箱隔离

**--launcher** _package_
> 将应用程序集成到桌面菜单和启动器中

**--relocate**
> 更改应用的本地安装目录

**-h**, **help**
> 显示所有可用选项

**-v**, **version**
> 输出版本信息

# DESCRIPTION

**appman** 是一个无 root 权限、可移植的软件包管理器，用于管理 AppImage 和其他便携 Linux 应用。它是 **AM Application Manager** 的一个再发行版本，不需要 root 权限，而是在用户主目录内本地安装和管理所有应用程序。

AppMan 从 AM 数据库下载安装脚本并将其转换为本地使用。应用程序存储在用户指定的目录（例如 **~/Applications**）中，可执行文件的链接放在 **~/.local/bin/**，桌面条目放在 **~/.local/share/applications/**。该数据库收录了超过 2500 个 AppImage 和便携程序。

AppMan 支持与 AM 相同的命令——只需将 **am** 替换为 **appman** 即可。它可以处理安装、更新、移除、沙箱隔离、回滚和桌面集成，全程无需 sudo 权限。

# CAVEATS

AppMan 依赖社区维护数据库中的安装脚本。这些脚本从第三方来源下载二进制文件，且没有经过中央机构的审计——安装前务必用 **-d** 审阅脚本。通过 Aisap 进行沙箱隔离需要系统上装有 Bubblewrap。如果上游更改了发布格式或下载 URL，某些应用程序可能无法正常更新。

# HISTORY

AppMan 由 **ivan-hc** 创建，作为 **AM Application Manager** 的配套工具，大约于 **2022** 年首次出现在 GitHub 上。AM 本身的灵感来自 Arch Linux 的 AUR 模式，目标是在所有 GNU/Linux 发行版上为 AppImage 和便携应用带来类似的社区驱动软件包管理体验。AppMan 的推出是为了在不要求 root 权限的情况下提供相同的功能，使其适用于受限环境和多用户系统。

# SEE ALSO

[flatpak](/man/flatpak)(1), [snap](/man/snap)(1), [wget](/man/wget)(1)
