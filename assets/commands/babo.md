# TAGLINE

运行由 Claude Code 编译的纯自然语言 `.babo` 脚本

# TLDR

**运行**一个 Babo 脚本（首次使用时构建，之后使用缓存）

```babo hello.babo```

编辑源描述后**强制重新构建**

```babo build hello.babo```

**检查**缓存构建是否仍然有效

```babo check hello.babo```

**显示**某个脚本的缓存元数据

```babo info hello.babo```

**删除**所有缓存的构建

```babo clean```

# SYNOPSIS

**babo** [_run_] _file.babo_ [_args_...]

**babo** _check_|_build_|_info_|_clean_ _file.babo_

# DESCRIPTION

**babo** 是一个 Python CLI，它将 `.babo` 文件——简短的自然语言程序描述——转换为可运行的 Python 程序。首次运行时，它会将描述发送给 **Claude Code**（`claude -p`），由后者生成入口点、可选的 `requirements.txt` 以及位于源文件旁 `.baboc/<name>.baboc/` 目录下的隔离虚拟环境（设计理念类似 Python 的 `__pycache__`）。

当 `.babo` 文件比其缓存目录更旧时，后续运行会跳过构建。脚本路径之后的参数会被转发给生成的程序。添加 shebang `#!/usr/bin/env babo` 后，只要 **babo** 位于 **PATH** 中，`.babo` 文件即可直接执行。

Babo 脚本可以通过生成的 `runtime.call_babo()` 辅助函数调用其他 `.babo` 模块，每个模块保留自己的虚拟环境，以避免依赖冲突。

# PARAMETERS

**run**

> 显式运行（当第一个参数是 `.babo` 文件时的默认行为）。

**build**

> 强制从 `.babo` 源文件重新生成，忽略新鲜缓存。

**check**

> 打印缓存是 **FRESH** 还是 **STALE**。

**info**

> 显示构建元数据（路径、时间戳、软件包列表）。

**clean**

> 删除当前目录树下所有 `.baboc/` 缓存目录。

# CAVEATS

需要 **Python** 3.10+、已安装并通过认证的 **claude** CLI，以及构建期间的网络访问。构建无法离线进行。该工具尚属实验性质，依赖 Claude Code API 的可用性。

# CONFIGURATION

没有全局配置文件。每个 `.babo` 文件拥有一个 `.baboc/<stem>.baboc/` 缓存目录，其中包含 `venv/`、`requirements.txt`、`metadata.json` 以及生成的 `babo` 可执行入口点。

# SEE ALSO

[claude](/man/claude)(1), [python3](/man/python3)(1), [pip](/man/pip)(1)
