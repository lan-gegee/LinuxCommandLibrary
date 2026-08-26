# TAGLINE

注重隐私的网络电台终端界面

# TLDR

**启动电台浏览器**

```onda```

**播放选中的电台**

```enter```

**按名称、国家或流派搜索电台**

```/```

**切换选中电台的收藏状态**

```f```

**停止播放**

```s```

**打开设置**

```,```

# SYNOPSIS

**onda**

# PARAMETERS

**/** 
> 打开搜索（默认实时搜索；输入即出结果）。

**f**
> 切换选中电台的收藏状态。

**F**
> 显示收藏列表。

**s**
> 停止播放。

**+** / **-**
> 音量增大 / 减小。

**b**
> 按国家、流派或语言浏览。

**p**
> 显示热门（得票最高）电台。

**r**
> 最近播放（启用历史记录时）。

**a**
> 添加自定义电台。

**,**（逗号）
> 打开设置。

**q**
> 退出。

# DESCRIPTION

**onda** 是一个用于浏览和收听网络电台的终端界面。它受 Radio Garden 启发，直接连接广播方的流媒体 URL，不做录制、代理或转播。播放依赖 PATH 中的 **mpv**。

电台来自公有领域的 Radio Browser 目录以及内置的 CC0 起始列表。你可以按地区浏览、本地或在线搜索、保存收藏并添加自定义电台。热度统计默认为 **never**——除非你主动选择加入，否则不会有任何遥测数据离开你的机器。

需要单独安装 **mpv**。支持 Linux、macOS 和 Windows。

# CONFIGURATION

配置和数据存放在操作系统配置目录下：

> Linux：**~/.config/onda/**
> macOS：**~/Library/Application Support/onda/**
> Windows：**%AppData%\onda\**

**config.toml** 的键包括 **quality**（highest|balanced|lowest）、**tracking**（never|opt-in|opt-out）、**history_enabled**、**theme**、**update_check**、**live_search**、**volume** 和 **normalize**。收藏和自定义电台以 JSON 形式与配置存放在一起。本地电台缓存位于操作系统缓存目录下（例如 Linux 上为 **~/.cache/onda/**）。

# CAVEATS

存在地区限制的流媒体在未解除地理封锁时无法播放。Radio Browser 没有规范的电台 ID，因此重复条目通过启发式方法合并。内置电台数据只是一小份起始集合；完整目录下载需自行选择开启（约 30 MB）。

# SEE ALSO

[mpv](/man/mpv)(1)

# RESOURCES

```[Source code](https://github.com/pedrosousa13/onda)```

<!-- verified: 2026-07-11 -->
