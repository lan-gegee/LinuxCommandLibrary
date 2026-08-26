# TAGLINE

Arch Linux AUR 助手

# TLDR

从仓库和 AUR **更新**所有软件包

```yay```

按名称或关键词交互式**搜索并安装**

```yay [search_term]```

**安装**软件包且不弹出确认提示

```yay -S [package] --noconfirm```

在仓库和 AUR 中**搜索**关键词

```yay -Ss [keyword]```

**移除**软件包连同不再使用的依赖和配置

```yay -Rns [package]```

清理 yay 跟踪的**孤立软件包**

```yay -Yc```

清理 **pacman/yay 软件包缓存**

```yay -Scc```

打印软件包/系统**统计信息**

```yay -Ps```

# SYNOPSIS

**yay** \<operation\> [options] [targets]

# DESCRIPTION

Yay 是一个支持 AUR 的 Pacman 封装器。它在解析出要安装/升级的软件包后，将选项传递给 Makepkg 和 Pacman。

#  YAY OPERATIONS

**-Y, --yay**

> 执行 yay 特有的操作。未选择其他操作时这是默认行为。

**-P, --show**

> 执行 yay 特有的打印操作。

**-G, --getpkgbuild**

> 从 ABS 或 AUR 下载 PKGBUILD。ABS 只能用于 Arch Linux 官方仓库。

如果**不提供任何参数**，将执行 'yay -Syu'。

如果**未选择任何操作**，则默认为 -Y。

# EXTENDED PACMAN OPERATIONS

**-S, -Si, -Sl, -Ss, -Su, -Sc, -Qu**

> 这些操作被扩展为同时支持 AUR 与仓库软件包。

**-Sc**

> Yay 还会清理缓存的 AUR 软件包以及缓存中所有未被跟踪的文件。清理未跟踪文件会抹去已下载的源码或已构建的软件包，但会保留已经下载的 VCS 源码。

**-R**

> Yay 还会移除关于 devel 软件包的缓存数据。

# YAY OPTIONS (APPLY TO -Y AND --YAY)

**<NO OPTION>**

> 显示与搜索词匹配的软件包列表，并提示用户选择要安装的软件包（yogurt 模式）。

**--gendb**

> 生成开发软件包数据库。它会跟踪每个开发软件包的最新提交，当有新提交时 Yay 便知道需要更新。每次同步软件包时都会对该软件包执行此操作。此选项只应在从其他 AUR 助手迁移到 Yay 时使用。

**-c, --clean**

> 移除不需要的依赖。

# SHOW OPTIONS (APPLY TO -P AND --SHOW)

**-c, --complete**

> 打印所有 AUR 与仓库软件包的列表。这用于 Shell 补全，并非供用户直接使用。

**-f, --fish**

> 补全时针对 fish shell 调整输出格式。

**-d, --defaultconfig**

> 打印默认的 yay 配置。

**-g, --currentconfig**

> 打印当前的 yay 配置。

**-n, --numberupgrades**

> 已弃用，请改用 **yay -Qu** 加 **wc -l**。

**-s, --stats**

> 显示已安装软件包和系统健康状况的信息。如果存在孤立软件包、过期的软件包或 AUR 上已不存在的软件包，将会显示警告。

**-u, --upgrades**

> 已弃用，请改用 **yay -Qu**。

**-w, --news**

> 打印 Archlinux 主页上的新消息。只有比所有原生软件包的构建日期更新的消息才被视为新消息。传递两次该标志可显示全部可用消息。

**-q, --quiet**

> 打印消息时仅显示标题。

# PERMANENT CONFIGURATION SETTINGS

**--save**

> 将其后的选项保存回配置文件。这提供了一种无需直接编辑文件即可修改配置项的简便方法。

**--aururl**

> 设置替代的 AUR URL。这对希望使用 https://aur.tuna.tsinghua.edu.cn/ 的中国用户尤其有用。

**--builddir <dir>**

> 用于构建 AUR 软件包的目录。在决定 Yay 是否应跳过构建时，该目录也用作 AUR 缓存。

**--editor <command>**

> 编辑 PKGBUILD 时使用的编辑器。若未设置，将依次检查 **EDITOR** 环境变量和 **VISUAL** 环境变量。若都未设置，Yay 会提示用户指定编辑器。

**--editorflags <flags>**

> 传递给编辑器的参数。这些标志会被传给 Yay 调用编辑器的每一次。参数在传递给编辑器之前按空白字符拆分。可以通过提供由 shell 引号包裹的空格分隔列表来传入多个参数。

**--makepkg <command>**

> 用于 **makepkg** 调用的命令。可以是 **PATH** 中的命令，也可以是文件的绝对路径。

**--pacman <command>**

> 用于 **pacman** 调用的命令。可以是 **PATH** 中的命令，也可以是文件的绝对路径。

**--tar <command>**

> 用于 **bsdtar** 调用的命令。可以是 **PATH** 中的命令，也可以是文件的绝对路径。

**--git <command>**

> 用于 **git** 调用的命令。可以是 **PATH** 中的命令，也可以是文件的绝对路径。

**--gpg <command>**

