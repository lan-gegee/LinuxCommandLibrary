# TAGLINE

为 hledger 提供 Web 界面

# TLDR

**启动 Web 界面**

```hledger-web```

**指定端口**

```hledger-web --port [5001]```

**打开指定日志**

```hledger-web -f [ledger.journal]```

**对外提供服务**

```hledger-web --serve --host [0.0.0.0]```

**只读模式**

```hledger-web --capabilities=view```

**允许包括编辑和删除在内的完整访问**

```hledger-web --capabilities=view,add,manage```

# SYNOPSIS

**hledger-web** [_options_]

# PARAMETERS

**-f** _FILE_
> 日志文件。

**--port** _PORT_
> 服务器端口（默认 5000）。

**--host** _HOST_
> 监听地址。

**--serve**
> 以服务方式运行，不自动打开浏览器。

**--serve-api**
> 只提供 JSON API，不提供 Web UI。

**--capabilities** _CAPS_
> 允许的操作：view、add、manage（默认：view,add）。

**--cors** _ORIGIN_
> 允许来自指定来源的跨域请求。

**--base-url** _URL_
> 链接使用的基础 URL（在反向代理后很有用）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hledger-web** 为 hledger 提供 Web 界面。它提供基于浏览器的方式查看报表、添加交易和管理日志条目。

该界面包含账户账簿、余额报表和交易录入表单。它可以在本地运行，也可以在网络中提供服务。默认监听 127.0.0.1 的 5000 端口并自动打开浏览器。

# CAVEATS

若没有反向代理和适当的身份验证，不建议直接暴露到公共互联网。内置的访问控制仅限于 **--capabilities** 标志。本命令属于 hledger 套件。

# HISTORY

hledger-web 作为 **hledger** 的 Web 界面而开发，旨在提供基于浏览器的纯文本记账体验。

# INSTALL

```dnf: sudo dnf install hledger-web```

```pacman: sudo pacman -S hledger-web```

```apk: sudo apk add hledger-web```

```nix: nix profile install nixpkgs#hledger-web```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hledger](/man/hledger)(1), [hledger-ui](/man/hledger-ui)(1), [ledger](/man/ledger)(1)
