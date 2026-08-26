# TAGLINE

修改 LDAP 目录条目

# TLDR

**从 LDIF 修改条目**

```ldapmodify -x -D "[cn=admin,dc=example,dc=com]" -W -f [changes.ldif]```

**添加条目（类似 ldapadd）**

```ldapmodify -a -x -D "[binddn]" -W -f [entry.ldif]```

**交互模式**

```ldapmodify -x -D "[binddn]" -W```

**删除属性**

```ldapmodify -x -D "[binddn]" -W -f [delete.ldif]```

**使用 LDAPS**

```ldapmodify -x -H ldaps://[server] -D "[binddn]" -W -f [file.ldif]```

# SYNOPSIS

**ldapmodify** [_options_] [**-f** _file_]

# PARAMETERS

**-x**
> 简单认证。

**-D** _binddn_
> 绑定 DN。

**-W**
> 提示输入密码。

**-w** _password_
> 密码（不安全）。

**-H** _URI_
> LDAP 服务器 URI。

**-f** _file_
> 包含修改内容的 LDIF 文件。

**-a**
> 添加模式（类似 ldapadd）。

**-c**
> 出错时继续。

**-M**
> 启用 manage DSA IT 控制。

**-n**
> 试运行。

# DESCRIPTION

**ldapmodify** 修改 LDAP 目录条目。它支持根据 LDIF 输入添加、替换和删除属性。

# LDIF MODIFICATION TYPES

```ldif
# Replace attribute
dn: uid=jdoe,ou=users,dc=example,dc=com
changetype: modify
replace: mail
mail: newemail@example.com

# Add attribute
dn: uid=jdoe,ou=users,dc=example,dc=com
changetype: modify
add: telephoneNumber
telephoneNumber: 555-1234

# Delete attribute
dn: uid=jdoe,ou=users,dc=example,dc=com
changetype: modify
delete: telephoneNumber
```

# CAVEATS

Schema 必须允许修改。必须使用正确的 changetype。多个操作之间用连字符（-）分隔。

# INSTALL

```apt: sudo apt install ldap-utils```

```dnf: sudo dnf install openldap-clients```

```apk: sudo apk add openldap-clients```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ldapadd](/man/ldapadd)(1), [ldapsearch](/man/ldapsearch)(1)