> 用于 **gpg** 调用的命令。可以是 **PATH** 中的命令，也可以是文件的绝对路径。

**--config <file>**

> 要使用的 pacman 配置文件。

**--makepkgconf <file>**

> makepkg 要使用的配置文件。若未设置，则使用默认配置文件。

**--nomakepkgconf**

> 将 makepkg 配置文件重置为默认值。

**--requestsplitn <number>**

> 每次 AUR 查询请求的最大软件包数量。数值越大 AUR 请求越快。单次 AUR 查询请求过多软件包会导致错误。只有在非常大的查询（超过 500 个软件包）时才会有明显差异。

**--completioninterval <days>**

> 刷新补全缓存的间隔天数。设为 0 表示每次都刷新缓存，设为 -1 则永不刷新缓存。

**--sortby <votes|popularity|id|baseid|name|base|submitted|modified>**

> 搜索时按特定字段对 AUR 结果排序。

**--searchby <name|name-desc|maintainer|depends|checkdepends|makedepends|optdepends>**

> 通过查询指定字段来搜索 AUR 软件包。

**--answerclean <All|None|Installed|NotInstalled|...>**

> 为清理构建菜单的问题设置预定答案。该答案将代替从标准输入读取的内容，但解析方式完全相同。

**--answerdiff <All|None|Installed|NotInstalled|...>**

> 为编辑 diff 菜单的问题设置预定答案。该答案将代替从标准输入读取的内容，但解析方式完全相同。

**--answeredit <All|None|Installed|NotInstalled|...>**

> 为编辑 pkgbuild 菜单的问题设置预定答案。该答案将代替从标准输入读取的内容，但解析方式完全相同。

**--answerupgrade <Repo|^Repo|None|...>**

> 为升级菜单的问题设置预定答案。选择更新时要排除哪些软件包范围或仓库。该答案将代替从标准输入读取的内容，但处理方式完全相同。

**--noanswerclean**

> 取消为清理构建菜单设置的答案。

**--noanswerdiff**

> 取消为 diff 菜单设置的答案。

**--noansweredit**

> 取消为编辑 pkgbuild 菜单设置的答案。

**--noanswerupgrade**

> 取消为升级菜单设置的答案。

**--cleanmenu**

> 显示清理菜单。该菜单让你有机会在重新下载全新副本之前，彻底删除 Yay 缓存中已下载的构建文件。

**--diffmenu**

> 显示 diff 菜单。该菜单让你可以在构建前查看构建文件的 diff。

diff 通过 **git diff** 显示，默认使用 less。可以通过 git 的配置、**$GIT_PAGER** 或 **$PAGER** 环境变量改变这一行为。

**--editmenu**

> 显示编辑菜单。该菜单让你可以在构建前编辑或查看 PKGBUILD。

**Warning**: Yay 会提前通过 RPC 解析依赖。除非你清楚自己在做什么，否则不建议编辑 pkgbuild 变量。

**--upgrademenu**

> 以类似 VerbosePkgLists 的格式显示详细的更新列表。可以使用数字、数字范围或仓库名称跳过升级。此外可以用 ^ 反转选择。

**Warning**: 不建议跳过来自官方仓库的更新，因为这可能导致部分升级。此功能旨在方便地临时跳过可能损坏或编译时间很长的 AUR 更新。最终跳过哪些升级由用户自行决定。

**--nocleanmenu**

> 不显示清理菜单。

**--nodiffmenu**

> 不显示 diff 菜单。

**--noeditmenu**

> 不显示编辑菜单。

**--noupgrademenu**

> 不显示升级菜单。

**--askremovemake**

> 安装软件包后询问是否移除 makedepends。

**--removemake**

> 安装软件包后移除 makedepends。

**--noremovemake**

> 安装软件包后不移除 makedepends。

**--topdown**

> 先显示仓库软件包，再显示 AUR 软件包。

**--bottomup**

> 先显示 AUR 软件包，再显示仓库软件包。

**--singlelineresults**

> 覆盖 pacman 常规的双行搜索结果格式，将每个结果单独列在一行。

**--doublelineresults**

> 遵循 pacman 的双行搜索结果格式，用两行显示每个结果。

**--devel**

> 系统升级时同时检查 AUR 开发软件包是否有更新。目前仅支持 Git 软件包。

devel 检查通过 **git ls-remote** 完成。将最新的提交哈希与安装时的哈希进行比较。这使得 devel 更新几乎可以即时检查，并且无需重新下载原始 pkgbuild。

较慢的类 pacaur 式 devel 检查可以通过把软件包列表管道输入 yay 来手动实现（参见 **examples**）。

**--nodevel**

> 系统升级时不检查开发软件包的更新。

**--cleanafter**

> 安装后移除未跟踪的文件。

移除未跟踪文件时会保留目录。这样 VCS 软件包可以轻松拉取更新，而不必重新克隆整个仓库。

**--nocleanafter**

> 安装成功后不移除软件包源码。

**--timeupdate**

> 系统升级时，还会将已安装软件包的构建时间与其 AUR 页面的最后修改时间进行比较。

**--notimeupdate**

> 系统升级时不考虑构建时间。

