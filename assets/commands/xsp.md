# TAGLINE

Mono ASP.NET 开发用 Web 服务器

# TLDR

**启动服务器**

```xsp```

**指定端口**

```xsp --port [8080]```

**设置根目录**

```xsp --root [/var/www]```

**启用 HTTPS**

```xsp --https --p12file [server.p12] --pkpwd [password]```

**运行 ASP.NET 4**

```xsp4```

**绑定到地址**

```xsp --address [0.0.0.0]```

# SYNOPSIS

**xsp** [_--port port_] [_--root path_] [_--address ip_] [_--https_] [_options_]

# PARAMETERS

**--port** _PORT_
> 监听端口（默认 8080）。

**--root** _PATH_
> 应用程序根目录。

**--address** _IP_
> 绑定地址。

**--https**
> 启用 HTTPS。

**--p12file** _FILE_
> PKCS#12 证书文件。

**--pkpwd** _PASSWORD_
> 证书密码。

**--nonstop**
> 不因按下 ENTER 而停止。

# DESCRIPTION

**xsp** 是 Mono 项目附带的一个轻量级独立 Web 服务器，用于在 Linux 和其他类 Unix 系统上托管 ASP.NET 应用程序。它是一个开发和测试服务器，提供了一种快速运行 ASP.NET WebForms 和 MVC 应用程序的方式，无需完整配置 Web 服务器。

该服务器通过 PKCS#12 证书文件支持 HTTPS，并可绑定到特定的地址和端口。生产部署时应以 Apache 后端的 mod_mono 或类似的反向代理配置替代 xsp，以获得更好的性能和安全性。

# CAVEATS

开发用服务器。需要 Mono。生产环境请配合 mod_mono 使用。

# HISTORY

**xsp** 是 **Mono** 项目的一部分，为 Linux 上的测试和开发提供独立的 ASP.NET Web 服务器。

# INSTALL

```dnf: sudo dnf install xsp```

```zypper: sudo zypper install xsp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mono](/man/mono)(1), [mcs](/man/mcs)(1), [apache2](/man/apache2)(1)
