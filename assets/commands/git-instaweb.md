# TAGLINE

通过网页界面浏览仓库

# TLDR

**启动网页界面**

```git instaweb```

**使用指定的 HTTP 守护进程启动**

```git instaweb --httpd=[lighttpd]```

**在指定端口启动**

```git instaweb --port=[8080]```

**仅绑定到 localhost 启动**

```git instaweb --local```

**停止 Web 服务器**

```git instaweb --stop```

**重启 Web 服务器**

```git instaweb --restart```

# SYNOPSIS

**git** **instaweb** [_options_]

# PARAMETERS

**-d**, **--httpd** _daemon_
> 要使用的 HTTP 守护进程（lighttpd、apache2、mongoose、plackup、python、webrick）。默认：lighttpd。

**-p**, **--port** _port_
> 要绑定的端口号。默认：1234。

**-b**, **--browser** _browser_
> 用于查看的 Web 浏览器。

**-m**, **--module-path** _path_
> 模块路径（仅 Apache 需要）。默认：/usr/lib/apache2/modules。

**--start**
> 启动 httpd 实例后退出。

**--stop**
> 停止 httpd 实例后退出。

**--restart**
> 重启 httpd 实例后退出。

**-l**, **--local**
> 仅绑定到 localhost（127.0.0.1）。

# DESCRIPTION

**git instaweb** 通过启动临时本地 Web 服务器，让你立即在 gitweb 中浏览当前工作仓库。它提供了一种无需搭建永久服务器即可通过网页界面快速查看仓库历史、分支和文件的方式。

该命令在端口 1234 上启动一个 Web 服务器（默认 lighttpd，也可以是 apache2、mongoose、plackup、python、webrick），并在默认浏览器中打开仓库。界面支持查看提交、浏览文件、blame 注记和 diff 查看。用完后，使用 `--stop` 关闭服务器。

它特别适用于向他人演示仓库历史，或者你偏好图形化视图但不想使用完整的 GUI 应用程序时。该网页界面是只读的，不需要网络访问。

# INSTALL

```dnf: sudo dnf install git-instaweb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gitweb](/man/gitweb)(1), [git-daemon](/man/git-daemon)(1)
