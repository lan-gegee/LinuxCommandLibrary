# TAGLINE

查询 LDAP 目录

# TLDR

**搜索用户**

```ldapsearch -x -H ldap://[server] -b "[dc=example,dc=com]" "(uid=[username])"```

**带认证搜索**

```ldapsearch -x -D "[cn=admin,dc=example,dc=com]" -W -b "[dc=example,dc=com]" "(objectClass=*)"```

**返回特定属性**

```ldapsearch -x -b "[dc=example,dc=com]" "(uid=[user])" cn mail```

**通过 TLS 搜索**

```ldapsearch -x -ZZ -H ldap://[server] -b "[base]" "[filter]"```

**以 LDIF 格式输出**

```ldapsearch -x -b "[base]" -LLL "(uid=[user])"```

# SYNOPSIS

**ldapsearch** [_options_] [_filter_] [_attrs_...]

# DESCRIPTION

**ldapsearch** 查询 LDAP 目录。它连接到 LDAP 服务器，根据过滤器执行搜索，并返回匹配的条目。

该工具是目录管理、用户查找和 LDAP 配置调试的必备工具。

# PARAMETERS

**-x**
> 简单认证。

**-H** _uri_
> LDAP 服务器 URI。

**-b** _dn_
> 搜索基准 DN。

**-D** _dn_
> 绑定 DN。

**-W**
> 提示输入密码。

**-w** _pass_
> 绑定密码。

**-s** _scope_
> 搜索范围（base、one、sub）。

**-Z**
> 启动 TLS。

**-ZZ**
> 要求 TLS。

**-L**
> LDIF 输出格式。

**-LL**
> 输出中不含注释。

**-LLL**
> 不含注释和版本信息。

# CAVEATS

过滤器语法必须正确。基准 DN 必须与目录结构匹配。许多操作需要凭据。出于安全考虑建议使用 TLS。

# HISTORY

**ldapsearch** 是 **OpenLDAP** 的一部分。OpenLDAP 始于 **1998 年**，是一个开源的 LDAP 实现。LDAP 协议本身则在 **20 世纪 90 年代**早期脱胎于 X.500 目录服务。

# INSTALL

```apt: sudo apt install ldap-utils```

```dnf: sudo dnf install openldap-clients```

```apk: sudo apk add openldap-clients```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ldapadd](/man/ldapadd)(1), [ldapmodify](/man/ldapmodify)(1), [slapd](/man/slapd)(8)
