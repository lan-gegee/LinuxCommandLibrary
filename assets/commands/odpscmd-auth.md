# TAGLINE

管理 odpscmd 控制台的 MaxCompute 身份验证

# TLDR

**以交互方式配置身份验证**

```odpscmd auth config```

**直接设置访问凭证**

```odpscmd auth set --access-id [id] --access-key [key]```

**显示当前已认证的用户**

```odpscmd auth whoami```

**清除已保存的凭证**

```odpscmd auth clear```

# SYNOPSIS

**odpscmd** **auth** [_command_] [_options_]

# PARAMETERS

**config**
> 以交互方式配置身份验证。

**set**
> 使用命令行标志以非交互方式设置凭证。

**whoami**
> 显示当前已认证的用户。

**clear**
> 移除已保存的凭证。

**--access-id** _ID_
> 阿里云 Access Key ID。

**--access-key** _KEY_
> 阿里云 Access Key Secret。

**--help**
> 显示帮助信息。

# DESCRIPTION

**odpscmd auth** 管理 odpscmd MaxCompute 控制台的身份验证，后者是基于 Java 的旧版阿里云 MaxCompute（前身为 ODPS）CLI。

凭证（Access Key ID 和 Secret）从阿里云控制台获取，并保存在本地的 odpscmd 配置文件中。`whoami` 子命令通过显示当前账户身份来验证连接是否正常。

较新的基于 Go 的 CLI 请参见 [odps-auth](/man/odps-auth)(1)。

# CAVEATS

属于旧版工具。凭证以明文形式存储在本地配置文件中。需要 Java 运行时。

# INSTALL

```aur: yay -S odpscmd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[odpscmd](/man/odpscmd)(1), [odps-auth](/man/odps-auth)(1)
