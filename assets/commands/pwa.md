# TAGLINE

构建可安装的离线 Web 应用

# TLDR

**创建 PWA 项目**

```pwa create [my-app]```

**构建 PWA**

```pwa build```

**启动开发服务器**

```pwa dev```

**生成 service worker**

```pwa sw```

# SYNOPSIS

**pwa** _command_ [_options_]

# DESCRIPTION

**PWA**（Progressive Web App，渐进式 Web 应用）工具帮助创建可离线工作、可安装且行为类似原生应用的 Web 应用。有多种 CLI 工具可用于 PWA 开发。

这里涵盖常见的 PWA CLI 用法模式。具体工具因框架而异。

# MANIFEST EXAMPLE

```json
{
  "name": "My App",
  "short_name": "App",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#000000",
  "icons": [
    {
      "src": "/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    }
  ]
}
```

# SERVICE WORKER

```javascript
// Basic service worker
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open('v1').then(cache =>
      cache.addAll(['/'])
    )
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request)
      .then(r => r || fetch(e.request))
  );
});
```

# CAVEATS

Service worker 需要 HTTPS。浏览器支持程度不一。工具因框架而异。

# HISTORY

PWA 由 **Google** 于 2015 年提出，旨在通过 Web 技术提供类应用体验。

# SEE ALSO

[lighthouse](/man/lighthouse)(1), [vite](/man/vite)(1)
