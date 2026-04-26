import streamlit as st

# إعداد الصفحة وتنسيق الاتجاه لليمين (RTL)
st.set_page_config(page_title="AI Smart Medical Agent", page_icon="🧠")
st.markdown("""<style>.main {direction: RTL; text-align: right;}</style>""", unsafe_allow_html=True)

# --- SIDEBAR: TEAM INFORMATION ---
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

st.title("🧠 نظام الوكيل الطبي الذكي المتكامل")
st.write("---")

st.subheader("الخيار الأول: تحليل الأعراض الشائعة")
col1, col2 = st.columns(2)
with col1:
    fever = st.checkbox("ارتفاع حرارة")
    cough = st.checkbox("سعال مستمر")
    chest_pain = st.checkbox("ألم في الصدر")
with col2:
    stomach_pain = st.checkbox("ألم في المعدة")
    blur_vision = st.checkbox("زغللة في العين")
    dizzy = st.checkbox("دوخة وصداع")

if st.button("تحليل الأعراض المختارة"):
    st.write("---")
    if fever and cough and chest_pain:
        st.error("التشخيص المحتمل: التهاب شعبي أو عدوى صدرية.")
        st.info("التوجه المقترح: دكتور أمراض صدرية.")
    elif stomach_pain and dizzy:
        st.warning("التشخيص المحتمل: اضطراب في الجهاز الهضمي.")
        st.info("التوجه المقترح: دكتور باطنة وجهاز هضمي.")
    elif blur_vision and dizzy:
        st.warning("التشخيص المحتمل: إجهاد عين أو ضغط دم غير منضبط.")
        st.info("التوجه المقترح: دكتور رمد أو باطنة.")
    elif fever:
        st.success("التشخيص المحتمل: بداية عرضية لبرد.")
        st.info("التوجه المقترح: طبيب عام.")
    else:
        st.info("الرجاء اختيار مجموعة أعراض للتحليل.")

st.write("---")
st.subheader("الخيار الثاني: اسأل الوكيل الذكي عن تخصص (كتابة)")
user_query = st.text_input("اكتبي عرضاً أو مرضاً (مثلاً: ألم في الأسنان، حساسية، عظام):").lower()

if user_query:
    if "سنان" in user_query or "ضرس" in user_query:
        st.success("التوجه المقترح: طبيب أسنان.")
    elif "عظم" in user_query or "ظهر" in user_query or "رجل" in user_query:
        st.success("التوجه المقترح: طبيب عظام وتأهيل.")
    elif "جلد" in user_query or "حساسية" in user_query:
        st.success("التوجه المقترح: طبيب أمراض جلدية.")
    elif "قلب" in user_query or "نهجان" in user_query:
        st.success("التوجه المقترح: طبيب أمراض القلب.")
    elif "مخ" in user_query or "أعصاب" in user_query:
        st.success("التوجه المقترح: طبيب مخ وأعصاب.")
    else:
        st.warning("لم يتم تحديد التخصص بدقة، يرجى استشارة طبيب عام.")

st.write("---")
st.write("---")
