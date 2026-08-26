# TAGLINE

Python Web 微框架的命令行界面

# TLDR

**运行开发服务器**

```flask run```

**以调试模式运行**并自动重载

```flask run --debug```

**在指定的主机和端口上运行**

```flask run --host [0.0.0.0] --port [8080]```

**在应用上下文中启动交互式 Python shell**

```flask shell```

**列出应用中的所有路由**

```flask routes```

**初始化数据库**（如果使用 Flask-Migrate）

```flask db init```

**执行数据库迁移**

```flask db upgrade```

**设置应用模块**

```FLASK_APP=[app.py] flask run```

# SYNOPSIS

**flask** [_--app module_] [_--debug_] _command_ [_options_]

# PARAMETERS

**--app** _module_
> 指定 Flask 应用模块（或设置 FLASK_APP 环境变量）。

**--debug** / **--no-debug**
> 启用/禁用带自动重载器和调试器的调试模式。

**run** [_--host host_] [_--port port_]
> 运行开发服务器。

**shell**
> 在应用上下文中打开交互式 Python shell。

**routes** [_--sort endpoint|methods|rule_]
> 显示所有已注册的 URL 规则。

**--version**
> 显示 Flask 版本。

**--help**
> 显示某个命令的帮助。

# RUN OPTIONS

**--host** _address_
> 要绑定的网络接口（默认：127.0.0.1）。

**--port** _port_
> 要监听的端口（默认：5000）。

**--reload** / **--no-reload**
> 启用/禁用代码更改时的自动重载。

**--debugger** / **--no-debugger**
> 启用/禁用交互式调试器。

**--cert** _path_
> 用于 HTTPS 的 SSL 证书文件。

**--key** _path_
> 用于 HTTPS 的 SSL 密钥文件。

# DESCRIPTION

**flask** 是 Flask 的命令行界面，Flask 是一个流行的 Python Web 微框架。它提供用于运行开发服务器、打开应用 shell 以及执行由 Flask 扩展或应用定义的自定义命令。

CLI 通过 **FLASK_APP** 环境变量或 **--app** 选项来发现 Flask 应用。它支持从模块加载、模块:工厂 模式或工厂函数。

开发服务器包含在代码更改时自动重启的自动重载器，以及在出现错误时显示在浏览器中的交互式调试器。这些功能只应在开发环境中使用，绝不能在生产环境中使用。

Flask 扩展通常会添加自己的 CLI 命令。Flask-Migrate 添加了用于数据库迁移的 **flask db** 命令，Flask-Admin 可能会添加管理命令，等等。应用程序可以使用 **@app.cli.command()** 装饰器定义自定义命令。

shell 命令提供一个已预加载应用及其上下文的交互式 Python 会话，便于测试和调试。

# CAVEATS

开发服务器不适合生产环境使用。调试模式会暴露敏感信息，在生产环境中绝不应当启用。该服务器默认是单线程的。部署时请使用 Gunicorn 或 uWSGI 等生产级 WSGI 服务器。

# HISTORY

**Flask** 由 Armin Ronacher 于 **2010 年**创建，最初是一个愚人节玩笑却意外走红。CLI 在 Flask 0.11（**2016 年**）中加入，取代了旧的 flask-script 扩展和服务器启动方式。Flask 已成为使用最广泛的 Python Web 框架之一。

# INSTALL

```apk: sudo apk add py3-flask```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gunicorn](/man/gunicorn)(1), [uvicorn](/man/uvicorn)(1), [python](/man/python)(1), [pip](/man/pip)(1), [django-admin](/man/django-admin)(1)

# RESOURCES

```[Documentation](https://flask.palletsprojects.com/)```

```[Source code](https://github.com/pallets/flask)```

<!-- verified: 2026-07-15 -->
