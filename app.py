import streamlit as st

st.set_page_config(page_title="AI Smart Medical Agent", page_icon="⚕️", layout="wide")
st.markdown("""<style>.main {direction: RTL; text-align: right;}</style>""", unsafe_allow_html=True)

# --- SIDEBAR: TEAM INFORMATION ---
st.sidebar.title("📑 Project Details")
st.sidebar.markdown(f"""
---
**Course:** Artificial Intelligence
**Supervised by:** Dr. Mai Ramadan Ibrahim
**University:** Horus University
**Faculty:** Faculty of Artificial Intelligence

**Team Members:**
1. **Abdulrahman Mohamed** (Leader) - 8251537
2. **Kareem Waleed** - 8251536
3. **Ahmed Waleed** - 8251755
4. **Omar Hassan** - 8241388
5. **Anas Reda** - 8251689
---
""")

# --- DATABASE: EXTENDED DOCTORS DATA ---
doctors_db = {
    "دمياط الجديدة": {
        "باطنة": [("د. أحمد علي", "⭐⭐⭐⭐⭐", "01011122233")],
        "تجميل": [("د. نورا الشربيني", "⭐⭐⭐⭐⭐", "01099887766")],
        "عظام": [("د. محمد حسن", "⭐⭐⭐⭐", "01222333444")],
        "أسنان": [("د. ليلى يوسف", "⭐⭐⭐⭐⭐", "01555667788")]
    },
    "القاهرة": {
        "تجميل": [("د. محمود سيد", "⭐⭐⭐⭐⭐", "01122334455")],
        "قلب": [("د. حسام موافي", "⭐⭐⭐⭐⭐", "01099887766")],
        "أعصاب": [("د. عمرو حسن", "⭐⭐⭐⭐", "01200011122")]
    },
    "الإسكندرية": {
        "باطنة": [("د. إبراهيم خالد", "⭐⭐⭐⭐⭐", "01044556677")],
        "تجميل": [("د. رنا أحمد", "⭐⭐⭐⭐⭐", "01122112211")]
    },
    "كفر الشيخ": {
        "عظام": [("د. فؤاد خليل", "⭐⭐⭐⭐", "01077889900")],
        "باطنة": [("د. مصطفى كمال", "⭐⭐⭐⭐⭐", "01288776655")]
    },
    "المنصورة": {
        "أطفال": [("د. منى زكي", "⭐⭐⭐⭐⭐", "01000998877")],
        "تجميل": [("د. هاني البحيري", "⭐⭐⭐⭐", "01511223344")]
    },
    "كفر سعد": {
        "باطنة": [("د. عادل إمام", "⭐⭐⭐⭐", "01055664422")],
        "أسنان": [("د. ريهام سعيد", "⭐⭐⭐⭐⭐", "01133221100")]
    },
    "الصعيد (أسيوط/سوهاج)": {
        "قلب": [("د. مجدي يعقوب (مركز أسوان)", "⭐⭐⭐⭐⭐", "19000")],
        "عظام": [("د. خلف الله الصعيدي", "⭐⭐⭐⭐⭐", "01022334455")]
    }
}

st.title("⚕️ الوكيل الطبي الذكي الشامل (Smart Medical Agent)")
st.write("نظام خبير مدعم بالذكاء الاصطناعي لتحليل الأعراض وترشيح الأطباء في كافة محافظات مصر.")

# --- STEP 1: CITY & TEMP ---
st.subheader("1️⃣ البيانات الأساسية")
col1, col2 = st.columns(2)
with col1:
    city = st.selectbox("اختر المدينة:", ["دمياط الجديدة", "القاهرة", "الإسكندرية", "المنصورة", "كفر الشيخ", "كفر سعد", "الصعيد (أسيوط/سوهاج)"])
with col2:
    temp = st.number_input("درجة الحرارة (مثال: 37):", min_value=34.0, max_value=42.0, value=37.0, step=0.1)

# --- STEP 2: COMMON SYMPTOMS (BUTTONS) ---
st.subheader("2️⃣ الأعراض المشهورة (اضغط للاختيار السريع)")
common_cols = st.columns(4)
symptom_list = []
with common_cols[0]:
    if st.checkbox("صداع"): symptom_list.append("صداع")
with common_cols[1]:
    if st.checkbox("ارتفاع حرارة"): symptom_list.append("حرارة")
with common_cols[2]:
    if st.checkbox("ألم ظهر/عظام"): symptom_list.append("عظام")
with common_cols[3]:
    if st.checkbox("استشارة تجميل"): symptom_list.append("تجميل")

st.write("**أو اكتب وصفاً مفصلاً لشكواك:**")
user_input = st.text_area("مثال: عندي وجع في ضرس العقل ومحتاج دكتور").lower()

# --- ANALYSIS & RECOMMENDATION ---
if st.button("بدء الفحص والبحث عن الأطباء"):
    st.write("---")
    specialty = ""
    diagnosis = ""

    # منطق الـ Agent لتحليل النص والأزرار
    combined_input = user_input + " " + " ".join(symptom_list)
    
    if "سنان" in combined_input or "ضرس" in combined_input:
        specialty, diagnosis = "أسنان", "احتمالية التهاب في العصب أو تسوس."
    elif "تجميل" in combined_input or "جلد" in combined_input or "بشرة" in combined_input:
        specialty, diagnosis = "تجميل", "استشارة بخصوص صحة الجلد أو إجراء تجميلي."
    elif "عظام" in combined_input or "ظهر" in combined_input or "رجل" in combined_input:
        specialty, diagnosis = "عظام", "احتمالية إجهاد عضلي أو مشاكل في الفقرات."
    elif "قلب" in combined_input or "نهجان" in combined_input:
        specialty, diagnosis = "قلب", "تحتاج لفحص كفاءة القلب والضغط."
    elif "صداع" in combined_input or "أعصاب" in combined_input:
        specialty, diagnosis = "أعصاب", "احتمالية إجهاد عصبي أو صداع نصفي."
    else:
        specialty, diagnosis = "باطنة", "أعراض عامة تتطلب فحص باطني شامل."

    # عرض النتائج
    st.subheader(f"🔍 تقرير الوكيل الذكي لمدينة {city}:")
    if temp >= 38.5:
        st.error(f"⚠️ تنبيه: درجة حرارتك ({temp}) مرتفعة. يرجى شرب سوائل وزيارة الطبيب فوراً.")
    
    st.info(f"**التشخيص المتوقع:** {diagnosis}")
    st.success(f"**التخصص المطلوب:** {specialty}")

    st.write(f"### 👩‍⚕️ قائمة الأطباء المرشحين في {city}:")
    city_data = doctors_db.get(city, {})
    specialists = city_data.get(specialty, [])

    if specialists:
        for name, stars, phone in specialists:
            st.write(f"✅ **{name}** | {stars} | 📞 {phone}")
    else:
        st.warning(f"عذراً، لم نجد دكتور {specialty} في قاعدة بيانات {city} حالياً، جاري البحث في أقرب منطقة.")

st.write("---")st.write("---")
