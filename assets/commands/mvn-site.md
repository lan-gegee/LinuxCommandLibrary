# TAGLINE

生成项目文档网站

# TLDR

**生成项目站点**

```mvn site```

**生成并部署站点**

```mvn site-deploy```

**在指定目录生成站点**

```mvn site -DoutputDirectory=[docs]```

**运行带报告的 site**

```mvn site -DgenerateReports=true```

**将站点暂存到本地**

```mvn site:stage```

**清理并重新生成**

```mvn clean site```

# SYNOPSIS

**mvn** **site** [_options_]

# PARAMETERS

**site**
> 生成项目网站。

**site-deploy**
> 将站点部署到服务器。

**site:stage**
> 将站点暂存到本地。

**-DoutputDirectory** _DIR_
> 输出位置。

**-DgenerateReports** _BOOL_
> 包含报告。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mvn site** 生成项目文档网站。它根据项目元数据创建 HTML。

该 goal 会生成报告、JavaDocs 和信息页面。通过 pom.xml 的 reporting 部分进行配置。

# CAVEATS

需要站点配置。依赖下载量大。内容由插件控制。

# HISTORY

Maven Site Plugin 是 **Apache Maven** 的组成部分，用于生成项目文档网站。

# SEE ALSO

[mvn](/man/mvn)(1), [javadoc](/man/javadoc)(1), [jekyll](/man/jekyll)(1)
