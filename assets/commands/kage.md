# TAGLINE

镜像网站以便离线、无 JavaScript 浏览

# TLDR

**克隆网站**到可离线浏览的文件夹

```kage clone [https://example.com]```

在本地 web 服务器中**预览**已克隆的文件夹

```kage serve [path/to/mirror]```

将镜像**打包**为自包含归档

```kage pack [path/to/mirror]```

打开已打包的归档并提供服务

```kage open [archive.zim]```

# SYNOPSIS

**kage** _command_ [_arguments_]

# DESCRIPTION

**kage** 将网站克隆为静态的、可离线浏览的副本。它驱动无头 Chrome 浏览器渲染每个页面，在脚本执行完毕后捕获最终 DOM，剥离所有 JavaScript，并把引用的 CSS、图片和字体下载到本地路径。其结果是一个完全离线可用、没有任何网络请求和跟踪行为的自包含镜像。

由于页面是在渲染之后保存而非保存原始 HTML，那些用 JavaScript 构建内容的站点会被捕获为纯静态标记。保存下来的副本可以直接浏览、在本地启动服务器预览，或打包成单个便携归档。

# COMMANDS

**clone** _url_
> 用无头 Chrome 渲染网站，并将静态、无 JavaScript 的镜像保存到本地文件夹。

**serve** [_dir_]
> 启动本地 web 服务器以预览之前克隆的文件夹。

**pack** _mirror-dir_
> 将镜像目录压缩为 ZIM 文件或自包含二进制文件。

**open** _file_
> 通过本地 web 服务器提供已打包归档（例如 .zim 文件）的服务。

# CAVEATS

需要安装无头 Chrome 或 Chromium 来渲染页面。剥离 JavaScript 意味着依赖客户端脚本的交互功能在镜像中将无法工作。位于身份验证或严格反爬保护之后的站点可能无法顺利克隆。

# HISTORY

**kage** 用 **Go** 编写，以 MIT 许可证发布。这个名字在日语中意为"影子"，反映了它的用途——为一个活跃网站生成静态的影子副本。

# SEE ALSO

[wget](/man/wget)(1), [httrack](/man/httrack)(1), [monolith](/man/monolith)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/tamnd/kage)```

```[Homepage](https://kage.tamnd.com)```

<!-- verified: 2026-06-14 -->
