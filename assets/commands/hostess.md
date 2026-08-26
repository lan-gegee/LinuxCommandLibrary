# TAGLINE

幂等的 /etc/hosts 管理命令行工具

# TLDR

**添加主机条目**

```sudo hostess add [local.example.com] [127.0.0.1]```

**删除主机条目**

```sudo hostess rm [local.example.com]```

**列出所有条目**

```hostess ls```

**启用已禁用的条目**

```sudo hostess on [local.example.com]```

**禁用条目**

```sudo hostess off [local.example.com]```

**检查条目是否存在**

```hostess has [local.example.com]```

# SYNOPSIS

**hostess** _command_ [_arguments_]

# SUBCOMMANDS

**add** _hostname_ _ip_
> 添加或更新主机条目。

**rm** _hostname_
> 删除主机条目。

**ls**
> 列出所有条目。

**on** _hostname_
> 启用已禁用的条目。

**off** _hostname_
> 禁用条目。

**has** _hostname_
> 检查条目是否存在。

**fix**
> 重新格式化 hosts 文件。

# DESCRIPTION

**hostess** 是一个幂等的命令行工具，用于管理 /etc/hosts。它简化了开发和测试中主机条目的添加、删除和切换操作。条目可以在不删除的情况下禁用。在 Unix 上需要 root/sudo，在 Windows 上需要提升权限的提示符。

# CAVEATS

修改 /etc/hosts 需要提升权限。设置 HOSTESS_PATH 可覆盖默认的 hosts 文件位置。设置 HOSTESS_FMT 为 'windows' 或 'unix' 可覆盖格式检测。

# INSTALL

```pacman: sudo pacman -S hostess```

```brew: brew install hostess```

```nix: nix profile install nixpkgs#hostess```

<!-- packages: 2026-07-22 -->

# SEE ALSO

