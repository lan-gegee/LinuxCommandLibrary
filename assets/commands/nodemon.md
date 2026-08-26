# TAGLINE

自动重启 Node.js 应用

# TLDR

**监视并重启 Node 应用**

```nodemon [app.js]```

**监视特定扩展名**

```nodemon -e [js,json] [app.js]```

**监视特定目录**

```nodemon --watch [src/] [app.js]```

**忽略文件**

```nodemon --ignore [test/] [app.js]```

**用其他运行时执行**

```nodemon --exec [ts-node] [app.ts]```

**延迟重启**

```nodemon --delay [2] [app.js]```

**使用配置文件**

```nodemon --config [nodemon.json]```

# SYNOPSIS

**nodemon** [_options_] [_script_] [_args_]

# PARAMETERS

_SCRIPT_
> 要运行的脚本。

**-e** _EXT_
> 要监视的文件扩展名。

**--watch** _DIR_
> 要监视的目录。

**--ignore** _PATTERN_
> 要忽略的模式。

**--exec** _CMD_
> 执行命令。

**--delay** _SECS_
> 重启延迟。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nodemon** 自动重启 Node.js 应用。监视文件变化。

该工具辅助开发。保存时自动重启，无需手动干预。

# CAVEATS

属于开发工具。不适合生产环境。会监视文件系统。

# HISTORY

nodemon 由 **Remy Sharp** 创建，旨在改进 Node.js 开发工作流。

# INSTALL

```nix: nix profile install nixpkgs#nodemon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [pm2](/man/pm2)(1), [forever](/man/forever)(1)
