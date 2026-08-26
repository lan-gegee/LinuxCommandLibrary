# TAGLINE

将 AppArmor 配置文件设为审计模式

# TLDR

将一个配置文件设为**审计模式**

```sudo aa-audit [profile_name]```

将**多个配置文件**设为审计模式

```sudo aa-audit [profile1] [profile2]```

从**指定目录**将配置文件设为审计模式

```sudo aa-audit -d /path/to/profiles [profile_name]```

将配置文件设为审计模式且**不重新加载**

```sudo aa-audit --no-reload [profile_name]```

# SYNOPSIS

**aa-audit** _executable_ [_executable_ ...] [_-d /path/to/profiles_] [_--no-reload_]

# DESCRIPTION

**aa-audit** 将 AppArmor 安全配置文件设为审计模式运行。在该模式下，安全策略仍然强制执行，并且**所有访问尝试**（无论成败）都会被记录到系统日志中。这使管理员能够在继续实施安全策略的同时监视应用行为。

# PARAMETERS

**-d, --dir /path/to/profiles**
> 指定存放 AppArmor 配置文件的目录；默认为 /etc/apparmor.d

**--no-reload**
> 修改后不自动重新加载配置文件

**-r, --remove**
> 为指定配置文件关闭审计模式（撤销 aa-audit 的效果）。

**-h, --help**
> 显示帮助信息

# CAVEATS

审计模式会记录所有访问尝试，产生大量日志输出。这可能影响系统性能，并在繁忙的系统上迅速填满日志文件。

# HISTORY

属于 **AppArmor** 应用安全框架的一部分，该框架作为 SELinux 的替代方案而开发。AppArmor 最初由 **Immunix** 开发，后于 2005 年被 **Novell** 收购。

# INSTALL

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-enforce](/man/aa-enforce)(8), [aa-complain](/man/aa-complain)(8), [aa-disable](/man/aa-disable)(8), [aa-status](/man/aa-status)(8), [apparmor](/man/apparmor)(7)
