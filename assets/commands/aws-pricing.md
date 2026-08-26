# TAGLINE

查询 AWS 服务定价信息

# TLDR

**列出** Price List API 可用的 **AWS 服务**

```aws pricing describe-services --region us-east-1```

**获取服务的属性值**（如 EC2 实例类型）

```aws pricing get-attribute-values --service-code [AmazonEC2] --attribute-name [instanceType] --region us-east-1```

带过滤器**获取产品价格**

```aws pricing get-products --service-code [AmazonEC2] --filters "Type=TERM_MATCH,Field=instanceType,Value=[t3.micro]" "Type=TERM_MATCH,Field=location,Value=[US East (N. Virginia)]" --region us-east-1```

**列出服务可用的价目表**

```aws pricing list-price-lists --service-code [AmazonEC2] --effective-date [2024-01-01] --currency-code USD --region us-east-1```

**获取批量价目表文件的下载 URL**

```aws pricing get-price-list-file-url --price-list-arn [arn:aws:pricing:::price-list/...] --file-format [json] --region us-east-1```

# SYNOPSIS

**aws pricing** _command_ [_options_]

# DESCRIPTION

**aws pricing** 是 AWS CLI 中访问 AWS Price List Query API 的接口，提供对 AWS 服务定价的编程式访问。它允许使用标准化的产品属性（如位置、实例类型、存储类别和操作系统）查询价格。

该 API 主要用于构建成本估算工具、预算预测和成本优化分析。价格按 SKU 返回，同时包含按需（On-Demand）和预留实例（Reserved Instance）两种定价选项。

# COMMANDS

**describe-services**
> 返回用于过滤的服务代码和属性名称。

**get-attribute-values**
> 返回给定服务属性的有效取值。

**get-products**
> 返回与所给过滤器匹配的产品及其价格。

**list-price-lists**
> 列出某服务和日期可用的批量价目表文件。

**get-price-list-file-url**
> 返回用于下载批量价目表文件的预签名 URL。

# PARAMETERS

**--service-code** _code_
> AWS 服务标识符（如 `AmazonEC2`、`AmazonS3`、`AmazonRDS`）。

**--filters** _filter_ ...
> 使用 `Type=TERM_MATCH,Field=_name_,Value=_value_` 按属性过滤产品。

**--region** _region_
> API 端点所在区域；必须为 `us-east-1`、`eu-central-1` 或 `ap-south-1`。

**--effective-date** _date_
> 要检索价格的生效日期（价格会随时间变化）。

**--currency-code** _code_
> 价目表的币种（如 `USD`、`CNY`）。

**--format-version** _version_
> 响应格式版本（`aws_v1`）。

# CAVEATS

Price List Query API 只能通过少数几个区域端点访问（通常是 **us-east-1** 和 **ap-south-1**）。结果集可能非常大，应尽量多使用 **--filters**。通过 **get-price-list-file-url** 下载的批量价目表文件可能有数 GB 之大。价格通常以美元计；并非所有服务都支持其他币种。

# HISTORY

AWS Price List API 于 **2015 年**上线，此前这些定价数据只能通过 AWS 控制台或静态批量 JSON 文件获取。Query API（**aws pricing**）随后加入，支持过滤式的按需查询，如今已成为成本感知自动化的标准组件。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ce](/man/aws-ce)(1), [aws-cur](/man/aws-cur)(1), [aws-budgets](/man/aws-budgets)(1)
