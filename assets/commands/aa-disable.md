# TAGLINE

禁用 AppArmor 安全配置文件

# TLDR

**禁用**一个配置文件

```sudo aa-disable [path/to/profile]```

禁用**多个配置文件**

```sudo aa-disable [path/to/profile1] [path/to/profile2]```

禁用某个**目录**中的配置文件

```sudo aa-disable --dir [path/to/profiles]```

禁用一个配置文件且**不重新加载**策略

```sudo aa-disable --no-reload [path/to/profile]```

# SYNOPSIS

**aa-disable** _executable_ [_executable_ ...] [_-d /path/to/profiles_] [_--no-reload_]

# DESCRIPTION

**aa-disable** 用于禁用一个或多个 AppArmor 配置文件。该命令会从内核中卸载配置文件，并阻止其在 AppArmor 启动时被加载。

它会在 **/etc/apparmor.d/disable/** 中创建指向该配置文件的符号链接，从而防止 AppArmor 重启时自动加载该文件。配置文件本身仍保留在 **/etc/apparmor.d** 中，但处于未激活状态。要重新启用被禁用的配置文件，请使用 **aa-enforce** 或 **aa-complain**。

# PARAMETERS

**-d, --dir /path/to/profiles**
> 指定存放 AppArmor 配置文件的目录；默认为 /etc/apparmor.d

**--no-reload**
> 修改后不重新加载配置文件

# CAVEATS

禁用配置文件会移除对相应应用的安全保护。在该配置文件重新启用之前，应用将在没有 AppArmor 约束的情况下运行。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **AppArmor** 工具包。

# INSTALL

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-enforce](/man/aa-enforce)(8), [aa-complain](/man/aa-complain)(8), [aa-remove-unknown](/man/aa-remove-unknown)(8), [aa-status](/man/aa-status)(8), [apparmor](/man/apparmor)(7)

# RESOURCES

```[Source code](https://gitlab.com/apparmor/apparmor)```

```[Homepage](https://apparmor.net/)```

```[Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/home)```

<!-- verified: 2026-06-10 -->
