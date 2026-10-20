import type { Metadata } from 'next';
import { IBM_Plex_Sans_Arabic, Tajawal } from 'next/font/google';
import './globals.css';
import { SiteProvider } from '@/components/SiteProvider';

const ibmPlexArabic = IBM_Plex_Sans_Arabic({
  subsets: ['arabic', 'latin'],
  weight: ['300', '400', '500', '600', '700'],
  variable: '--font-ibm-plex',
  display: 'swap',
});

const tajawal = Tajawal({
  subsets: ['arabic', 'latin'],
  weight: ['400', '500', '700', '800', '900'],
  variable: '--font-tajawal',
  display: 'swap',
});

export const metadata: Metadata = {
  metadataBase: new URL('https://mokafahalriyadh.com'),
  title: 'شركة حصن المملكة الوطنية لمكافحة الحشرات والوقاية الإنشائية | معتمدة رسمياً SFDA والأمانات',
  description: 'المؤسسة الوطنية الرائدة في مكافحة الآفات والحشرات، حقن وتدفين النمل الأبيض (الأرضة) بضمان 15 سنة، إبادة الصراصير وبق الفراش والقوارض وطرد الحمام بمبيدات معتمدة من هيئة الغذاء والدواء SFDA ووزارة البلديات والإسكان. خدمة 24 ساعة بكافة مدن المملكة. اتصل: 0558141870.',
  keywords: [
    'شركة مكافحة حشرات بالرياض',
    'رش مبيدات معتمدة SFDA',
    'مكافحة النمل الأبيض والأرضة',
    'حقن مبيدات النمل الابيض بضمان 15 سنة',
    'تدفين خرساني للمباني قبل الصبة',
    'رش الصراصير بالجل الالماني',
    'مكافحة بق الفراش بالحرارة والبخار',
    'طرد الحمام وتركيب الشبك',
    'عقود مكافحة حشرات المنشآت والتراخيص',
    'شركة مكافحة حشرات بجدة',
    'شركة رش مبيدات بالدمام والشرقية',
    'حصن المملكة للخدمات البيئية'
  ],
  authors: [{ name: 'شركة حصن المملكة للخدمات البيئية ومكافحة الآفات' }],
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  alternates: {
    canonical: 'https://mokafahalriyadh.com/',
  },
  icons: {
    icon: '/favicon.ico',
    apple: '/icon.png',
  },
  openGraph: {
    title: 'شركة حصن المملكة الوطنية لمكافحة الحشرات والتعقيم',
    description: 'معتمدون لدى هيئة الغذاء والدواء SFDA والجهات الرقابية. حلول هندسية متكاملة لإبادة الآفات مع ضمانات موثقة تصل إلى 15 عاماً وسرعة وصول في 25 دقيقة بكافة مناطق المملكة.',
    url: 'https://mokafahalriyadh.com/',
    siteName: 'شركة حصن المملكة الوطنية لمكافحة الحشرات',
    images: [
      {
        url: 'https://mokafahalriyadh.com/logo.png',
        width: 512,
        height: 512,
        alt: 'شركة حصن المملكة الوطنية لمكافحة الحشرات والوقاية الإنشائية',
      },
    ],
    type: 'website',
    locale: 'ar_SA',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'شركة حصن المملكة لمكافحة الحشرات والوقاية الإنشائية',
    description: 'المؤسسة المعتمدة الأولى بالمملكة العربية السعودية لمكافحة الآفات ورش المبيدات - هاتف: 0558141870',
    images: ['https://mokafahalriyadh.com/logo.png'],
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const siteLogoUrl = 'https://mokafahalriyadh.com/logo.png';

  const rootSchemaGraph = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'Organization',
        '@id': 'https://mokafahalriyadh.com/#organization',
        'name': 'شركة حصن المملكة الوطنية لمكافحة الحشرات والوقاية الإنشائية',
        'alternateName': 'حصن المملكة',
        'url': 'https://mokafahalriyadh.com/',
        'logo': siteLogoUrl,
        'telephone': '+966558141870',
        'contactPoint': [
          {
            '@type': 'ContactPoint',
            'telephone': '+966558141870',
            'contactType': 'customer service',
            'areaServed': 'SA',
            'availableLanguage': ['Arabic', 'English']
          }
        ]
      },
      {
        '@type': ['HomeAndConstructionBusiness', 'LocalBusiness'],
        '@id': 'https://mokafahalriyadh.com/#localbusiness',
        'parentOrganization': {
          '@id': 'https://mokafahalriyadh.com/#organization'
        },
        'name': 'شركة مكافحة الحشرات والنمل الأبيض المعتمدة بـالرياض',
        'url': 'https://mokafahalriyadh.com/',
        'telephone': '+966558141870',
        'priceRange': '$$',
        'image': siteLogoUrl,
        'description': 'شركة مكافحة حشرات ونمل أبيض معتمدة من هيئة الغذاء والدواء (SFDA) ووزارة البلديات، تقدم خدمات الإبادة الفورية والرش بضمان يصل إلى 15 عاماً في الرياض.',
        'address': {
          '@type': 'PostalAddress',
          'addressLocality': 'الرياض',
          'addressRegion': 'منطقة الرياض',
          'addressCountry': 'SA'
        },
        'geo': {
          '@type': 'GeoCoordinates',
          'latitude': 24.7136,
          'longitude': 46.6753
        },
        'openingHoursSpecification': [
          {
            '@type': 'OpeningHoursSpecification',
            'dayOfWeek': [
              'Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday',
              'Saturday',
              'Sunday'
            ],
            'opens': '00:00',
            'closes': '23:59'
          }
        ],
        'areaServed': [
          {
            '@type': 'City',
            'name': 'الرياض'
          },
          {
            '@type': 'Country',
            'name': 'المملكة العربية السعودية'
          }
        ],
        'aggregateRating': {
          '@type': 'AggregateRating',
          'ratingValue': '4.9',
          'reviewCount': '3240',
          'bestRating': '5',
          'worstRating': '1'
        },
        'hasOfferCatalog': {
          '@type': 'OfferCatalog',
          'name': 'خدمات مكافحة الحشرات والوقاية الإنشائية',
          'itemListElement': [
            {
              '@type': 'Offer',
              'itemOffered': {
                '@type': 'Service',
                'name': 'مكافحة النمل الأبيض (الأرضة)',
                'description': 'حقن ومعالجة النمل الأبيض والخرسانات بمبيدات بايفلكس بضمان رسمي حتى 15 سنة.'
              }
            },
            {
              '@type': 'Offer',
              'itemOffered': {
                '@type': 'Service',
                'name': 'إبادة بق الفراش بالحرارة والضباب ULV',
                'description': 'استئصال حشرة الفراش بالبخار النفاذ بدون إخلاء المنزل.'
              }
            },
            {
              '@type': 'Offer',
              'itemOffered': {
                '@type': 'Service',
                'name': 'إبادة الصراصير بالمطابخ',
                'description': 'مكافحة فورية بالجل الألماني والسويسري بدون رائحة ومصرح من SFDA.'
              }
            },
            {
              '@type': 'Offer',
              'itemOffered': {
                '@type': 'Service',
                'name': 'تركيب طوارد وشبك الحمام',
                'description': 'حماية أسطح وواجهات المباني وشبابيك الفلل من الطيور والحمام.'
              }
            }
          ]
        }
      },
      {
        '@type': 'FAQPage',
        '@id': 'https://mokafahalriyadh.com/#faq',
        'mainEntity': [
          {
            '@type': 'Question',
            'name': 'ما هي مدة الضمان على مكافحة النمل الأبيض؟',
            'acceptedAnswer': {
              '@type': 'Answer',
              'text': 'نقدم ضماناً رسمياً معتمداً وموثقاً يصل من 10 إلى 15 سنة على خدمات مكافحة النمل الأبيض ورش الدفان باستخدام مبيدات بايفلكس الأصلية.'
            }
          },
          {
            '@type': 'Question',
            'name': 'هل تتطلب عملية الرش إخلاء المنزل أو إزالة الأواني؟',
            'acceptedAnswer': {
              '@type': 'Answer',
              'text': 'لا، نستخدم مبيدات وتقنيات جل ألمانية وأمريكية معتمدة من هيئة الغذاء والدواء (SFDA) بدون رائحة وآمنة تماماً على الأطفال، وتتم الإبادة دون الحاجة لمغادرة المنزل.'
            }
          },
          {
            '@type': 'Question',
            'name': 'كم يستغرق وصول فريق الرش والمعاينة الميدانية في الرياض؟',
            'acceptedAnswer': {
              '@type': 'Answer',
              'text': 'تغطي فرقنا الميدانية أحياء الرياض كافة بمتوسط زمن استجابة ووصول يتراوح بين 25 إلى 30 دقيقة للمعاينة المجانية الفورية.'
            }
          }
        ]
      }
    ]
  };

  return (
    <html lang="ar" dir="rtl" className={`${ibmPlexArabic.variable} ${tajawal.variable}`}>
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(rootSchemaGraph) }}
        />
      </head>
      <body className="antialiased bg-slate-50 text-slate-900 font-sans selection:bg-emerald-600 selection:text-white" suppressHydrationWarning>
        <SiteProvider>{children}</SiteProvider>
      </body>
    </html>
  );
}
