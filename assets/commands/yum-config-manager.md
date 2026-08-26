# TAGLINE

管理 yum 软件仓库配置

# TLDR

**查看**当前配置

```yum-config-manager```

从 URL 或文件**添加软件仓库**

```yum-config-manager --add-repo [url_or_path]```

**启用**一个或多个软件仓库

```yum-config-manager --enable [repo_id]```

**禁用**一个或多个软件仓库

```yum-config-manager --disable [repo_id]```

**设置**某个配置选项并保存

```yum-config-manager --setopt=[repo_id.option=value] --save```

# SYNOPSIS

**yum-config-manager** [_options_] [_section_...]

# PARAMETERS

**-h, --help**
> 显示帮助信息。

**--save**
> 保存当前选项（常与 **--setopt** 搭配使用）。

**--enable**
> 启用指定的软件仓库（自动保存）。

**--disable**
> 禁用指定的软件仓库（自动保存）。

**--add-repo=**_URL_|_FILE_
> 从给定的 .repo 文件或 URL 添加（并启用）一个软件仓库。

**--setopt=**_option_=_value_
> 设置 yum 配置或仓库文件中的任意配置选项。针对特定仓库的选项使用 _repoid.option=value_ 形式；_repoid_ 可包含通配符。

# DESCRIPTION

**yum-config-manager** 是用于管理 **yum** 主配置及其软件仓库的工具。它可以显示当前设置、切换仓库的启用状态、从 URL 或 .repo 文件添加新仓库，以及调整个别选项，无需手动编辑 `/etc/yum.conf` 或 `/etc/yum.repos.d/` 下的文件。

在现代 Red Hat 系发行版（RHEL 8+、Fedora、CentOS Stream）上，**yum** 已被 **dnf** 取代，此命令通常作为 `dnf config-manager` 的别名或封装提供。

# CAVEATS

修改配置必须以 root 身份运行。在基于 DNF 的系统上，**yum-config-manager** 是 **dnf config-manager** 的别名，需要安装 `dnf-plugins-core` 软件包。

# HISTORY

**yum-config-manager** 是 RPM 软件管理项目中 **yum-utils** 软件包（后为 **dnf-utils**）的一部分。在向 DNF 过渡之前，它被广泛用于 RHEL、CentOS 和 Fedora 上管理软件仓库。

# SEE ALSO

[dnf](/man/dnf)(8), [yum](/man/yum)(8), [rpm](/man/rpm)(8), [createrepo](/man/createrepo)(8)
