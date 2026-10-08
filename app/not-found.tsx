import React from 'react';
import Link from 'next/link';
import { ShieldCheck, Home, PhoneCall, ArrowRight } from 'lucide-react';

export default function NotFound() {
  return (
    <main className="min-h-[70vh] flex items-center justify-center bg-slate-50 px-4 py-16 text-center">
      <div className="max-w-md mx-auto space-y-6">
        <div className="inline-flex items-center justify-center w-20 h-20 rounded-3xl bg-emerald-100 text-emerald-800 shadow-sm border border-emerald-200">
          <ShieldCheck className="w-10 h-10 text-emerald-700" />
        </div>
        
        <div className="space-y-2">
          <span className="text-sm font-black tracking-widest text-emerald-700 uppercase">خطأ 404</span>
          <h1 className="text-2xl sm:text-3xl font-black text-slate-900">
            الصفحة المطلوبة غير موجودة
          </h1>
          <p className="text-sm text-slate-600 leading-relaxed">
            عذراً، قد يكون الرابط خاطئاً أو تم نقل المحتوى. تصفح دليل خدماتنا وموسوعتنا الشاملة لمكافحة الآفات بالمملكة.
          </p>
        </div>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
          <Link
            href="/"
            className="w-full sm:w-auto px-6 py-3 bg-emerald-700 hover:bg-emerald-800 text-white font-bold rounded-xl text-sm flex items-center justify-center gap-2 shadow-sm transition active:scale-95"
          >
            <Home className="w-4 h-4" />
            <span>الرئيسية</span>
          </Link>
          <Link
            href="/blog"
            className="w-full sm:w-auto px-6 py-3 bg-white hover:bg-slate-100 text-slate-800 font-bold rounded-xl text-sm border border-slate-300 flex items-center justify-center gap-2 shadow-xs transition"
          >
            <span>الموسوعة والمقالات</span>
            <ArrowRight className="w-4 h-4 rotate-180" />
          </Link>
          <a
            href="tel:0558141870"
            className="w-full sm:w-auto px-6 py-3 bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold rounded-xl text-sm flex items-center justify-center gap-2 shadow-sm transition active:scale-95"
          >
            <PhoneCall className="w-4 h-4" />
            <span>0558141870</span>
          </a>
        </div>
      </div>
    </main>
  );
}
