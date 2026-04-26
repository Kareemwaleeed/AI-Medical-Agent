import streamlit as st

st.set_page_config(page_title="AI Smart Medical Agent", page_icon="🧠")
st.markdown("""<style>.main {direction: RTL; text-align: right;}</style>""", unsafe_allow_html=True)

st.sidebar.title("بيانات الطالبة")
st.sidebar.info("""
**الاسم:** نور
**المادة:** ذكاء اصطناعي
**المشروع:** Intelligent Medical Agent
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
        st.warning("التشخيص المحتمل: اضطراب في الجهاز الهضمي أو تسمم بسيط.")
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
    st.write("تحليل النص المدخل...")
    if "سنان" in user_query or "ضرس" in user_query:
        st.success("التوجه المقترح: طبيب أسنان.")
    elif "عظم" in user_query or "ظهر" in user_query or "رجل" in user_query:
        st.success("التوجه المقترح: طبيب عظام وتأهيل.")
    elif "جلد" in user_query or "حساسية" in user_query:
        st.success("التوجه المقترح: طبيب أمراض جلدية.")
    elif "قلب" in user_query or "نهجان" in user_query:
        st.success("التوجه المقترح: طبيب أمراض القلب والأوعية الدموية.")
    elif "مخ" in user_query or "أعصاب" in user_query:
        st.success("التوجه المقترح: طبيب مخ وأعصاب.")
    else:
        st.warning("لم يتم تحديد التخصص بدقة، يرجى استشارة طبيب عام لتوجيهك.")

st.write("---")
