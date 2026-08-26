# TAGLINE

Docker 容器的终端用户界面

# TLDR

**启动容器管理 TUI**

```sen```

**在 Docker 容器中运行 sen**

```docker run -v /var/run/docker.sock:/run/docker.sock -ti -e TERM tomastomecek/sen```

# SYNOPSIS

**sen** [_options_]

# DESCRIPTION

**sen** 是一款用于管理 Docker 容器和镜像的交互式 TUI。你可以启动、停止、重启、强杀和删除容器，查看容器和镜像详情，实时查看日志流，浏览镜像层树，以及监控磁盘使用情况。它提供类 Vim 的快捷键绑定和实时的 Docker 事件更新。还通过 Docker 兼容 API 支持 Podman v2.0+。

# CAVEATS

该项目处于维护模式。作者仅提供缺陷修复；新功能需通过社区拉取请求贡献。

# HISTORY

**sen** 由 **Tomas Tomecek**（TomasTomecek）创建，使用 **Python** 编写。

# INSTALL

```dnf: sudo dnf install sen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lazydocker](/man/lazydocker)(1), [ctop](/man/ctop)(1), [oxker](/man/oxker)(1)
