# TAGLINE

AdGuard Home 的终端仪表盘

# TLDR

使用连接信息**启动仪表盘**

```ADGUARD_IP="192.168.1.1" ADGUARD_PORT="3000" ADGUARD_USERNAME="admin" ADGUARD_PASSWORD="pass" adguardian```

**通过命令行标志启动**

```adguardian --adguard-ip [192.168.1.1] --adguard-port [3000] --adguard-username [admin] --adguard-password [pass]```

**通过 Docker 运行**

```docker run -e ADGUARD_IP=192.168.1.1 -e ADGUARD_PORT=3000 -e ADGUARD_USERNAME=admin -e ADGUARD_PASSWORD=pass -it lissy93/adguardian```

# SYNOPSIS

**adguardian** [_options_]

# PARAMETERS

**--adguard-ip** _address_
> AdGuard Home 实例的 IP 地址

**--adguard-port** _port_
> AdGuard Home 实例的端口号

**--adguard-username** _user_
> 认证用户名

**--adguard-password** _pass_
> 认证密码

# DESCRIPTION

**adguardian-term** 是一个基于终端的 AdGuard Home 实例实时流量监控与统计仪表盘。它在交互式 TUI 中显示 DNS 查询活动、拦截/放行统计、生效中的过滤列表以及查询量最高的域名。它以 Rust 编写并使用 ratatui 构建界面，通过与 AdGuard Home API 通信，成为 Web UI 的轻量替代品。

仪表盘会自动刷新，显示被放行、过滤或拦截的查询，以及历史趋势和域名分析数据。

# CONFIGURATION

可以通过环境变量或命令行标志进行配置。支持的环境变量：**ADGUARD_IP**、**ADGUARD_PORT**、**ADGUARD_USERNAME**、**ADGUARD_PASSWORD**、**ADGUARD_PROTOCOL**（默认 http）以及 **ADGUARD_UPDATE_INTERVAL**（默认 2 秒）。

# CAVEATS

需要一个正在运行且可访问 API 的 AdGuard Home 实例。凭据必须通过环境变量或命令行标志提供。该工具只与所配置的 AdGuard Home 实例通信，不会发出其他外部请求。

# HISTORY

**adguardian-term** 由 **Alicia Sykes**（Lissy93）创建，以 MIT 许可证开源。它最初用 Go 编写，后来用 Rust 重写。该项目受 Pi-hole 的同类仪表盘 **PADD** 启发。

# SEE ALSO

[pihole](/man/pihole)(1), [htop](/man/htop)(1)
