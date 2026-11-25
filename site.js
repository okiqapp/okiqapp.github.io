// روابط تحميل ملفات الأندرويد. غيّر DL_BASE إذا رفعت الملفات بمكان ثاني.
const DL_BASE = 'https://github.com/okiqapp/okiqapp.github.io/releases/latest/download/';
document.querySelectorAll('[data-apk]').forEach(a => { a.href = DL_BASE + 'okiq-' + a.dataset.apk + '.apk'; });

// الأسعار تُقرأ من السيرفر (يتحكم بيها المطوّر من لوحة الإدارة)، والنص المكتوب بالصفحة احتياط فقط
const API = 'https://midad-api.mostafa1muhamd2jasm333333.workers.dev';
(async () => {
  if (!document.querySelector('[data-price],[data-m],[data-trial]')) return;
  try {
    const p = await (await fetch(API + '/pricing?cc=IQ')).json();
    const iqd = p.currency === 'IQD' ? p.rate : 0;
    const fmt = n => Math.round(n / 250) * 250;
    const ar = n => fmt(n).toLocaleString('en-US');
    const days = n => n === 1 ? 'يوماً واحداً' : n === 2 ? 'يومين' : n === 7 ? 'أسبوعاً' : n <= 10 ? n + ' أيام' : n + ' يوماً';
    const usd = k => p.usd[k] ?? p.usd.default;
    const year = m => Math.round(m * p.yearMonths * 100) / 100;
    document.querySelectorAll('[data-price]').forEach(el => {
      const m = usd(el.dataset.price);
      const paid = (p.trialDays > 0 ? 'جرّبه ' + days(p.trialDays) + ' مجاناً، ثم ' : '') + m + '$ شهرياً أو ' + year(m) + '$ سنوياً.';
      el.textContent = el.dataset.price === 'trips'
        ? 'مجاني لقوافل الحج طوال موسم الحج. للعمرة والزيارات: ' + paid
        : paid;
    });
    document.querySelectorAll('[data-m]').forEach(el => { const m = usd(el.dataset.m); el.innerHTML = m + '$' + (iqd ? '<span class="iqd">≈ ' + ar(m * iqd) + ' د.ع</span>' : ''); });
    document.querySelectorAll('[data-y]').forEach(el => { const y = year(usd(el.dataset.y)); el.innerHTML = y + '$' + (iqd ? '<span class="iqd">≈ ' + ar(y * iqd) + ' د.ع</span>' : ''); });
    document.querySelectorAll('[data-trial]').forEach(el => { el.textContent = days(p.trialDays); });
  } catch { /* يبقى النص الاحتياطي */ }
})();
