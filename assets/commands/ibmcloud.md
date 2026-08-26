# TAGLINE

管理 IBM Cloud 资源的命令行界面

# TLDR

**交互式登录**

```ibmcloud login```

**使用单点登录**

```ibmcloud login --sso```

使用 API 密钥**非交互式登录**

```ibmcloud login --apikey [API_KEY]```

**设置目标区域和资源组**

```ibmcloud target -r [us-south] -g [default]```

**列出资源实例**

```ibmcloud resource service-instances```

**显示账户信息**

```ibmcloud account show```

从 IBM Cloud 仓库**安装插件**

```ibmcloud plugin install [plugin-name]```

**列出已安装的插件**

```ibmcloud plugin list```

# SYNOPSIS

**ibmcloud** _command_ [_subcommand_] [_options_]

# PARAMETERS

**login** [**--sso**] [**--apikey** _KEY_] [**-r** _REGION_] [**-g** _GROUP_] [**-c** _ACCOUNT_ID_]
> 对 IBM Cloud 进行身份验证。`--sso` 使用单点登录，`--apikey` 使用平台 API 密钥。

**logout**
> 结束当前会话。

**target** [**-r** _REGION_] [**-g** _GROUP_] [**-o** _ORG_] [**-s** _SPACE_]
> 设置或显示当前目标区域、资源组、Cloud Foundry 组织或空间。

**account** _subcommand_
> 管理账户（例如 `account show`、`account users`、`account list`）。

**resource** _subcommand_
> 管理资源组和服务实例（例如 `resource groups`、`resource service-instances`、`resource service-instance-create`）。

**plugin** _subcommand_
> 管理插件：`install`、`uninstall`、`list`、`update`、`repo-plugins`。

**cf** _subcommand_
> Cloud Foundry 命令（需要 `cloud-foundry` 插件）。

**iam** _subcommand_
> 管理用户、服务 ID、API 密钥和访问策略。

**config** [**--http-timeout** _N_] [**--color** _on|off_] [**--locale** _LOCALE_] [**--check-version** _true|false_]
> 配置 CLI 行为（HTTP 超时、输出颜色、区域设置、版本检查）。

**--help**, **-h**
> 显示帮助。

**--version**
> 打印 CLI 版本。

# DESCRIPTION

**ibmcloud** 是 IBM Cloud 的官方命令行界面。它封装了 IBM Cloud 用于账户、IAM 和资源管理的 REST API，并通过可安装的插件提供各服务专属的功能。

大多数工作流以 `ibmcloud login` 开始，随后用 `ibmcloud target` 选择区域和资源组。之后即可通过 `resource`、`iam` 和各插件命令创建和管理服务、集群与函数。`kubernetes-service`、`code-engine`、`container-registry`、`cloud-databases` 等插件会添加相应服务的子命令。

# CONFIGURATION

**~/.bluemix/config.json**
> 存储会话、目标和配置信息。

**IBMCLOUD_API_KEY**
> 若设置，`ibmcloud login` 将用它进行非交互式身份验证。

**IBMCLOUD_HOME**
> 覆盖默认的 `~/.bluemix` 配置目录。

# CAVEATS

需要 IBM Cloud 账户以及访问 `cloud.ibm.com` 的网络连接。许多服务命令位于插件中，必须先安装。某些区域需要特定的资源组；在 `ibmcloud target` 之前运行命令常常会导致 "no target" 错误。

# HISTORY

**ibmcloud** 是 **IBM Cloud**（前身为 **Bluemix**）的官方 CLI。当前的二进制程序在 2018 年前后统一并取代了较旧的 `bluemix`（`bx`）CLI，随着 IBM 将 Bluemix 品牌重塑为 IBM Cloud，命令名也改为 `ibmcloud`。

# SEE ALSO

[aws](/man/aws)(1), [gcloud](/man/gcloud)(1), [az](/man/az)(1), [oc](/man/oc)(1), [kubectl](/man/kubectl)(1)
