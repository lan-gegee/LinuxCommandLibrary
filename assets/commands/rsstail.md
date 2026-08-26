# TAGLINE

像 tail 监视文件一样监视 RSS 订阅源

# TLDR

**跟踪 RSS 订阅源**

```rsstail -u [https://example.com/feed.rss]```

**显示时间戳**

```rsstail -u [url] -p```

**包含描述**

```rsstail -u [url] -d```

**同时跟踪多个订阅源**

```rsstail -u [url1] -u [url2]```

**自定义检查间隔**

```rsstail -u [url] -i [300]```

**显示链接**

```rsstail -u [url] -l```

# SYNOPSIS

**rsstail** [_-u url_] [_-i seconds_] [_-d_] [_-l_] [_options_]

# PARAMETERS

**-u** _URL_
> 订阅源 URL。

**-i** _SEC_
> 检查间隔。

**-d**
> 显示描述。

**-l**
> 显示链接。

**-p**
> 显示时间戳。

**-n** _NUM_
> 初始显示的条目数。

**-N**
> 不显示初始条目。

**-1**
> 只检查一次然后退出。

# DESCRIPTION

**rsstail** 从命令行监视 RSS 订阅源，其作用就像网页订阅源版的 **tail -f**。它会周期性地检查指定的订阅源 URL，并在新条目出现时立即打印出来，为无需完整阅读器就能跟踪更新提供了简单途径。

通过重复使用 **-u** 标志可以同时监视多个订阅源，检查间隔可通过 **-i** 配置（单位为秒）。输出可以包含标题、描述（**-d**）、链接（**-l**）和时间戳（**-p**），默认则只显示标题。**-1** 标志会执行一次检查便退出，适合在脚本中对订阅源做轮询。

# CAVEATS

依赖网络。订阅源格式会有影响。两次检查之间可能遗漏部分条目。

# HISTORY

**rsstail** 的设计目标是提供一个类似 tail 的界面，用于在命令行监视 RSS 订阅源的更新。

# INSTALL

```apt: sudo apt install rsstail```

```zypper: sudo zypper install rsstail```

```nix: nix profile install nixpkgs#rsstail```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [tail](/man/tail)(1), [newsboat](/man/newsboat)(1)
