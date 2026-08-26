# TAGLINE

将 AppArmor 配置文件设为强制模式

# TLDR

以强制模式**启用**一个配置文件

```sudo aa-enforce [path/to/profile]```

以强制模式**启用多个配置文件**

```sudo aa-enforce [path/to/profile1] [path/to/profile2]```

启用来自**指定目录**的配置文件

```sudo aa-enforce -d [path/to/profiles]```

设置强制模式且**不重新加载**策略

```sudo aa-enforce --no-reload [path/to/profile]```

# SYNOPSIS

**aa-enforce** _executable_ [_executable_ ...] [_-d /path/to/profiles_] [_--no-reload_]

# DESCRIPTION

**aa-enforce** 将一个或多个 AppArmor 安全配置文件设为强制模式，这是默认也是最安全的模式。在强制模式下，安全策略被严格执行，任何访问违规行为都会被阻止并记录。

该命令用于撤销 **aa-complain**（设为投诉模式）和 **aa-disable**（卸载配置文件）的效果。

# PARAMETERS

**-d, --dir /path/to/profiles**
> 指定存放 AppArmor 配置文件的目录；默认为 /etc/apparmor.d

**--no-reload**
> 修改后不重新加载配置文件

# CAVEATS

如果配置文件未经充分测试就启用强制模式，过于严格的策略可能导致应用无法正常工作。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **AppArmor** 工具包。

# INSTALL

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-complain](/man/aa-complain)(8), [aa-disable](/man/aa-disable)(8), [aa-logprof](/man/aa-logprof)(8), [aa-status](/man/aa-status)(8), [apparmor](/man/apparmor)(7)

# RESOURCES

```[Source code](https://gitlab.com/apparmor/apparmor)```

```[Homepage](https://apparmor.net/)```

```[Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/home)```

<!-- verified: 2026-06-10 -->
