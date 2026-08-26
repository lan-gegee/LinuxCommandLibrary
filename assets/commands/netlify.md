# TAGLINE

登录 Netlify

# TLDR

**登录 Netlify**

```netlify login```

**部署当前目录**

```netlify deploy```

**部署到生产环境**

```netlify deploy --prod```

**创建新站点**

```netlify sites:create```

**在浏览器中打开站点**

```netlify open```

**查看部署日志**

```netlify watch```

**关联已有站点**

```netlify link```

**运行开发服务器**

```netlify dev```

# SYNOPSIS

**netlify** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> Netlify CLI 命令。

**login**
> 向 Netlify 进行身份验证。

**deploy**
> 部署站点。

**sites:create**
> 创建新站点。

**open**
> 在浏览器中打开。

**dev**
> 启动开发服务器。

**link**
> 关联站点。

**--help**
> 显示帮助信息。

# DESCRIPTION

**netlify** 是 Netlify 的命令行界面。它用于在 Netlify 平台上部署和管理站点。

该工具负责处理部署，支持 serverless 函数和本地开发。

# CAVEATS

需要 Netlify 账户。基于 Node.js。建议配合 Git 集成使用。

# HISTORY

Netlify CLI 由 **Netlify** 创建，用于通过命令行进行部署和站点管理。

# INSTALL

```aur: yay -S netlify```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vercel](/man/vercel)(1), [firebase](/man/firebase)(1), [gh-pages](/man/gh-pages)(1)
