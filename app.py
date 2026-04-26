import streamlit as st

# 1. إعداد الصفحة وتنسيق الاتجاه لليمين (RTL)
st.set_page_config(page_title="AI Smart Medical Agent", page_icon="⚕️", layout="wide")
st.markdown("""<style>.main {direction: RTL; text-align: right;}</style>""", unsafe_allow_html=True)

# 2. بيانات الفريق في القائمة الجانبية
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

# 3. قاعدة بيانات الأطباء الشاملة
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
        "تجميل": [("د. رنا أحمد", "⭐⭐⭐⭐⭐", "01122112211")],
        "باطنة": [("د. إبراهيم خالد", "⭐⭐⭐⭐⭐", "01044556677")]
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
    "الصعيد": {
        "قلب": [("د. مجدي يعقوب (أسوان)", "⭐⭐⭐⭐⭐", "19000")],
        "عظام": [("د. خلف الله الصعيدي", "⭐⭐⭐⭐⭐", "01022334455")]
    }
}

st.title("⚕️ الوكيل الطبي الذكي (Smart Medical Agent)")
st.write("نظام خبير لتحليل الأعراض وترشيح الأطباء في كافة محافظات مصر.")
st.write("---")

# المدخلات الأساسية
col1, col2 = st.columns(2)
with col1:
    city = st.selectbox("اختر المدينة:", ["دمياط الجديدة", "القاهرة", "الإسكندرية", "المنصورة", "كفر الشيخ", "كفر سعد", "الصعيد"])
with col2:
    temp = st.number_input("درجة الحرارة:", min_value=34.0, max_value=42.0, value=37.2, step=0.1)

# الأعراض الشائعة
st.subheader("ما هي الأعراض التي تشعر بها؟")
common_cols = st.columns(4)
symptoms = []
with common_cols[0]:
    if st.checkbox("صداع"): symptoms.append("صداع")
with common_cols[1]:
    if st.checkbox("ارتفاع حرارة"): symptoms.append("حرارة")
with common_cols[2]:
    if st.checkbox("ألم ظهر/عظام"): symptoms.append("عظام")
with common_cols[3]:
    if st.checkbox("تجميل"): symptoms.append("تجميل")

user_input = st.text_area("أو اكتب وصفاً مفصلاً لشكواك:").lower()

if st.button("بدء الفحص والبحث عن الأطباء"):
    st.write("---")
    combined = user_input + " " + " ".join(symptoms)
    specialty = "باطنة"
    diagnosis = "أعراض عامة تتطلب فحص باطني."

    if "سنان" in combined or "ضرس" in combined:
        specialty, diagnosis = "أسنان", "احتمالية التهاب في العصب."
    elif "تجميل" in combined or "جلد" in combined:
        specialty, diagnosis = "تجميل", "استشارة جلدية أو تجميلية."
    elif "عظام" in combined or "ظهر" in combined:
        specialty, diagnosis = "عظام", "احتمالية إجهاد في المفاصل."
    elif "قلب" in combined:
        specialty, diagnosis = "قلب", "تحتاج لفحص كفاءة القلب."

    st.subheader(f"🔍 تقرير الوكيل الذكي:")
    if temp >= 38.5:
        st.error(f"⚠️ تنبيه: درجة حرارتك ({temp}) مرتفعة جداً.")
    
    st.info(f"**التشخيص المتوقع:** {diagnosis}")
    st.success(f"**التخصص المطلوب:** {specialty}")

    st.write(f"### 👩‍⚕️ قائمة الأطباء في {city}:")
    city_data = doctors_db.get(city, {})
    list_docs = city_data.get(specialty, [])

    if list_docs:
        for name, stars, phone in list_docs:
            st.write(f"✅ **{name}** | {stars} | 📞 {phone}")
    else:
        st.warning(f"لا توجد بيانات حالياً لدكتور {specialty} في {city}.")

st.write("---")
