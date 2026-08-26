# TAGLINE

netlify CLI 简写

# TLDR

**启动开发服务器**

```ntl dev```

**部署站点**

```ntl deploy```

**部署到生产环境**

```ntl deploy --prod```

**在浏览器中打开站点**

```ntl open```

**列出站点**

```ntl sites:list```

# SYNOPSIS

**ntl** [_command_] [_options_]

# PARAMETERS

**dev**
> 启动本地开发服务器。

**deploy**
> 将站点部署到 Netlify。

**--prod**
> 部署到生产环境。

**open**
> 在浏览器中打开站点。

**sites:list**
> 列出所有站点。

**login**
> 向 Netlify 进行身份验证。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ntl** 是 Netlify CLI 的简写形式，用于管理部署和开发。

该工具提供对 Netlify 平台的访问，是 netlify 命令的别名。

# CAVEATS

需要 Netlify 账户。与 netlify 命令相同。需要身份验证。

# HISTORY

ntl 是 Netlify CLI 的**简写别名**，为方便起见而引入。

# INSTALL

```dnf: sudo dnf install ntl```

```pacman: sudo pacman -S ntl```

```brew: brew install ntl```

```nix: nix profile install nixpkgs#ntl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[netlify](/man/netlify)(1), [npm](/man/npm)(1), [vercel](/man/vercel)(1)
