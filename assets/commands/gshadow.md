# TAGLINE

影子组密码文件格式

# TLDR

**查看 gshadow（需要 root）**

```sudo cat /etc/gshadow```

**安全编辑 gshadow**

```sudo vigr -s```

**检查 gshadow 一致性**

```sudo grpck```

# DESCRIPTION

**/etc/gshadow** 包含加密的组密码和组管理员信息。它是 /etc/group 的影子文件，用于限制对敏感组信息的访问。

每行的格式为：**groupname:password:admins:members**。密码字段使用 * 表示未设置密码，! 表示密码已禁用，或使用加密哈希（如 $6$ 表示 SHA-512）。

列在 admins 字段中的组管理员可以使用 gpasswd 在不需要 root 权限的情况下添加/移除成员以及修改组密码。

# FILE FORMAT

```
groupname:password:admins:members
```

**字段说明：**
- **groupname**: 组名（与 /etc/group 一致）
- **password**: 加密密码（! 或 * 表示禁用）
- **admins**: 以逗号分隔的组管理员列表
- **members**: 以逗号分隔的组成员列表

# PASSWORD FIELD

```
*   - 未设置密码
!   - 密码已禁用
$6$ - SHA-512 加密密码
```

# GROUP ADMINISTRATORS

管理员可以使用 gpasswd 在不需要 root 权限的情况下添加/移除成员以及修改组密码。

# CAVEATS

文件权限必须为 0640 或更严格。请使用 vigr -s 编辑以防损坏。并非所有系统都使用 gshadow。组密码很少被使用。

# SEE ALSO

[group](/man/group)(5), [gpasswd](/man/gpasswd)(1), [grpck](/man/grpck)(8)
