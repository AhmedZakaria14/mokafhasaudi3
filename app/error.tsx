'use client';

import React, { useEffect } from 'react';
import Link from 'next/link';
import { AlertTriangle, Home, RefreshCw } from 'lucide-react';

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error('Unhandled app error:', error);
  }, [error]);

  return (
    <main className="min-h-[70vh] flex items-center justify-center bg-slate-50 px-4 py-16 text-center">
      <div className="max-w-md mx-auto space-y-6">
        <div className="inline-flex items-center justify-center w-20 h-20 rounded-3xl bg-amber-100 text-amber-800 shadow-sm border border-amber-200">
          <AlertTriangle className="w-10 h-10 text-amber-700" />
        </div>
        
        <div className="space-y-2">
          <h1 className="text-2xl sm:text-3xl font-black text-slate-900">
            حدث خطأ غير متوقع
          </h1>
          <p className="text-sm text-slate-600 leading-relaxed">
            نعتذر عن هذا الخطأ المؤقت. يمكنك إعادة المحاولة أو العودة إلى الصفحة الرئيسية.
          </p>
        </div>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
          <button
            onClick={() => reset()}
            className="w-full sm:w-auto px-6 py-3 bg-emerald-700 hover:bg-emerald-800 text-white font-bold rounded-xl text-sm flex items-center justify-center gap-2 shadow-sm transition active:scale-95 cursor-pointer"
          >
            <RefreshCw className="w-4 h-4" />
            <span>إعادة المحاولة</span>
          </button>
          <Link
            href="/"
            className="w-full sm:w-auto px-6 py-3 bg-white hover:bg-slate-100 text-slate-800 font-bold rounded-xl text-sm border border-slate-300 flex items-center justify-center gap-2 shadow-xs transition"
          >
            <Home className="w-4 h-4" />
            <span>الرئيسية</span>
          </Link>
        </div>
      </div>
    </main>
  );
}
