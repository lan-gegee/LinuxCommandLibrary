# TAGLINE

Symfony PHP 变量转储接收服务器

# TLDR

**在默认地址启动服务器**

```var-dump-server```

**在自定义主机和端口启动**

```var-dump-server --host=[127.0.0.1:9912]```

**以 HTML 格式将转储输出到文件**

```var-dump-server --format=html > [dump.html]```

# SYNOPSIS

**var-dump-server** [_--host address_] [_--format fmt_] [_options_]

# PARAMETERS

**--host** _ADDR_
> 绑定地址和端口（默认：127.0.0.1:9912，或 VAR_DUMPER_SERVER 环境变量）。

**--format** _FMT_
> 输出格式（cli 或 html）。

**--help**
> 显示帮助。

# DESCRIPTION

**var-dump-server** 启动一个服务器，用于收集并显示来自使用 Symfony VarDumper 组件的 PHP 应用的变量转储。应用不再把变量直接输出到浏览器或控制台，而是发送到这个集中式服务器进行结构化显示。

这种方式让调试输出与应用响应分离，对调试 API 端点、AJAX 请求和命令行脚本尤其有用。服务器以语法高亮和可折叠结构呈现转储内容，比内联的 var_dump 输出提供更清爽的调试体验。

# CAVEATS

仅限 Symfony/PHP 环境。需要 VarDumper。属于开发工具。

# HISTORY

**var-dump-server** 是 **Symfony VarDumper** 组件的一部分，用于接收和显示来自 PHP 应用的变量转储。

# SEE ALSO

[php](/man/php)(1), [symfony](/man/symfony)(1)
