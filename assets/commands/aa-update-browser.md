# TAGLINE

管理 AppArmor 配置文件中的浏览器抽象 include

# TLDR

**列出**可用的浏览器抽象配置文件

```sudo aa-update-browser -l```

显示将要进行的更改（**试运行**）

```sudo aa-update-browser -d [path/to/profile]```

用指定的抽象**更新**配置文件

```sudo aa-update-browser -u [abstraction1,abstraction2] [path/to/profile]```

**移除**配置文件中的所有抽象

```sudo aa-update-browser -u '' [path/to/profile]```

# SYNOPSIS

**aa-update-browser** [_option_] _profile_

# DESCRIPTION

**aa-update-browser** 更新 AppArmor 浏览器配置文件，使其使用受支持的抽象。该工具让管理员能够添加、修改或删除浏览器相关的抽象 include，从而帮助维护浏览器配置文件。

浏览器抽象为常见的浏览器操作提供预定义的访问规则，简化了配置文件的管理。

# PARAMETERS

**-l**
> 显示受支持的浏览器抽象。

**-d**
> 试运行。只显示对给定配置文件将执行的操作，不实际应用更改。

**-u** _ABSTRACTIONS_
> 用逗号分隔的 ABSTRACTIONS 列表更新给定配置文件。指定 '' 则移除所有抽象。

**-h**
> 显示帮助信息。

# CAVEATS

修改浏览器配置文件可能影响浏览器的功能。建议先在投诉模式下测试更改，再启用强制模式。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **AppArmor** 工具包。

# SEE ALSO

[aa-logprof](/man/aa-logprof)(8), [aa-enforce](/man/aa-enforce)(8), [aa-complain](/man/aa-complain)(8), [apparmor](/man/apparmor)(7)

# RESOURCES

```[Source code](https://gitlab.com/apparmor/apparmor)```

```[Homepage](https://apparmor.net/)```

```[Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/home)```

<!-- verified: 2026-06-10 -->
