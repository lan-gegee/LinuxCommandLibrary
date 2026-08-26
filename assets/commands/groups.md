# TAGLINE

显示用户的组成员关系

# TLDR

**显示当前用户的组**

```groups```

**显示指定用户的组**

```groups [username]```

**显示多个用户的组**

```groups [user1] [user2]```

# SYNOPSIS

**groups** [_options_] [_users_]

# PARAMETERS

_USERS_
> 要查询所属组的用户名。

**--help**
> 显示帮助信息。

**--version**
> 显示版本。

# DESCRIPTION

**groups** 显示一个用户的组成员关系。不带参数时，它显示当前用户所属的组。主组排在最前，其后是补充组。

该命令从 **/etc/group** 和用户的补充组列表中读取信息。它等价于 **id -Gn**，但输出格式更简单。

# CAVEATS

显示的是登录时缓存的组。新加入的组需要重新登录才能生效。主组排在最前面。

# HISTORY

groups 是标准的 Unix 命令，在 Linux 系统上属于 **GNU coreutils**。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add uutils-coreutils-groups```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[id](/man/id)(1), [groupmems](/man/groupmems)(8), [newgrp](/man/newgrp)(1)
