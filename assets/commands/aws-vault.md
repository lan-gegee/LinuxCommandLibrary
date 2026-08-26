# TAGLINE

在系统钥匙串中安全地存储和访问 AWS 凭证。

# TLDR

**添加** AWS 凭证

```aws-vault add [profile-name]```

使用凭证**执行**命令

```aws-vault exec [profile-name] -- aws s3 ls```

**登录** AWS 控制台

```aws-vault login [profile-name]```

**列出**已存储的凭证

```aws-vault list```

**移除**凭证

```aws-vault remove [profile-name]```

**轮换**凭证

```aws-vault rotate [profile-name]```

# SYNOPSIS

**aws-vault** _command_ [_options_] _profile_

# DESCRIPTION

**aws-vault** 使用操作系统的钥匙串安全地存储和访问 AWS 凭证。它通过 STS 生成临时凭证，避免在纯文本文件中保存长期访问密钥。

该工具为 AWS 凭证提供纵深防御的安全保障，并支持在多个 AWS 账户之间轻松切换。

# PARAMETERS

**add** _profile_
> 将新凭证添加到钥匙串

**exec** _profile_ **--** _command_
> 使用临时凭证执行命令

**login** _profile_
> 在浏览器中打开 AWS 控制台

**list**
> 列出 profile 和会话状态

**remove** _profile_
> 从钥匙串移除凭证

**rotate** _profile_
> 轮换访问密钥

**export** _profile_
> 将凭证导出为环境变量。

**clear** _profile_
> 清除会话存储中的临时凭证。

**--duration=**_time_
> 会话时长（如 12h、1h30m）。

**--mfa-token=**_token_
> MFA 验证码。

**--no-session**
> 不创建 STS 会话而直接使用长期凭证。

**--server**
> 启动本地 EC2 元数据服务器，而不使用环境变量。

**--backend=**_backend_
> 凭证存储后端（keychain、kwallet、pass、secret-service、file）。

# FEATURES

- 在系统钥匙串中安全存储凭证
- 自动提示输入 MFA
- 生成临时凭证
- 支持多个 AWS 账户
- 凭证轮换
- 生成控制台登录链接

# WORKFLOW

```bash
aws-vault add work
aws-vault exec work -- aws s3 ls
aws-vault exec work
aws-vault login work
```

# CONFIGURATION

**~/.aws/config**
> AWS profile 设置，包括 role_arn、source_profile、mfa_serial 和 region。

**~/.aws/credentials**
> 主凭证保存在系统钥匙串中；此文件用于发现 profile。

# CAVEATS

需要访问系统钥匙串（macOS Keychain、GNOME Keyring 等）。必须在 AWS 中配置好 MFA 设备。临时凭证会过期。某些工具无法使用会话凭证。

# HISTORY

**aws-vault** 由 99designs 于 **2015 年**创建，旨在为 AWS 提供安全的凭证管理，解决以明文形式存放凭证带来的安全风险。

# INSTALL

```pacman: sudo pacman -S aws-vault```

```brew: brew install aws-vault```

```nix: nix profile install nixpkgs#aws-vault```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-configure](/man/aws-configure)(1), [pass](/man/pass)(1)
