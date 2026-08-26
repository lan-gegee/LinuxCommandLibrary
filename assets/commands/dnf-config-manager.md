# TAGLINE

管理 DNF 软件仓库与配置

# TLDR

从 URL **添加**软件仓库

```dnf config-manager --add-repo=[repository_url]```

**打印**当前配置

```dnf config-manager --dump```

**启用**软件仓库

```dnf config-manager --set-enabled [repository_id]```

**禁用**软件仓库

```dnf config-manager --set-disabled [repository_id1] [repository_id2]```

**设置**配置选项

```dnf config-manager --setopt=[option]=[value]```

# SYNOPSIS

**dnf config-manager** [_options_]

# DESCRIPTION

**dnf config-manager** 提供通过命令行管理 DNF 软件仓库和配置设置的能力。它是 dnf-plugins-core 的一部分，可作为手动编辑配置文件的替代方案。

该工具可以从 URL 添加软件仓库（自动创建 .repo 文件）、启用或禁用已有仓库，以及即时修改 DNF 配置选项。对软件仓库的更改会持久保存到 /etc/yum.repos.d/ 下的 .repo 文件中。它尤其适合脚本化管理仓库、添加第三方仓库或临时调整配置而无需手动编辑文件。--dump 选项能显示完整的生效配置，便于排查问题。

# PARAMETERS

**--add-repo** _url_
> 从 URL 添加软件仓库

**--dump**
> 打印当前配置

**--set-enabled** _repo_
> 启用软件仓库

**--set-disabled** _repo_
> 禁用软件仓库

**--setopt** _opt=val_
> 设置配置选项

**--save**
> 将 `--setopt` 的修改持久写入相应配置文件（默认仅当前会话有效）。

**--dump-variables**
> 打印 DNF 内置变量的生效值（`$releasever`、`$basearch` 等）。

**--help-cmd**
> 显示帮助

# CONFIGURATION

**/etc/yum.repos.d/*.repo**
> 软件仓库配置文件。dnf config-manager 所做的更改会持久保存在这里。

**/etc/dnf/dnf.conf**
> DNF 主配置文件。可通过 --setopt 修改其中的选项。

# CAVEATS

在 DNF 4 上需要 **dnf-plugins-core** 插件。在 DNF 5（Fedora 41+）中该插件已并入主程序，子命令改为 **dnf5 config-manager**；大多数标志保持不变，但 **--set-enabled**/**--set-disabled** 变成了 **enable**/**disable** 子命令。仓库操作需要 root 权限。`.repo` 文件的更改会持久保存在 `/etc/yum.repos.d/` 中。

# SEE ALSO

[dnf](/man/dnf)(8), [dnf5](/man/dnf5)(8), [yum-config-manager](/man/yum-config-manager)(1), [yum](/man/yum)(8)
