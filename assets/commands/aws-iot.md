# TAGLINE

管理 IoT 设备、证书和消息路由。

# TLDR

**列出所有 IoT 事物**

```aws iot list-things```

**创建新的事物**

```aws iot create-thing --thing-name [device_name]```

**查看事物详情**

```aws iot describe-thing --thing-name [device_name]```

**为设备创建密钥和证书**

```aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile [cert.pem] --private-key-outfile [private.key]```

**为证书附加策略**

```aws iot attach-policy --policy-name [policy_name] --target [certificate_arn]```

**将证书附加到事物**

```aws iot attach-thing-principal --thing-name [device_name] --principal [certificate_arn]```

**获取账户的 IoT 端点**

```aws iot describe-endpoint --endpoint-type iot:Data-ATS```

**列出证书**

```aws iot list-certificates```

# SYNOPSIS

**aws iot** _subcommand_ [_options_]

# DESCRIPTION

**aws iot** 是 AWS CLI 的子命令，用于管理 AWS IoT Core——一个将 IoT 设备连接到云端的平台。它负责设备注册表、安全和消息路由。

事物（thing）是物理设备在注册表中的表示。每个事物可拥有属性、类型和组以便组织管理。设备使用 X.509 证书进行认证，策略则控制它们可以执行的操作。

消息代理使用 MQTT、HTTPS 和 WebSocket 协议。规则引擎处理传入的消息，并将其路由到 Lambda、S3、DynamoDB 等 AWS 服务或其他 IoT 主题。

# PARAMETERS

**list-things**
> 列出已注册的事物。

**create-thing**
> 注册新的事物。

**describe-thing**
> 获取事物详情。

**delete-thing**
> 从注册表中移除事物。

**create-keys-and-certificate**
> 生成新的证书和密钥对。

**list-certificates**
> 列出账户中的证书。

**attach-policy**
> 将 IoT 策略附加到证书或身份。

**detach-policy**
> 移除策略附加关系。

**attach-thing-principal**
> 将证书与事物关联。

**describe-endpoint**
> 获取用于连接的 IoT 端点。

**create-policy**
> 创建 IoT 策略文档。

**list-thing-groups**
> 列出事物组。

**create-topic-rule**
> 创建用于路由消息的规则。

**search-index**
> 搜索事物索引。

**create-job**
> 为目标设备创建远程作业。

**list-topic-rules**
> 列出主题规则。

**--thing-name** _name_
> 事物名称。

**--certificate-pem-outfile** _file_
> 用于写入证书 PEM 的文件。

**--private-key-outfile** _file_
> 用于写入私钥的文件。

**--policy-name** _name_
> IoT 策略名称。

**--endpoint-type** _type_
> 端点类型（推荐 iot:Data-ATS）。

**--set-as-active**
> 将新建的证书设为激活状态。

**--target** _arn_
> 要附加策略的目标 ARN（证书或 Cognito 身份）。

# CAVEATS

证书必须先激活才能使用。删除事物不会删除其证书或策略。生产环境应使用 ATS（Amazon Trust Services）端点。事物名称在每个账户/区域内唯一。IoT 策略独立于 IAM 策略，遵循 IoT 特有的语法。

# HISTORY

**AWS IoT** 在 **AWS re:Invent 2015** 上发布，并于 **2016 年 1 月** 正式可用。该平台已扩展至面向边缘计算的 IoT Greengrass、用于数据分析的 IoT Analytics、用于设备车队运维的 IoT Device Management，以及面向工业数据的 IoT SiteWise。核心服务仍在持续演进，加入了车队预置（fleet provisioning）和可配置端点等特性。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [mosquitto](/man/mosquitto)(1), [aws-s3](/man/aws-s3)(1), [aws-lambda](/man/aws-lambda)(1)
