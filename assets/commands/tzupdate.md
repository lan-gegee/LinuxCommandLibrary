# TAGLINE

通过 IP 地理定位自动设置系统时区

# TLDR

**自动设置系统时区**

```tzupdate```

**打印检测到的时区但不应用**

```tzupdate -p```

**检测特定 IP 的时区**

```tzupdate -i [8.8.8.8]```

# SYNOPSIS

**tzupdate** [_options_]

# PARAMETERS

**-p**
> 打印检测到的时区而不更改系统设置

**-i** _IP_
> 使用指定的 IP 地址而不是自动检测

# DESCRIPTION

**tzupdate** 对你的 IP 地址进行地理定位，确定正确的时区并更新系统的本地时区。它会查询地理定位服务，并能防范无效结果。适用于在服务器或全新安装的系统上自动配置时区。更新系统时区通常需要 root 权限。

# HISTORY

**tzupdate** 由 **cdown** 开发，使用 **Rust** 编写（之前是 Python）。

# INSTALL

```nix: nix profile install nixpkgs#tzupdate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timedatectl](/man/timedatectl)(1), [date](/man/date)(1), [tz](/man/tz)(1)
