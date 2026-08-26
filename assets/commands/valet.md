# TAGLINE

macOS 上的 Laravel 本地开发环境

# TLDR

**安装 Valet**

```valet install```

**注册当前目录以服务所有站点**

```valet park```

**将当前目录链接为站点**

```valet link [site-name]```

**通过 HTTPS 提供站点**

```valet secure [site-name]```

**通过 ngrok 公开共享站点**

```valet share```

**全局切换 PHP 版本**

```valet use php@[8.2]```

**将站点隔离到特定的 PHP 版本**

```valet isolate php@[7.4]```

# SYNOPSIS

**valet** _command_ [_options_]

# COMMANDS

**install**：安装并配置 Valet（Nginx、DnsMasq）。

**park**：注册目录以通配方式服务所有站点。

**link** _name_：将当前目录链接为命名站点。

**unlink** _name_：移除已链接的站点。

**links**：列出所有已链接的站点。

**secure** _site_：通过 HTTPS 提供站点。

**unsecure** _site_：改回 HTTP。

**share**：通过 ngrok 或 Expose 公开共享站点。

**use** _php_：切换全局 PHP 版本。

**isolate** _php_：将站点固定到特定 PHP 版本。

**unisolate**：移除 PHP 版本隔离。

**php** _args_：代理到站点配置的 PHP。

**composer** _args_：代理到站点配置的 Composer。

**restart**：重启 Nginx 和 DnsMasq 服务。

**stop**：停止 Valet 服务。

**start**：启动 Valet 服务。

**trust**：添加 sudoers 条目以支持免密码命令。

# DESCRIPTION

**valet** 是 Laravel 为 macOS 打造的极简开发环境。它会将 Mac 配置为在后台运行 Nginx，并使用 DnsMasq 将 *.test 域上的所有请求代理到本地站点。

Valet 是完整虚拟机或容器化技术栈的轻量替代方案。它占用极少的资源，同时可以通过 项目名.test 这样的 URL 即时访问站点。park 命令注册整个目录，自动把每个子目录作为独立站点提供服务。

站点可通过自动生成的证书以 HTTPS 提供，能通过隧道服务公开共享，还可以按项目配置不同的 PHP 版本。

# CAVEATS

仅限 macOS。需要 Homebrew 和 PHP。端口 80 必须可用（不能运行 Apache 或其他服务器）。*.test 域默认是硬编码的，但可以修改。

# HISTORY

**Laravel Valet** 由 Taylor Otwell 和 Laravel 团队创建，是 macOS 上零配置的开发环境。对于偏好原生性能的开发者来说，它是 Homestead（基于 Vagrant）之外更简单的选择。Linux 平台存在功能类似的社区分支（Valet Linux）。

# SEE ALSO

[nginx](/man/nginx)(8), [php](/man/php)(1), [composer](/man/composer)(1), [brew](/man/brew)(1)
