# TAGLINE

将 R Markdown 文档渲染为多种格式

# TLDR

**将 R Markdown 渲染为 HTML**

```Rscript -e "rmarkdown::render('[file.Rmd]')"```

**渲染为 PDF**

```Rscript -e "rmarkdown::render('[file.Rmd]', output_format='pdf_document')"```

**渲染为 Word**

```Rscript -e "rmarkdown::render('[file.Rmd]', output_format='word_document')"```

**带参数渲染**

```Rscript -e "rmarkdown::render('[file.Rmd]', params=list(year=2024))"```

# SYNOPSIS

R Markdown 文档处理

# DESCRIPTION

**R Markdown** 将 R 代码与 Markdown 文本结合，创建动态文档。它可以生成 HTML、PDF、Word 文档、演示文稿、仪表盘等。

# YAML HEADER

```yaml
---
title: "My Report"
author: "Name"
date: "`r Sys.Date()`"
output:
  html_document:
    toc: true
    theme: united
---
```

# EXAMPLES

```r
# In R
library(rmarkdown)
render("report.Rmd")

# Specify output
render("report.Rmd", output_format = "pdf_document")

# With parameters
render("report.Rmd", params = list(data = "sales.csv"))
```

# CODE CHUNKS

````markdown
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

```{r plot-example, fig.width=8}
plot(cars)
```
````

# OUTPUT FORMATS

```
html_document
pdf_document (requires LaTeX)
word_document
ioslides_presentation
beamer_presentation
flexdashboard
```

# CAVEATS

需要 R 和 rmarkdown 软件包。PDF 需要 LaTeX（tinytex）。处理过程可能较慢。

# HISTORY

R Markdown 由 **RStudio**（现为 Posit）在 **Yihui Xie** 开发的 knitr 基础上开发。

# SEE ALSO

[pandoc](/man/pandoc)(1), [quarto](/man/quarto)(1)
