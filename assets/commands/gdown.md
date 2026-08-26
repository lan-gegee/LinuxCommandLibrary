# TAGLINE

命令行 Google Drive 下载工具

# TLDR

**从 Google** Drive 下载

```gdown [https://drive.google.com/uc?id=FILE_ID]```

**按 ID 下载**

```gdown [file_id]```

**下载文件夹**

```gdown --folder [https://drive.google.com/drive/folders/FOLDER_ID]```

**输出到文件**

```gdown [file_id] -O [output.zip]```

**模糊搜索**

```gdown --fuzzy [https://drive.google.com/...]```

# SYNOPSIS

**gdown** [_options_] _url_or_id_

# PARAMETERS

_URL_OR_ID_
> Google Drive URL 或文件 ID。

**-O** _FILE_, **--output** _FILE_
> 输出文件名或目录（用于文件夹）。

**--folder**
> 递归下载整个文件夹（每个文件夹限制约 50 个文件）。

**--fuzzy**
> 从非标准或重定向 URL 中提取文件 ID。

**--id**
> 将位置参数严格视为文件 ID（已弃用：现在会自动推断）。

**--continue**, **-c**
> 续传部分下载的文件。

**--format** _FMT_
> Google Docs/Sheets/Slides 的导出格式（例如 docx、xlsx、pptx、pdf）。

**--speed** _RATE_
> 限制下载速度（例如 `10MB`）。

**--proxy** _URL_
> 通过 HTTP/HTTPS 代理下载。

**--no-cookies**
> 忽略位于 `~/.cache/gdown/cookies.txt` 的 cookie 缓存。

**--no-check-certificate**
> 跳过 TLS 证书验证。

**--user-agent** _STRING_
> 覆盖默认的 User-Agent 请求头。

**--remaining-ok**
> 下载文件夹时超过 50 文件限制仍继续。

**-q**, **--quiet**
> 抑制进度和信息输出。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**gdown** 是一个从 Google Drive 下载文件和文件夹的命令行工具，专门针对 Drive URL 提供 wget/curl 式的功能。它会自动处理 Google Drive 的下载机制，包括大文件所需的病毒扫描确认步骤，使自动化下载成为可能。

该工具能智能地从各种 Google Drive URL 格式中提取文件 ID，无论是分享链接、直链还是文件夹 URL。它可以下载单个文件或递归下载整个文件夹，并且适用于公开链接和共享链接，公开内容无需 OAuth 身份验证。

gdown 在机器学习和数据科学工作流中特别流行，因为大型数据集和模型权重经常通过 Google Drive 分享。它支持可复现的研究流水线和脚本中的自动化数据获取。当 URL 嵌在重定向中或格式异常时，模糊匹配选项很有帮助。

对于需要身份验证的文件或 Drive 私有内容，gdown 的功能有限。它最适合处理可公开访问的共享文件和文件夹，是开放数据集和模型分发的理想工具。

# CAVEATS

可能受速率限制。大文件下载可能失败。某些文件需要访问权限。未经身份验证无法下载私有文件。

# HISTORY

gdown 的创建是为了简化 Google Drive 下载，尤其是机器学习数据集的下载。它为 Drive URL 提供 wget/curl 式的功能。

# INSTALL

```brew: brew install gdown```

```nix: nix profile install nixpkgs#gdown```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wget](/man/wget)(1), [curl](/man/curl)(1), [gdrive](/man/gdrive)(1)
