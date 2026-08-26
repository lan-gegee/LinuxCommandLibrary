# TAGLINE

基于终端的交互式 SSH 管理器

# TLDR

**启动 SSH 管理器界面**

```lazyssh```

# SYNOPSIS

**lazyssh**

# KEYBINDINGS

**/**
> 切换搜索栏的显示。

**Up/Down** 或 **j/k**
> 浏览服务器列表。

**Enter**
> SSH 连接选中的服务器。

**c**
> 将 SSH 命令复制到剪贴板。

**g**
> Ping 选中的服务器。

**r**
> 刷新后台数据。

**a**
> 添加服务器。

**e**
> 编辑服务器。

**t**
> 编辑标签。

**d**
> 删除服务器。

**p**
> 固定/取消固定服务器。

**s**
> 切换排序字段。

**S**
> 反转排序顺序。

**q**
> 退出。

# DESCRIPTION

**lazyssh** 是一个键盘驱动的 SSH 管理器，让你可以直接在命令行中轻松浏览、连接和管理服务器。它会读取你的 **~/.ssh/config**，并将其中的服务器呈现在一个可滚动的界面中。

功能包括按别名、IP 或标签进行模糊搜索，添加或编辑 SSH 配置条目，固定常用服务器，ping 服务器测试连通性，用标签做分类，配置端口转发，以及连接复用。只需按一个键即可 SSH 进入选中的服务器。

所有 SSH 连接都通过系统原生的 **ssh** 二进制文件执行。私钥、密码和凭据绝不会被 lazyssh 存储、传输或修改。在进行任何改动之前，都会自动创建一份 SSH 配置备份。

# CAVEATS

需要有现成的 **~/.ssh/config** 文件。连接依赖系统安装的 OpenSSH 二进制文件。

# HISTORY

**lazyssh** 由 **Adembc** 创建，使用 **Go** 基于 tview 和 tcell 库编写。其灵感来自 lazydocker 和 k9s。

# INSTALL

```brew: brew install lazyssh```

```nix: nix profile install nixpkgs#lazyssh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [ssh-keygen](/man/ssh-keygen)(1)
