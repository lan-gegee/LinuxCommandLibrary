# TAGLINE

面向非容器化应用的调度器和编排器

# TLDR

**启动 process-compose.yaml 中定义的所有进程**

```process-compose```

**使用指定的配置文件启动**

```process-compose -f [path/to/config.yaml]```

**以无 TUI 模式运行并提供 API**

```process-compose --tui=false```

# SYNOPSIS

**process-compose** [_options_] [_command_]

# DESCRIPTION

**process-compose** 是一个简单灵活的调度器和编排器，用于管理非容器化的应用。它的配置语法沿用 docker-compose 风格，使用 YAML。它提供 TUI 和 CLI 模式、进程恢复策略、依赖管理、按进程设置的环境变量、日志缓存、定时进程（cron 和基于间隔）、命名空间支持、进程副本、带令牌身份验证的 REST API 以及主题。

# HISTORY

**process-compose** 由 **F1bonacc1** 创建，使用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#process-compose```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker-compose](/man/docker-compose)(1), [supervisord](/man/supervisord)(1), [mprocs](/man/mprocs)(1)
