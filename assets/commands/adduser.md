# TAGLINE

Debian 友好的用户与组管理前端

# TLDR

创建新用户并使用**默认主目录**，同时提示设置密码

```adduser [username]```

创建**没有**主目录的新用户

```adduser --no-create-home [username]```

以**指定路径**创建带主目录的新用户

```adduser --home [path/to/home] [username]```

以**指定 Shell** 创建新用户

```adduser --shell [path/to/shell] [username]```

创建属于**指定组**的新用户

```adduser --ingroup [group] [username]```

将现有用户添加到**组**

```adduser [username] [group]```

# SYNOPSIS

**adduser** [_options_] _user_ [_group_]

# DESCRIPTION

**adduser** 依据命令行选项和 /etc/adduser.conf 中的配置向系统添加用户和组。它是 **useradd**、**groupadd** 和 **usermod** 程序的 Debian 专用前端，提供符合发行版策略的默认值。

该工具会选取合适的 UID/GID 值，创建带有骨架配置文件的主目录，并同时支持普通账户和系统账户。

# PARAMETERS

**--home dir**
> 指定主目录

**--no-create-home**
> 跳过创建主目录

**--shell shell**
> 设置登录 Shell

**--uid ID**
> 指定用户 ID

**--gid GID**
> 设置主组 ID

**--ingroup GROUP**
> 按名称设置主组

**--system**
> 创建系统账户

**--group**
> 创建组（或为系统用户创建同名组）

**--disabled-login**
> 禁用登录（未设置密码，启用前无法登录）

**--disabled-password**
> 不设置密码（仍可通过 SSH 密钥等其他方式登录）

**--gecos GECOS**
> 无需交互提示即设置 GECOS 字段（全名、房间、电话等）

**--add-extra-groups**
> 将用户加入配置中定义的 EXTRA_GROUPS

**--firstuid ID**
> 覆盖新用户 UID 范围的起始值

**--lastuid ID**
> 覆盖新用户 UID 范围的结束值

**--quiet**
> 抑制提示性消息，只显示警告和错误

**--debug**
> 输出详细日志，便于排查问题

**--conf file**
> 使用替代配置文件而非 /etc/adduser.conf

# CONFIGURATION

**/etc/adduser.conf**
> 控制各种默认行为，包括主目录的基础路径、默认 Shell、骨架目录、UID/GID 范围，以及是否自动将用户加入额外组。

# CAVEATS

这是 **Debian/Ubuntu 专用**的前端；其他发行版可能直接使用默认值不同的 **useradd**。adduser 命令默认采用更严格的名称校验。

# HISTORY

作为 **Debian 专用**工具开发，旨在通过符合策略的默认值提供更友好的用户管理界面。

# INSTALL

```apt: sudo apt install adduser```

```aur: yay -S adduser```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[useradd](/man/useradd)(8), [deluser](/man/deluser)(8), [usermod](/man/usermod)(8), [passwd](/man/passwd)(1), [addgroup](/man/addgroup)(8)
