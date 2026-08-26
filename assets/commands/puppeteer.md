# TAGLINE

浏览器自动化与测试库

# TLDR

**安装 Puppeteer**

```npm install puppeteer```

**运行 Puppeteer 脚本**

```node [script.js]```

**安装但不捆绑 Chrome**

```npm install puppeteer-core```

# SYNOPSIS

**puppeteer** 用于浏览器自动化的 JavaScript 库

# DESCRIPTION

**Puppeteer** 是一个用于控制 Chrome/Chromium 的 Node.js 库。它提供高级 API，支持无头浏览器自动化、测试、截图和 PDF 生成。

# BASIC SCRIPT

```javascript
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  await page.screenshot({path: 'example.png'});
  await browser.close();
})();
```

# EXAMPLES

```javascript
// Generate PDF
await page.pdf({path: 'page.pdf', format: 'A4'});

// Click element
await page.click('#submit');

// Type text
await page.type('#search', 'query');

// Wait for selector
await page.waitForSelector('.result');

// Evaluate in page context
const title = await page.evaluate(() => document.title);

// Headful mode
const browser = await puppeteer.launch({headless: false});
```

# COMMON OPTIONS

```javascript
puppeteer.launch({
  headless: true,
  slowMo: 100,           // Slow down
  args: ['--no-sandbox'],
  executablePath: '/path/to/chrome'
});
```

# CAVEATS

默认下载 Chromium（约 150MB）。可使用 puppeteer-core 配合自带的浏览器。内存占用较高。

# HISTORY

Puppeteer 由 **Google Chrome DevTools** 团队开发，于 2017 年发布，是官方的 Chrome 自动化 Node.js 库。

# INSTALL

```aur: yay -S puppeteer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[playwright](/man/playwright)(1)
