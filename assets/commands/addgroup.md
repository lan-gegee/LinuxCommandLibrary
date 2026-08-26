# TAGLINE

创建组并管理组成员身份

# TLDR

**创建**新组

```sudo addgroup [groupname]```

创建**系统**组

```sudo addgroup --system [groupname]```

将**用户**添加到现有组

```sudo addgroup [username] [groupname]```

以**指定 GID** 创建组

```sudo addgroup --gid [1001] [groupname]```

# SYNOPSIS

**addgroup** [_options_] _group_

**addgroup** [_options_] _user_ _group_

# DESCRIPTION

**addgroup** 是 Debian/Ubuntu 上一个友好的前端，封装了底层的 **groupadd** 命令。它遵循 adduser.conf 中定义的命名策略和约定，用于创建新组或将现有用户加入组。

把用户加入组时，它会修改 /etc/group 以将该用户列为成员。这是基于 Debian 的系统上管理组成员身份的推荐方式。

# PARAMETERS

**--gid** _id_
> 指定新组的组 ID（GID）

**--system**
> 创建系统组（GID 取自系统范围）

**--allow-bad-names**
> 允许不符合命名规范的组名

**--conf** _file_
> 使用备用配置文件

**--quiet**
> 抑制提示性消息

**--debug**
> 打印调试信息

# CONFIGURATION

**/etc/adduser.conf**
> 控制 addgroup 和 adduser 的默认行为，包括普通组和系统组的 GID 范围、命名策略以及组创建的默认设置。

# CAVEATS

组名必须遵循 adduser.conf 中定义的命名规则。系统组的 GID 通常低于 1000。用户需要注销并重新登录后，新的组成员身份才会生效。

# HISTORY

**addgroup** 作为 Debian adduser 软件包的一部分而创建，提供了一个遵循发行版策略的友好组管理界面。自 **1990** 年代中期起它便是 Debian 的一部分。

# INSTALL

```apt: sudo apt install adduser```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[groupadd](/man/groupadd)(8), [adduser](/man/adduser)(8), [delgroup](/man/delgroup)(8), [groups](/man/groups)(1)
