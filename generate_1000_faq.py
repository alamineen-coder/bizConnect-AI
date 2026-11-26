import pandas as pd

# Core Business Knowledge Base across 15+ domains in English, Bengali, and Korean
topics = [
    # 1. Starting a Business & Registration
    ("How do I register a new business?",
     "To register a business, choose a legal structure (Sole Proprietorship, LLC, or Corporation), verify your company name, open a corporate bank account, and apply for a Business Registration Certificate at the tax office.",
     ["How to start a new company?", "What are the steps for business registration?", "How can I legally register my startup?", "Where do I apply for a business license?"]),
    ("নতুন ব্যবসা শুরু করতে কী কী করতে হয়?",
     "নতুন ব্যবসা শুরু করতে প্রথমে ব্যবসার ধরন (একক মালিকানা বা লিমিটেড কোম্পানি) নির্ধারণ করুন, ট্রেড লাইসেন্স বা বিজনেস রেজিস্ট্রেশন নিন, কর্পোরেট ব্যাংক অ্যাকাউন্ট খুলুন এবং ট্যাক্স/ভ্যাট নিবন্ধন সম্পন্ন করুন।",
     ["কীভাবে নতুন কোম্পানি রেজিস্ট্রেশন করব?", "ব্যবসা শুরুর প্রাথমিক ধাপগুলো কী কী?", "ট্রেড লাইসেন্স বা বিজনেস লাইসেন্স কীভাবে পাব?", "নতুন বিজনেস সেটআপ করার নিয়ম কী?"]),
    ("신규 사업자 등록은 어떻게 하나요?",
     "신규 사업자 등록을 위해서는 법인 또는 개인사업자 형태를 결정한 후, 임대차계약서와 신분증을 지참하여 관할 세무서 또는 홈택스에서 사업자등록증을 신청해야 합니다.",
     ["창업 절차와 사업자 등록 방법을 알려주세요.", "사업자등록증 발급에 필요한 서류는 무엇인가요?", "새로운 회사를 설립하려면 어떻게 해야 하나요?"]),

    # 2. Doing Business in South Korea (Foreign Entrepreneurs & Visas)
    ("How can a foreigner start a business in South Korea?",
     "Foreign entrepreneurs in South Korea can apply for a D-8-1 Corporate Investor Visa (minimum 100M KRW investment) or a D-8-4 Startup Visa via the OASIS program, followed by court and tax office registration.",
     ["What visa is required to do business in South Korea?", "How to open a company in Korea as a foreigner?", "Tell me about D-8 visa requirements in Korea.", "What is the OASIS startup visa in Korea?"]),
    ("দক্ষিণ কোরিয়ায় ব্যবসা করতে করণীয় কী?",
     "দক্ষিণ কোরিয়ায় বিদেশি উদ্যোক্তাদের ব্যবসা শুরু করতে D-8 ইনভেস্টর ভিসা (ন্যূনতম ১০০ মিলিয়ন উওন বিনিয়োগ) অথবা OASIS প্রোগ্রামের মাধ্যমে D-8-4 স্টার্টআপ ভিসা নিতে হয় এবং ট্যাক্স অফিস থেকে বিজনেস রেজিস্ট্রেশন (사업자등록증) করতে হয়।",
     ["South Korea-এ ব্যবসা করতে করণীয় কি?", "কোরিয়ায় কোম্পানি খোলার নিয়ম কী?", "কোরিয়ায় D-8 বা স্টার্টআপ ভিসা কীভাবে পাওয়া যায়?", "বিদেশি হিসেবে কোরিয়ায় ব্যবসা শুরু করব কীভাবে?"]),
    ("외국인이 한국에서 창업하려면 어떤 비자가 필요한가요?",
     "외국인이 한국에서 창업하려면 최소 1억 원 이상 투자하는 D-8 기업투자 비자 또는 오아시스(OASIS) 프로그램을 통한 D-8-4 기술창업 비자를 취득한 후 법인 설립 및 사업자등록을 진행해야 합니다.",
     ["한국에서 외국인 법인 설립 절차가 어떻게 되나요?", "D-8-4 기술창업 비자 신청 조건을 알려주세요.", "외국인 사업자 등록 방법을 알고 싶습니다."]),

    # 3. E-commerce & F-commerce Operations
    ("How do I launch an online e-commerce store?",
     "To launch an online store, select your product niche, register an e-commerce business license, set up a website or social shop (Facebook/Instagram), integrate payment gateways, and partner with reliable couriers.",
     ["How can I start selling products online?", "What is needed for an e-commerce business?", "How do I start an F-commerce business on Facebook?", "Tips for running a successful online shop?"]),
    ("অনলাইনে ই-কমার্স বা এফ-কমার্স ব্যবসা কীভাবে শুরু করব?",
     "অনলাইনে ব্যবসা শুরু করতে প্রথমে লাভজনক পণ্য নির্বাচন করুন, ফেসবুক পেজ বা ওয়েবসাইট তৈরি করুন, পেমেন্ট গেটওয়ে যুক্ত করুন এবং বিশ্বস্ত কুরিয়ার সার্ভিসের সাথে চুক্তি করে মার্কেটিং শুরু করুন।",
     ["ফেসবুকে ব্যবসা বা এফ-কমার্স শুরু করার নিয়ম কী?", "অনলাইন শপ খোলার জন্য কী কী প্রয়োজন?", "ই-কমার্স বিজনেস সফল করার উপায় কী?", "অনলাইনে পণ্য বিক্রি করব কীভাবে?"]),
    ("온라인 쇼핑몰 창업을 위해 무엇을 준비해야 하나요?",
     "온라인 쇼핑몰 창업을 위해서는 사업자등록 후 통신판매업 신고를 완료해야 하며, 자사몰 또는 스마트스토어 개설, PG사 결제 연동 및 택배사 계약을 진행해야 합니다.",
     ["통신판매업 신고는 어떻게 하나요?", "인터넷 쇼핑몰 운영 절차를 알려주세요.", "스마트스토어 시작하는 방법이 궁금합니다."]),

    # 4. Import, Export & Product Sourcing (China / Global)
    ("How can I import products from China for my business?",
     "Source verified suppliers on Alibaba or 1688, request product samples, negotiate MOQ and Incoterms (FOB/CIF), hire a freight forwarder for sea or air cargo, and clear customs with your commercial invoice and packing list.",
     ["How to source wholesale products from China?", "What documents are needed for import and export?", "How does customs clearance work for commercial imports?", "How to find reliable overseas suppliers?"]),
    ("চীন থেকে পণ্য ইমপোর্ট বা সোর্সিং করার নিয়ম কী?",
     "চীন থেকে পণ্য আনতে Alibaba বা 1688 থেকে ভেরিফায়েড সাপ্লায়ার নির্বাচন করুন, স্যাম্পল যাচাই করুন, ফ্রেইট ফরওয়ার্ডারের মাধ্যমে শিপমেন্ট বুক করুন এবং কমার্শিয়াল ইনভয়েস ও প্যাকিং লিস্ট দিয়ে কাস্টমস ক্লিয়ারেন্স সম্পন্ন করুন।",
     ["বিদেশ থেকে পণ্য আমদানি করতে কী কী কাগজপত্র লাগে?", "হোলসেল বা পাইকারি পণ্য কোথা থেকে সোর্সিং করব?", "ইমপোর্ট-এক্সপোর্ট ব্যবসা কীভাবে শুরু করা যায়?", "চায়না থেকে প্রোডাক্ট আনার সহজ উপায় কী?"]),
    ("중국에서 상품을 수입(소싱)하려면 어떻게 해야 하나요?",
     "알리바바(1688) 등에서 검증된 공급업체를 선정해 샘플을 확인한 후, 포워딩 업체를 통해 해상/항공 운송을 진행하고 인보이스와 패킹리스트를 제출하여 관세청 통관 절차를 거쳐야 합니다.",
     ["무역업 및 수출입 통관 절차를 알려주세요.", "해외 소싱 시 필요한 기본 서류는 무엇인가요?", "도매 물품을 수입하는 방법이 궁금합니다."]),

    # 5. Business Funding, Loans & Capital Management
    ("How can I raise capital or get a small business loan?",
     "Small businesses can secure funding through bank SME loans, government startup grants, angel investors, venture capital, or crowdfunding by presenting a solid business plan and financial projections.",
     ["Where can I get funding for my startup?", "How to apply for a business loan?", "What documents are required for an SME loan?", "How to manage startup capital effectively?"]),
    ("ব্যবসার জন্য মূলধন বা লোন কীভাবে পাব?",
     "ব্যবসার মূলধন সংগ্রহের জন্য ব্যাংকের এসএমই (SME) লোন, সরকারি স্টার্টআপ অনুদান, এনজেল ইনভেস্টর অথবা সুনির্দিষ্ট বিজনেস প্রোফাইল ও প্রজেক্ট প্রপোজাল জমা দিয়ে ঋণের আবেদন করতে পারেন।",
     ["নতুন ব্যবসার জন্য ফান্ডিং পাব কীভাবে?", "ব্যাংক থেকে বিজনেস লোন নেওয়ার নিয়ম কী?", "কম পুঁজিতে লাভজনক ব্যবসা কীভাবে শুরু করব?", "প্রজেক্ট প্রপোজাল তৈরি করে লোন নেওয়ার উপায় কী?"]),
    ("창업 자금이나 중소기업 대출은 어떻게 받을 수 있나요?",
     "사업계획서를 준비하여 중소벤처기업진흥공단 정책자금, 신용보증기금 보증서 대출, 시중 은행 SME 대출 또는 정부 창업지원사업을 통해 자금을 조달할 수 있습니다.",
     ["정부 창업 지원금을 신청하는 방법을 알려주세요.", "소상공인 정책자금 대출 조건이 궁금합니다.", "스타트업 투자 유치 방법이 무엇인가요?"]),

    # 6. Accounting, Tax & Financial Planning
    ("How should a small business manage accounting and taxes?",
     "Maintain separate business bank accounts, record all daily revenues and expenses, issue proper tax invoices, track cash flow monthly, and file VAT and corporate income taxes on schedule.",
     ["What is VAT and how does business tax filing work?", "How to calculate profit margin for a product?", "Why is cash flow management important in business?", "How to prepare a business budget?"]),
    ("ব্যবসার হিসাব-নিকাশ ও ট্যাক্স কীভাবে পরিচালনা করব?",
     "ব্যবসার জন্য আলাদা ব্যাংক অ্যাকাউন্ট ব্যবহার করুন, প্রতিদিনের আয়-ব্যয়ের হিসাব রাখুন, পণ্যের উৎপাদন ও মার্কেটিং খরচ বাদ দিয়ে নেট প্রফিট হিসাব করুন এবং নির্ধারিত সময়ে ভ্যাট ও আয়কর রিটার্ন জমা দিন।",
     ["পণ্যের লাভ বা প্রফিট মার্জিন কীভাবে হিসাব করব?", "ব্যবসার ক্যাশ ফ্লো ম্যানেজমেন্ট কেন জরুরি?", "ভ্যাট ও ট্যাক্স প্রদানের নিয়ম কী?", "ব্যবসার বাজেট পরিকল্পনা কীভাবে তৈরি করব?"]),
    ("소규모 사업장의 회계와 세무 관리는 어떻게 하나요?",
     "사업용 계좌와 카드를 별도로 사용하고, 모든 매출과 매입 증빙(세금계산서, 현금영수증)을 기록하며, 부가가치세와 종합소득세(또는 법인세)를 기한 내에 신고해야 합니다.",
     ["부가가치세 신고 기간과 방법을 알려주세요.", "제품 마진율과 손익분기점은 어떻게 계산하나요?", "사업자 현금흐름 관리 요령이 궁금합니다."]),

    # 7. Marketing, Branding & Customer Acquisition
    ("What are the best digital marketing strategies for small businesses?",
     "Focus on targeted social media ads (Facebook, Instagram, TikTok), search engine optimization (SEO), high-converting video hooks, content marketing, and email retargeting to maximize ROI.",
     ["How can I increase my online sales?", "How to run effective Facebook video ads?", "What is branding and why does it matter?", "How to attract more customers to my business?"]),
    ("ব্যবসার বিক্রি বাড়াতে ডিজিটাল মার্কেটিং কীভাবে করব?",
     "বিক্রি বাড়াতে টার্গেটেড ফেসবুক ও ইনস্টাগ্রাম ভিডিও অ্যাড চালান, আকর্ষণীয় প্রোডাক্ট কনটেন্ট তৈরি করুন, কাস্টমার রিভিউ শেয়ার করুন এবং পুরনো ক্রেতাদের রি-টার্গেটিং অফার দিন।",
     ["ফেসবুক মার্কেটিং করে সেল বাড়ানোর উপায় কী?", "ব্র্যান্ডিং কীভাবে তৈরি করব?", "নতুন কাস্টমার আকর্ষণ করার কৌশল কী কী?", "কম খরচে ব্যবসার প্রচার করব কীভাবে?"]),
    ("소상공인을 위한 효과적인 디지털 마케팅 전략은 무엇인가요?",
     "타겟 SNS 광고(인스타그램, 페이스북, 틱톡), 네이버 검색광고 및 블로그 체험단, 고품질 숏폼 영상 콘텐츠 제작, 그리고 기존 고객 재구매 유도 프로모션이 효과적입니다.",
     ["온라인 매출을 늘리는 마케팅 방법을 알려주세요.", "SNS 광고 효율(ROAS)을 높이는 팁이 있나요?", "브랜드 인지도를 높이는 전략이 궁금합니다."]),

    # 8. Business Hours, Office Location & Contact
    ("What are your business hours?",
     "Our customer support and corporate office operate Monday to Friday from 9:00 AM to 6:00 PM KST. Automated AI support is available 24/7.",
     ["When are you open?", "What time do you close?", "Are you open on Saturday and Sunday?", "How can I reach your support team?"]),
    ("আপনাদের অফিস বা বিজনেস আওয়ার কখন?",
     "আমাদের অফিস ও কাস্টমার সাপোর্ট সোমবার থেকে শুক্রবার সকাল ৯:০০ টা থেকে সন্ধ্যা ৬:০০ টা (KST) পর্যন্ত খোলা থাকে। তবে আমাদের AI চ্যাটবট ২৪ ঘণ্টা সচল থাকে।",
     ["আপনাদের কাস্টমার কেয়ার কখন খোলা থাকে?", "অফিস বন্ধের দিন কোনগুলো?", "আপনাদের সাথে যোগাযোগের ঠিকানা বা ইমেইল কী?", "সাপোর্ট টিমের সাথে কথা বলব কীভাবে?"]),
    ("영업시간과 고객센터 운영시간이 어떻게 되나요?",
     "당사 고객지원 센터는 평일(월~금) 오전 9시부터 오후 6시까지 운영됩니다. 주말 및 공휴일에는 AI 챗봇을 통해 24시간 문의 접수가 가능합니다.",
     ["주말에도 상담이 가능한가요?", "고객센터 전화번호와 이메일을 알려주세요.", "회사 본사 위치가 어디인가요?"]),

    # 9. Order Tracking, Delivery & Shipping
    ("How can I track my order status?",
     "You can track your shipment in real time using the tracking ID sent to your registered email or SMS immediately after dispatch.",
     ["Where is my order?", "How long does shipping take?", "Why is my delivery delayed?", "Do you offer international shipping and express delivery?"]),
    ("আমার অর্ডার কীভাবে ট্র্যাক করব?",
     "অর্ডার কনফার্ম ও ডিসপ্যাচ হওয়ার পর আপনার ইমেইল বা এসএমএস-এ পাঠানো ট্র্যাকিং আইডি ব্যবহার করে আপনি রিয়েল-টাইমে আপনার পণ্যের অবস্থান জানতে পারবেন।",
     ["ডেলিভারি হতে কত দিন সময় লাগে?", "আমার পার্সেল আসতে দেরি হচ্ছে কেন?", "আপনারা কি ইন্টারন্যাশনাল শিপিং করেন?", "ক্যাশ অন ডেলিভারি সুবিধা আছে কি?"]),
    ("주문한 상품의 배송 조회는 어떻게 하나요?",
     "상품 발송 후 이메일 또는 문자(SMS)로 안내된 운송장 번호를 통해 실시간 배송 위치를 조회하실 수 있습니다.",
     ["배송 기간은 보통 며칠 걸리나요?", "배송이 지연되고 있는데 어떻게 확인하나요?", "해외 배송 및 특급 배송도 지원하나요?"]),

    # 10. Returns, Refunds, Warranty & Complaints
    ("What is your return and refund policy?",
     "We offer a 14-day hassle-free return and exchange policy for unused items in original packaging. Refunds are processed within 3–5 business days after inspection.",
     ["How do I get a refund for a damaged item?", "Can I exchange my product for another size?", "How long does warranty coverage last?", "I want to file a complaint about my order."]),
    ("পণ্য রিটার্ন ও রিফান্ড পলিসি কী?",
     "পণ্য অব্যবহৃত ও মূল প্যাকেজিং অক্ষত থাকলে ডেলিভারির ১৪ দিনের মধ্যে রিটার্ন বা এক্সচেঞ্জ করা যায়। পণ্য যাচাইয়ের পর ৩-৫ কার্যদিবসের মধ্যে রিফান্ড সম্পন্ন হয়।",
     ["নষ্ট বা ভুল পণ্য পেলে কীভাবে পরিবর্তন করব?", "রিফান্ডের টাকা ফেরত পেতে কত দিন লাগে?", "পণ্যের ওয়ারেন্টি বা গ্যারান্টি কত দিনের?", "আমার অর্ডার নিয়ে অভিযোগ জানাতে চাই।"]),
    ("반품, 교환 및 환불 절차가 어떻게 되나요?",
     "상품 수령 후 14일 이내에 미사용 및 원래 포장 상태인 경우 반품과 교환이 가능합니다. 반품 검수 완료 후 영업일 기준 3~5일 이내에 환불됩니다.",
     ["파손되거나 불량인 상품을 받았을 때 어떻게 하나요?", "제품 무상 보증(A/S) 기간은 얼마나 되나요?", "환불 처리 기간이 궁금합니다."]),

    # 11. B2B Wholesale, Partnerships & Contracts
    ("How can I apply for a B2B wholesale account or partnership?",
     "For bulk orders (50+ units) or distribution partnerships, email your company profile to partners@bizconnect.ai to receive wholesale pricing tiers and contract terms.",
     ["Do you provide bulk discounts for corporate buyers?", "How to negotiate a supplier contract?", "Can we become an authorized reseller?", "What are your B2B payment terms?"]),
    ("পাইকারি (B2B) অর্ডার বা বিজনেস পার্টনারশিপ কীভাবে করব?",
     "৫০টির বেশি পণ্যের বাল্ক অর্ডার বা ডিস্ট্রিবিউটরশিপের জন্য আপনার কোম্পানির প্রোফাইলসহ partners@bizconnect.ai ঠিকানায় ইমেইল করুন। কর্পোরেট ক্রেতাদের জন্য বিশেষ হোলসেল মূল্য ও ক্রেডিট সুবিধা রয়েছে।",
     ["বাল্ক বা পাইকারি কিনলে কত শতাংশ ডিসকাউন্ট পাওয়া যায়?", "সাপ্লায়ারদের সাথে চুক্তি বা কন্ট্রাক্ট করার নিয়ম কী?", "আপনাদের ডিলার বা রিসেলার হতে চাই।"]),
    ("B2B 대량 구매 및 공식 파트너십 문의는 어떻게 하나요?",
     "50개 이상 대량 구매 또는 총판 파트너십을 원하시면 회사 소개서를 첨부하여 partners@bizconnect.ai 로 문의해 주세요. 기업 전용 도매 단가표를 안내해 드립니다.",
     ["기업 대량 주문 시 할인율이 어떻게 되나요?", "공식 리셀러 및 대리점 계약 조건을 알려주세요.", "B2B 세금계산서 및 후불 결제가 가능한가요?"]),

    # 12. Eco-Friendly & Sustainable Business Models
    ("What are profitable eco-friendly business ideas?",
     "High-potential sustainable businesses include plastic flake recycling, organic vermicompost fertilizer production, biodegradable packaging, areca leaf tableware, and eco-tourism.",
     ["How to start a plastic recycling business?", "Is organic fertilizer production profitable?", "Why is sustainable packaging in high demand?", "How to get green business certification?"]),
    ("পরিবেশবান্ধব বা ইকো-ফ্রেন্ডলি লাভজনক ব্যবসার আইডিয়া কী কী?",
     "বর্তমানে প্লাস্টিক রিসাইক্লিং, জৈব সার বা ভার্মিকম্পোস্ট উৎপাদন, বায়োডিগ্রেডেবল প্যাকেজিং, সুপারি পাতার প্লেট তৈরি এবং ইকো-ট্যুরিজম অত্যন্ত লাভজনক ও টেকসই ব্যবসা।",
     ["প্লাস্টিক রিসাইক্লিং ব্যবসা কীভাবে শুরু করা যায়?", "জৈব সার বা ভার্মিকম্পোস্ট তৈরির ব্যবসায় লাভ কেমন?", "পরিবেশবান্ধব প্যাকেজিং ব্যবসার চাহিদা কেমন?"]),
    ("친환경(그린) 유망 창업 아이템에는 어떤 것들이 있나요?",
     "플라스틱 재활용(플레이크 가공), 유기농 퇴비 생산, 생분해성 친환경 패키징, 제로 웨이스트 생활용품 및 생태 관광 비즈니스가 높은 성장세를 보이고 있습니다.",
     ["플라스틱 재활용 사업의 수익성이 어떤가요?", "친환경 포장재 시장 전망을 알려주세요.", "ESG 경영과 친환경 인증 절차가 궁금합니다."]),

    # 13. AI Automation & Customer Support Governance
    ("How does BizConnect AI improve business customer support?",
     "BizConnect AI automates routine multilingual inquiries in English, Bengali, and Korean using Character N-gram TF-IDF while escalating frustrated or low-confidence (<22%) queries to human agents.",
     ["How does BizConnect AI prevent hallucinations?", "What happens when a customer is angry?", "Which languages does BizConnect AI support?", "Who developed BizConnect AI?"]),
    ("BizConnect AI কীভাবে ব্যবসার কাস্টমার সাপোর্ট উন্নত করে?",
     "BizConnect AI ইংরেজি, বাংলা ও কোরিয়ান ভাষায় স্বয়ংক্রিয়ভাবে সাধারণ প্রশ্নের উত্তর দেয় এবং কাস্টমার বিরক্ত থাকলে বা কনফিডেন্স ২২%-এর কম হলে ভুল উত্তর না দিয়ে হিউম্যান এজেন্টের কাছে পাঠিয়ে দেয়।",
     ["BizConnect AI কীভাবে ভুল উত্তর বা হ্যালুসিনেশন রোধ করে?", "কাস্টমার রেগে গেলে এই চ্যাটবট কী করে?", "BizConnect AI কোন কোন ভাষা সমর্থন করে?", "এই অ্যাপটি কে তৈরি করেছেন?"]),
    ("BizConnect AI는 기업 고객지원을 어떻게 개선하나요?",
     "BizConnect AI는 영어, 벵골어, 한국어 문의를 실시간으로 분석하여 정확한 FAQ 답변을 제공하며, 신뢰도 22% 미만이거나 고객 불만 감지 시 즉시 전문 상담원 검토로 연결해 오답을 방지합니다.",
     ["AI 챗봇의 환각(오답) 현상을 어떻게 방지하나요?", "고객이 화가 났을 때 시스템이 어떻게 작동하나요?", "BizConnect AI는 누가 개발했나요?"])
]

