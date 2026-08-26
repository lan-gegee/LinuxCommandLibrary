# TAGLINE

Bitwarden 密码管理器命令行界面

# TLDR

**登录** Bitwarden

```bw login```

**解锁**密码库

```bw unlock```

**列出**条目

```bw list items```

**获取**密码

```bw get password [example.com]```

**创建**条目

```bw create item```

**同步**密码库

```bw sync```

# SYNOPSIS

**bw** _command_ [_options_]

# DESCRIPTION

**bw** 是开源密码管理器 Bitwarden 的官方命令行界面。它支持从终端或脚本中访问和管理密码、笔记以及凭据。

该工具提供对 Bitwarden 密码库的完全访问，用于自动化和集成。

# PARAMETERS

**--session** _key_
> 用于认证的会话密钥

**--organizationid** _id_
> 组织 ID 过滤器

**--pretty**
> 美化输出 JSON

**--raw**
> 只返回原始值

# COMMON COMMANDS

**login** [_email_]
> 登录账户

**unlock**
> 解锁密码库（返回会话密钥）

**lock**
> 锁定密码库

**sync**
> 与服务器同步密码库

**list** _object_
> 列出条目、文件夹、集合

**get** _object_ _id_
> 获取特定条目

**create** _object_ _encodedJson_
> 创建新条目

**edit** _object_ _id_ _encodedJson_
> 编辑已有条目

**delete** _object_ _id_
> 删除条目

# WORKFLOW

```bash
# Login
bw login user@example.com

# Unlock vault (save session key)
export BW_SESSION="$(bw unlock --raw)"

# List all items
bw list items

# Get password
bw get password github.com

# Search items
bw list items --search "google"

# Get username
bw get username amazon.com

# Generate password
bw generate -ulns --length 20

# Create item
echo '{"name":"My Login","username":"user","password":"pass"}' | \
  bw encode | bw create item
```

# FEATURES

- 完整的密码库访问
- 密码生成
- 安全笔记存储
- 双因素认证
- 组织支持
- 自托管服务器支持
- 用于脚本的 JSON 输出

# CAVEATS

大多数操作需要会话密钥。请安全地存储会话密钥（环境变量）。输出为 JSON（需要解析）。CLI 需要频繁解锁。自托管服务器需要额外配置。

# HISTORY

**Bitwarden CLI** 于 **2018 年**前后发布，是 Bitwarden 密码管理器的组成部分，用于提供终端和脚本访问能力。

# SEE ALSO

[pass](/man/pass)(1), [gopass](/man/gopass)(1), [op](/man/op)(1)

# RESOURCES

```[Source code](https://github.com/bitwarden/clients)```

```[Documentation](https://bitwarden.com/help/cli/)```

<!-- verified: 2026-06-22 -->
