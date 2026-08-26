# TAGLINE

从命令行创建和管理 GitHub Gists

# TLDR

**在本机上进行一次身份验证**

```gist --login```

**从文件创建**公开 gist

```gist [file.rb]```

**创建**私有 gist

```gist -p [file.rb]```

**从标准输入创建** gist 并为文件命名

```echo "[content]" | gist -f [snippet.txt]```

**创建**带描述的 gist

```gist -d "[what this does]" [file.rb]```

**创建** gist 并将其 URL 复制到剪贴板

```gist -c [file.rb]```

**列出**你的 gist

```gist -l```

将 gist **读取**到标准输出

```gist -r [gist_id]```

**更新**已有的 gist

```gist -u [gist_id] [file.rb]```

**删除** gist

```gist --delete [gist_id]```

# SYNOPSIS

**gist** [**-p**] [**-d** _description_] [**-t** _extension_] [_file_ ...]

**gist** [**-l** [_user_]] [**-r** _id_] [**-u** _id_] [**--delete** _id_]

# PARAMETERS

**-p**, **--private**
> 将 gist 设为私有。Gist 默认是**公开**的。

**--no-private**
> 强制创建公开 gist，覆盖之前出现的 **-p**。

**-d**, **--description** _DESCRIPTION_
> 为 gist 添加描述。

**-f**, **--filename** [_NAME.EXTENSION_]
> 设置文件名和语法类型。主要用于从标准输入读取时。

**-t**, **--type** [_EXTENSION_]
> 设置文件扩展名和语法类型。

**-l**, **--list** [_USER_]
> 列出 gist。不带参数时列出你自己的；带用户名时列出该用户的公开 gist。

**-r**, **--read** _ID_ [_FILENAME_]
> 读取一个 gist 并将其内容打印到标准输出。

**-u**, **--update** [_URL_ | _ID_]
> 更新已有的 gist。

**--delete** [_URL_ | _ID_]
> 删除 gist。

**-c**, **--copy**
> 将生成的 URL 复制到剪贴板。

**-e**, **--embed**
> 将 gist 的嵌入代码复制到剪贴板。

**-o**, **--open**
> 在浏览器中打开生成的 URL。

**--no-open**
> 不打开浏览器。

**-P**, **--paste**
> 用剪贴板内容创建 gist。

**-R**, **--raw**
> 显示新 gist 的原始 URL。

**-s**, **--shorten**
> 使用 git.io 缩短 gist URL。

**--skip-empty**
> 跳过空文件，而不是为它们创建 gist。

**--login**
> 在本机上对 gist 进行身份验证并存储令牌。

**-h**, **--help**
> 显示帮助消息。

**-v**, **--version**
> 打印版本号。

# DESCRIPTION

**gist** 从命令行将文件上传到 **GitHub Gists**。Gist 是一种轻量级方式，无需创建仓库即可分享代码片段、日志和笔记；每个 gist 底层都是一个真正的 git 仓库，具备修订历史、复刻（fork）和评论功能。

给定一个或多个文件名时，它会上传这些文件并打印生成的 URL。不给任何参数时则从标准输入读取，这使它天然适合放在管道末尾：**command | gist -f output.log**。由于文件名决定了 GitHub 应用的语法高亮，在管道中使用时值得设置 **-f** 或 **-t**。

身份验证只需通过 **gist --login** 进行一次，它会在 **~/.gist** 中存储一个 OAuth 令牌。没有令牌时，在 API 仍允许的情况下会上传为匿名 gist。

# CONFIGURATION

**~/.gist**
> 存储 **gist --login** 写入的 OAuth2 访问令牌。

**GITHUB_URL**
> 让 gist 指向 GitHub Enterprise 实例而不是 github.com。

**GIST_CLIENT_ID**
> OAuth 客户端 ID，用于对 Enterprise 实例启用设备码流程。

**GIST_USE_USERNAME_AND_PASSWORD**
> 使用已弃用的用户名加密码流程。

**HTTP_PROXY**, **http_proxy**
> 通过 HTTP 代理路由请求。

**BROWSER**
> **-o** 使用的浏览器。

# CAVEATS

Gist 默认**公开**。**-p** 可将其设为私有，且 gist 创建后无法更改可见性，因此未带 **-p** 上传的片段从存在那一刻起就对全世界可读。粘贴任何包含凭据的内容前请三思。

"私有"（secret）gist 只是不被列出，并非访问受控：任何拿到 URL 的人都能读取它，而且它并未加密。不要把它当作密钥保险箱。

**-c**、**-e** 和 **-P** 需要可用的剪贴板工具，在 Linux 上意味着必须安装 **xclip** 或 **xsel**。

GitHub 官方的 **gh gist** 子命令覆盖了大部分相同功能，且随 GitHub CLI 附带，如果你已经安装并认证了 **gh**，它是更省事的选择。

# HISTORY

**gist** 是由 GitHub 联合创始人 **Chris Wanstrath**（**defunkt**）编写的 Ruby gem，是最古老的 GitHub 命令行工具之一，比官方 **gh** CLI 早了大约十年。通过 **gem install gist** 安装。

# INSTALL

```apt: sudo apt install yorick```

```pacman: sudo pacman -S gist```

```brew: brew install gist```

```nix: nix profile install nixpkgs#gist```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh-gist](/man/gh-gist)(1), [gh](/man/gh)(1), [curl](/man/curl)(1), [xclip](/man/xclip)(1)

# RESOURCES

```[Source code](https://github.com/defunkt/gist)```

<!-- verified: 2026-07-16 -->
