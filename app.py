import streamlit as st

st.set_page_config(page_title="AI Medical Agent - Nour", page_icon="⚕️")
st.markdown("""<style>.main {direction: RTL; text-align: right;}</style>""", unsafe_allow_html=True)

st.sidebar.title("بيانات الطالبة")
st.sidebar.info("""
**الاسم:** نور (اكتبي اسمك بالكامل هنا)
**المادة:** ذكاء اصطناعي
**المشروع:** Intelligent Medical Agent
""")

st.title("⚕️ نظام الخبير الطبي الذكي")
st.write("---")

st.subheader("خطوة 1: إدخال البيانات الحيوية")
temp = st.number_input("درجة حرارة المريض:", min_value=35.0, max_value=42.0, value=37.0)

st.subheader("خطوة 2: تحديد الأعراض")
col1, col2 = st.columns(2)
with col1:
    cough = st.checkbox("سعال")
    sore_throat = st.checkbox("احتقان حلق")
with col2:
    headache = st.checkbox("صداع")
    fatigue = st.checkbox("خمول وتعب")

if st.button("تشغيل الـ AI Agent للتشخيص"):
    st.write("---")
    st.subheader("نتيجة التحليل:")
    
    if temp >= 38.5:
        st.error("⚠️ تحذير: حمى شديدة. ينصح بزيارة الطبيب فوراً.")
    elif temp >= 37.5 and (cough or sore_throat):
        st.warning("🔔 تشخيص مبدئي: اشتباه في عدوى فيروسية.")
        st.info("النصيحة: الراحة والسوائل الدافئة.")
    elif headache and fatigue:
        st.success("✅ تشخيص مبدئي: إرهاق عام ونقص راحة.")
    else:
        st.success("🌟 الحالة مستقرة. نتمنى لك دوام الصحة!")
        st.balloons()

st.write("---")
