# TAGLINE

基于 HTTP 的部分差分文件下载工具

# TLDR

**通过 .zsync URL 下载文件**

```zsync [http://example.com/path/to/file.zsync]```

**用本地文件作为种子进行差分下载**

```zsync -i [path/to/existing_file] [http://example.com/path/to/file.zsync]```

**以指定名称保存下载的文件**

```zsync -o [path/to/output_file] [http://example.com/path/to/file.zsync]```

**把 .zsync 文件保存到本地，便于日后条件请求**

```zsync -k [path/to/saved.zsync] [http://example.com/path/to/file.zsync]```

**安静模式下载，不显示进度条**

```zsync -q [http://example.com/path/to/file.zsync]```

**向服务器进行身份验证**

```zsync -A [hostname]=[user]:[password] [http://hostname/path/to/file.zsync]```

# SYNOPSIS

**zsync** [_OPTIONS_] _URL_

# PARAMETERS

**-i** _FILE_
> 使用本地文件作为差分下载的种子。可以多次指定。

**-o** _FILE_
> 以指定名称保存下载的文件，而非默认名称

**-k** _FILE_
> 以给定的文件名保存下载的 .zsync 文件。若文件已存在，则发起条件请求，只在服务器上的副本较新时才下载。

**-q**
> 安静模式，隐藏进度条、下载速率和预计剩余时间显示

**-s**
> -q 的已弃用同义词

**-u** _URL_
> 指定引用 URL。使用包含相对 URL 的本地 .zsync 文件时必须提供。

**-A** _hostname=username:password_
> 为指定主机名提供认证凭据。可对不同的服务器多次使用。

**-V**
> 打印版本信息

# DESCRIPTION

**zsync** 是一个部分/差分文件下载器。它借助 .zsync 控制文件只下载文件中发生变化的部分，类似 rsync，但运行在 HTTP 之上。

适用于更新 ISO 镜像这类大文件：当只有一小部分内容变化时，无需完整重新下载。

# CAVEATS

需要服务器端预先生成 .zsync 控制文件。服务器必须支持 HTTP 范围请求。是否支持 HTTPS 取决于具体构建版本。

# INSTALL

```apt: sudo apt install zsync```

```dnf: sudo dnf install zsync```

```pacman: sudo pacman -S zsync```

```zypper: sudo zypper install zsync```

```brew: brew install zsync```

```nix: nix profile install nixpkgs#zsync```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsync](/man/rsync)(1), [wget](/man/wget)(1), [curl](/man/curl)(1)
