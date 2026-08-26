# TAGLINE

使用配置组（profile）管理 /etc/hosts

# TLDR

**列出所有配置组**及其条目

```hostctl list```

**向配置组添加条目**

```hostctl add [profile_name] [ip] [hostname]```

**启用一个配置组**

```hostctl enable [profile_name]```

**禁用一个配置组**

```hostctl disable [profile_name]```

**删除一个配置组**

```hostctl remove [profile_name]```

**从文件导入配置组**

```hostctl set [profile_name] -from [path/to/file]```

**创建 hosts 文件的备份**

```hostctl backup```

**与 Docker Compose 容器同步**配置组

```hostctl sync dockercompose -f [docker-compose.yml] -p [profile_name]```

# SYNOPSIS

**hostctl** _command_ [_options_] [_arguments_]

# DESCRIPTION

**hostctl** 是一个使用配置组（profile）管理 **/etc/hosts** 文件的 CLI 工具。你可以拥有多个配置组，精确启用或禁用所需内容，并用简单命令在不同主机配置之间切换。它会自动检测操作系统并使用正确的 hosts 文件位置。

配置组允许将主机条目按不同环境（开发、预发布、生产）分组，并无需手动编辑文件即可切换开关状态。它还支持与 **Docker** 和 **Docker Compose** 容器同步配置组。

# PARAMETERS

**list**
> 显示配置组和条目的详细列表

**add** _profile_ _ip_ _hostname_
> 向配置组添加条目

**enable** _profile_
> 启用一个配置组

**disable** _profile_
> 禁用一个配置组

**remove** _profile_
> 完全删除一个配置组

**set** _profile_
> 替换某个配置组的内容

**backup**
> 创建 hosts 文件的备份

**sync**
> 与 Docker 或 Docker Compose 同步

# CAVEATS

修改 hosts 文件需要 **root/管理员**权限。错误的条目可能破坏本地 DNS 解析。进行大规模更改前务必使用 **backup** 命令。

# HISTORY

**hostctl** 由 **guumaster** 创建，用 **Go** 编写。它旨在用结构化的、基于配置组的方式取代手动编辑 hosts 文件，并与现代开发工作流集成。

# INSTALL

```nix: nix profile install nixpkgs#hostctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

