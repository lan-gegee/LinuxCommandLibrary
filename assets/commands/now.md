# TAGLINE

最早的 Vercel CLI

# TLDR

**部署项目**

```now```

**部署并设置别名**

```now --alias [myapp]```

**部署到生产环境**

```now --prod```

**列出部署**

```now ls```

**移除部署**

```now rm [deployment-url]```

**查看日志**

```now logs [deployment-url]```

# SYNOPSIS

**now** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> Now CLI 命令。

**--alias** _NAME_
> 设置部署别名。

**--prod**
> 生产环境部署。

**ls**
> 列出部署。

**rm** _URL_
> 移除部署。

**logs** _URL_
> 查看日志。

**--help**
> 显示帮助信息。

# DESCRIPTION

**now** 是最早的 Vercel CLI，用于将应用部署到 Vercel 平台。

该工具已更名为 vercel，旧命令仍然可用。

# CAVEATS

该名称已被弃用，请改用 vercel。需要 Vercel 账户。

# HISTORY

now 是 **Vercel CLI** 的原始名称，后来公司从 ZEIT 更名而随之改名。

# INSTALL

```aur: yay -S now```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vercel](/man/vercel)(1), [netlify](/man/netlify)(1), [firebase](/man/firebase)(1)
