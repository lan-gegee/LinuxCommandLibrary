# TAGLINE

具备端到端加密的 Matrix IRC 网关

# TLDR

首次**运行服务器**时启用注册功能

```matrirc --allow-register```

以普通模式**运行服务器**（注册完成后）

```matrirc```

**配置**用于存储加密媒体文件的目录

```matrirc --media-dir [path/to/media]```

**设置**用于提供上传媒体文件的 URL 前缀

```matrirc --media-url [https://media.example.com/]```

通过将 IRC 客户端指向 matrirc 端口（默认 6667）并输入注册的 Matrix 密码来**建立连接**。

# SYNOPSIS

**matrirc** [_--allow-register_] [_--media-dir path_] [_--media-url url_]

# PARAMETERS

**--allow-register**
> 允许新的 IRC 客户端在首次连接时绑定 Matrix 账号。昵称/密码绑定成功后，请去掉此选项重启以进入正常运行状态。

**--media-dir** _path_
> 本地目录，供 IRC 客户端下载时解密并存储 Matrix 加密媒体。

**--media-url** _url_
> 替换到消息中的 URL 前缀，使 IRC 客户端收到指向保存在 **--media-dir** 中媒体的可点击链接。

# DESCRIPTION

**matrirc** 是一个小型单二进制文件的 IRC 网关，让标准 IRC 客户端能够连接到 Matrix homeserver。与 **matrix-appservice-irc** 这类服务器端应用服务不同，matrirc 在用户的 IRC 客户端本地运行，并在两种协议之间进行转换。它支持 Matrix 端到端加密（Olm/Megolm）以及跨签名设备验证，因此加密房间依然可以阅读。

首次以 **--allow-register** 启动时，当 IRC 客户端使用选定的昵称和密码连接，服务器会提示输入 Matrix 登录凭据。登录成功后，昵称/密码对便绑定到 Matrix 会话，后续重新连接即可恢复会话，无需再次注册。加密媒体附件可以解密并通过本地目录暴露给 IRC 客户端，该目录由可配置的 URL 前缀提供服务。

该项目用 **Rust** 编写，面向偏好 IRC 客户端体验但同时也参与 Matrix 房间的用户。

# CAVEATS

若干 Matrix 功能尚未实现：话题与图标变更通知、从 IRC 侧加入房间、@提及以及语音/视频通话。媒体清理需手动进行 —— **--media-dir** 中已下载的文件必须由用户自行删除。有时需要带着 **--allow-register** 重启才能添加第二个账号；绑定完成后请去掉该选项。

# CONFIGURATION

状态（会话、加密密钥、房间缓存）持久化保存在 matrirc 的数据目录中。具体路径取决于构建方式，通常位于 **$XDG_DATA_HOME/matrirc** 或 matrirc 的启动目录下。使用任意 IRC 客户端连接时，将其指向 matrirc 绑定的端口（默认 IRC 端口 6667），并输入你注册时使用的密码。

# HISTORY

**matrirc** 由 **Dominique Martinet**（**martinetd**）创建，托管于 **github.com/martinetd/matrirc**。它的开发目的是让长期使用 IRC 的用户无需运营 homeserver 级别的 appservice，就能获得一个轻量的本地运行的 Matrix 桥接。

# INSTALL

```aur: yay -S matrirc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[weechat](/man/weechat)(1), [irssi](/man/irssi)(1)
