# TAGLINE

终端打字速度游戏

# TLDR

**开始游戏**

```typespeed```

**使用指定词表启动**

```typespeed -w [wordlist]```

**作为服务器启动网络游戏**

```typespeed -n s```

**连接到网络游戏**

```typespeed -n c -o [hostname]```

**以训练模式游玩**

```typespeed -r training```

# SYNOPSIS

**typespeed** [_options_]

# PARAMETERS

**-w** _wordlist_
> 使用指定的词表文件。

**-n** _mode_
> 网络模式：s 表示服务器，c 表示客户端。

**-o** _host_
> 客户端模式下连接到指定主机。

**-r** _rules_
> 游戏规则：default、classic 或 training。

**-h**
> 显示帮助。

**-v**
> 显示版本。

# GAMEPLAY

单词从左向右飞过屏幕。在它们到达右边缘之前正确输入即可消除。漏掉 10 个单词则游戏结束。打字越快得分越高。

# PREVIEW

```
 defend -->
   score -->
 compile ------>
 result ------->
```

# DESCRIPTION

**typespeed** 是一款测试并提升打字速度的终端打字游戏。单词在屏幕上滚动，必须在它们消失前输入完毕。游戏会测量每秒字符数（CPS）、准确率并计算得分。

游戏包含多个词表和三种玩法模式。default 模式随进度提升单词速度，classic 保持恒定速度，training 则允许以固定节奏练习。

网络模式支持通过网络进行双人竞赛，双方玩家同时收到相同的单词。一名玩家作为服务器主持，另一名玩家作为客户端连接。

统计功能追踪总字符数、正确字符数、错误比例和分数。日志会保存以往会话的历史记录，便于追踪长期进步。

# CAVEATS

要求终端尺寸至少为 80x24。网络模式需要系统之间的端口访问权限。词表是每行一个单词的纯文本文件。高分记录保存在本地。

# HISTORY

**typespeed** 的灵感来自 Zorlim 开发的 DOS 打字游戏 ztspeed。它的目标是提供一种有趣的方式来提升 Unix 系统上的打字速度。这款游戏作为 GUI 打字教学软件的终端替代品，在 Linux 社区中广受欢迎。

# INSTALL

```dnf: sudo dnf install typespeed```

```brew: brew install typespeed```

```nix: nix profile install nixpkgs#typespeed```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ttyper](/man/ttyper)(1), [gtypist](/man/gtypist)(1), [wpm](/man/wpm)(1)
