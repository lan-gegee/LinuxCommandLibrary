# TAGLINE

远程服务器上的浏览器版 VS Code

# TLDR

**启动 code-server**

```code-server```

**在指定端口上启动**

```code-server --bind-addr [0.0.0.0:8080]```

**以指定目录启动**

```code-server [/path/to/project]```

**禁用认证**

```code-server --auth none```

**使用特定配置**

```code-server --config [~/.config/code-server/config.yaml]```

**显示密码**

```cat ~/.config/code-server/config.yaml```

# SYNOPSIS

**code-server** [_options_] [_path_]

# DESCRIPTION

**code-server** 在远程服务器上运行 Visual Studio Code，使其可以通过任意网页浏览器访问。这让 Chromebook、平板电脑等无法原生运行 VS Code 的设备也能进行开发，同时保持一致的开发环境并完整访问服务器资源。

该服务提供的功能与桌面版 VS Code 几乎相同，包括扩展支持、终端访问和文件系统集成。它对远程开发、云工作区以及需要标准化环境的团队尤其有用。所有计算和存储都发生在服务器上，浏览器中只渲染界面。

认证可以基于密码，也可在受信任的网络中禁用。TLS 证书可启用安全的 HTTPS 连接。该工具由 Coder 开发，作为长期运行的服务运行，在生产部署中通常位于反向代理之后。

# PARAMETERS

**--bind-addr** _host:port_
> 要绑定的地址（默认：127.0.0.1:8080）

**--auth** _type_
> 认证方式：password、none

**--password** _pass_
> 设置密码（或使用 PASSWORD 环境变量）

**--cert** _file_
> TLS 证书文件

**--cert-key** _file_
> TLS 密钥文件

**--config** _file_
> 配置文件路径

**--user-data-dir** _dir_
> 用户数据目录

**--extensions-dir** _dir_
> 扩展目录

**--disable-telemetry**
> 禁用遥测

# CONFIGURATION

~/.config/code-server/config.yaml:
```yaml
bind-addr: 127.0.0.1:8080
auth: password
password: yourpassword
cert: false
```

# REQUIREMENTS

- 至少 1 GB 内存
- 2 个 vCPU
- 启用 WebSockets

# INSTALLATION

```
curl -fsSL https://code-server.dev/install.sh | sh
```

# CAVEATS

配置文件中包含默认密码。生产环境请使用 TLS。部分扩展可能无法在浏览器中使用。

# INSTALL

```brew: brew install code-server```

```nix: nix profile install nixpkgs#code-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[code](/man/code)(1), [vim](/man/vim)(1)

# RESOURCES

```[Source code](https://github.com/coder/code-server)```

```[Documentation](https://coder.com/docs/code-server)```

<!-- verified: 2026-06-22 -->
