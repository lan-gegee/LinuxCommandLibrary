# TAGLINE

用于浏览 Git 仓库的 Web 界面

# TLDR

通过 git instaweb 快速启动本地 gitweb 服务器

```git instaweb --httpd=[webrick]```

停止 instaweb 服务器

```git instaweb --stop```

配置 gitweb 项目根目录

```git config --global instaweb.httpd [webrick]```

# SYNOPSIS

**gitweb** _cgi_

# DESCRIPTION

**gitweb** 是 Git 仓库的 Web 界面，以 Perl CGI 脚本实现。它提供通过网页浏览器浏览仓库内容、提交历史、分支、标签、diff、blame 注释以及搜索功能。

**gitweb** 通常部署在 Web 服务器（Apache、nginx、lighttpd）之后供共享浏览仓库使用。如需快速本地浏览，可使用 **git instaweb**，它会自动启动一个临时 Web 服务器。配置文件使用 Perl 语法设置控制显示和行为的变量。

# CONFIGURATION

**/etc/gitweb.conf**
> 系统级配置文件，指定项目根目录、站点名称和显示选项。

**gitweb_config.perl**
> 每实例的配置文件（与 gitweb CGI 脚本位于同一目录），优先于 /etc/gitweb.conf。

# CAVEATS

CGI 脚本，生产使用需要 Web 服务器。没有内置身份验证；需依赖 Web 服务器的认证机制。只读界面；无法推送或修改仓库。

# HISTORY

gitweb 是 **Git** 发行版的一部分，自 Git 早期版本就提供网页端仓库浏览功能。它是 Gitea 和 GitLab 等现代 git 托管界面的前身。

# INSTALL

```dnf: sudo dnf install gitweb```

```nix: nix profile install nixpkgs#gitweb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-instaweb](/man/git-instaweb)(1), [gitea](/man/gitea)(1)
