# TAGLINE

Google 通讯录命令行接口

# TLDR

完成 **OAuth2** 设置，让 goobook 可以读取 Google 通讯录

```goobook authenticate```

将所有联系人以 **XML** 格式导出到标准输出

```goobook dump_contacts```

# SYNOPSIS

**goobook** _command_ [_arguments_]

# PARAMETERS

**authenticate**
> 向 Google 进行身份验证并存储 OAuth2 凭据

**query** _QUERY_
> 搜索与查询匹配的联系人

**add**
> 从邮件头（标准输入）添加联系人

**dump_contacts**
> 将所有联系人导出为 XML 格式

**reload**
> 重新从 Google 加载联系人并缓存

# DESCRIPTION

**goobook** 提供对 Google 通讯录的命令行访问，主要设计用于与 mutt 邮件客户端集成。它可以搜索联系人来补全电子邮件地址，也能根据邮件头添加新联系人。

要与 mutt 集成，请在 **.muttrc** 中添加：

```
set query_command="goobook query %s"
```

配置存储在 **~/.goobookrc** 中，包含通过 OAuth2 身份验证流程获得的 Google API 凭据。

# CONFIGURATION

**~/.goobookrc**
> 包含 Google API 凭据、OAuth2 令牌和缓存设置的配置文件。

# CAVEATS

需要 Google API 凭据和 OAuth2 身份验证。Google 的 API 配额可能会限制频繁查询。联系人的更改同步可能需要时间。访问 Google Contacts API 需要正确的 OAuth 授权范围。

# HISTORY

goobook 的诞生是为了打通 mutt 等命令行邮件客户端与 Google 联系人管理之间的隔阂。它为 Google 通讯录提供了一个简单接口，能很好地融入 Unix 文本处理工具和邮件工作流。

# INSTALL

```apk: sudo apk add goobook```

```nix: nix profile install nixpkgs#goobook```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mutt](/man/mutt)(1)
