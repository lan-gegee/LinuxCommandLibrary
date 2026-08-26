# TAGLINE

通过删除冗余规则清理 AppArmor 配置文件

# TLDR

**清理**一个配置文件以移除无用的规则

```sudo aa-cleanprof [profile_name]```

一次清理**多个配置文件**

```sudo aa-cleanprof [profile1] [profile2]```

指定配置文件所在的**目录**

```sudo aa-cleanprof -d /path/to/profiles [profile_name]```

以**静默**方式运行，不做提示

```sudo aa-cleanprof -s [profile_name]```

清理后阻止重新加载配置文件

```sudo aa-cleanprof --no-reload [profile_name]```

# SYNOPSIS

**aa-cleanprof** _executable_ [_executable_ ...] [_-d /path/to/profiles_] [_--no-reload_] [_-s_]

# DESCRIPTION

**aa-cleanprof** 会移除 AppArmor 安全配置文件中的多余规则，包括已被 include 指令或其他规则覆盖的规则。该工具还会重排规则，把相似的规则归为一组，并删除配置文件中的所有注释。

# PARAMETERS

**-d, --dir /path/to/profiles**
> 指定存放 AppArmor 配置文件的目录；默认为 /etc/apparmor.d

**--no-reload**
> 修改后不重新加载配置文件

**-s, --silent**
> 不询问用户，自动覆盖配置文件

**-h, --help**
> 显示帮助信息

# CAVEATS

此工具会移除配置文件中的所有注释，可能丢失配置文件中有用的文档或备注。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **AppArmor** 工具包。

# INSTALL

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-logprof](/man/aa-logprof)(8), [aa-genprof](/man/aa-genprof)(8), [aa-enforce](/man/aa-enforce)(8), [aa-complain](/man/aa-complain)(8), [aa-disable](/man/aa-disable)(8), [apparmor](/man/apparmor)(7)

# RESOURCES

```[Source code](https://gitlab.com/apparmor/apparmor)```

```[Homepage](https://apparmor.net/)```

```[Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/home)```

<!-- verified: 2026-06-10 -->
