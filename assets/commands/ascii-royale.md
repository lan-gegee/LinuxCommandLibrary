# TAGLINE

终端中的点对点大逃杀游戏

# TLDR

**直接进入**公共竞技场

```ascii-royale play```

**浏览开放对局**并选择加入

```ascii-royale browse```

**离线对战**机器人

```ascii-royale solo --bots [9]```

**创建对局**供他人加入

```ascii-royale host```

凭票据**加入指定**对局

```ascii-royale join [ticket]```

# SYNOPSIS

**ascii-royale** _command_ [_options_]

# PREVIEW

```
 ~~~~~~~~~~~~~
 ~ . @ . o . ~
 ~ . ### . . ~
 ~ x . . . o ~
 ~~~ storm ~~~
```

# DESCRIPTION

**ascii-royale** 是一款完全在终端中运行的大逃杀游戏。最多 16 名战斗者在程序生成的 ASCII 岛屿上厮杀，不断缩小的风暴迫使玩家互相靠近，直到只剩一人存活。空位由机器人补齐，因此单人游玩无需其他玩家。

对局通过 iroh 网络库以点对点方式进行，没有中央游戏服务器，也无需账号：整个游戏只是一个单一的二进制文件。玩家可以直接进入公共竞技场、浏览并加入开放对局、自建对局，或运行无头竞技场服务器。同一款游戏也可以在浏览器中玩。

# COMMANDS

**play**
> 直接进入公共竞技场。

**browse**
> 列出开放对局并选择一个加入。

**join** _ticket_
> 使用票据加入指定对局。

**host**
> 创建一局。接受 **--bots** _N_ 和 **--name** _NAME_。

**solo --bots** _N_
> 离线对抗指定数量的 AI 对手。

**serve**
> 运行无头竞技场服务器。

# PARAMETERS

**--bots** _N_
> 要添加的机器人玩家数量。

**--http-port** _PORT_
> 在给定端口上提供 Web 界面。

**--ticket-file** _PATH_
> 将加入票据写入文件。

**--stats-file** _PATH_
> 将排行榜数据持久化到文件。

# CONTROLS

**w a s d** / **方向键**
> 移动并设定瞄准方向。

**f** / **空格**
> 开火（对排成直线的敌人自动瞄准）。

**e** / **g**
> 拾取物品。

**h** / **m**
> 使用医疗包。

**t**
> 投掷手榴弹。

**M**
> 静音或取消静音。

**q** / **Esc**
> 退出。

# CAVEATS

网络基于 iroh 的点对点连接，因此对局依赖玩家之间的直接连通性。项目使用 Rust 构建，需要较新的工具链从源码安装。

# HISTORY

**ascii-royale** 以 **Rust** 编写，采用 MIT 许可证发布。它以纯文本呈现大逃杀玩法，使用 iroh 实现无服务器的点对点联机，并配有 8 位合成音效。

# SEE ALSO

[ninvaders](/man/ninvaders)(1), [hunt](/man/hunt)(1), [nethack-console](/man/nethack-console)(1)

# RESOURCES

```[Source code](https://github.com/chad/ascii-royale)```

<!-- verified: 2026-06-14 -->
