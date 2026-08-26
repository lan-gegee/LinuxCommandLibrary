# TAGLINE

创建和查询 Postfix 查找表

# TLDR

**从文本文件创建 hash 数据库**

```postmap [/etc/postfix/virtual]```

**以特定类型创建数据库**

```postmap hash:[/etc/postfix/transport]```

**查询数据库**

```postmap -q [key] [/etc/postfix/virtual]```

**显示所有条目**

```postmap -s [/etc/postfix/virtual]```

# SYNOPSIS

**postmap** [_options_] [_file_type:_]_name_

# PARAMETERS

**-q** _key_
> 查询指定的键。

**-s**
> 显示所有条目。

**-d** _key_
> 删除键。

**-i**
> 增量模式。

**-N**
> 将表名作为查找键或值的一部分包含在内。

**-w**
> 等待被锁定的文件。

# DESCRIPTION

**postmap** 用于创建和查询 Postfix 查找表。它将包含键值对的纯文本文件转换为索引数据库格式（hash、btree、dbm），供 Postfix 邮件系统高效查找。常见用途包括虚拟别名映射、传输映射和访问控制表。

编辑文本查找文件后，必须运行 postmap 重建 Postfix 实际读取的 .db 文件。查询模式（-q）可用于测试单个查找，显示模式（-s）可列出所有条目——两者都有助于在将映射应用到实际邮件投递之前验证其是否按预期工作。

# EXAMPLES

```bash
# Create virtual alias map
postmap /etc/postfix/virtual

# Create transport map
postmap hash:/etc/postfix/transport

# Query specific entry
postmap -q "user@example.com" /etc/postfix/virtual

# Show all mappings
postmap -s /etc/postfix/virtual

# Delete entry
postmap -d "olduser@example.com" /etc/postfix/virtual
```

# FILE FORMAT

```
# /etc/postfix/virtual
user@example.com    localuser
@example.com        catchall@other.com
```

# CAVEATS

编辑文本文件后需运行 postmap。Postfix 读取的是 .db 文件而非文本文件。使用 postmap -q 进行验证。

# HISTORY

postmap 是 **Wietse Venema** 创建的邮件传输代理 **Postfix** 的组成部分。

# INSTALL

```apt: sudo apt install postfix```

```dnf: sudo dnf install postfix```

```pacman: sudo pacman -S postfix```

```apk: sudo apk add postfix```

```zypper: sudo zypper install postfix```

```nix: nix profile install nixpkgs#postfix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[postconf](/man/postconf)(1), [postfix](/man/postfix)(1), [postqueue](/man/postqueue)(1), [newaliases](/man/newaliases)(1)
