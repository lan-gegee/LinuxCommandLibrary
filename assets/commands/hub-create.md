# TAGLINE

创建新的 GitHub 仓库并将其添加为 remote

# TLDR

**创建新的 GitHub 仓库**

```hub create```

**带描述创建**

```hub create -d "[description]"```

**创建私有仓库**

```hub create -p```

**在组织中创建**

```hub create [org/repo]```

**创建并在浏览器中打开**

```hub create --browse```

**带主页 URL 创建**

```hub create -h [https://example.com]```

# SYNOPSIS

**hub** **create** [_options_] [_name_]

# PARAMETERS

**-d**, **--description** _text_
> 仓库描述。

**-p**, **--private**
> 创建私有仓库。

**-h**, **--homepage** _url_
> 仓库主页 URL。

**-o**, **--browse**
> 在 Web 浏览器中打开新仓库。

**-c**, **--copy**
> 将新仓库的 URL 复制到剪贴板而不是打印出来。

**--remote-name** _name_
> 设置新 git remote 的名称（默认：origin）。

# DESCRIPTION

**hub create** 创建一个新的 GitHub 仓库并将其添加为 remote。未指定名称时使用当前目录名。可以通过 org/repo 格式在组织中创建仓库。

# CAVEATS

Hub 已被弃用。建议改用 **gh repo create**。

# INSTALL

```apt: sudo apt install hub```

```pacman: sudo pacman -S hub```

```zypper: sudo zypper install hub```

```brew: brew install hub```

```nix: nix profile install nixpkgs#hub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hub](/man/hub)(1), [gh-repo-create](/man/gh-repo-create)(1)
