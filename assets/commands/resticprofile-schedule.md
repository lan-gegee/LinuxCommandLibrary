# TAGLINE

为 restic 备份配置创建定时任务

# TLDR

**为配置创建定时任务**

```resticprofile schedule [profile]```

**为所有配置创建定时任务**

```resticprofile schedule --all```

**以指定命令调度**

```resticprofile schedule [profile] --[backup]```

# SYNOPSIS

**resticprofile schedule** [_options_] [_profile_]

# PARAMETERS

_profile_
> 要调度的配置名称。

**--all**
> 调度所有配置。

**--backup**
> 调度 backup 命令。

**--check**
> 调度 check 命令。

**--prune**
> 调度 prune 命令。

# DESCRIPTION

**resticprofile schedule** 为 restic 备份配置创建定时任务。它与 systemd timer、launchd 或 Windows 任务计划程序集成。是 restic 备份的 resticprofile 封装的一部分。

# INSTALL

```brew: brew install resticprofile```

```nix: nix profile install nixpkgs#resticprofile```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[resticprofile](/man/resticprofile)(1), [restic](/man/restic)(1), [resticprofile-unschedule](/man/resticprofile-unschedule)(1)