# Systematic query templates to generate 1,050+ natural, diverse business Q&A pairs
en_prefixes = [
    "", "Can you tell me ", "Please explain ", "I want to know ", "Help me understand ",
    "Quick question: ", "Could you clarify ", "What should I know about ", "Guide me on ", "Details about "
]
bn_prefixes = [
    "", "দয়া করে বলুন ", "আমি জানতে চাই ", "আমাকে একটু বুঝিয়ে দিন ", "বিস্তারিত জানান: ",
    "একটা প্রশ্ন ছিল: ", "এই বিষয়ে তথ্য দিন: ", "সঠিক নিয়মটি কী: ", "সাহায্য করুন: ", "জানতে চাচ্ছি "
]
ko_prefixes = [
    "", "자세히 알려주세요: ", "궁금한 점이 있습니다. ", "문의드립니다: ", "설명 부탁드립니다. ",
    "빠른 질문입니다: ", "확인하고 싶습니다. ", "안내해 주세요: ", "도움이 필요합니다. ", "정보를 알고 싶습니다. "
]

rows = []
for base_q, ans, variants in topics:
    # Determine language prefixes
    if any('\u0980' <= ch <= '\u09FF' for ch in base_q):
        prefixes = bn_prefixes
    elif any('\uAC00' <= ch <= '\uD7AF' for ch in base_q):
        prefixes = ko_prefixes
    else:
        prefixes = en_prefixes

    all_qs = [base_q] + variants
    for q in all_qs:
        for pref in prefixes:
            if pref == "":
                formatted_q = q
            else:
                # Adjust lowercase first letter for English mid-sentence
                if prefixes is en_prefixes and q[0].isupper() and not q.startswith(("South Korea", "BizConnect", "OASIS", "B2B", "VAT")):
                    formatted_q = pref + q[0].lower() + q[1:]
                else:
                    formatted_q = pref + q
            rows.append({"Question": formatted_q, "Answer": ans})

# Remove any accidental duplicates while preserving order
df = pd.DataFrame(rows).drop_duplicates(subset=["Question"])
df.to_csv("business_faq.csv", index=False, encoding="utf-8")
print(f"SUCCESS! Generated {len(df)} unique business Q&A pairs in business_faq.csv")
