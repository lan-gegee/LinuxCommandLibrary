# TAGLINE

将静态网站发布到 GitHub Pages 分支

# TLDR

**将 dist 文件夹部署到 gh-pages**

```npx gh-pages -d [dist]```

**使用自定义提交信息部署**

```npx gh-pages -d [dist] -m "[Deploy to GitHub Pages]"```

**部署到自定义分支**

```npx gh-pages -d [dist] -b [docs]```

**部署特定文件**

```npx gh-pages -d [dist] -s "[*.html,*.css]"```

**使用自定义远程仓库部署**

```npx gh-pages -d [dist] -o [upstream]```

**使用自定义域名部署（CNAME）**

```npx gh-pages -d [dist] --cname [example.com]```

# SYNOPSIS

**gh-pages** [_options_]

# PARAMETERS

**-d**, **--dist** _dir_
> 要部署的目录。

**-s**, **--src** _pattern_
> dist 内的文件匹配模式。

**-b**, **--branch** _branch_
> 目标分支（默认：gh-pages）。

**-o**, **--remote** _remote_
> 远程仓库名称（默认：origin）。

**-m**, **--message** _msg_
> 提交信息。

**-u**, **--user** _name_
> Git 用户名。

**-e**, **--email** _email_
> Git 用户邮箱。

**-a**, **--add**
> 只添加文件，不移除已有文件。

**-t**, **--dotfiles**
> 包含点文件。

**-r**, **--repo** _url_
> 要推送到的仓库 URL（不在 git 仓库内或要推送到其他位置时使用）。

**--cname** _domain_
> 使用自定义域名创建 CNAME 文件。

**--nojekyll**
> 添加 .nojekyll 文件，跳过 GitHub Pages 上的 Jekyll 处理。

# DESCRIPTION

**gh-pages** 是一个 npm 软件包，用于将文件发布到 GitHub Pages 分支。它会自动把构建好的静态网站推送到 gh-pages 分支进行托管，并将产物文件夹以干净的提交推送到目标分支。

该工具让部署只需一条命令，常用于 CI/CD 流水线，也可以作为 package.json 中的脚本使用。

# CONFIGURATION

**package.json**
> 在 scripts 部分配置 `"deploy": "gh-pages -d dist"` 部署脚本。

# CAVEATS

需要 git 和 npm。默认情况下，目标分支上已有的文件会在部署前被移除；如需保留请使用 **-a**。必须在 GitHub Pages 的仓库设置中配置为从目标分支提供服务。不需要 Jekyll 处理的网站请使用 **--nojekyll**。推送时需要提供凭据。

# HISTORY

gh-pages 由 **Tim Schaub** 创建，旨在简化 GitHub Pages 部署。它已成为 JavaScript 生态中进行静态网站部署的标准工具。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [git](/man/git)(1), [npm](/man/npm)(1)
