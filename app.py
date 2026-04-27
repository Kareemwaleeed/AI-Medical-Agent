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
1. **Abdulrahman Mohamed**  - 8251537
2. **Kareem Waleed** (Leader) - 8251536
4. **Omar Hassan** - 8241388
---
""")

# 3. قاعدة بيانات الأطباء الشاملة (تشمل الإضافات الجديدة)
doctors_db = {
    "دمياط الجديدة": {
        "باطنة": [("د. أحمد علي", "⭐⭐⭐⭐⭐", "01011122233")],
        "تجميل": [("د. نورا الشربيني", "⭐⭐⭐⭐⭐", "01099887766")],
        "عظام": [("د. محمد حسن", "⭐⭐⭐⭐", "01222333444")],
        "أسنان": [("د. ليلى يوسف", "⭐⭐⭐⭐⭐", "01555667788")]
    },
    "دمياط القديمة": {
        "باطنة": [("د. مصطفى العوضي", "⭐⭐⭐⭐⭐", "01066778899")],
        "عظام": [("د. محمود صيام", "⭐⭐⭐⭐", "01288775544")],
        "تجميل": [("د. نهى الجمل", "⭐⭐⭐⭐⭐", "01555443322")]
    },
    "رأس البر": {
        "باطنة": [("د. عصام الدين", "⭐⭐⭐⭐⭐", "01044332211")],
        "أسنان": [("د. منى الشامي", "⭐⭐⭐⭐", "01122113344")]
    },
    "جمصة": {
        "باطنة": [("د. خالد الصاوي", "⭐⭐⭐⭐", "01088776655")],
        "عظام": [("د. سامح مبروك", "⭐⭐⭐⭐⭐", "01200998877")]
    },
    "المنزلة": {
        "باطنة": [("د. محمد غنيم", "⭐⭐⭐⭐⭐", "01012123434")],
        "قلب": [("د. يوسف البطريق", "⭐⭐⭐⭐⭐", "01144556677")],
        "أعصاب": [("د. أحمد عويضة", "⭐⭐⭐⭐", "01566778899")]
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
    "الصعيد": {
        "قلب": [("د. مجدي يعقوب (أسوان)", "⭐⭐⭐⭐⭐", "19000")],
        "عظام": [("د. خلف الله الصعيدي", "⭐⭐⭐⭐⭐", "01022334455")]
    }
}

st.title("⚕️ الوكيل الطبي الذكي الشامل (AI Medical Agent)")
st.write("نظام خبير متطور لتحليل الأعراض وترشيح الأطباء في مختلف المدن المصرية.")
st.write("---")

# المدخلات الأساسية
col1, col2 = st.columns(2)
with col1:
    city = st.selectbox("اختر المدينة:", list(doctors_db.keys()))
with col2:
    temp = st.number_input("درجة الحرارة (مثال: 37.2):", min_value=34.0, max_value=42.0, value=37.2, step=0.1)

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
    if st.checkbox("استشارة تجميل"): symptoms.append("تجميل")

user_input = st.text_area("أو اكتب وصفاً مفصلاً لشكواك (مثال: عندي وجع في بطني):").lower()

if st.button("بدء الفحص والبحث عن الأطباء"):
    st.write("---")
    combined = user_input + " " + " ".join(symptoms)
    specialty = "باطنة"
    diagnosis = "أعراض عامة تتطلب فحص باطني للاطمئنان."

    # منطق التحليل الذكي
    if "سنان" in combined or "ضرس" in combined:
        specialty, diagnosis = "أسنان", "احتمالية وجود التهاب في اللثة أو تسوس."
    elif "تجميل" in combined or "جلد" in combined:
        specialty, diagnosis = "تجميل", "استشارة بخصوص إجراء تجميلي أو صحة البشرة."
    elif "عظام" in combined or "ظهر" in combined or "ركبة" in combined:
        specialty, diagnosis = "عظام", "احتمالية إجهاد عضلي أو مشاكل في المفاصل."
    elif "قلب" in combined or "نهجان" in combined:
        specialty, diagnosis = "قلب", "تحتاج لفحص كفاءة القلب والضغط."
    elif "مخ" in combined or "أعصاب" in combined or "صداع" in combined:
        specialty, diagnosis = "أعصاب", "احتمالية إجهاد عصبي أو صداع نصفي."

    st.subheader(f"🔍 تقرير الوكيل الذكي لمدينة {city}:")
    if temp >= 38.5:
        st.error(f"⚠️ تنبيه: درجة حرارتك ({temp}) مرتفعة جداً. يرجى زيارة الطبيب فوراً.")
    
    st.info(f"**التشخيص المتوقع:** {diagnosis}")
    st.success(f"**التخصص المطلوب:** {specialty}")

    st.write(f"### 👩‍⚕️ قائمة الأطباء المرشحين في {city}:")
    city_data = doctors_db.get(city, {})
    list_docs = city_data.get(specialty, [])

    if list_docs:
        for name, stars, phone in list_docs:
            st.write(f"✅ **{name}** | {stars} | 📞 {phone}")
    else:
        st.warning(f"عذراً، لم يتم العثور على دكتور {specialty} في قاعدة بيانات {city} حالياً.")

st.write("---")
