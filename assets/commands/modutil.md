# TAGLINE

管理 NSS 数据库中的 PKCS#11 安全模块

# TLDR

**列出模块**

```modutil -list -dbdir [sql:/etc/pki/nssdb]```

**添加模块**

```modutil -add [module_name] -libfile [/path/to/lib.so] -dbdir [sql:/etc/pki/nssdb]```

**删除模块**

```modutil -delete [module_name] -dbdir [sql:/etc/pki/nssdb]```

**启用模块**

```modutil -enable [module_name] -dbdir [sql:/etc/pki/nssdb]```

# SYNOPSIS

**modutil** [_options_]

# PARAMETERS

**-list**
> 列出已安装的模块。

**-add** _name_
> 添加 PKCS#11 模块。

**-delete** _name_
> 移除模块。

**-enable** _name_
> 启用模块。

**-disable** _name_
> 禁用模块。

**-libfile** _path_
> 模块库路径。

**-dbdir** _dir_
> NSS 数据库目录。

# DESCRIPTION

**modutil** 管理 NSS 数据库中的 PKCS#11 安全模块。可用于添加、移除和配置硬件令牌及软件模块。它是 Mozilla NSS 工具集的一部分。

# INSTALL

```apt: sudo apt install libnss3-tools```

```dnf: sudo dnf install nss-tools```

```apk: sudo apk add nss-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[certutil](/man/certutil)(1)
