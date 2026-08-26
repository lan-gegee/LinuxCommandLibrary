# TAGLINE

将图片上传到各种图床服务

# TLDR

**上传图片**

```picgo upload [image.png]```

**从剪贴板上传**

```picgo upload```

**设置默认图床**

```picgo use [smms]```

**列出图床**

```picgo list uploader```

**安装插件**

```picgo install [plugin-name]```

**配置图床**

```picgo set uploader```

**显示配置**

```picgo config```

# SYNOPSIS

**picgo** _command_ [_options_] [_files_]

# PARAMETERS

**upload** [_files_...]
> 上传图片；不带参数时从剪贴板上传。

**use** _uploader_
> 设置默认图床。

**list** [_type_]
> 列出可用的插件或图床。

**install** _plugin_
> 安装插件。

**uninstall** _plugin_
> 移除插件。

**set** _type_
> 以交互方式配置图床设置。

**config**
> 显示当前配置。

**-v**, **--version**
> 显示版本号。

**-d**, **--debug**
> 启用调试模式。

**-s**, **--silent**
> 启用静默模式。

**-c** _path_, **--config** _path_
> 设置自定义配置文件路径。

**-p** _url_, **--proxy** _url_
> 设置上传使用的代理。

**-h**, **--help**
> 显示帮助。

# UPLOADERS

**smms** - SM.MS
**github** - GitHub 仓库
**imgur** - Imgur
**aliyun** - 阿里云 OSS
**qiniu** - 七牛云
**tcyun** - 腾讯云 COS
**upyun** - 又拍云

# DESCRIPTION

**PicGo**（PicGo-Core）是一个命令行图片上传工具，支持多种图床后端。它会返回 markdown 格式的 URL，适合用于文档和博客文章。

通过插件系统支持多种后端，包括 GitHub、Imgur、SM.MS 以及多家中国云服务商。剪贴板上传可直接捕获截图，无需先保存为文件。输出格式包括 markdown、HTML 和纯 URL，便于直接集成到文档工作流中。

# CAVEATS

大多数图床服务需要 API 密钥或令牌。部分服务有上传大小或速率限制。插件质量参差不齐。需要 Node.js 运行时。

# HISTORY

**PicGo** 是为中国开发者打造的图片上传工具。它负责上传和 URL 生成，简化了向文档和博客添加图片的过程。

# INSTALL

```nix: nix profile install nixpkgs#picgo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[imgur-upload](/man/imgur-upload)(1), [curl](/man/curl)(1)
