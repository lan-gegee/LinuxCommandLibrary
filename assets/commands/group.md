# TAGLINE

系统组数据库文件

# TLDR

**查看 group 文件**

```cat /etc/group```

**查找用户所属的组**

```groups [username]```

**按名称查找组**

```getent group [groupname]```

**列出组成员**

```getent group [groupname] | cut -d: -f4```

# DESCRIPTION

**/etc/group** 是定义组及其成员的系统文件。每行包含一个组条目，由四个冒号分隔的字段组成：组名、密码占位符、数字 GID，以及逗号分隔的成员用户名列表。

组控制文件的访问权限，是 Unix 安全的基础。用户可以属于多个组，其中一个主组在 /etc/passwd 中设置。

# FILE FORMAT

```
groupname:password:GID:members
```

**字段说明：**
- **groupname**：组名
- **password**：通常为 'x'（参见 /etc/gshadow）
- **GID**：数字组 ID
- **members**：逗号分隔的用户列表

# RELATED COMMANDS

```bash
groupadd groupname      # Create group
groupdel groupname      # Delete group
groupmod -n new old     # Rename group
gpasswd -a user group   # Add user to group
gpasswd -d user group   # Remove user from group
newgrp groupname        # Switch primary group
```

# CAVEATS

不建议直接编辑；请使用 groupadd/groupmod。更改可能需要注销后才能生效。低于 1000 的 GID 通常保留给系统组。

# SEE ALSO

[groups](/man/groups)(1), [groupadd](/man/groupadd)(8), [groupmod](/man/groupmod)(8), [passwd](/man/passwd)(5)

# RESOURCES

```[Source code](https://github.com/shadow-maint/shadow)```

<!-- verified: 2026-07-17 -->
