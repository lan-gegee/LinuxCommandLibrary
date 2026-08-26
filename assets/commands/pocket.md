# TAGLINE

在终端管理 Pocket 稍后阅读服务

# TLDR

**添加 URL 到 Pocket**

```pocket add [url]```

**列出已保存的条目**

```pocket list```

**归档条目**

```pocket archive [item_id]```

**搜索已保存的条目**

```pocket search [query]```

# SYNOPSIS

**pocket** _command_ [_options_] [_args_]

# PARAMETERS

**add** _url_
> 添加 URL 到 Pocket。

**list**
> 列出已保存的条目。

**archive** _id_
> 归档条目。

**delete** _id_
> 删除条目。

**search** _query_
> 搜索已保存的条目。

**favorite** _id_
> 收藏条目。

# DESCRIPTION

**pocket** 是 Pocket 稍后阅读服务的命令行客户端。它让你可以在终端管理 Pocket 列表，包括添加、列出和整理已保存的文章。

# EXAMPLES

```bash
# Add article
pocket add https://example.com/article

# List unread items
pocket list

# Archive item
pocket archive 12345

# Search for tag
pocket search --tag programming

# Export list
pocket list --format json > pocket.json
```

# AUTHENTICATION

```bash
# First run requires authentication
pocket auth

# Uses OAuth to get access token
# Token stored in config file
```

# CAVEATS

需要 Pocket 账户和 API 身份验证。这是第三方 CLI 客户端，功能可能因实现而异。

# HISTORY

Pocket CLI 客户端是与 **Pocket** 服务（最初名为 Read It Later）交互的社区开发工具，该服务于 2017 年被 **Mozilla** 收购。

# INSTALL

```aur: yay -S pocket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1)
