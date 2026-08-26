# TAGLINE

AWS S3 存储桶的目录树可视化工具

# TLDR

**显示 S3 存储桶的树形结构**

```stree [my-bucket] -p [my_profile]```

**以深度限制 3 显示目录树**

```stree [my-bucket/data] -p [my_profile] -L 3```

**使用 LocalStack 显示目录树**

```stree [my-bucket] -l```

# SYNOPSIS

**stree** _bucket_[/_prefix_] [**-p** _profile_] [**-r** _region_] [**-L** _level_] [_options_]

# PARAMETERS

**-p** _PROFILE_
> 要使用的 AWS 配置文件名称。

**-r** _REGION_
> AWS 区域。

**-L** _LEVEL_
> 显示的最大目录深度。

**-l**
> 使用 LocalStack 进行本地测试。

# DESCRIPTION

**stree** 是一个以彩色输出显示 AWS S3 存储桶目录树结构的 CLI 工具。它支持自定义 AWS 配置文件、区域配置、深度层级控制、用于本地测试的 LocalStack，以及 MFA 角色切换功能。

# HISTORY

**stree** 由 **orangekame3** 创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S stree```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stu](/man/stu)(1), [aws](/man/aws)(1), [tree](/man/tree)(1)
