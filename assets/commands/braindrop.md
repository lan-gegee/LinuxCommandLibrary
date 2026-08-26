# TAGLINE

Raindrop.io 书签的 TUI 客户端

# TLDR

**启动** Raindrop.io TUI

```braindrop```

**指定 API 令牌**

```braindrop --api-key [YOUR_TOKEN]```

**使用自定义主题**

```braindrop --theme [textual-dark]```

# SYNOPSIS

**braindrop** [_options_]

# DESCRIPTION

**braindrop** 是 **Raindrop.io**（一款流行的云书签管理器）的终端用户界面客户端。它让用户可以直接在终端中浏览、搜索和管理自己的 Raindrop.io 书签收藏。

该 TUI 提供基于键盘的导航，可以遍历收藏夹、跨书签搜索，并在浏览器中打开已保存的链接。它与 Raindrop.io API 通信以同步并显示书签数据。

# CONFIGURATION

需要 **Raindrop.io API 令牌**进行身份验证。令牌通常在首次启动时配置，或通过配置文件设置。

# CAVEATS

需要有有效的 **Raindrop.io** 账户和 API 访问权限。书签变更会同步到云服务。所有操作都需要联网。

# SEE ALSO

[buku](/man/buku)(1), [bmm](/man/bmm)(1)
