# TAGLINE

代码中的机密与凭据扫描器

# TLDR

扫描 git 仓库

```trufflehog git [https://github.com/user/repo]```

扫描本地 git 仓库

```trufflehog git file://[/path/to/repo]```

扫描文件系统

```trufflehog filesystem [/path/to/scan]```

扫描 GitHub 组织

```trufflehog github --org [organization]```

扫描 S3 存储桶

```trufflehog s3 --bucket [bucket-name]```

仅显示已验证的机密

```trufflehog git --only-verified [https://github.com/user/repo]```

输出为 JSON

```trufflehog git --json [https://github.com/user/repo]```

扫描特定分支

```trufflehog git --branch [main] [https://github.com/user/repo]```

# SYNOPSIS

**trufflehog** _source_ [_--only-verified_] [_--json_] [_options_] _target_

# PARAMETERS

**git** _URL_
> 扫描 git 仓库。

**github**
> 扫描 GitHub（组织、用户或仓库）。

**gitlab**
> 扫描 GitLab。

**filesystem** _PATH_
> 扫描本地文件系统。

**s3**
> 扫描 S3 存储桶。

**gcs**
> 扫描 Google Cloud Storage。

**docker**
> 扫描 Docker 镜像。

**--only-verified**
> 仅报告经过验证的凭据。

**--json**
> 输出为 JSON。

**--no-update**
> 不检查更新。

**--concurrency** _NUM_
> 扫描并发数。

**--include-paths** _FILE_
> 只扫描匹配的路径。

**--exclude-paths** _FILE_
> 跳过匹配的路径。

**--include-detectors** _LIST_
> 只使用指定的检测器。

**--exclude-detectors** _LIST_
> 跳过指定的检测器。

**--branch** _NAME_
> 扫描特定分支。

**--since-commit** _HASH_
> 从指定提交开始。

**--max-depth** _NUM_
> 最大提交历史深度。

**--no-verification**
> 跳过针对相关服务的凭据验证。

# DESCRIPTION

**trufflehog** 在代码仓库、文件系统和云存储中查找机密信息和凭据。它使用数百个检测器来识别 API 密钥、密码和令牌。

该工具会扫描 git 历史，捕捉那些曾经提交、后来又被删除的机密。每个提交都会与检测器模式进行比对。高熵字符串会被标记为潜在的机密。

验证模式 (--only-verified) 会主动向相应服务测试找到的凭据。这能确认机密是否仍然有效，从而优先呈现真实泄露而非误报。

检测器覆盖主流服务：AWS、GCP、Azure、GitHub、Slack、Stripe、Twilio 等等。自定义正则模式可以扩展检测能力。

多种源类型支持全面扫描：仓库、组织、云存储、Docker 镜像和本地文件系统。

JSON 输出可与安全工具和 CI/CD 流水线集成。退出码表明是否发现机密，便于实现自动化门禁。

# CAVEATS

验证过程会向第三方服务发起网络请求。扫描大型仓库的历史较慢。高熵字符串可能产生误报。加密或混淆过的机密可能被漏掉。验证可能触发安全警报。

# HISTORY

**trufflehog** 由 **Truffle Security** 的 **Dylan Ayrey** 于 **2016 年**前后创建。最初是一个 Python 工具，第 3 版为提升性能改用 Go 重写。该项目旨在解决机密信息被提交到版本控制这一严重问题，在泄露发生之前实现自动化检测。

# INSTALL

```zypper: sudo zypper install trufflehog```

```brew: brew install trufflehog```

```nix: nix profile install nixpkgs#trufflehog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gitleaks](/man/gitleaks)(1), [git-secrets](/man/git-secrets)(1), [detect-secrets](/man/detect-secrets)(1)
