# TAGLINE

开源钓鱼模拟框架

# TLDR

**启动 Gophish 服务器**

```./gophish```

**以自定义配置启动**

```./gophish -config [config.json]```

**访问管理后台**

```https://localhost:3333```

# SYNOPSIS

**gophish** [_options_]

# PARAMETERS

**-config** _file_
> 配置文件的路径。

# DESCRIPTION

**Gophish** 是一个用于安全意识培训和渗透测试的开源钓鱼框架。它提供 Web 界面来创建和管理钓鱼活动，包括邮件模板编辑、落地页克隆和结果跟踪。

安全团队用它来测试组织内部对钓鱼攻击的意识和响应能力。平台提供活动管理、用户组处理，并支持 API 以便自动化操作。

# CONFIGURATION

**config.json**
> 主配置文件，指定管理服务器地址、钓鱼服务器地址、数据库路径和 TLS 设置。

# DEFAULT CREDENTIALS

```
Admin Panel: https://localhost:3333
Username: admin
Password: (shown on first run)
```

# CAVEATS

仅限授权的安全测试使用。使用前必须获得适当授权。发送邮件需要配置 SMTP。可能被安全软件标记为威胁。请妥善保管凭据。

# HISTORY

Gophish 由 **Jordan Wright** 于 **2015 年**创建，作为商业钓鱼模拟平台的开源替代品。它被广泛应用于安全意识培训和渗透测试中。

# INSTALL

```nix: nix profile install nixpkgs#gophish```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[setoolkit](/man/setoolkit)(1)
