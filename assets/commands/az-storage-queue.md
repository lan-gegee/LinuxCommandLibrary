# TAGLINE

管理 Azure 队列存储和消息

# TLDR

**创建队列**

```az storage queue create --name [myqueue] --account-name [mystorageaccount]```

**列出所有队列**

```az storage queue list --account-name [mystorageaccount]```

**删除队列**

```az storage queue delete --name [myqueue] --account-name [mystorageaccount]```

**向队列添加消息**

```az storage message put -q [myqueue] --content [Hello World] --account-name [mystorageaccount]```

**获取（出队）消息**，并在可见性超时期间将其隐藏

```az storage message get -q [myqueue] --num-messages [5] --visibility-timeout [30] --account-name [mystorageaccount]```

**窥探（peek）消息**，不移除也不隐藏

```az storage message peek -q [myqueue] --num-messages [5] --account-name [mystorageaccount]```

**从队列删除消息**

```az storage message delete --id [message-id] --pop-receipt [receipt] -q [myqueue] --account-name [mystorageaccount]```

# SYNOPSIS

**az** **storage** **queue** _subcommand_ [_options_]

**az** **storage** **message** _subcommand_ [_options_]

# SUBCOMMANDS

**create**
> 在给定账户下创建队列。

**delete**
> 删除队列及其包含的所有消息。

**list**
> 列出存储账户中的队列。

**exists**
> 返回指示队列是否存在的布尔值。

**generate-sas**
> 为队列生成共享访问签名。

**stats**
> 获取队列服务的复制统计信息（需要 RA-GRS）。

**metadata show**
> 返回队列的所有用户定义元数据。

**metadata update**
> 设置队列的用户定义元数据。

**policy create / delete / list / show / update**
> 管理队列的存储访问策略。

**message put / get / peek / delete / update / clear**
> 管理队列消息。这些子命令位于 **az storage message** 下，而不是 **az storage queue** 下。

# PARAMETERS

**--name** **-n**
> 队列的名称（用于 queue 子命令）。

**--queue-name** **-q**
> 队列的名称（用于 **az storage message** 子命令）。

**--account-name**
> 存储账户名。环境变量：AZURE_STORAGE_ACCOUNT。

**--account-key**
> 存储账户密钥。环境变量：AZURE_STORAGE_KEY。

**--connection-string**
> 存储连接字符串。环境变量：AZURE_STORAGE_CONNECTION_STRING。

**--auth-mode** _value_
> 身份验证模式：key（旧式账户密钥）或 login（Azure AD 凭据）。

**--content**
> **message put** 和 **message update** 的消息内容，最大 64 KB。

**--visibility-timeout** _seconds_
> 将取回的消息对其他使用者隐藏指定的秒数（1 秒至 7 天）。

**--time-to-live** _seconds_
> **message put** 时消息的生存期。-1 表示无限。默认 7 天。

**--num-messages** _value_
> 要获取或窥探的消息数量，最多 32 条。默认 1。

# DESCRIPTION

**az storage queue** 管理 Azure 队列存储（Queue Storage），它在应用程序组件之间提供云消息传递能力。队列可实现异步通信和解耦架构。

消息大小最大为 64 KB，默认生存时间（time-to-live）为 7 天。单个消息通过 **az storage message** 命令组管理（put、get、peek、delete、update、clear）。

# CAVEATS

**az storage queue** 和 **az storage message** 命令组目前处于预览阶段。需要 Azure CLI 和有效的存储凭据（账户密钥、连接字符串、SAS 令牌或 `--auth-mode login`）。队列名称必须为 3-63 个字符，只能包含小写字母、数字和连字符。执行 **get** 后，消息会在可见性超时期间保持隐藏；若在超时结束前未删除，消息会重新出现，因此使用者必须使用返回的消息 ID 和 pop receipt 来删除消息。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [azure-cli](/man/azure-cli)(1), [az-storage](/man/az-storage)(1), [az-storage-table](/man/az-storage-table)(1), [az-storage-account](/man/az-storage-account)(1)

# RESOURCES

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/storage/queue)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

```[Source code](https://github.com/Azure/azure-cli)```

<!-- verified: 2026-06-19 -->
