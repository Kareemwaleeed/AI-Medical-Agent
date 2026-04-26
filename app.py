import streamlit as st

st.set_page_config(page_title="AI Smart Medical Agent", page_icon="🧠")
st.markdown("""<style>.main {direction: RTL; text-align: right;}</style>""", unsafe_allow_html=True)

# --- بيانات الفريق والدكتورة مي ---
st.sidebar.title("📑 Project Details")
st.sidebar.markdown(f"""
---
**Course:** Artificial Intelligence
**Supervised by:** Dr. Mai Ramadan Ibrahim
**University:** Horus University
**Faculty:** Faculty of Artificial Intelligence

---
**Team Members:**
1. **Abdulrahman Mohamed** (Leader) - 8251537
2. **Kareem Waleed** - 8251536
3. **Ahmed Waleed** - 8251755
4. **Omar Hassan** - 8241388
5. **Anas Reda** - 8251689
---
""")

# --- قاعدة بيانات تجريبية موسعة (يمكنك زيادتها) ---
doctors_db = {
    "دمياط الجديدة": {
        "باطنة": [("د. أحمد علي", "⭐⭐⭐⭐⭐", "01012345678"), ("د. سارة محمود", "⭐⭐⭐⭐", "01223344556")],
        "عظام": [("د. محمد حسن", "⭐⭐⭐⭐⭐", "01144556677")],
        "أسنان": [("د. ليلى يوسف", "⭐⭐⭐⭐⭐", "01555667788")]
    },
    "المنصورة": {
        "باطنة": [("د. إبراهيم الشربيني", "⭐⭐⭐⭐⭐", "01000998877")],
        "أطفال": [("د. منى زكي", "⭐⭐⭐⭐", "01222333444")]
    },
    "القاهرة": {
        "قلب": [("د. حسام موافي", "⭐⭐⭐⭐⭐", "01099887766")],
        "أعصاب": [("د. عمرو حسن", "⭐⭐⭐⭐", "01200011122")]
    }
}

st.title("🧠 الوكيل الطبي الذكي الشامل لمصر")
st.write("نظام خبير يغطي المدن والقرى المصرية لتقديم الدعم الطبي.")
st.write("---")

# --- المدخلات ---
col_city, col_temp = st.columns(2)
with col_city:
    city_input = st.text_input("اكتب اسم مدينتك أو قريتك (مثال: دمياط الجديدة، بلقاس، شربين):")
with col_temp:
    temp = st.number_input("درجة الحرارة:", min_value=34.0, max_value=42.0, value=37.0, step=0.1)

st.subheader("ما هي الأعراض التي تشعر بها؟")
user_text = st.text_area("اكتب أعراضك بالتفصيل هنا (مثال: عندي صداع وزغللة في العين):").lower()

if st.button("بدء الفحص والبحث عن الأطباء"):
    if not city_input or not user_text:
        st.warning("من فضلك ادخل اسم المدينة والأعراض أولاً.")
    else:
        st.write("---")
        # تحليل الأعراض وتحديد التخصص
        specialty = "طبيب عام"
        diagnoses = []

        if "سنان" in user_text or "ضرس" in user_text:
            specialty = "أسنان"
            diagnoses.append("احتمالية التهاب في اللثة أو عصب الأسنان.")
        elif "عظم" in user_text or "ضهر" in user_text or "ركبة" in user_text:
            specialty = "عظام"
            diagnoses.append("احتمالية إجهاد في المفاصل أو الفقرات.")
        elif "صداع" in user_text or "عين" in user_text:
            specialty = "أعصاب"
            diagnoses.append("احتمالية إجهاد عصبي أو ضغط دم.")
        elif "بطن" in user_text or "معدة" in user_text:
            specialty = "باطنة"
            diagnoses.append("احتمالية اضطراب في الجهاز الهضمي.")

        # عرض النتائج
        st.subheader(f"🔍 تحليل الـ Agent لمدينة {city_input}:")
        for d in diagnoses:
            st.info(d)
        
        st.success(f"📌 التخصص المرشح: {specialty}")

        # البحث في قاعدة البيانات
        st.write(f"### الأطباء المتاحين في {city_input} والقريبين منها:")
        
        found = False
        if city_input in doctors_db:
            if specialty in doctors_db[city_input]:
                for doc, stars, phone in doctors_db[city_input][specialty]:
                    st.write(f"👩‍⚕️ **{doc}** | التقييم: {stars} | 📞 {phone}")
                    found = True
        
        if not found:
            st.warning(f"عذراً، قاعدة البيانات الحالية تغطي المدن الكبرى فقط. ولكن كـ AI Agent، أنصحك بالتوجه إلى أقرب مستشفى مركزي في مركز {city_input} لقسم الـ {specialty}.")
            st.write("💡 **نصيحة إضافية:** يمكنك البحث في تطبيق 'فيزيتا' عن دكاترة في قريتك لبيانات أدق.")

st.write("---")
