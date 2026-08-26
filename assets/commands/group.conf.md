# TAGLINE

PAM 动态组成员分配配置

# TLDR

**查看** group.conf 文件

```cat /etc/security/group.conf```

每次控制台登录时将用户**加入 audio 组**（规则行）

```*;tty*;[user];Al0000-2400;audio```

仅对工作日登录**授予 video 和 cdrom**

```login;*;[user];Wk0800-1800;video,cdrom```

仅适用于 SSH 的**特定服务规则**

```sshd;*;[user];Al0000-2400;developers```

在 PAM 中**启用**模块（位于 **/etc/pam.d/login**）

```auth optional pam_group.so```

# DESCRIPTION

**/etc/security/group.conf** 配置 pam_group 模块，该模块根据用户登录的服务和当天时间为其分配补充组。

这个 PAM 配置文件允许动态组成员关系，而无需永久修改 /etc/group。规则由五个分号分隔的字段定义，分别指定服务、终端、用户、时间窗口和要分配的组。

# FILE FORMAT

```
services;ttys;users;times;groups
```

**字段说明：**
- **services**：PAM 服务名（login、sshd、*）
- **ttys**：终端名称（tty*、pts/*、*）
- **users**：用户名，或 * 表示全部
- **times**：时间规格（Al0000-2400 = 总是）
- **groups**：要分配的组

# TIME FORMAT

```
Al - All days
Wk - Weekdays
Wd - Weekends
Mo,Tu,We,Th,Fr,Sa,Su - Specific days
0000-2400 - Time range (24h format)
```

# CONFIGURATION

**/etc/security/group.conf**
> 配置文件本身，登录期间由 pam_group.so 读取。

# CAVEATS

需要在 PAM 配置中包含 pam_group.so。只对新会话生效。不能替代永久的组成员关系。

# SEE ALSO

[pam_group](/man/pam_group)(8), [group](/man/group)(5), [pam.conf](/man/pam.conf)(5)
