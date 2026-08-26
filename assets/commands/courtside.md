# TAGLINE

NBA 比赛、比分和排名的终端界面

# TLDR

**启动** NBA 记分牌 TUI

```courtside```

从源码**安装**

```git clone https://github.com/NolanFogarty/courtside.git && cd courtside && go build -o courtside```

用 Go **安装**

```go install github.com/NolanFogarty/courtside@latest```

# SYNOPSIS

**courtside**

# DESCRIPTION

**courtside** 是一个以键盘驱动的终端应用，用于关注 NBA 比赛。它通过 **nba-sdk** 库从 NBA 的公开 JSON 端点获取实时和历史数据，因此无需 API 密钥或账户。

启动时，应用会打开今日比赛的页面。你可以浏览赛程、打开某场比赛查看技术统计和逐回合详情、跳转到任意日期、过滤列表以及查看联盟排名。进行中的比赛大约每 15 秒自动刷新。

所有导航都通过键盘完成。界面包含三个主要视图：比赛列表、比赛详情和联盟排名。

# GAME LIST KEYS

**↑**/**k**, **↓**/**j**
> 在比赛之间移动

**Enter**
> 打开选中的比赛

**←**/**h**, **→**/**l**
> 前一天或后一天

**d**
> 跳转到指定日期

**s**
> 打开联盟排名

**/**
> 过滤比赛

**q**
> 退出

# GAME DETAIL KEYS

**↑**/**k**, **↓**/**j**
> 滚动逐回合记录

**o**
> 切换展开的统计数据

**q**, **Esc**
> 返回比赛列表

# CAVEATS

NBA 的这些端点是非官方且未公开文档的。它们可能随时变更或施加速率限制。

由于数据来源公开但非官方，其可用性和字段准确性无法保证用于生产环境。

# SEE ALSO

[go](/man/go)(1)
