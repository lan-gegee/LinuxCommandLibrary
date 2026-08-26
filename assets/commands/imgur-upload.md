# TAGLINE

从命令行上传图像到 Imgur

# TLDR

**上传图像**

```imgur-upload [image.png]```

**从剪贴板上传**

```imgur-upload -c```

**以自定义标题上传**

```imgur-upload -t "[My Image]" [image.jpg]```

**从 URL 上传**

```imgur-upload -u "[https://example.com/image.png]"```

# SYNOPSIS

**imgur-upload** [_options_] [_file_]

# PARAMETERS

_file_
> 要上传的图像文件。

**-c**, **--clipboard**
> 从剪贴板上传。

**-u**, **--url** _url_
> 从 URL 上传图像。

**-t**, **--title** _text_
> 图像标题。

**-d**, **--description** _text_
> 图像描述。

**-a**, **--album** _id_
> 添加到相册。

# DESCRIPTION

**imgur-upload** 从命令行将图像上传到 Imgur。它会返回图像的直接 URL，便于快速分享截图或图片。

该命令存在多种实现；有些需要 Imgur API 凭据，另一些则使用匿名上传。

# EXAMPLE SCRIPT

```bash
#!/bin/bash
# Screenshot and upload
scrot /tmp/screenshot.png
url=$(imgur-upload /tmp/screenshot.png)
echo "$url" | xclip -selection clipboard
notify-send "Uploaded: $url"
```

# CAVEATS

某些版本需要 Imgur API 密钥。匿名上传可能有限制。违反服务条款的图像可能被删除。存在多种实现，功能各不相同。

# HISTORY

社区创建了多种 imgur 命令行上传工具。它们支持从终端快速分享图像，在截图工作流和自动化场景中很受欢迎。

# SEE ALSO

[curl](/man/curl)(1), [scrot](/man/scrot)(1), [xclip](/man/xclip)(1)
