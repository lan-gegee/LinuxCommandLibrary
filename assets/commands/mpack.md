# TAGLINE

将文件编码为 MIME 格式以便通过电子邮件传输

# TLDR

**将文件编码为 MIME 消息**并保存到文件

```mpack -o [output.mime] [file]```

将文件**编码并通过邮件发送**给一个或多个收件人

```mpack -s "[Subject]" [file] [user@example.com]```

**编码到 stdout** 以便通过管道传给其他邮件程序

```mpack -o - [file]```

将大文件**拆分为多条消息**，每条最多 100 000 个字符

```mpack -s "[Subject]" -m [100000] [large_file] [user@example.com]```

**强制指定 MIME 内容类型**

```mpack -c application/pdf [report.pdf] [user@example.com]```

将文件**投递到 Usenet 新闻组**而非电子邮件

```mpack -n [comp.misc] [file]```

# SYNOPSIS

**mpack** [**-a**] [**-s** _subject_] [**-d** _descriptionfile_] [**-m** _maxsize_] [**-c** _content-type_] _file_ _address_...

**mpack** [**-a**] [**-s** _subject_] [**-d** _descriptionfile_] [**-m** _maxsize_] [**-c** _content-type_] **-o** _outputfile_ _file_

**mpack** [**-a**] [**-s** _subject_] [**-d** _descriptionfile_] [**-m** _maxsize_] [**-c** _content-type_] **-n** _newsgroups_ _file_

# PARAMETERS

**-s** _subject_
> 邮件主题行。

**-d** _descriptionfile_
> 将 _descriptionfile_ 的内容作为附件前的介绍性文本部分包含进去。

**-m** _maxsize_
> 将消息分片为不超过 _maxsize_ 字符的块（0 = 无限制）。

**-c** _content-type_
> 覆盖附件的 MIME **Content-Type**（如 **application/pdf**、**image/png**）。

**-a**
> 将编码后的文件标记为**附件**（Content-Disposition: attachment）而非内联内容。

**-o** _outputfile_
> 将编码后的消息写入 _outputfile_（用 **-** 表示 stdout）。分片时会追加带编号的后缀。

**-n** _newsgroups_
> 投递到指定的 Usenet 新闻组而不是发邮件。

# DESCRIPTION

**mpack** 将二进制或文本文件编码为一条或多条 MIME 格式的消息，可以选择将其邮寄给一组地址或投递到新闻组。它会生成必要的头部（**MIME-Version**、**Content-Type**、**Content-Transfer-Encoding**、**Content-Disposition**），并对二进制内容进行 base64 编码。使用 **-m** 时，消息会被拆分为可独立邮寄的分片，由对端的 **munpack** 重新组装。

# CAVEATS

是 **munpack** 的配套工具。发邮件或投递新闻需要已配置好的本地 MTA（与 sendmail 兼容）或新闻传输系统。分片消息必须全部送达收件人，并在解码前用 **munpack** 重新组装。

# HISTORY

mpack 由卡内基梅隆大学的 **John G. Myers** 编写，是处理二进制邮件附件的 MIME 工具之一。

# INSTALL

```apt: sudo apt install mpack```

```brew: brew install mpack```

```nix: nix profile install nixpkgs#mpack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[munpack](/man/munpack)(1), [uuencode](/man/uuencode)(1), [base64](/man/base64)(1), [sendmail](/man/sendmail)(1)
