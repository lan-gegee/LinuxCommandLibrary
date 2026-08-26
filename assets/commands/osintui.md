# TAGLINE

面向 Shodan、Censys 和 VirusTotal 的开源情报 TUI

# TLDR

**启动 OSINT 界面**

```osintui```

# SYNOPSIS

**osintui** [_options_]

# DESCRIPTION

**osintui** 是一个终端用户界面，用于查询 **Shodan**、**Censys** 和 **VirusTotal** 等开源情报服务。它以可导航的 TUI 形式展示搜索结果，让你无需离开终端即可浏览和分析 OSINT 数据。

API 令牌配置于 **~/.osintui/config/config.toml**，该文件会在首次运行时自动创建。

# CONFIGURATION

**~/.osintui/config/config.toml**
> 包含各服务 API 令牌的 TOML 配置文件。

# CAVEATS

需要为你要使用的每个服务准备有效的 API 密钥。免费 API 层级有速率限制。

# HISTORY

**osintui** 由 **wssheldon** 创建，使用 **Rust** 编写。其架构仿照 spotify-tui 设计。

# SEE ALSO

[nmap](/man/nmap)(1), [theHarvester](/man/theHarvester)(1)
