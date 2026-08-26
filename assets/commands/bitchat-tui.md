# TAGLINE

终端中基于蓝牙 LE 的点对点加密聊天

# TLDR

**启动 bitchat-tui** 并连接附近节点

```bitchat-tui```

**设置昵称**（启动后）

```/name [alice]```

**加入频道**（可选密码）

```/j #[channel] [password]```

**向用户发送私信**

```/dm [bob] [message]```

**列出所有在线用户**

```/online```

**快速回复最后一条私信**

```/reply```

**返回公共聊天室**

```/public```

**离开当前频道**

```/leave```

**屏蔽一个用户**

```/block @[username]```

**显示所有可用命令**

```/help```

# SYNOPSIS

**bitchat-tui**

# DESCRIPTION

**bitchat-tui** 是 BitChat 的终端用户界面客户端。BitChat 是一种基于蓝牙低功耗（Bluetooth Low Energy）运行的安全点对点消息协议，可在没有互联网连接或中央服务器的情况下实现离线加密通信。该应用通过蓝牙 LE 自动扫描附近的节点，并建立直接的网状连接。

所有消息均经端到端加密：使用 **X25519** 椭圆曲线 Diffie-Hellman 进行密钥交换，使用 **AES-256-GCM** 进行消息加密与完整性认证，使用 **Ed25519** 数字签名验证消息真实性。频道密码采用 100,000 轮的 **PBKDF2-SHA256** 派生。大消息会自动分片，并在蓝牙 LE 有限的包大小限制下重组。

该 TUI 基于 **ratatui** 和 **crossterm** 构建了侧边栏式界面，将对话组织为公共聊天、命名频道、私信和被屏蔽用户列表。未读消息指示器和分区计数器帮助跟踪各频道的动态。

bitchat-tui 使用 Rust 编写，可运行于 Linux、macOS 和 Windows。

# COMMANDS

**/help**
> 列出所有可用命令。

**/name** _nick_
> 更改当前会话的昵称。

**/status**
> 显示连接信息与当前状态。

**/clear**
> 清空当前会话视图中的所有消息。

**/exit**
> 退出应用。

**/public**
> 返回 **#public** 聊天室。

**/dm** _name_ [_message_]
> 与某用户开始私信，可选择附带初始消息。

**/reply**
> 快速回复最后一个给你发私信的人。

**/j** **#**_channel_ [_password_]
> 加入频道，可选密码。

**/leave**
> 离开当前频道并返回 **#public**。

**/pass** _password_
> 设置频道密码（仅频道所有者）。

**/transfer** **@**_user_
> 转让频道所有权（仅频道所有者）。

**/channels**
> 列出你已发现或已加入的所有频道。

**/online**, **/w**
> 列出网络中可见的用户。

**/block** **@**_user_
> 屏蔽特定用户的消息。

**/unblock** **@**_user_
> 取消屏蔽之前被屏蔽的用户。

# CONFIGURATION

状态持久化保存在 **~/.bitchat/state.json** 中，内容包括：

**Identity** -- Ed25519 签名密钥与 X25519 加密密钥，首次启动时生成
**Nickname** -- 用户选择的显示名称
**Channels** -- 已加入的频道、所有权信息以及加密的频道密码
**Blocked peers** -- 被屏蔽用户的 SHA256 指纹

频道密码在存储时使用 AES-256-GCM 加密，密钥由身份密钥派生。

# CAVEATS

该应用不接受任何命令行标志或选项；所有配置均在启动后通过 TUI 命令交互完成。需要支持蓝牙 LE 的适配器。在 Linux 上，访问蓝牙需要 **dbus** 系统。在 Windows 上从源码构建需要安装带有"使用 C++ 的桌面开发"工作负载的 Microsoft Visual C++ Build Tools。通信范围受蓝牙 LE 信号覆盖限制，通常约 10-100 米，视硬件而定。

# INSTALL

```aur: yay -S bitchat-tui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bluetuith](/man/bluetuith)(1), [bluetoothctl](/man/bluetoothctl)(1), [hcitool](/man/hcitool)(1)
