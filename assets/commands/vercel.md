# TAGLINE

部署到 Vercel 托管平台

# TLDR

**部署项目**

```vercel```

**部署到生产环境**

```vercel --prod```

**将本地项目关联到 Vercel**

```vercel link```

**列出部署**

```vercel ls```

**显示部署日志**

```vercel logs [deployment_url]```

**设置环境变量**

```vercel env add [VARIABLE_NAME]```

**列出环境变量**

```vercel env ls```

**拉取环境变量到本地**

```vercel env pull```

# SYNOPSIS

**vercel** [_command_] [_--prod_] [_--yes_] [_options_] [_arguments_]

# PARAMETERS

**(deploy)**
> 部署项目（默认命令）。

**dev**
> 启动本地开发服务器。

**build**
> 在本地构建项目。

**link**
> 关联到 Vercel 项目。

**ls** / **list**
> 列出部署。

**logs** _URL_
> 显示部署日志。

**inspect** _URL_
> 显示部署详情。

**env** _subcommand_
> 管理环境变量。

**domains** _subcommand_
> 管理域名。

**dns** _subcommand_
> 管理 DNS 记录。

**certs** _subcommand_
> 管理证书。

**secrets** _subcommand_
> 管理机密（secret）。

**--prod**
> 部署到生产环境。

**--yes**, **-y**
> 跳过确认提示。

**--no-clipboard**
> 不将 URL 复制到剪贴板。

**--local-config** _FILE_
> 本地配置文件路径。

**--confirm**
> 确认默认选项。

**--scope** _TEAM_
> 团队或用户名范围。

**--token** _TOKEN_
> 身份验证令牌。

# DESCRIPTION

**vercel** 是 Vercel 部署平台的 CLI。它部署前端应用和无服务器函数，自动提供 HTTPS、CDN，且无需配置。

部署即时完成——运行 `vercel` 即可获得一个 URL。每次部署都不可变，并拥有唯一的 URL。生产部署会更新主域名。

dev 命令运行模拟 Vercel 环境的本地开发服务器。无服务器函数在本地的工作方式与部署后完全一致。

框架检测会为 Next.js、React、Vue、Angular 等众多框架自动配置构建。自定义构建使用 vercel.json 配置。

环境变量按环境管理（development、preview、production）。env pull 命令将其下载供本地使用。

与 GitHub/GitLab 的集成可为 pull request 自动创建预览部署，并在合并时进行生产部署。

域名管理通过 CLI 处理自定义域名、SSL 证书和 DNS 配置。

# CAVEATS

需要 Vercel 账户。部分功能需要付费方案。无服务器函数有用量限制。Edge 函数存在限制。构建时间计入配额。某些框架需要额外配置。

# HISTORY

**Vercel**（前身 ZEIT）由 **Guillermo Rauch** 于 **2015 年**创立。CLI 最初名为 `now`，于 **2020 年**更名为 `vercel`。该平台开创了无服务器前端托管模式，也是 Next.js 背后的公司。它强调开发者体验和零配置部署。

# INSTALL

```brew: brew install vercel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[netlify](/man/netlify)(1), [firebase](/man/firebase)(1), [surge](/man/surge)(1), [next](/man/next)(1)
