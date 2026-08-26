# TAGLINE

用于管理 Marzban 代理面板的 CLI 工具

# TLDR

**列出**所有管理员

```marzban cli admin list```

**创建**新管理员

```marzban cli admin create -u [username]```

**列出**所有用户

```marzban cli user list```

**转移**用户的所有权给另一个管理员

```marzban cli user set-owner -u [username] --owner [owner]```

为用户生成**订阅配置**

```marzban cli subscription get-config -u [username] -f [v2ray|clash]```

显示用户的**订阅链接**

```marzban cli subscription get-link -u [username]```

显示**帮助**

```marzban cli --help```

# SYNOPSIS

**marzban cli** [_OPTIONS_] _COMMAND_ [_ARGS_]...

# PARAMETERS

**admin**
> 管理面板管理员（`create`、`delete`、`list`、`update`、`import-from-env`）

**user**
> 管理用户（`list`、`set-owner`）

**subscription**
> 订阅辅助命令（`get-config`、`get-link`）

**completion**
> 生成或安装 shell 补全脚本

**admin create** **-u** _username_
> 创建管理员；可选 `--sudo`、`-tg`/`--telegram-id`、`-dc`/`--discord-webhook`

**user list**
> 列出用户；可用 `-u`、`-s`/`--search`、`--status`、`--admin`/`--owner` 过滤

**subscription get-config** **-u** _username_ **-f** {_v2ray_|_clash_}
> 生成订阅配置；可选 `-o`/`--output` 和 `--base64`

**subscription get-link** **-u** _username_
> 打印订阅 URL（需要设置 `XRAY_SUBSCRIPTION_URL_PREFIX`）

# DESCRIPTION

**marzban cli** 是 [Marzban](https://github.com/Gozargah/Marzban) 的命令行界面。Marzban 是一个围绕 Xray 构建的开源代理管理面板。该 CLI 无需使用 Web UI 即可管理管理员、用户和订阅内容。

管理员密码可以通过 `MARZBAN_ADMIN_PASSWORD` 非交互式提供。`admin import-from-env` 会根据 `SUDO_USERNAME`/`SUDO_PASSWORD` 创建一个 sudo 管理员，并将无主用户挂到它名下。

# CAVEATS

需要已正常运行的 Marzban 安装和数据库访问权限（通常在面板主机上运行）。`subscription get-link` 需要正确设置 `XRAY_SUBSCRIPTION_URL_PREFIX`。`admin update` 仅支持交互式操作。

# HISTORY

属于 **Marzban** 的一部分，Marzban 是 Gozargah 开发的基于 Python 的多协议代理面板。

# SEE ALSO

[curl](/man/curl)(1), [docker](/man/docker)(1)

# RESOURCES

```[Source code](https://github.com/Gozargah/Marzban)```

```[Documentation](https://github.com/Gozargah/Marzban/blob/master/cli/README.md)```

<!-- verified: 2026-07-28 -->
