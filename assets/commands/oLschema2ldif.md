# TAGLINE

将 OpenLDAP 模式转换为 LDIF

# TLDR

**转换 OpenLDAP 模式**

```oLschema2ldif -i [schema.schema] -o [output.ldif]```

**转换多个模式**

```oLschema2ldif -i [schema1.schema] -i [schema2.schema] -o [output.ldif]```

**指定 Base DN**

```oLschema2ldif -b "[cn=config]" -i [schema.schema]```

# SYNOPSIS

**oLschema2ldif** [_options_]

# PARAMETERS

**-i** _FILE_
> 输入的模式文件。

**-o** _FILE_
> 输出的 LDIF 文件。

**-b** _DN_
> 模式的 Base DN。

**--help**
> 显示帮助信息。

# DESCRIPTION

**oLschema2ldif** 将 OpenLDAP 模式转换为 LDIF，用于迁移模式格式。

该工具可转换模式定义，用于 LDAP 配置。

# CAVEATS

Samba 工具的组成部分。仅针对特定模式格式。

# HISTORY

oLschema2ldif 为 LDAP 环境中的**模式迁移**而创建。

# INSTALL

```apt: sudo apt install samba```

```dnf: sudo dnf install samba```

```pacman: sudo pacman -S samba```

```apk: sudo apk add samba-client```

```zypper: sudo zypper install samba```

```brew: brew install samba```

```nix: nix profile install nixpkgs#samba```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ldapadd](/man/ldapadd)(1), [slapd](/man/slapd)(1), [ldapmodify](/man/ldapmodify)(1)