**--redownload**

> 总是重新下载目标的 pkgbuild，即使缓存中已有副本。

**--redownloadall**

> 总是重新下载所有 AUR 软件包的 pkgbuild，即使缓存中已有副本。

**--noredownload**

> 下载 pkgbuild 时，如果缓存中的 pkgbuild 与 AUR 版本相同或更新，则使用缓存版本而不是重新下载。

**--provides**

> 搜索 AUR 软件包时查找匹配的提供者（provider）。找到多个提供者时会弹出菜单提示你选择其一。这会增加依赖解析时间，不过应该察觉不到。

**--noprovides**

> 搜索 AUR 软件包时不查找匹配的提供者。Yay 永远不会显示其提供者菜单，但对于仓库软件包，Pacman 仍会显示自己的提供者菜单。

**--pgpfetch**

> 提示从每个 PKGBUILD 的 **validpgpkeys** 字段导入未知的 PGP 密钥。

**--nopgpfetch**

> 不提示导入未知 PGP 密钥。这很可能导致构建失败，除非使用诸如 **--skippgpcheck** 之类的选项或自定义 gpg 配置。

**--useask**

> 使用 pacman 的 --ask 标志自动确认软件包冲突。Yay 会提前列出冲突。Yay 有可能未能检测到某个冲突，导致软件包在没有用户确认的情况下被移除。不过这种情况极不可能发生。

**--nouseask**

> 在安装过程中手动解决软件包冲突。不冲突的软件包无需手动处理。

**--combinedupgrade**

> 系统升级时，Yay 会先刷新数据库，然后显示即将升级的仓库与 AUR 软件包的合并菜单。查看 pkgbuild 后，仓库和 AUR 升级将直接开始，无需人工干预。

如果在刷新之后 Yay 因任何原因退出而未进行升级，则需要用户自行解决 Yay 退出的原因，或者直接通过 pacman 执行系统升级。

**--nocombinedupgrade**

> 系统升级时，先调用 Pacman -Syu，然后开始 AUR 升级。这意味着升级菜单和 pkgbuild 审查将在系统升级完成后进行。

**--batchinstall**

> 构建并安装 AUR 软件包时，不是每构建完一个就立即安装，而是将每个软件包加入安装队列。然后一旦所有软件包都构建完成，或构建队列中的某个软件包被另一个软件包作为依赖所需，就一次性安装队列中的所有软件包。

**--nobatchinstall**

> 构建 AUR 软件包后总是立即安装。

**--rebuild**

> 总是重建目标软件包，即使缓存中已有副本。

**--rebuildall**

> 总是重建所有 AUR 软件包，即使缓存中已有副本。

**--rebuildtree**

> 安装某个 AUR 软件包时，递归地重建并重装它的所有 AUR 依赖，包括已经安装过的。当这些依赖与当前系统的库变得不兼容时，此标志可以让你方便地对它们进行重建。

**--norebuild**

> 构建软件包时，如果缓存中的软件包与所需版本相同，则跳过构建并使用现有的软件包。

**--mflags <flags>**

> 传递给 makepkg 的参数。这些标志会被传给 Yay 调用 makepkg 的每一次。参数在传递给 makepkg 之前按空白字符拆分。可以通过提供由 shell 引号包裹的空格分隔列表来传入多个参数。

**--gpgflags <flags>**

> 传递给 gpg 的参数。这些标志会被传给 Yay 调用 gpg 的每一次。参数在传递给 gpg 之前按空白字符拆分。可以通过提供由 shell 引号包裹的空格分隔列表来传入多个参数。

**--sudo <command>**

> 用于 **sudo** 调用的命令。可以是 **PATH** 中的命令，也可以是文件的绝对路径。自定义 **sudo** 命令不保证能与 sudoloop 一起工作。

**--sudoflags <flags>**

> 传递给 sudo 的参数。这些标志会被传给 Yay 调用 sudo 的每一次。参数在传递给 sudo 之前按空白字符拆分。可以通过提供由 shell 引号包裹的空格分隔列表来传入多个参数。

**--sudoloop**

> 在后台循环调用 sudo，防止长时间构建期间 sudo 超时。

**--nosudoloop**

> 不在后台循环调用 sudo。

# CAVEAT

与其他 AUR 助手一样，yay 便于安装来自 Arch User Repository 的**用户提交软件包**，这些软件包**未经官方审核**，可能包含恶意代码——安装前务必审查 PKGBUILD 文件以降低安全风险。

# HISTORY

yay 命令是 "**Yet Another Yogurt**" 的缩写，是一款用 **Go** 编写的 AUR（Arch User Repository）助手工具，旨在简化 **Arch Linux** 及其衍生发行版上软件包的安装与管理。它由开发者 Jguer 创建，始于 **2016 年 9 月**。

# INSTALL

```nix: nix profile install nixpkgs#yay```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[makepkg](/man/makepkg)(8), [pacman](/man/pacman)(8)

# RESOURCES

```[Source code](https://github.com/Jguer/yay)```

```[Documentation](https://github.com/Jguer/yay/wiki)```

<!-- verified: 2026-06-09 -->
