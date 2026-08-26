# TAGLINE

管理多个 Erlang/OTP 安装

# TLDR

**列出可用版本**

```kerl list releases```

**构建 Erlang 版本**

```kerl build [26.0] [26.0-build]```

**安装已构建的版本**

```kerl install [26.0-build] [~/.kerl/26.0]```

**激活安装**

```source ~/.kerl/26.0/activate```

**列出安装**

```kerl list installations```

**显示构建和安装的状态**

```kerl status```

**删除构建**

```kerl delete build [26.0-build]```

**清理构建产物**

```kerl cleanup [26.0-build]```

# SYNOPSIS

**kerl** _command_ [_args_]

# PARAMETERS

**list releases**
> 显示可用版本。

**list builds**
> 显示已完成的构建。

**list installations**
> 显示已安装的版本。

**build** _VSN_ _NAME_
> 构建 Erlang 版本。

**install** _BUILD_ _PATH_
> 将构建安装到指定路径。

**delete** _TYPE_ _NAME_
> 删除构建或安装。

**update releases**
> 获取最新的可用版本列表。

**build-install** _VSN_ _NAME_ _PATH_
> 将构建和安装合并为一步。

**status**
> 打印可用的构建和安装。

**path** [_NAME_]
> 打印当前激活或指定安装的路径。

**active**
> 打印当前激活的安装。

**cleanup** _NAME_
> 移除某次构建的编译产物。

**deploy** _HOST_ _DIR_
> 通过 SSH 将安装部署到远程主机。

# DESCRIPTION

**kerl** 管理多个 Erlang/OTP 安装。它可以并排构建和安装不同的版本。

该工具处理从源码开始的编译。激活脚本会为每个版本设置好环境。

# CAVEATS

从源码构建，因此必须安装构建依赖（gcc、make、ncurses-dev、libssl-dev 等）。Shell 脚本工具——通过 **$HOME/.kerlrc** 配置。设置 **KERL_INCLUDE_RELEASE_CANDIDATES=yes** 可包含候选发布版本。

# INSTALL

```brew: brew install kerl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[erl](/man/erl)(1), [asdf](/man/asdf)(1)
