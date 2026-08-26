# TAGLINE

终端中的 Discord 客户端

# TLDR

**启动** Discordo

```discordo```

**使用 token / 浏览器流程登录**（参见首次运行提示）

```discordo```

# SYNOPSIS

**discordo** [*options*]

# DESCRIPTION

**discordo** 是一个用 Go 编写的轻量级 TUI Discord 客户端。它支持浏览服务器/频道、发送消息以及键盘驱动的导航。可通过发行版软件包、nightly 二进制文件安装，或从源码构建。

**注意：**自动化用户账号（"self-bot"）违反 Discord 的服务条款。在适用的情况下请优先使用官方 bot 账号；风险自负。

# PARAMETERS

以交互操作为主。配置与 token 存储路径见上游 README。运行 **discordo --help** 查看你所用版本的可用标志。

# CAVEATS

使用用户 token 登录存在违反服务条款的风险。项目仍在开发中——可能出现破坏性变更。请像保管密码一样保管认证 token。

# INSTALL

```nix: nix profile install nixpkgs#discordo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[discord](/man/discord)(1), [weechat](/man/weechat)(1)

# RESOURCES

```[Source code](https://github.com/ayn2op/discordo)```

<!-- verified: 2026-07-19 -->
