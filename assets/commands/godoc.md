# TAGLINE

Go 文档 Web 服务器

# TLDR

**在端口 6060 上启动文档服务器**

```godoc -http=:6060```

**启用搜索索引启动服务器**

```godoc -http=:6060 -index```

**支持 Go playground 启动服务器**

```godoc -http=:6060 -play```

**打印某个 URL 路径所对应的文档内容**

```godoc -url=/pkg/[fmt]/```

**使用自定义 GOROOT 启动服务器**

```godoc -http=:6060 -goroot=[/usr/local/go]```

# SYNOPSIS

**godoc** [_flags_]

# PARAMETERS

**-http** _addr_
> HTTP 服务地址（例如 `:6060` 或 `127.0.0.1:6060`）。

**-index**
> 启用标识符与全文搜索索引。不加此标志时不显示搜索框。

**-play**
> 为可执行示例启用 Go playground。

**-url** _path_
> 把针对给定路径发起 HTTP 请求时本应返回的内容打印到标准输出，然后退出。

**-goroot** _dir_
> 设置 Go 根目录（默认：`$GOROOT`）。

**-v**
> 详细模式。

**-timestamps**
> 在目录列表中显示时间戳（默认：true）。

**-links**
> 将标识符链接到其声明处（默认：true）。

**-index_interval** _duration_
> 索引更新的时间间隔；0 表示每 5 分钟更新一次，负值表示仅在启动时建立索引。

**-index_throttle** _float_
> 索引节流值，介于 0.0 与 1.0 之间（默认：0.75）。

**-maxresults** _n_
> 全文搜索结果显示的最大数量（默认：10000）。设为 0 可禁用全文搜索。

**-notes** _regexp_
> 匹配要显示的注释标记的正则表达式（默认：`BUG`）。

**-templates** _dir_
> 存放备用模板文件的目录。

**-zip** _file_
> 提供服务所用文件系统的 zip 文件，用于替代本地文件系统。

# DESCRIPTION

**godoc** 提取并生成 Go 包的文档，以可浏览的 Web 界面提供服务。它会为 GOROOT 和 GOPATH 中的所有包建立索引，支持带源码链接的全面浏览以及可选的搜索功能。

Web 界面支持通过 URL 参数控制呈现方式：`?m=all` 显示未导出的声明，`?m=methods` 显示所有内嵌方法，`?m=src` 显示源代码，`?m=flat` 使用扁平化的目录列表。

如果只想在命令行快速查询单个包或符号，请改用 `go doc`。godoc 主要用作本地文档服务器。

# CAVEATS

自 Go 1.12 起，godoc 需要通过 `go install golang.org/x/tools/cmd/godoc@latest` 单独安装。它无法选择显示包的哪个版本。较新的 `pkgsite` 工具（`golang.org/x/pkgsite/cmd/pkgsite`）是本地文档浏览的推荐替代方案。

# HISTORY

godoc 是最早的 **Go** 文档工具，在 1.12 版之前一直随 Go 捆绑发行。现在它可从 `golang.org/x/tools/cmd/godoc` 单独获取；在本地使用场景已在很大程度上被 `pkgsite` 取代，而在线文档则由 `pkg.go.dev` 承担。

# INSTALL

```apt: sudo apt install golang-golang-x-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go-doc](/man/go-doc)(1), [go](/man/go)(1), [gofmt](/man/gofmt)(1)
