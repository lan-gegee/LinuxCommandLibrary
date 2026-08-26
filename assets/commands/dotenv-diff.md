# TAGLINE

扫描并校验整个代码库中环境变量的使用情况

# TLDR

**扫描代码库**，找出缺失、未使用、重复和误用的环境变量

```dotenv-diff```

将运行时的 .env 文件与 .env.example 进行**比对**

```dotenv-diff --compare```

**比较指定文件**，包括它们的值

```dotenv-diff --compare --env [.env.production] --example [.env.example] --check-values```

**自动修复**缺失键和重复项等问题

```dotenv-diff --fix```

**解释单个变量**：定义位置、使用位置及其状态

```dotenv-diff --explain [DATABASE_URL]```

**生成默认配置文件**

```dotenv-diff --init```

在既有项目中引入该工具时，**将当前警告记录为基线**

```dotenv-diff --baseline```

**在 CI 中运行**，将警告视为错误

```dotenv-diff --ci --strict```

# SYNOPSIS

**dotenv-diff** [**--compare**] [**--env** _FILE_] [**--example** _FILE_] [_options_]

# DESCRIPTION

**dotenv-diff** 是一个 Node.js 命令行工具，扫描 JavaScript/TypeScript 代码库中的环境变量引用并在它们引发运行时错误之前加以校验。它能检测代码中使用但 .env 文件中缺失的变量、已定义但从未使用的变量、重复键、空值，以及被纳入版本控制的文件中意外出现的密钥。

在比较模式（**--compare**）下，它将运行时的 **.env** 文件与 **.env.example** 等参考文件进行对比，报告缺失键、多余键、空值、重复项，以及 .env 文件是否已列入 .gitignore。**--matrix** 模式可将多个环境文件中键的存在情况并排展示。

该工具对 SvelteKit、Next.js 和 Nuxt 提供一等支持，会对框架特有的误用发出警告，例如把仅限服务器端的变量暴露给客户端。未发现错误时退出状态为 **0**，出现错误时（严格模式下警告也算）为 **1**，因此适用于 git 钩子和 CI/CD 流水线。

它通过 npm 分发，可以用 ```npx dotenv-diff``` 免安装运行。

# OPTIONS

**--compare**

> 将运行时的 .env 文件与参考文件比较，而不是扫描代码库。

**--env** _FILE_

> 要检查的主环境文件（默认：.env）。

**--example** _FILE_

> 用于比较的参考文件（默认：.env.example）。

**--check-values**

> 在两个文件之间同时比较值和键。

**--only** _LIST_

> 将比较限制于特定问题：missing、extra、empty、duplicate、gitignore。

**--matrix** [_FILES_...]

> 并排比较多个 env 文件，显示每个键的存在位置。

**--fix**

> 自动修正缺失键和重复项等问题。

**--ignore** _KEYS_

> 从检查中排除特定键（逗号分隔）。

**--ignore-regex** _PATTERNS_

> 排除匹配正则表达式模式的键。

**--include-files** _PATTERNS_

> 在默认扫描模式基础上增加额外的文件，monorepo 场景很有用。

**--exclude-files** _PATTERNS_

> 在默认规则之外跳过指定文件。

**--explain** _KEY_

> 显示某变量在哪里定义、在哪里使用及其整体状态。

**--list-all**

> 列出扫描发现的所有唯一环境变量。

**--strict**

> 将警告视为错误并以失败码退出。

**--no-secrets**

> 跳过内置的密钥检测。

**--baseline**

> 把当前警告记录到基线文件中，使既有问题在后续运行中被忽略。

**--init**

> 生成默认配置文件。

**--json**

> 以 JSON 格式输出结果。

**--ci**

> 面向 CI/CD 流水线的非交互、只读模式。

**-y**, **--yes**

> 自动接受所有提示。

# CONFIGURATION

**dotenv-diff.config.json**

> 项目根目录下的可选配置文件。接受所有 CLI 标志的 camelCase 形式（如 ```allowDuplicates```、```ignoreRegex```）。命令行参数优先于文件设置。

内联忽略注释（```// dotenv-diff-ignore```）可抑制单行代码的警告，还可以在 .env 文件中用 ```# @expire YYYY-MM-DD``` 为变量附加过期日期，以便在凭据失效前收到警告。

# CAVEATS

需要 Node.js，面向 JavaScript/TypeScript 项目；代码库扫描查找的是 ```process.env.KEY``` 这类引用及框架特有模式，因此不会检测用其他语言读取的变量。若干检查（密钥检测、未使用变量报告、大写键强制、过期警告）默认启用，在非常规环境下可能需要用对应的 ```--no-``` 选项禁用。

# HISTORY

dotenv-diff 是 GitHub 用户 Chrilleweb 的 MIT 许可开源项目，**2025 年 7 月**首次发布于 npm。它起初只是一个简单的 .env 与 .env.example 差异工具，后来成长为具备框架感知、密钥检测和 CI 集成的代码库级环境变量扫描器；3.0.0 版本于 **2026 年 7 月**发布。

# SEE ALSO

[dotenvx](/man/dotenvx)(1), [direnv](/man/direnv)(1), [env](/man/env)(1), [envsubst](/man/envsubst)(1), [trufflehog](/man/trufflehog)(1)

# RESOURCES

```[Source code](https://github.com/Chrilleweb/dotenv-diff)```

```[Documentation](https://dotenv-diff-docs.vercel.app)```

<!-- verified: 2026-07-11 -->
