# TAGLINE

审计 Kubernetes 集群和清单中的安全漏洞

# TLDR

**审计运行中的集群**

```kubeaudit all```

**审计清单文件**

```kubeaudit all -f [deployment.yaml]```

**运行指定审计器**

```kubeaudit [privileged] -f [manifest.yaml]```

**在集群内审计**

```kubeaudit all -c [cluster]```

**以 JSON 格式输出**

```kubeaudit all -f [manifest.yaml] -p json```

**审计指定命名空间**

```kubeaudit all -n [namespace]```

**自动修复清单文件**

```kubeaudit autofix -f [manifest.yaml]```

# SYNOPSIS

**kubeaudit** [_auditor_] [_options_]

# PARAMETERS

**all**
> 运行所有审计器。

**-f** _file_
> 审计清单文件。

**-d** _dir_
> 审计清单目录。

**-c**, **--context** _name_
> Kubernetes 上下文。

**-n**, **--namespace** _name_
> 目标命名空间。

**-p**, **--format** _format_
> 输出格式：logrus、json、sarif。

**--kubeconfig** _path_
> kubeconfig 文件的路径。

**--minSeverity** _level_
> 报告的最低严重级别（error、warning、info）。

# AUDITORS

```
privileged       Privileged containers
capabilities     Added capabilities
rootfs           Read-only root filesystem
runAsNonRoot     Running as root user
limits           Resource limits
hostns           Host namespace usage
seccomp          Seccomp profile
apparmor         AppArmor profile
image            Image tag requirements
automountServiceAccountToken  Service account token
```

# DESCRIPTION

**kubeaudit** 审计 Kubernetes 集群和清单中的安全漏洞。它依据安全最佳实践检查配置。

该工具可以审计运行中的集群、本地清单或两者，提供可操作的发现结果以改善集群安全。

# CAVEATS

某些发现可能是有意为之的配置。集群审计需要相应权限。特殊工作负载可能出现误报。

# HISTORY

kubeaudit 由 **Shopify** 创建，用于在 Kubernetes 部署进入生产环境之前识别安全风险。

# INSTALL

```zypper: sudo zypper install kubeaudit```

```brew: brew install kubeaudit```

```nix: nix profile install nixpkgs#kubeaudit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kube-linter](/man/kube-linter)(1), [trivy](/man/trivy)(1)
