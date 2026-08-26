# TAGLINE

Google Cloud 项目管理

# TLDR

**列出项目**

```gcloud projects list```

**创建项目**

```gcloud projects create [project_id]```

**查看项目详情**

```gcloud projects describe [project_id]```

**删除项目**

```gcloud projects delete [project_id]```

**设置 IAM 政策**

```gcloud projects set-iam-policy [project_id] [policy.json]```

# SYNOPSIS

**gcloud** **projects** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出当前账户有权查看的项目。

**create** _PROJECT_ID_ [**--name=**_NAME_] [**--organization=**_ORG_] [**--folder=**_FOLDER_]
> 创建新项目。ID 必须为 6–30 个字符，只能包含小写字母、数字或连字符。

**describe** _PROJECT_ID_
> 显示项目的元数据（名称、编号、生命周期状态、标签）。

**delete** _PROJECT_ID_
> 将项目标记为待删除（在永久移除前会软删除保留 30 天）。

**get-iam-policy** _PROJECT_ID_
> 输出绑定到该项目的 IAM 政策。

**set-iam-policy** _PROJECT_ID_ _POLICY_FILE_
> 用 JSON 或 YAML 文件中定义的政策替换现有 IAM 政策。

**add-iam-policy-binding** _PROJECT_ID_ **--member=**_MEMBER_ **--role=**_ROLE_
> 向项目的 IAM 政策添加单个成员/角色绑定。

**remove-iam-policy-binding** _PROJECT_ID_ **--member=**_MEMBER_ **--role=**_ROLE_
> 从项目的 IAM 政策中移除成员/角色绑定。

**update** _PROJECT_ID_
> 更新项目元数据，例如显示名称或标签。

**move** _PROJECT_ID_ **--organization=**_ORG_ | **--folder=**_FOLDER_
> 将项目移动到其他组织或文件夹。

**undelete** _PROJECT_ID_
> 在 30 天宽限期内恢复软删除的项目。

# DESCRIPTION

**gcloud projects** 提供管理 Google Cloud 项目的命令。项目是 GCP 中最基本的组织单元，Google Cloud 中的每个资源都恰好属于一个项目，项目是计费、访问控制和资源隔离的基础。

该命令组支持完整的项目生命周期，包括创建、删除以及恢复软删除的项目。它还负责项目级别的 IAM 政策管理，控制哪些主体有权访问项目资源。

项目包含若干设置：项目 ID（不可变）、项目名称（可更改）和项目编号（由 Google 分配）。由于计费按项目追踪，理解项目管理对于在 Google Cloud 中组织资源和管理成本至关重要。

# SEE ALSO

[gcloud](/man/gcloud)(1), [gcloud-config](/man/gcloud-config)(1)
