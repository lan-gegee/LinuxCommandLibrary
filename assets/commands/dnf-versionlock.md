# TAGLINE

锁定软件包版本以阻止更新

# TLDR

**列出**版本锁定条目

```dnf versionlock list```

**为**软件包按当前版本添加版本锁

```dnf versionlock add [package]```

**添加**不解析到具体版本的版本锁

```dnf versionlock add --raw [package-name-spec]```

**排除**指定的软件包版本使其无法被安装

```dnf versionlock exclude [package]```

**删除**特定的版本锁定条目

```dnf versionlock delete [package]```

**清空**所有版本锁定条目

```dnf versionlock clear```

# SYNOPSIS

**dnf versionlock** [_options_] [_add_|_exclude_|_list_|_delete_|_clear_] [_package-name-spec_]

# DESCRIPTION

**dnf versionlock** 保护软件包不被更新到更新的版本。它是 dnf-plugins-core 软件包的一部分。

该插件逐行读取版本锁文件，解析名称和版本，并排除名称相同但不匹配所列版本的所有软件包。它也可以反向工作：在前面加 '!' 来排除特定版本。

适合锁定已知稳定的软件包版本，或避免有问题的更新。

# PARAMETERS

**add** _package-name-spec_
> 将软件包锁定在当前已安装的版本。此后只有匹配的版本才能参与事务。

**exclude** _package-name-spec_
> 排除匹配该 spec 的软件包，使其不能被安装或更新到。

**list**
> 显示当前的版本锁定条目（未给出子命令时的默认行为）。

**delete** _package-name-spec_
> 删除匹配该 spec 的版本锁定条目。

**clear**
> 移除所有版本锁定条目。

**--raw**
> 不把 package-name-spec 解析为具体的 NEVRA。按原样使用 spec，允许锁定尚不可用的版本。

# CONFIGURATION

**/etc/dnf/plugins/versionlock.list**
> 存放软件包版本锁定条目。每行包含一条 NEVRA 格式的软件包规格。以 '!' 开头的行作为排除规则。

# CAVEATS

需要 dnf-plugins-core 软件包。被锁定的软件包不会收到安全更新，除非移除或更新锁定。请定期使用 `dnf versionlock list` 审查锁定情况。锁文件采用 NEVRA 格式（name-epoch:version-release.arch）以实现精确的版本匹配。

# SEE ALSO

[dnf](/man/dnf)(8), [yum-versionlock](/man/yum-versionlock)(8), [rpm](/man/rpm)(8), [yum](/man/yum)(8)
