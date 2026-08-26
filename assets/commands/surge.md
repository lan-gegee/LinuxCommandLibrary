# TAGLINE

即时静态网站发布平台

# TLDR

**部署当前目录**

```surge```

**部署指定目录**

```surge [./dist]```

**部署到自定义域名**

```surge [./dist] [mysite.surge.sh]```

**用显式参数部署**

```surge --project [./dist] --domain [mysite.surge.sh]```

**列出已部署的项目**

```surge list```

**移除部署**

```surge teardown [mysite.surge.sh]```

**登录**

```surge login```

**登出**

```surge logout```

**显示当前用户**

```surge whoami```

# SYNOPSIS

**surge** [_directory_] [_domain_]

# PARAMETERS

_directory_
> 要部署的路径。

_domain_
> 自定义域名。

**list**
> 显示项目。

**teardown** _DOMAIN_
> 移除项目。

**login**
> 进行认证。

**logout**
> 登出。

**whoami**
> 显示用户。

**token**
> 获取用于 CI/CD 的认证令牌。

**--project** _path_
> 指定项目目录。

**--domain** _domain_
> 指定目标域名。

**--token** _token_
> 提供认证令牌（用于 CI/CD）。

# DESCRIPTION

**surge** 是一个静态网站发布平台，只需一条命令即可部署 Web 项目。将它指向一个包含 HTML、CSS、JavaScript 及其他静态资源的目录，它就会立即发布到 *.surge.sh 子域名或自定义域名。

所有部署均附带用于 HTTPS 的免费 SSL 证书。支持自定义域名且不额外收费，只需一条 DNS CNAME 记录。该平台面向需要快速、简单托管而无需服务器配置的前端开发者。

认证令牌可在 CI/CD 流水线中实现自动化部署。list 命令显示所有已部署的项目，teardown 则移除某个部署。Surge 在发布文档站点、单页应用和项目演示方面尤其受欢迎。

# CAVEATS

仅支持静态网站；不支持服务端代码。免费套餐有诸多限制。自定义域名需要将 DNS CNAME 记录指向 na-east1.surge.sh。

# INSTALL

```nix: nix profile install nixpkgs#surge```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[netlify](/man/netlify)(1), [vercel](/man/vercel)(1), [firebase](/man/firebase)(1)
