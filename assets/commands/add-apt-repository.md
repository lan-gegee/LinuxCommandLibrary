# TAGLINE

管理 APT 软件仓库源

# TLDR

**添加**新的 apt 软件仓库

```add-apt-repository [repository_spec]```

**移除**apt 软件仓库

```add-apt-repository -r [repository_spec]```

添加仓库后**不**更新软件包缓存

```add-apt-repository -n [repository_spec]```

允许从仓库下载**源码包**

```add-apt-repository -s [repository_spec]```

添加 **PPA**（个人软件包归档）

```add-apt-repository ppa:[user]/[ppa-name]```

**列出**当前已配置的软件仓库

```add-apt-repository -L```

# SYNOPSIS

**add-apt-repository** [_OPTIONS_] [_LINE_]

# DESCRIPTION

**add-apt-repository** 是 Debian/Ubuntu 上的实用工具，用于管理第三方 APT 软件仓库源。它可以向 /etc/apt/sources.list 添加条目，或在 /etc/apt/sources.list.d/ 下创建单独的文件，也可以移除之前添加的软件仓库。

该工具最常用于添加来自 Launchpad 的 PPA（个人软件包归档），并自动处理 source list 条目和相应的 GPG 密钥导入。默认情况下，它在修改软件源后会更新软件包缓存；传入 **-n** 可跳过这一步。

# PARAMETERS

**-r, --remove**
> 移除指定的软件仓库（禁用匹配的行；删除空的 source 文件）

**-y, --yes**
> 对交互提示一律自动应答为是

**-n, --no-update**
> 添加仓库后跳过软件包缓存更新

**-s, --enable-source**
> 允许从该仓库下载源码包

**-c, --component**
> 指定仓库组件；未指定时默认为 'main'

**-p, --pocket**
> 定义 pocket 类型（默认为 release pocket）

**-P, --ppa**
> 添加 Ubuntu Launchpad 个人软件包归档（格式：ppa:USER/PPA）

**-C, --cloud**
> 添加 Ubuntu Cloud Archive（格式：cloud-archive:CANAME）

**-U, --uri**
> 通过单个 URI 添加归档源

**-S, --sourceslist**
> 使用完整的 sources.list 格式行添加归档源

**-L, --list**
> 列出当前已配置的软件仓库

**-l, --login**
> 登录 Launchpad 以访问私有 PPA

**--dry-run**
> 预览更改而不实际执行

**-d, --debug**
> 输出调试信息

# CAVEATS

此工具为 **Debian/Ubuntu 专用**，在其他 Linux 发行版上不可用。添加第三方软件仓库可能引入安全风险。

# HISTORY

为 **Ubuntu** 开发，用于简化添加 PPA（个人软件包归档）及其他第三方软件仓库的过程。

# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [apt-cache](/man/apt-cache)(8), [apt-key](/man/apt-key)(8)

# RESOURCES

```[Source code](https://salsa.debian.org/debian/software-properties)```

```[Documentation](https://manpages.ubuntu.com/manpages/noble/man1/add-apt-repository.1.html)```

<!-- verified: 2026-06-11 -->
