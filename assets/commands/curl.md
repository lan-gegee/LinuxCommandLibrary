# TAGLINE

通过 URL 传输数据

# TLDR

**下载**文件

```curl -O [https://example.com/file.zip]```

保存到指定文件

```curl -o [filename] [https://example.com/file]```

**POST** 数据

```curl -X POST -d ["key=value"] [https://api.example.com]```

跟随重定向

```curl -L [https://example.com]```

发送 JSON

```curl -H ["Content-Type: application/json"] -d ['{"key":"value"}'] [https://api.example.com]```

显示响应头

```curl -I [https://example.com]```

# SYNOPSIS

**curl** [_options_] [_URL_...]

# DESCRIPTION

**curl** 是一个通过 URL 传输数据的命令行工具。它支持 HTTP、HTTPS、FTP 等众多协议，是 Web 开发、API 测试和文件传输的必备工具。

该工具在脚本、CI/CD 流水线和系统管理中无处不在。

# PARAMETERS

**-O**, **--remote-name**
> 以远端文件名保存

**-o**, **--output** _file_
> 保存到指定文件

**-L**, **--location**
> 跟随重定向

**-X**, **--request** _method_
> HTTP 方法（GET、POST、PUT、DELETE）

**-d**, **--data** _data_
> 发送 POST 数据

**-H**, **--header** _header_
> 添加自定义请求头

**-u**, **--user** _user:pass_
> 身份验证

**-I**, **--head**
> 只获取响应头

**-v**, **--verbose**
> 详细输出

**-s**, **--silent**
> 静默模式

**-f**, **--fail**
> 遇到 HTTP 错误时静默失败

**-k**, **--insecure**
> 允许不安全的 SSL 连接

**-C**, **--continue-at** _offset_
> 继续之前的下载（用 `-` 表示自动）

**--cookie** _data|file_
> 发送 cookie（内联字符串或文件路径）

**--cookie-jar** _file_
> 将收到的 cookie 写入文件

**--max-time** _seconds_
> 整个传输允许的最长时间

**--retry** _N_
> 失败的传输最多重试 N 次

**-A**, **--user-agent** _string_
> 发送 User-Agent 请求头

**-e**, **--referer** _url_
> 发送 Referer 请求头

# CONFIGURATION

**~/.curlrc**
> 每次 curl 调用都会加载的默认选项（每行一个选项）。

**~/.netrc**
> 存放远程主机的认证凭据（配合 --netrc 使用）。

# CAVEATS

默认静默失败（可用 -f 改变此行为）。大文件下载默认显示进度条（脚本中可用 -s 关闭）。Cookie 文件需要自行管理。SSL 证书问题需要 -k（不安全）。高级功能的语法较为复杂。

# HISTORY

**curl** 起源于 **1996 年**的 httpget（Rafael Sagula 编写，Daniel Stenberg 参与贡献），1997 年增加 FTP 支持后更名为 urlget，并于 **1998 年 3 月**在 4.0 版本中定名 **curl**。它是最广泛使用的数据传输命令行工具之一。

# INSTALL

```apt: sudo apt install curl```

```dnf: sudo dnf install curl```

```pacman: sudo pacman -S curl```

```apk: sudo apk add curl```

```zypper: sudo zypper install curl```

```brew: brew install curl```

```nix: nix profile install nixpkgs#curl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wget](/man/wget)(1), [http](/man/http)(1)
