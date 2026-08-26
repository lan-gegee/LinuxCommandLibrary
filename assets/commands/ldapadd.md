# TAGLINE

向 LDAP 目录添加条目

# TLDR

**从 LDIF 文件添加条目**

```ldapadd -x -D "[cn=admin,dc=example,dc=com]" -W -f [entry.ldif]```

**使用简单绑定添加**

```ldapadd -x -H ldap://[server] -D "[binddn]" -w "[password]" -f [file.ldif]```

**使用 SASL 添加**

```ldapadd -Y EXTERNAL -H ldapi:/// -f [file.ldif]```

**详细输出**

```ldapadd -v -x -D "[binddn]" -W -f [file.ldif]```

**试运行**

```ldapadd -n -x -D "[binddn]" -W -f [file.ldif]```

# SYNOPSIS

**ldapadd** [_options_] [**-f** _file_]

# PARAMETERS

**-x**
> 使用简单认证而非 SASL。

**-D** _binddn_
> 用于认证的绑定 DN（distinguished name）。

**-W**
> 提示输入绑定密码。

**-w** _password_
> 绑定密码（不安全，在进程列表中可见）。

**-H** _URI_
> LDAP 服务器 URI（如 ldap://host、ldaps://host、ldapi:///）。

**-f** _file_
> 从 LDIF 文件而不是标准输入读取条目。

**-c**
> 出错时继续（报告错误但不停止）。

**-n**
> 试运行，显示将执行的操作但不修改条目。

**-v**
> 详细输出。

**-d** _debuglevel_
> 设置 LDAP 调试级别。

**-Y** _mechanism_
> SASL 认证机制（如 EXTERNAL、GSSAPI）。

**-Z**
> 发起 StartTLS 扩展操作。

**-ZZ**
> 要求 StartTLS 必须成功。

# DESCRIPTION

**ldapadd** 向 LDAP 目录添加条目。它读取包含新条目的 LDIF（LDAP Data Interchange Format）文件，并将这些条目添加到目录中。

ldapadd 实际上是指向 ldapmodify 的硬链接，并自动启用了 -a 标志。它会连接到 LDAP 服务器，使用提供的凭据完成绑定，然后添加指定的条目。不带 -H 时，它会连接 ldap.conf 中配置的默认 LDAP 服务器。

# LDIF EXAMPLE

```ldif
dn: uid=jdoe,ou=users,dc=example,dc=com
objectClass: inetOrgPerson
uid: jdoe
cn: John Doe
sn: Doe
mail: jdoe@example.com
```

# CAVEATS

需要适当的权限。LDIF 语法必须正确。父条目必须存在。出于安全考虑请用 -W 而不是 -w。

# HISTORY

ldapadd 是 **OpenLDAP** 的一部分。OpenLDAP 是一个免费的 LDAP 实现，由 Kurt Zeilenga 于 **1998 年**创建，是密歇根大学 LDAP 项目的延续。

# INSTALL

```apt: sudo apt install ldap-utils```

```dnf: sudo dnf install openldap-clients```

```apk: sudo apk add openldap-clients```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ldapmodify](/man/ldapmodify)(1), [ldapsearch](/man/ldapsearch)(1)
