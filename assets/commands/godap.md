# TAGLINE

用于浏览 LDAP 目录的 TUI

# TLDR

**连接**到 LDAP 服务器

```godap [ldap://server:389]```

**带身份验证连接**

```godap -D [bind-dn] -W [ldap://server]```

在指定的 base DN 下**搜索**

```godap -b [ou=users,dc=example,dc=com] [ldap://server]```

# SYNOPSIS

**godap** [_options_] [_ldap-uri_]

# PARAMETERS

**-D, --bind-dn** _DN_
> 用于身份验证的 bind DN

**-W**
> 提示输入 bind 密码

**-w, --password** _PASSWORD_
> bind 密码（不安全）

**-b, --base-dn** _DN_
> 搜索所用的 base DN

**-H, --uri** _URI_
> LDAP 服务器 URI

**-Z, --starttls**
> 使用 StartTLS

**-x, --simple-auth**
> 使用简单认证

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**godap** 是一个用于浏览 LDAP 目录的终端用户界面。它允许用户导航目录树、查看条目并进行交互式搜索。

该工具支持多种 LDAP 身份验证方式与 TLS/SSL 连接，并以易读的格式显示 LDAP 条目。

# KEYBINDINGS

**↑/↓**
> 在条目之间导航

**Enter**
> 查看条目详情

**n**
> 新建搜索

**/ or s**
> 在当前上下文中搜索

**b**
> 返回

**q**
> 退出

# CAVEATS

需要能访问 LDAP 服务器。bind 凭据必须具有适当的权限。过大的目录可能出现性能问题。TLS 证书验证取决于系统配置。

# HISTORY

**godap** 的创建目的是提供一种从终端交互式浏览 LDAP 目录的方式，类似于 GUI 的 LDAP 浏览器。

# INSTALL

```apk: sudo apk add godap```

```brew: brew install godap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ldapsearch](/man/ldapsearch)(1)
