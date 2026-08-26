# TAGLINE

移除已调度的 restic 备份任务

# TLDR

**移除已调度的备份**

```resticprofile unschedule [profile]```

**移除所有定时任务**

```resticprofile unschedule --all```

# SYNOPSIS

**resticprofile unschedule** [_options_] [_profile_]

# PARAMETERS

_profile_
> 要取消调度的配置名称。

**--all**
> 移除所有已调度的配置。

# DESCRIPTION

**resticprofile unschedule** 移除由 resticprofile schedule 创建的定时备份任务。会移除 systemd timer、launchd 任务或 Windows 任务计划程序条目。

# INSTALL

```brew: brew install resticprofile```

```nix: nix profile install nixpkgs#resticprofile```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[resticprofile](/man/resticprofile)(1), [resticprofile-schedule](/man/resticprofile-schedule)(1)
