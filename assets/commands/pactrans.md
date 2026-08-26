# TAGLINE

使用 ALPM 事务安装、移除和升级软件包

# TLDR

**从仓库安装**软件包

```sudo pactrans --install [package]```

**移除**软件包

```sudo pactrans --remove [package]```

**升级**所有已安装的软件包

```sudo pactrans --sysupgrade```

安装一个**软件包文件**

```sudo pactrans --file [path/to/package.pkg.tar.zst]```

在单个事务中**同时安装和移除**软件包

```sudo pactrans --install [new_package] --remove [old_package]```

**打印**将要执行的操作而不实际执行

```pactrans --print-only --install [package]```

**从指定仓库安装**

```sudo pactrans [repo]/[package]```

# SYNOPSIS

**pactrans** [_options_] [_target_...]

# PARAMETERS

**--install**
> 将后续目标视为要从仓库安装的软件包。

**--remove**
> 将后续目标视为要移除的软件包。

**--sysupgrade**
> 将所有已安装的软件包升级到最新的可用版本。

**--file**
> 将后续目标视为要安装的本地软件包文件。

**--spec**
> 将后续目标视为 pkgspec：若是文件或仓库软件包则安装，若是本地数据库条目则移除。

**--print-only**
> 显示事务将要执行的操作后退出，不做任何更改。

**--no-confirm**
> 不提示确认。

**--no-deps**
> 忽略依赖检查。

**--dbonly**
> 只修改数据库，不提取或移除文件。

**--config** _file_
> 使用替代的 pacman 配置文件。

**--dbpath** _path_
> 使用替代的数据库路径。

**--sysroot** _path_
> 设置替代的系统根目录。

# DESCRIPTION

**pactrans** 使用 ALPM（Arch Linux 软件包管理）库处理软件包的安装、移除和系统升级。它为常见软件包操作提供统一接口，并支持混合事务。

该工具可以在单个事务中同时安装和移除软件包。软件包规格可以包含仓库前缀（例如 **extra/vim**），以便精确控制软件包来源。如果只提供软件包名称，则按声明顺序搜索各仓库。

**pacinstall** 和 **pacremove** 命令是与 **pactrans** 功能相同的别名，区别仅在于对目标的默认解释方式。

如果 stdin 未连接到终端，则从 stdin 读取软件包规格。

# CAVEATS

修改系统需要 root 权限。使用 pacman 的配置和数据库。属于 **pacutils** 软件包的一部分。事务冲突必须手动解决。

# HISTORY

**pactrans** 是由 **Andrew Gregory** 创建的 **pacutils** 的一部分。它提供对 ALPM 事务的编程式访问，适用于需要对软件包操作进行细粒度控制的脚本和自动化任务。

# SEE ALSO

[pacman](/man/pacman)(8), [pacsync](/man/pacsync)(1), [pacinstall](/man/pacinstall)(1), [pacremove](/man/pacremove)(1), [pacconf](/man/pacconf)(1)
