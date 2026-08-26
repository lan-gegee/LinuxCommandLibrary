# TAGLINE

基于 SSH 的聊天服务器，用你现有的 SSH 客户端即可加入

# TLDR

**连接**到公共 Devzat 服务器

```ssh [devzat.hackclub.com]```

**选择显示名**——把它作为 SSH 用户名传入即可

```ssh [nickname]@[devzat.hackclub.com]```

**通过 443 端口连接**（在受限防火墙后很有用）

```ssh [devzat.hackclub.com] -p 443```

**运行自己的 Devzat 服务器**（从源码构建的二进制）

```devzat```

**在自定义端口上运行服务器**

```devzat --port [4242]```

# SYNOPSIS

**ssh** [_user_@]_devzat-host_ [**-p** _port_]

**devzat** [**--port** _N_] [**--admin** _key_] [_options_]   _(server-side)_

# DESCRIPTION

**Devzat** 是一个定制的 SSH 服务器，它把连接进来的客户端送入实时聊天室，而不是提供 shell。由于使用的是标准 SSH 协议，**无需安装任何客户端**——任何带有 SSH 客户端的设备（Linux、macOS、Windows，甚至移动端 SSH 应用）都能加入。

聊天中显示的名字就是 SSH 握手时提供的用户名（**user@host**）；换个名字重新连接，或使用房间内的 **/nick** 命令即可更改。服务器通过 SSH 公钥识别用户，因此同一把密钥在多次重连中始终对应同一个身份。

命令行中提到的 **devzat** 二进制是**服务器端**程序；普通用户几乎不需要运行它。自托管者用它对外提供自己的聊天实例。

# IN-ROOM COMMANDS

**/users**
> 列出当前房间里的用户。

**/dm** _user_ _message_（或 **/msg**）
> 向其他用户发送私信。

**/nick** _name_
> 更改你的显示名。

**/rooms**
> 列出可用的聊天室。

**/join** _room_
> 切换到另一个房间（不存在时自动创建）。

**/help**
> 显示所有可用的斜杠命令。

**/exit**
> 离开聊天（Ctrl+C 也可以）。

# CAVEATS

多数包管理器中的 **devzat** 软件包安装的是**服务器端**而非客户端。想聊天直接用 **ssh** 即可——某些地方记载的"客户端 CLI"用法从未存在过。服务器运营者能以明文看到所有消息（SSH 加密只覆盖到服务器这一跳）；不要在聊天中分享机密信息。

# HISTORY

**Devzat** 由 **Arjun Salyan / Ishan Goel (quackduck)** 创建，让开发者借助他们本就信任的 SSH 基础设施聊天。旗舰公共实例运行于 **devzat.hackclub.com**，由 Hack Club 赞助。

# SEE ALSO

[ssh](/man/ssh)(1), [weechat](/man/weechat)(1), [irssi](/man/irssi)(1)
