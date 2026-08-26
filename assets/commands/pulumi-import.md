# TAGLINE

将现有云资源导入 Pulumi

# TLDR

**按类型、名称和云 ID 导入现有资源**

```pulumi import [aws:s3/bucket:Bucket] [my-bucket] [my-bucket-id]```

**从 JSON 文件导入**

```pulumi import -f [resources.json]```

**导入并将生成的代码写入文件**

```pulumi import [type] [name] [id] -o [code.ts]```

**不带删除保护地导入**

```pulumi import --protect=false [type] [name] [id]```

**仅预览导入而不执行**

```pulumi import --preview-only [type] [name] [id]```

**导入并跳过确认提示**

```pulumi import -y [type] [name] [id]```

**仅导入指定的属性**

```pulumi import --properties [prop1,prop2] [type] [name] [id]```

# SYNOPSIS

**pulumi** **import** [_options_] _type_ _name_ _id_

# PARAMETERS

**-f**, **--file** _file_
> 从包含资源定义的 JSON 文件中导入资源。

**-o**, **--out** _file_
> 将生成的资源声明代码写入指定文件。

**--protect**
> 以启用删除保护的方式导入资源（默认：true）。

**--generate-code**
> 为导入的资源生成资源声明代码（默认：true）。

**--parent** _name=urn_
> 父资源名称和 URN，格式为 `name=urn`。

**--provider** _name=urn_
> Provider 资源名称和 URN，格式为 `name=urn`。

**--properties** _names_
> 用于导入的属性名列表，以逗号分隔。

**--preview-only**
> 仅显示导入的预览而不执行。

**--skip-preview**
> 执行导入前跳过预览计算。

**--diff**
> 以富文本差异形式显示整体变更。

**-s**, **--stack** _name_
> 要操作的目标堆栈。

**-p**, **--parallel** _n_
> 允许 N 个资源操作并行运行（默认：16）。

**-y**, **--yes**
> 预览后自动确认导入。

**-m**, **--message** _msg_
> 更新操作的可选消息。

**--from** _converter_
> 调用转换器来导入资源（例如从 Terraform 状态）。

**--suppress-outputs**
> 不显示堆栈输出（当其中包含敏感值时很有用）。

**-d**, **--debug**
> 操作过程中打印详细的调试输出。

**-j**, **--json**
> 将输出序列化为 JSON。

# DESCRIPTION

**pulumi import** 将现有的云资源导入 Pulumi 状态，并可选择生成管理它们所需的代码。这有助于将已有基础设施纳入 Pulumi 管理，而无需重新创建资源。

该命令需要资源类型（格式为 `provider:module/resource:Resource`）、该资源在 Pulumi 中的逻辑名称以及云提供商的资源 ID。导入后，资源会出现在堆栈状态中，后续的 `pulumi up` 操作将会管理它。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-up](/man/pulumi-up)(1), [pulumi-state](/man/pulumi-state)(1), [pulumi-preview](/man/pulumi-preview)(1), [pulumi-refresh](/man/pulumi-refresh)(1)
