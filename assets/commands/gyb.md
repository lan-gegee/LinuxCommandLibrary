# TAGLINE

用于备份和恢复 Gmail 的命令行工具

# TLDR

**备份 Gmail**

```gyb --email [user@gmail.com] --action backup```

**恢复邮件**

```gyb --email [user@gmail.com] --action restore```

**估算备份大小**

```gyb --email [user@gmail.com] --action estimate```

**只备份最近的邮件**

```gyb --email [user@gmail.com] --action backup --search "newer_than:[7d]"```

**统计邮件数量**

```gyb --email [user@gmail.com] --action count```

**快速增量备份**（跳过已备份邮件的标签刷新）

```gyb --email [user@gmail.com] --action backup --fast-incremental```

# SYNOPSIS

**gyb** [_options_]

# PARAMETERS

**--email** _ADDR_
> Gmail 地址。

**--action** _ACT_
> 操作：backup、restore、restore-mbox、estimate、count、purge、print-labels、quota、reindex。

**--local-folder** _DIR_
> 本地备份目录。

**--search** _QUERY_
> 用于过滤邮件的 Gmail 搜索查询。

**--fast-incremental**
> 跳过已备份邮件的标签/标志刷新。

**--label-restored** _LABEL_
> 恢复时为所有邮件额外应用此标签。

**--strip-labels**
> 恢复期间移除现有标签。

**--spam-trash**
> 包含垃圾邮件和回收站文件夹。

**--service-account**
> 使用 Google 服务账号身份验证。

**--help**
> 显示帮助信息。

# DESCRIPTION

**GYB**（Got Your Back）是一款用于备份和恢复 Gmail 的命令行工具，通过 HTTPS 使用 Gmail API。

它支持增量备份和用于筛选特定邮件的搜索查询，还可以从 mbox 导出文件恢复（例如 Google Takeout）。备份以 SQLite 索引的形式存储在本地。

# CAVEATS

需要 OAuth 授权。受 Gmail API 速率限制。大型邮箱耗时较长。

# HISTORY

GYB 由 **Jay Lee** 创建，是一款开源 Gmail 备份工具，广泛用于 Google Workspace 迁移。

# INSTALL

```brew: brew install gyb```

```nix: nix profile install nixpkgs#gyb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[offlineimap](/man/offlineimap)(1), [mbsync](/man/mbsync)(1), [mutt](/man/mutt)(1)
