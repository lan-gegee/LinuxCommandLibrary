# TAGLINE

将 AppArmor 配置文件设为投诉模式

# TLDR

将一个配置文件设为**投诉模式**

```sudo aa-complain [path/to/profile]```

将**多个配置文件**设为投诉模式

```sudo aa-complain [path/to/profile1] [path/to/profile2]```

将某个**目录**中的所有配置文件设为投诉模式

```sudo aa-complain -d [path/to/profiles]```

将配置文件设为投诉模式且**不重新加载**

```sudo aa-complain --no-reload [path/to/profile]```

# SYNOPSIS

**aa-complain** _executable_ [_executable_ ...] [_-d /path/to/profiles_] [_--no-reload_]

# DESCRIPTION

**aa-complain** 将 AppArmor 安全配置文件切换到投诉模式。在该模式下，安全策略**不会被强制执行**，但访问违规行为会被记录到系统日志中。这对在不阻碍应用功能的前提下测试和开发新配置文件非常有用。

# PARAMETERS

**-d, --dir /path/to/profiles**
> 指定存放 AppArmor 配置文件的目录；默认为 /etc/apparmor.d

**--no-reload**
> 修改后不自动重新加载配置文件

# CAVEATS

即使启用了投诉模式，**拒绝规则依然生效**。投诉模式只影响允许规则，显式拒绝仍会阻止访问。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **AppArmor** 工具包。

# INSTALL

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-enforce](/man/aa-enforce)(8), [aa-disable](/man/aa-disable)(8), [aa-logprof](/man/aa-logprof)(8), [aa-status](/man/aa-status)(8), [aa-audit](/man/aa-audit)(8), [apparmor](/man/apparmor)(7)

# RESOURCES

```[Source code](https://gitlab.com/apparmor/apparmor)```

```[Homepage](https://apparmor.net/)```

```[Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/home)```

<!-- verified: 2026-06-10 -->
