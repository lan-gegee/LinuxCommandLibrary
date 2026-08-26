# TAGLINE

合并 AppArmor 安全配置文件

# TLDR

将一个或多个配置文件**合并**到默认的配置目录

```sudo aa-mergeprof [file1] [file2]```

将配置文件**合并**到**指定目录**

```sudo aa-mergeprof -d /path/to/profiles [file1] [file2]```

# SYNOPSIS

**aa-mergeprof** _file_ [_file_ ...] [**-d** _/path/to/profiles_]

# DESCRIPTION

**aa-mergeprof** 是一个交互式工具，用于把一个或多个 AppArmor 安全配置文件合并进系统的配置目录。当传入的配置文件与现有配置文件存在冲突时，它会展示差异，并允许管理员选择如何解决。这在从其他系统导入配置文件、合并来自不同来源的配置文件，或在系统迁移后整合配置文件时很有用。

# PARAMETERS

**-d**, **--dir** _/path/to/profiles_
> 指定合并后配置文件的目标目录。默认为 **/etc/apparmor.d**。

**-h**, **--help**
> 显示帮助信息并退出。

# CAVEATS

合并配置文件可能覆盖目标目录中的现有配置文件。该工具是交互式的，需要手动解决冲突——无法无人值守运行。需要 root 权限。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **AppArmor** 工具包。

# INSTALL

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-genprof](/man/aa-genprof)(8), [aa-logprof](/man/aa-logprof)(8), [aa-cleanprof](/man/aa-cleanprof)(8), [aa-enforce](/man/aa-enforce)(8), [aa-complain](/man/aa-complain)(8), [apparmor](/man/apparmor)(7)
