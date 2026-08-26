# TAGLINE

加密文件共享客户端

# TLDR

**上传文件**

```ffsend upload [file.zip]```

带密码上传

```ffsend upload -p [password] [file.zip]```

设置下载次数限制

```ffsend upload -d [5] [file.zip]```

**下载文件**

```ffsend download [url]```

删除已上传的文件

```ffsend delete [url]```

# SYNOPSIS

**ffsend** _command_ [_options_] [_file_|_url_]

# PARAMETERS

_COMMAND_
> 操作：upload、download、delete、info、history。

**upload** _FILE_
> 上传文件并获取分享链接。

**download** _URL_
> 从分享链接下载。

**delete** _URL_
> 删除已上传的文件。

**-p** _PASSWORD_, **--password** _PASSWORD_
> 用密码保护。

**-d** _N_, **--downloads** _N_
> 最大下载次数。

**-e** _TIME_, **--expiry** _TIME_
> 过期时间（如 1h、7d）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ffsend** 是 Firefox Send 的命令行客户端，通过加密上传实现安全的文件共享。文件在上传前经过端到端加密，并可用密码保护。

该工具生成的分享链接可在达到设定下载次数或时间期限后过期。加密在客户端完成，确保服务器永远无法访问未加密的内容。

ffsend 兼容官方和自托管的 Send 实例，用于私密文件共享。

# CAVEATS

Firefox Send 官方服务已停止运营。需要兼容的 Send 服务器。大文件加密可能耗时。

# HISTORY

ffsend 作为 Mozilla 加密文件共享服务 **Firefox Send** 的 CLI 客户端而创建。虽然 Mozilla 于 2020 年停止了官方服务，但自托管的 Send 实例和 ffsend 仍可使用。

# INSTALL

```brew: brew install ffsend```

```nix: nix profile install nixpkgs#ffsend```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [croc](/man/croc)(1)
