# TAGLINE

GCP 云安全评估

# TLDR

对所有可访问的项目**运行 GCP 安全评估**

```prowler gcp```

**扫描特定项目**

```prowler gcp --project-ids [project-id-1] [project-id-2]```

**只运行特定检查项**

```prowler gcp --checks [cloudstorage_bucket_public_access]```

**只运行特定服务**的检查

```prowler gcp --services [iam] [compute]```

**按某个合规框架运行**

```prowler gcp --compliance [cis_2.0_gcp]```

**模拟服务账号身份**

```prowler gcp --impersonate-service-account [name@project.iam.gserviceaccount.com]```

**列出可访问的 GCP 项目**

```prowler gcp --list-project-ids```

**跳过 API 启用检查**

```prowler gcp --skip-api-check```

# SYNOPSIS

**prowler** **gcp** [_options_]

# PARAMETERS

**--project-ids** _ID_...
> 只扫描给定的 GCP 项目 ID（默认：所有可访问的项目）。

**--excluded-project-ids** _ID_...
> 从扫描中排除给定的项目 ID。

**--list-project-ids**
> 列出当前凭据可访问的所有 GCP 项目 ID，然后退出。

**--credentials-file** _PATH_
> 服务账号应用凭据 JSON 文件的路径。

**--impersonate-service-account** _EMAIL_
> 调用 API 时模拟指定的服务账号。

**--skip-api-check**
> 跳过 API 启用验证，假定所有必需的 API 均已启用。

**-c**, **--checks** _CHECK_...
> 只运行指定的检查项。

**-s**, **--services** _SERVICE_...
> 只运行针对指定 GCP 服务的检查（如 _iam_、_compute_、_cloudstorage_）。

**--compliance** _FRAMEWORK_
> 运行指定的合规框架（如 _cis_2.0_gcp_、_mitre_attack_gcp_）。

**-M**, **--output-modes** _FORMAT_
> 输出格式：_csv_、_json-ocsf_、_json-asff_、_html_。

**-F**, **--output-filename** _NAME_
> 输出文件的基础名称。

**-o**, **--output-directory** _DIR_
> 输出报告写入的目录。

# DESCRIPTION

**prowler gcp** 对 Google Cloud Platform 项目执行安全评估。它依据 CIS、MITRE ATT&CK、GDPR 等最佳实践和合规框架评估配置，并以 CSV、JSON 或 HTML 报告的形式呈现结果。

默认情况下，Prowler 会扫描经过身份验证的主体可访问的每个项目。身份验证可以使用应用默认凭据（ADC）、凭据文件或服务账号模拟。

# CAVEATS

需要具有目标项目至少 _Viewer_ 和 _Security Reviewer_ 角色的有效 GCP 凭据。部分检查需要启用额外的 API（Cloud Asset、Cloud Resource Manager、IAM）。大型组织的速率限制可能会显著拖慢扫描速度。

# INSTALL

```brew: brew install prowler```

```nix: nix profile install nixpkgs#prowler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[prowler](/man/prowler)(1), [prowler-aws](/man/prowler-aws)(1), [prowler-azure](/man/prowler-azure)(1), [prowler-kubernetes](/man/prowler-kubernetes)(1), [gcloud](/man/gcloud)(1)
