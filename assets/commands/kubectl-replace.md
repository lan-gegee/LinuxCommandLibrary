# TAGLINE

按文件名或 stdin 替换资源

# TLDR

**从文件替换资源**

```kubectl replace -f [manifest.yaml]```

**强制替换（删除并重建）**

```kubectl replace --force -f [manifest.yaml]```

**从 stdin 替换**

```cat [manifest.yaml] | kubectl replace -f -```

**试运行而不应用更改**

```kubectl replace -f [manifest.yaml] --dry-run=client```

**替换并处理 kustomization 目录**

```kubectl replace -k [directory/]```

**从多个文件替换资源**

```kubectl replace -f [file1.yaml] -f [file2.yaml]```

# SYNOPSIS

**kubectl** **replace** **-f** _FILENAME_ [_options_]

# PARAMETERS

**-f**, **--filename** _file_
> 用于替换资源的文件名、目录或 URL。

**-k**, **--kustomize** _dir_
> 处理 kustomization 目录。不能与 -f 或 -R 一起使用。

**-R**, **--recursive**
> 递归处理 -f 使用的目录。

**--force**
> 如果为 true，立即从 API 移除资源并跳过优雅删除。

**--cascade** _mode_
> 对依赖资源的级联删除策略："background"、"orphan" 或 "foreground"。默认："background"。

**--grace-period** _seconds_
> 给予资源优雅终止的时间（秒）。负值时忽略。默认：-1。

**--dry-run** _strategy_
> 必须是 "none"、"server" 或 "client"。默认："none"。

**--validate** _mode_
> 校验模式："strict"、"warn" 或 "ignore"。默认："strict"。

**-o**, **--output** _format_
> 输出格式：json、yaml、name、go-template、jsonpath 等。

**--save-config**
> 将当前对象的配置保存到其注解中，以便日后配合 kubectl apply 使用。

**--field-manager** _name_
> 用于跟踪字段所有权的管理器名称。默认："kubectl-replace"。

**--subresource** _name_
> 如果指定，replace 将操作请求对象的子资源。

**--timeout** _duration_
> 放弃删除前的等待时长。

**--wait**
> 如果为 true，等待资源消失后再返回。

**--raw** _URI_
> 要 PUT 到服务器的原始 URI。

# DESCRIPTION

**kubectl replace** 按文件名或 stdin 替换资源。接受 JSON 和 YAML 格式。资源必须已存在。与 apply 不同，replace 需要完整的资源配置，可以通过 `kubectl get TYPE NAME -o yaml` 获取。使用 --force 可删除并重建资源。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-apply](/man/kubectl-apply)(1), [kubectl-create](/man/kubectl-create)(1), [kubectl-delete](/man/kubectl-delete)(1), [kubectl-edit](/man/kubectl-edit)(1), [kubectl-patch](/man/kubectl-patch)(1)
