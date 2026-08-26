# TAGLINE

SonarQube 静态代码分析扫描器

# TLDR

**运行分析**

```sonar-scanner```

**指定项目键**

```sonar-scanner -Dsonar.projectKey=[myproject]```

**指定服务器**

```sonar-scanner -Dsonar.host.url=[http://localhost:9000]```

**使用身份验证令牌**

```sonar-scanner -Dsonar.token=[token]```

**设置源码目录**

```sonar-scanner -Dsonar.sources=[src]```

**调试模式**

```sonar-scanner -X```

**指定配置文件**

```sonar-scanner -Dproject.settings=[sonar-project.properties]```

# SYNOPSIS

**sonar-scanner** [_-D property=value_] [_-X_] [_options_]

# PARAMETERS

**-D** _PROPERTY=VALUE_
> 设置属性。

**-X**, **--debug**
> 调试输出。

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 显示版本。

# PROPERTIES

**sonar.projectKey** - 项目标识符
**sonar.host.url** - 服务器 URL
**sonar.token** - 身份验证令牌（替代已弃用的 sonar.login）
**sonar.sources** - 源码目录
**sonar.language** - 语言
**sonar.exclusions** - 排除模式
**sonar.inclusions** - 包含模式
**sonar.sourceEncoding** - 源文件编码（默认：系统编码）
**sonar.verbose** - 启用详细输出（true/false）

# DESCRIPTION

**sonar-scanner** 为 SonarQube/SonarCloud 执行静态分析。它扫描代码中的 bug、漏洞和代码异味（code smells）。

可通过属性或文件进行配置。sonar-project.properties 用于定义项目。

分析结果上传到服务器。Web 界面展示发现的问题。

支持多种语言，包括 Java、JavaScript、Python 等众多语言。

CI 集成可自动化扫描。可在每次构建或拉取请求时运行。

# CONFIGURATION

**sonar-project.properties**
> 项目级配置文件，用于定义项目键、源码目录、语言和排除模式。

**SONAR_TOKEN**
> 用于向 SonarQube 或 SonarCloud 进行身份验证的令牌环境变量。

**SONAR_HOST_URL**
> 指定 SonarQube 服务器 URL 的环境变量。

# CAVEATS

需要 SonarQube/SonarCloud 实例。上传需要令牌。大型项目耗时较长。

# HISTORY

**SonarQube** 由 **SonarSource** 创建，用于持续代码质量管理。该扫描器是向服务器发送数据的分析客户端。

# INSTALL

```apk: sudo apk add sonar-scanner```

```brew: brew install sonar-scanner```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[eslint](/man/eslint)(1), [phpstan](/man/phpstan)(1)
