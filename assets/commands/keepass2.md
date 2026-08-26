# TAGLINE

将密码存储在加密数据库中的免费开源密码管理器

# TLDR

**打开 KeePass**

```keepass2```

**打开指定的数据库**

```keepass2 [database.kdbx]```

**使用密钥文件打开数据库**

```keepass2 [database.kdbx] -keyfile:[keyfile.key]```

# SYNOPSIS

**keepass2** [_options_] [_database_]

# PARAMETERS

**-keyfile:**_file_
> 使用密钥文件进行身份验证。

**-pw:**_password_
> 数据库密码（不安全）。

**-minimize**
> 启动后最小化。

**-auto-type**
> 执行自动输入。

# DESCRIPTION

**keepass2** 是一个免费的开源密码管理器，将密码存储在加密数据库中。支持强加密、密码生成和浏览器集成。数据库文件可以用主密码和/或密钥文件保护。

# CAVEATS

避免在命令行使用 -pw:，因为它会把密码暴露在进程列表和 shell 历史记录中。

# SEE ALSO

[keepassxc-cli](/man/keepassxc-cli)(1)
