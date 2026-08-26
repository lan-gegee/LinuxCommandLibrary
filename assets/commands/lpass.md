# TAGLINE

LastPass 密码管理器的命令行界面

# TLDR

**登录 LastPass**

```lpass login [user@example.com]```

**显示某网站的密码**

```lpass show --password [sitename]```

**复制密码到剪贴板**

```lpass show --clip --password [sitename]```

**列出所有账户**

```lpass ls```

**搜索条目**

```lpass show -G [pattern]```

**添加新密码**

```lpass add [Folder/sitename]```

**生成一个密码**

```lpass generate [sitename] [20]```

**登出**

```lpass logout```

# SYNOPSIS

**lpass** _command_ [_options_] [_arguments_]

# PARAMETERS

**login** _EMAIL_
> 向 LastPass 进行身份验证。

**logout**
> 结束会话并清除缓存。

**show** _NAME_
> 显示条目详情。

**ls** [_GROUP_]
> 列出条目，可按分组筛选。

**add** _NAME_
> 以交互方式添加新条目。

**edit** _NAME_
> 修改现有条目。

**rm** _NAME_
> 删除条目。

**generate** _NAME_ _LENGTH_
> 生成随机密码并保存。

**sync**
> 将本地缓存与服务器同步。

**export**
> 将密码库导出为 CSV。

**import** _FILE_
> 从 CSV 导入条目。

**--password**
> 仅显示密码字段。

**--username**
> 仅显示用户名字段。

**--url**
> 仅显示 URL 字段。

**--clip**, **-c**
> 复制到剪贴板而不是打印。

**-G**, **--basic-regexp**
> 使用正则表达式匹配。

**--sync=auto|now|no**
> 控制同步行为。

**--color=auto|always|never**
> 控制彩色输出。

# DESCRIPTION

**lpass** 是 LastPass 密码管理器的命令行界面。它让你可以在终端中完整访问自己的密码库，支持以脚本方式获取和管理密码。

身份验证会创建加密的本地缓存。代理进程会保持会话有效，避免重复输入主密码。会话超时时间可通过 LPASS_AGENT_TIMEOUT 环境变量配置。

条目按文件夹组织，支持完整路径（如 "Work/email"）。字段包括用户名、密码、URL 和备注。安全备注可存储任意文本，也支持自定义字段。

在自动化场景中，**--clip** 会通过管道传给剪贴板工具，**--password** 只输出凭据本身供脚本使用。**generate** 命令可生成满足复杂度要求的随机密码。

通过网页密码库提供的共享和企业功能仅部分受支持。两步验证支持 TOTP 应用。

# CAVEATS

首次同步需要联网。本地缓存虽经加密但仍存在于磁盘上。剪贴板内容可能被某些系统记录。代理超时时长关系到安全与便利的取舍。部分企业功能无法通过 CLI 使用。LastPass 数据泄露事件（2022 年）引发了安全方面的担忧。

# HISTORY

**lpass** 由 **LastPass** 开发，约于 **2014 年**开源。它为 LastPass 服务提供命令行访问能力；LastPass 公司创立于 **2008 年**，于 **2015 年**被 LogMeIn 收购，后来又出售给私募股权。尽管面临 Bitwarden、1Password 等工具的竞争，这款 CLI 工具在自动化和终端工作流中依然广受欢迎。

# INSTALL

```dnf: sudo dnf install lastpass-cli```

```apk: sudo apk add lastpass-cli```

```brew: brew install lastpass-cli```

```nix: nix profile install nixpkgs#lastpass-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [rbw](/man/rbw)(1), [bw](/man/bw)(1), [gopass](/man/gopass)(1), [keepassxc-cli](/man/keepassxc-cli)(1)
