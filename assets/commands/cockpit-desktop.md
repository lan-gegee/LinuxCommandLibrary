# TAGLINE

安全访问 Cockpit 页面的桌面入口

# TLDR

**打开**一个 Cockpit 页面

```cockpit-desktop [url] [SSH_host]```

打开 **storage** 页面

```cockpit-desktop /cockpit/@localhost/storage/index.html```

# SYNOPSIS

**cockpit-desktop** [_url_] [_ssh_host_]

# DESCRIPTION

**cockpit-desktop** 让你可以在本地桌面会话内安全访问 Cockpit 服务器管理页面，而无需暴露任何网络端口。它在一个隔离的网络命名空间中启动 cockpit-ws 和一个网页浏览器，并在用户会话中运行 cockpit-bridge。

网络命名空间隔离确保 Cockpit Web 服务只能被本地启动的浏览器访问，从而消除了监听网络套接字带来的安全暴露面。这对于不需要完整 Cockpit 网络服务的单用户工作站非常理想。

可选的 SSH 主机参数允许通过本地桌面界面管理远程机器，SSH 连接将充当传输层，取代直接的网络服务。

# PARAMETERS

_url_
> 要打开的 Cockpit 页面 URL

_ssh_host_
> 用于远程连接的可选 SSH 主机

# CAVEATS

Cockpit 套件的组成部分。需要图形桌面环境。使用网络命名空间实现隔离，这需要相应的内核支持。

# SEE ALSO

[cockpit-ws](/man/cockpit-ws)(8), [cockpit-bridge](/man/cockpit-bridge)(1)

# RESOURCES

```[Source code](https://github.com/cockpit-project/cockpit)```

```[Documentation](https://cockpit-project.org/guide/latest/)```

<!-- verified: 2026-06-22 -->
