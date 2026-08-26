# TAGLINE

无需服务器的命令行 Fediverse 客户端

# TLDR

**查看用户资料**

```servitor open [@user@instance.org]```

**打开 fediverse 链接**

```servitor open [https://instance.org/post/123]```

**查看命名 feed**

```servitor feed [my-feed]```

# SYNOPSIS

**servitor** _command_ [_arguments_]

# DESCRIPTION

**servitor** 是一款基于终端的 ActivityPub/Fediverse 客户端，不需要运行服务器。它直接从源站拉取帖子，避免了解除联合（defederation）的问题，并在本地存储订阅，因此你可以关注他人而无需发送关注请求。它支持 Mastodon、Lemmy、PeerTube 以及其他 fediverse 平台。

# HISTORY

**servitor** 由 **Benton Edmondson**（BentonEdmondson）创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S servitor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[toot](/man/toot)(1), [tuisky](/man/tuisky)(1)
