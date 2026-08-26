# TAGLINE

在 CapRover 上部署和管理应用

# TLDR

**登录** CapRover 服务器

```caprover login```

**部署**应用

```caprover deploy```

**带指定选项部署**

```caprover deploy -n [machine-name] -a [app-name] -b [branch]```

**部署 Docker 镜像**

```caprover deploy -i [image-name]```

**从 tar 文件部署**

```caprover deploy -t [app.tar]```

**初始化新的 CapRover 服务器**

```caprover serversetup```

**列出已登录的服务器**

```caprover list```

**退出服务器登录**

```caprover logout```

# SYNOPSIS

**caprover** _command_ [_options_]

# DESCRIPTION

**caprover** 是 CapRover 的 CLI。CapRover 是一个现代化的自动化应用部署与 Web 服务器管理器。使用该 CLI 可完成服务器的初始设置，并通过 captain-definition 文件、Dockerfile、tar 文件或 Docker 镜像部署应用。

# COMMANDS

**serversetup**, **setup**
> 执行初始服务器设置（域名、SSL、密码）

**login**
> 向 CapRover 服务器进行身份验证

**logout**
> 移除某台服务器的身份验证信息

**deploy**
> 将应用部署到 CapRover

**list**, **ls**
> 列出所有已登录的服务器

**api**
> 调用 CapRover 服务器的通用 API

# PARAMETERS

**-n**, **--caproverName** _name_
> 目标 CapRover 服务器名称

**-a**, **--caproverApp** _app_
> 要部署的应用名称

**-b**, **--branch** _branch_
> 要部署的 Git 分支

**-t**, **--tarFile** _file_
> 用于部署的 tar 文件路径

**-i**, **--imageName** _image_
> 要部署的 Docker 镜像

**-d**, **--default**
> 使用之前输入过的值

**-c**, **--configFile** _file_
> 部署配置文件路径

**-u**, **--caproverUrl** _url_
> CapRover 服务器 URL

**-p**, **--caproverPassword** _password_
> CapRover 密码

**--appToken** _token_
> 应用级身份验证令牌

**-V**, **--version**
> 输出版本号

**-h**, **--help**
> 显示帮助信息

# CI/CD INTEGRATION

用于自动化时，直接提供各选项即可：

```caprover deploy -n machine -a app -b main```

前提是之前已登录该服务器。

# CAVEATS

需要 Node.js 和 npm。部署分支时不包含未提交和被 git 忽略的文件。通过 npm install -g caprover 安装。

# INSTALL

```aur: yay -S caprover```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [kubectl](/man/kubectl)(1), [heroku](/man/heroku)(1)
