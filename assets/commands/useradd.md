# TAGLINE

创建新的用户账户

# TLDR

创建一个**新用户**

```sudo useradd username```

以指定的**用户 ID** 创建用户

```sudo useradd -u 1001 username```

以指定的 **shell** 创建用户

```sudo useradd -s /bin/zsh username```

创建带**附加组**的用户

```sudo useradd -G group1,group2 username```

创建带**主目录**的用户

```sudo useradd -m username```

使用**骨架目录**模板创建用户

```sudo useradd -k /etc/skel -m username```

创建不带主目录的**系统用户**

```sudo useradd -r username```

# SYNOPSIS

**useradd** [_options_] _LOGIN_

# DESCRIPTION

**useradd** 是一个向系统添加用户的底层工具。它更新系统文件，并可选择为用户创建带有初始文件的主目录。在 Debian 系系统上，人们往往更倾向于使用更高层的 **adduser** 命令。

# PARAMETERS

**-c, --comment COMMENT**
> 设置用户的全名或描述（GECOS 字段）

**-d, --home-dir HOME_DIR**
> 指定自定义的主目录路径

**-e, --expiredate DATE**
> 设置账户过期日期（YYYY-MM-DD）

**-f, --inactive DAYS**
> 密码过期后多少天将账户禁用

**-g, --gid GROUP**
> 分配主要组

**-G, --groups GROUP1,GROUP2**
> 加入若干补充组

**-k, --skel SKEL_DIR**
> 指定为家目录提供初始文件的骨架目录

**-m, --create-home**
> 创建用户的主目录

**-M, --no-create-home**
> 不创建主目录

**-p, --password PASSWORD**
> 设置加密后的密码

**-r, --system**
> 创建系统账户

**-s, --shell SHELL**
> 设置登录 shell

**-u, --uid UID**
> 分配指定的用户 ID

**-U, --user-group**
> 创建与用户同名的组

**-N, --no-user-group**
> 不创建对应的同名组

**-D**
> 显示或修改默认值

# CONFIGURATION

**/etc/default/useradd**
> 主目录基准路径、shell、组、过期时间和骨架目录等默认值。

**/etc/login.defs**
> 系统级的用户账户创建策略，包括 UID/GID 取值范围、密码时效以及主目录创建设置。

**/etc/skel/**
> 骨架目录；使用 -m 创建主目录时，其内容会被复制到新主目录中。

# CAVEATS

**-p** 选项要求传入已经加密的密码。不要在命令行上使用明文密码。建议在创建用户后再用 **passwd** 设置密码。

# HISTORY

**useradd** 属于 **shadow-utils** 软件包，负责 Unix 系统上的用户账户安全管理。在 Debian 系统上，**adduser** 提供了更友好的操作界面。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[adduser](/man/adduser)(8), [userdel](/man/userdel)(8), [usermod](/man/usermod)(8), [passwd](/man/passwd)(1), [groupadd](/man/groupadd)(8)
