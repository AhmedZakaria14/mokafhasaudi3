'use client';

import React from 'react';

export default function GlobalError({
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <html lang="ar" dir="rtl">
      <body className="min-h-screen flex items-center justify-center bg-slate-50 text-slate-900 font-sans p-6 text-center">
        <div className="max-w-md mx-auto space-y-4">
          <h2 className="text-2xl font-bold">حدث خطأ عام في التطبيق</h2>
          <p className="text-slate-600 text-sm">نرجو المعذرة، حدث خلل تقني غير متوقع.</p>
          <button
            onClick={() => reset()}
            className="px-6 py-2.5 bg-emerald-700 text-white rounded-xl font-bold text-sm cursor-pointer"
          >
            إعادة المحاولة
          </button>
        </div>
      </body>
    </html>
  );
}
