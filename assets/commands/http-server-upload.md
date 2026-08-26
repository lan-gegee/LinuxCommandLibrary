# TAGLINE

用于上传文件的简单零配置 HTTP 服务器

# TLDR

**在默认端口 8080 上启动上传服务器**

```http-server-upload```

**在指定端口上以令牌启动**

```http-server-upload --port [9090] --token [my-secret-token]```

**设置上传目录和最大文件大小**

```http-server-upload --upload-dir [./uploads] --max-file-size [500]```

**启用自动创建文件夹**

```http-server-upload --enable-folder-creation```

**通过环境变量配置**

```PORT=9000 UPLOAD_DIR=~/uploads/ TOKEN=secret http-server-upload```

# SYNOPSIS

**http-server-upload** [_options_] [_uploadRootPath_]

# PARAMETERS

可通过命令行参数或环境变量进行配置。若两者同时使用，参数优先级更高。

**--port** _PORT_ (env: PORT)
> 服务器端口。默认：8080。如果端口已被占用，会自动递增，直到找到空闲端口为止。

**--upload-dir** _DIR_ (env: UPLOAD_DIR)
> 存放上传文件的目录。默认：当前工作目录。

**--upload-tmp-dir** _DIR_ (env: UPLOAD_TMP_DIR)
> 上传文件在被移动到最终位置之前的临时目录。

**--token** _TOKEN_ (env: TOKEN)
> 可选的上传所需令牌，提供基本的访问保护。

**--max-file-size** _MB_ (env: MAX_FILE_SIZE)
> 允许的最大文件大小（单位 MB）。默认：200。

**--disable-auto-port** (env: DISABLE_AUTO_PORT)
> 端口被占用时禁止自动递增端口。

**--enable-folder-creation** (env: ENABLE_FOLDER_CREATION)
> 上传到不存在的路径时自动创建文件夹。

**--path-regexp** _REGEX_ (env: PATH_REGEXP)
> 用于校验上传路径的正则表达式。

**--index-file** _FILE_ (env: INDEX_FILE)
> 使用自定义 HTML 文件作为上传表单页面。

**-h**, **--help**
> 显示帮助文本。

# DESCRIPTION

**http-server-upload** 是一个简单的零配置 Node.js 命令行 HTTP 服务器，用于上传文件。运行后访问 http://localhost:8080/ 即可打开上传表单。默认情况下，文件会上传到当前工作目录。

该工具适合在不搭建完整文件共享服务的情况下快速传输文件。可选的令牌提供基本的访问保护。

# CAVEATS

不适用于生产环境。需要 Node.js 14.18 或更高版本。如果目标端口已被占用，端口会自动递增，直到找到空闲端口为止。

# INSTALL

```brew: brew install http-server```

```nix: nix profile install nixpkgs#http-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[http-server](/man/http-server)(1), [updog](/man/updog)(1)
