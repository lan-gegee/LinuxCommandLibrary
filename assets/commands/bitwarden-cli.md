# TAGLINE

在终端中管理密码与机密信息

# TLDR

**登录 Bitwarden**

```bw login [email]```

**解锁密码库**

```bw unlock```

**列出所有条目**

```bw list items```

**搜索某个密码**

```bw list items --search [query]```

**按 ID 获取指定条目**

```bw get item [item_id]```

**获取某条目的密码**

```bw get password [item_id]```

**创建新的登录条目**

```echo '[json]' | bw create item```

**生成一个密码**

```bw generate -ulns --length [20]```

**同步密码库**

```bw sync```

# SYNOPSIS

**bw** _command_ [_options_]

# PARAMETERS

**login** [_email_]
> 向 Bitwarden 服务器进行身份验证。

**unlock**
> 用主密码解锁密码库。

**lock**
> 锁定密码库。

**sync**
> 与 Bitwarden 服务器同步。

**list** _object_
> 列出对象（items、folders、collections、organizations、org-members、org-collections、send）。

**get** _object_ _id_
> 获取指定对象（item、password、username、uri、totp、notes、exposed、attachment、folder、template）。

**create** _object_
> 创建新对象（item、folder、attachment、org-collection）；接受 base64 编码的 JSON。

**edit** _object_ _id_
> 编辑已有对象（item、folder、org-collection）。

**delete** _object_ _id_
> 删除对象。使用 **--permanent** 可跳过回收站直接永久删除。

**restore** _object_ _id_
> 从回收站恢复对象。

**import** _format_ _path_
> 从第三方格式或 JSON 导出文件导入数据。

**export**
> 导出密码库。选项：**--format** json|csv|encrypted_json，**--output** _path_。

**generate**
> 生成密码或口令短语（passphrase）。

**encode**
> 对标准输入进行 Base64 编码（常用于将 JSON 管道传给 create/edit）。

**status**
> 以 JSON 显示状态（服务器 URL、上次同步时间、邮箱、密码库状态）。

**serve**
> 启动本地 REST API 服务器（**--port**，**--hostname**）。

**config** _setting_ _value_
> 配置 CLI 设置（如 `bw config server <url>`）。

**--session** _key_
> unlock 返回的会话密钥（或设置 BW_SESSION 环境变量）。

**--search** _query_
> list 命令的搜索过滤条件。

**--pretty**
> 格式化输出 JSON。

**--raw**
> 输出原始值而非 JSON。

**--nointeraction**
> 不提示输入（用于脚本）。

**-u**, **-l**, **-n**, **-s**
> 密码生成选项：大写字母、小写字母、数字、特殊字符。

**--length** _n_
> 生成密码的长度（最小为 5）。

**--passphrase**
> 生成口令短语而非密码（配合 **--words**、**--separator**、**--capitalize** 使用）。

# DESCRIPTION

**bw** 是开源密码管理器 Bitwarden 的官方命令行接口。它让你从终端完全访问加密的密码库，可用于取回密码、管理条目以及与脚本和自动化集成。

登录后必须用主密码解锁密码库。解锁会返回一个会话密钥，后续命令需通过 **--session** 或 **BW_SESSION** 环境变量提供该密钥。密码库会在超时后自动锁定。

条目以 JSON 形式表示，因此该 CLI 非常适合脚本编写和与其他工具集成。generate 命令可创建安全密码且不会存储它们。

# CAVEATS

会话密钥可完全访问你的密码库，务必妥善保护。命令默认输出 JSON，可能需要用 jq 解析。大多数操作前必须先解锁密码库。自托管实例可能受 API 速率限制。

# HISTORY

Bitwarden 由 **Kyle Spearrin** 创立，于 **2016 年**发布，作为专有密码管理器的开源替代品。CLI 的推出是为了补充网页端、桌面端和移动端应用。Bitwarden 已成长为最受欢迎的密码管理器之一，以其透明的开源模式和实惠的价格著称。

# INSTALL

```pacman: sudo pacman -S bitwarden-cli```

```brew: brew install bitwarden-cli```

```nix: nix profile install nixpkgs#bitwarden-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [gopass](/man/gopass)(1), [keepassxc-cli](/man/keepassxc-cli)(1), [op](/man/op)(1)
