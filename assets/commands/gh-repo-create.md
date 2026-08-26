# TAGLINE

创建新的 GitHub 仓库

# TLDR

**以交互方式创建仓库**

```gh repo create```

**从当前目录创建仓库**

```gh repo create [name] --source=.```

**创建空仓库**

```gh repo create [name] --public```

**创建私有仓库**

```gh repo create [name] --private```

**从模板创建仓库**

```gh repo create [name] --template [owner/template]```

**创建后克隆**

```gh repo create [name] --clone```

**带描述创建仓库**

```gh repo create [name] -d "[description]"```

# SYNOPSIS

**gh** **repo** **create** [_name_] [_options_]

# PARAMETERS

**--public**
> 设为公开。

**--private**
> 设为私有。

**--internal**
> 设为内部可见。

**--source** _dir_
> 从本地目录创建。

**--template** _repo_
> 从模板创建。

**--clone**
> 创建后克隆。

**-d**, **--description** _text_
> 描述。

**--homepage** _url_
> 主页 URL。

**--gitignore** _template_
> 添加 .gitignore。

**--license** _license_
> 添加许可证。

# DESCRIPTION

**gh repo create** 在命令行中创建 GitHub 仓库，支持多种创建工作流。它可以创建空仓库、从当前目录初始化，或者基于仓库模板生成新仓库。

不带参数交互运行时，命令会引导你完成仓库创建，提示选择可见性、描述和初始化选项。--source 标志可将现有的本地 git 仓库发布到 GitHub。模板仓库（--template）则为常见项目类型提供起始配置。

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

[gh-repo](/man/gh-repo)(1)
