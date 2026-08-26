# TAGLINE

检测 Git 仓库中的机密信息和敏感数据

# TLDR

**扫描 Git 仓库的历史**

```gitleaks git [path/to/repo]```

**扫描磁盘上的目录**（不含 git 历史）

```gitleaks dir [path]```

**扫描管道输入**

```cat [file] | gitleaks stdin```

**写出 JSON 报告**

```gitleaks git --report-format json --report-path [report.json]```

**使用自定义配置并忽略基线**

```gitleaks git --config [.gitleaks.toml] --baseline-path [baseline.json]```

仍然接受已弃用的旧形式

```gitleaks detect --source [path]```

# SYNOPSIS

**gitleaks** _command_ [_options_]

# COMMANDS

**git** [_path_]
> 扫描 Git 仓库的提交日志。它是旧 `detect` 命令的替代品。

**dir** [_path_]（别名：**files**、**directory**）
> 扫描磁盘上的目录树，不参考 git。

**stdin**
> 从标准输入读取原始文本并进行扫描。适用于 pre-commit 钩子或通过管道传入 diff 输出。

**version**
> 打印 gitleaks 版本。

**completion** _shell_
> 为 bash、zsh、fish 或 powershell 输出 shell 补全脚本。

**detect**, **protect**
> 自 v8.19.0 起弃用但仍可使用；在 `--help` 中隐藏。建议改用 **git** 或 **stdin**。

# PARAMETERS

**-c**, **--config** _FILE_
> gitleaks TOML 配置文件的路径。

**-f**, **--report-format** _FORMAT_
> 输出格式：`json`、`csv`、`junit`、`sarif`、`template`。

**-r**, **--report-path** _FILE_
> 输出文件路径。不指定时结果只打印到终端。

**-b**, **--baseline-path** _FILE_
> 忽略先前报告中已存在的发现项（减少噪音）。

**-v**, **--verbose**
> 在发现每个问题时立即打印。

**-l**, **--log-level** _LEVEL_
> 日志详细程度（debug、info、warn、error）。

**--exit-code** _N_
> 检测到至少一个泄漏时使用的退出码（默认 `1`）。

**--max-decode-depth** _N_
> 递归解码 base64/hex 负载的最大深度。

**--max-archive-depth** _N_
> 深入归档文件（zip、tar 等）检查的最大深度。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gitleaks** 在文本中扫描 API 密钥、令牌和密码等机密信息。它可以检查 Git 仓库的全部提交日志、磁盘上的任意目录，或来自标准输入的数据流。

规则以正则表达式形式定义在自带的默认配置或用户提供的 `.gitleaks.toml` 中。每条规则都可附带白名单（路径、正则、停用词）来抑制已知误报。发现项可以导出为 JSON、CSV、JUnit 或 SARIF 格式供 CI 使用。

典型的 pre-commit 钩子会运行 `git diff --cached | gitleaks stdin --no-banner`；CI 任务则常用 `gitleaks git --exit-code 2 --report-format sarif --report-path leaks.sarif`。

# CONFIGURATION

**.gitleaks.toml**
> 自定义规则配置文件，定义正则模式、白名单和扫描行为。设置 `extend.useDefault = true` 可继承随附的默认规则集。

# CAVEATS

误报较为常见——请优化规则或添加白名单。大型仓库的历史扫描较慢；使用 **--baseline-path** 只跟踪新出现的发现项。旧的 `protect` 命令已被 `git`/`stdin` 取代。

# HISTORY

gitleaks 由 **Zachary Rice** 创建，用于应对机密信息被意外提交到 git 仓库的安全风险。8.19.0 版本将 CLI 重组为 **git**、**dir** 和 **stdin**，弃用了早期的 `detect`/`protect` 命令。

# INSTALL

```apt: sudo apt install gitleaks```

```dnf: sudo dnf install gitleaks```

```pacman: sudo pacman -S gitleaks```

```zypper: sudo zypper install gitleaks```

```brew: brew install gitleaks```

```nix: nix profile install nixpkgs#gitleaks```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trufflehog](/man/trufflehog)(1), [git-secret](/man/git-secret)(1), [detect-secrets](/man/detect-secrets)(1)
