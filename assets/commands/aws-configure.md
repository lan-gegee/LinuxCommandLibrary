# TAGLINE

配置 AWS CLI 的凭据、区域和输出格式。

# TLDR

**配置**默认凭据

```aws configure```

配置**指定配置文件**

```aws configure --profile [production]```

**设置**单个值

```aws configure set region [us-west-2]```

**获取**配置值

```aws configure get region```

**列出**所有配置文件

```aws configure list-profiles```

**配置** SSO 会话（交互式）

```aws configure sso```

# SYNOPSIS

**aws configure** [_options_] [_command_]

# DESCRIPTION

**aws configure** 管理 AWS CLI 的配置，包括凭据、默认区域和输出格式。设置存储在 ~/.aws/credentials 和 ~/.aws/config 文件中。

该工具既提供交互式界面来设置 AWS 访问，也可以通过编程方式读写单个配置值。

# PARAMETERS

**--profile** _name_
> 配置指定的命名配置文件

# SUBCOMMANDS

**list**
> 显示当前配置及每个值的来源

**get** _key_
> 获取单个配置值

**set** _key_ _value_
> 设置单个配置值

**import** _--csv file_
> 从 IAM 生成的 CSV 文件导入凭据

**list-profiles**
> 列出所有已配置的配置文件

**sso**
> 以交互方式配置 AWS IAM Identity Center（SSO）配置文件

**sso-session**
> 以交互方式配置可复用的 SSO 会话

**add-model**
> 向 CLI 添加自定义服务模型

# CONFIGURATION VALUES

**aws_access_key_id**
> AWS 访问密钥

**aws_secret_access_key**
> AWS 私有访问密钥

**region**
> 默认 AWS 区域

**output**
> 输出格式（json、text、table、yaml）

# WORKFLOW

交互式设置：
```bash
aws configure
```

# CONFIGURATION

**~/.aws/credentials**
> 存储每个命名配置文件的访问密钥 ID 和私有访问密钥。

**~/.aws/config**
> 存储每个命名配置文件的区域、输出格式和其他设置。

# CAVEATS

凭据以明文形式存储。在 EC2 上应尽量使用 IAM 角色代替凭据。切勿将凭据提交到版本控制系统。可考虑使用 aws-vault 进行更安全的凭据管理。使用 --profile 可避免覆盖默认凭据。

# HISTORY

**aws configure** 于 **2013 年** 随 AWS CLI 一同推出，是设置 AWS 凭据和配置的标准方式。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-vault](/man/aws-vault)(1), [aws-sso](/man/aws-sso)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/configure/index.html)```

<!-- verified: 2026-06-18 -->
