# TAGLINE

管理 Kaggle CLI 配置设置

# TLDR

**查看当前配置**

```kaggle config view```

**设置默认竞赛**

```kaggle config set -n competition -v [competition_name]```

**设置默认下载路径**

```kaggle config set -n path -v [/path/to/download/folder]```

**为 HTTP 请求设置代理**

```kaggle config set -n proxy -v [http://proxy:port]```

**取消某个配置值**

```kaggle config unset -n [name]```

# SYNOPSIS

**kaggle** **config** _subcommand_ [_options_]

# PARAMETERS

**set** **-n** _name_ **-v** _value_
> 设置配置选项。有效名称：competition、path、proxy。

**view**
> 显示当前配置值。

**unset** **-n** _name_
> 移除配置选项，恢复默认行为。

**-n** _NAME_, **--name** _NAME_
> 配置参数的名称。

**-v** _VALUE_, **--value** _VALUE_
> 配置参数的值。

# DESCRIPTION

**kaggle config** 管理 Kaggle CLI 的配置设置。可用的配置参数有 **competition**（默认竞赛 URL 后缀）、**path**（默认下载文件夹，默认为当前工作目录）和 **proxy**（HTTP 请求代理）。配置存储在 **~/.kaggle/kaggle.json** 中。

# INSTALL

```nix: nix profile install nixpkgs#kaggle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kaggle](/man/kaggle)(1)
