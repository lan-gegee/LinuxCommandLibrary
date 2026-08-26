# TAGLINE

带缓存的 HTTP 代理服务器

# TLDR

**启动 squid**

```squid```

**检查配置**

```squid -k parse```

**重新加载配置**

```squid -k reconfigure```

**平滑关机**

```squid -k shutdown```

**显示版本**

```squid -v```

**以前台方式运行**

```squid -N```

**调试模式**

```squid -d [5]```

**清空缓存**

```squid -k rotate && rm -rf [/var/spool/squid/*] && squid -z```

# SYNOPSIS

**squid** [_-k command_] [_-f config_] [_-N_] [_options_]

# PARAMETERS

**-k** _COMMAND_
> 向运行中的 squid 发送命令。

**-f** _FILE_
> 配置文件。

**-N**
> 非守护进程模式。

**-d** _LEVEL_
> 调试级别。

**-z**
> 创建 swap 目录。

**-v**
> 显示版本。

# COMMANDS

**parse** - 检查配置
**reconfigure** - 重新加载配置
**shutdown** - 平滑停止
**interrupt** - 立即停止
**rotate** - 轮转日志

# DESCRIPTION

**squid** 是一个支持 HTTP、HTTPS、FTP 及其他协议的缓存代理服务器。它既可以作为客户端访问互联网的正向代理，也可以作为 Web 服务器的反向代理（加速器），缓存频繁请求的内容以降低带宽消耗并提升响应速度。

服务器使用访问控制列表（ACL）来过滤流量、验证用户身份、限制对特定站点或内容类型的访问，并实施带宽限制。缓存存储可配置内存和磁盘两种后端，并支持通过父级与同级代理构建层级缓存。

配置通过一个功能完备的配置文件管理，其中定义了监听端口、ACL 规则、缓存策略、身份认证方案和日志行为。**-k** 标志可向运行中的实例发送管理命令，执行重新加载配置、轮转日志和平滑关机等操作。

# CONFIGURATION

**/etc/squid/squid.conf**
> 主配置文件，定义监听端口、ACL 规则、缓存策略、认证辅助程序和日志设置。

**/var/spool/squid/**
> 存放缓存 Web 内容的默认磁盘缓存目录。

**/var/log/squid/**
> 日志目录，包含 access.log、cache.log 和 store.log。

# CAVEATS

配置复杂。ACL 的顺序很重要。HTTPS 拦截需要证书。

# HISTORY

**Squid** 源自 **1996 年****科罗拉多大学**的 **Harvest** 项目。它成为部署最广泛的缓存代理。

# INSTALL

```dnf: sudo dnf install squid```

```pacman: sudo pacman -S squid```

```apk: sudo apk add squid```

```zypper: sudo zypper install squid```

```brew: brew install squid```

```nix: nix profile install nixpkgs#squid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nginx](/man/nginx)(1), [apache](/man/apache)(1), [privoxy](/man/privoxy)(1)
