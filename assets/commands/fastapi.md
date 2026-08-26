# TAGLINE

现代 Python Web 框架 CLI

# TLDR

**运行开发服务器**

```fastapi dev [main.py]```

**指定主机和端口运行**

```fastapi dev [main.py] --host [0.0.0.0] --port [8080]```

**运行生产服务器**

```fastapi run [main.py]```

**禁用自动重载运行**

```fastapi dev [main.py] --no-reload```

**指定应用位置**

```fastapi dev [main.py:app]```

# SYNOPSIS

**fastapi** _command_ [_options_] _path_

# COMMANDS

**dev** _path_
> 启动带自动重载的开发服务器。

**run** _path_
> 启动生产服务器。

# PARAMETERS

**--host** _address_
> 绑定地址。默认：127.0.0.1（dev）、0.0.0.0（run）。

**--port** _port_
> 服务器端口。默认：8000。

**--reload**
> 启用自动重载（dev 默认）。

**--no-reload**
> 禁用自动重载。

**--workers** _count_
> 工作进程数量。

**--root-path** _path_
> 用于代理部署的 ASGI 根路径。

**--app** _name_
> 应用变量名。默认：app。

**--reload-dir** _path_
> 监视文件变更的目录（dev 模式）。

**--proxy-headers**
> 信任 X-Forwarded 头。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fastapi** 是 FastAPI 的 CLI。FastAPI 是一个用于构建 API 的现代 Python Web 框架。它封装了 Uvicorn ASGI 服务器，便于开发和部署。

**fastapi dev** 启动带自动重载的开发服务器——代码变更会触发自动重启。本地开发时可使用 **--host 0.0.0.0** 以允许外部访问。

**fastapi run** 启动面向生产的服务器，不启用自动重载并绑定所有接口。实际生产环境建议直接使用 Uvicorn 或 Gunicorn，以获得更多配置选项。

路径参数指向包含 FastAPI 实例的 Python 文件。可使用 **path:variable** 语法指定非默认的应用变量名。

FastAPI 会根据路由定义和类型注解，在 **/docs**（Swagger UI）和 **/redoc** 端点自动生成 API 文档。

# CAVEATS

该 CLI 只是便捷封装；生产部署通常直接使用 Uvicorn/Gunicorn 以获得更多控制权。自动重载可能遗漏部分文件变更。调试模式会暴露详细的错误页面。

# HISTORY

FastAPI 由 **Sebastián Ramírez** 创建，于 **2018 年 12 月**首次发布。它构建在 Starlette 和 Pydantic 之上，强调利用类型注解进行校验、序列化和文档生成。该框架迅速成为最受欢迎的 Python Web 框架之一。**fastapi** CLI 是后来加入的，用于简化开发体验。微软、Netflix、Uber 等众多公司都在生产环境中使用 FastAPI。

# INSTALL

```apk: sudo apk add py3-fastapi```

```brew: brew install fastapi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uvicorn](/man/uvicorn)(1), [gunicorn](/man/gunicorn)(1), [flask](/man/flask)(1), [django-admin](/man/django-admin)(1)
