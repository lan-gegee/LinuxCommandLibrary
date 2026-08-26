# TAGLINE

在 Matrix 家园服务器上创建用户

# TLDR

**交互式**创建用户

```register_new_matrix_user --config path/to/homeserver.yaml```

交互式创建**管理员用户**

```register_new_matrix_user --config path/to/homeserver.yaml --admin```

**非交互式**创建管理员用户

```register_new_matrix_user --config path/to/homeserver.yaml --user [username] --password [password] --admin```

在**远程**家园服务器上创建用户

```register_new_matrix_user --config path/to/homeserver.yaml --user [username] --password [password] --no-admin [https://matrix.example.com]```

# SYNOPSIS

**register_new_matrix_user** [_options_]

# PARAMETERS

**--config** _file_
> Synapse homeserver.yaml 配置文件路径

**--user** _name_
> 新账户的用户名

**--password** _password_
> 新账户的密码

**--admin**
> 创建管理员账户

**--no-admin**
> 不将新用户设为管理员（默认）

**-k** _secret_, **--shared-secret** _secret_
> 共享密钥（作为通过配置文件提供的替代方案）。

**-t** _type_, **--user-type** _type_
> 用户类型，取值见 synapse.api.constants.UserTypes。

**-h**, **--help**
> 显示帮助信息并退出。

**server_url**
> 家园服务器 URL（默认：https://localhost:8448）。

# DESCRIPTION

**register_new_matrix_user** 在开放注册被禁用时向 Matrix 家园服务器注册新用户。它从家园服务器配置中读取共享密钥来授权用户创建。

这是在关闭注册的 Synapse 服务器上创建用户的官方方式。

# CONFIGURATION

**homeserver.yaml**
> Synapse 家园服务器配置文件，包含用于授权用户创建的 **registration_shared_secret**。路径通过 **--config** 指定。

# CAVEATS

需要能够访问 homeserver.yaml 配置文件或注册共享密钥。非交互模式会将密码暴露到 shell 历史记录中；为了更好的安全性，请使用交互模式或 **-k**。

# HISTORY

属于 **Synapse**（Matrix 参考家园服务器实现）的一部分，提供管理性的用户管理功能。

# INSTALL

```dnf: sudo dnf install synapse```

```pacman: sudo pacman -S synapse```

```apk: sudo apk add synapse```

```nix: nix profile install nixpkgs#synapse```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[synctl](/man/synctl)(1)
