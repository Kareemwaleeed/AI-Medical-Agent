import streamlit as st
from google import genai

# 1. إعداد الصفحة وتنسيق الاتجاه لليمين (RTL)
st.set_page_config(page_title="AI Smart Medical Agent", page_icon="⚕️", layout="wide")
st.markdown("""<style>.main {direction: RTL; text-align: right;}</style>""", unsafe_allow_html=True)

# 2. إعداد مفتاح الـ API لـ Gemini
api_key = st.secrets.get("GEMINI_API_KEY") or st.sidebar.text_input("أدخل مفتاح Gemini API الخاص بك:", type="password")

if not api_key:
    st.sidebar.warning("يرجى إدخال مفتاح الـ API الخاص بـ Gemini لاستخدام الذكاء الاصطناعي.")
    st.stop()

# تهيئة العميل باستخدام مكتبة google-genai
client = genai.Client(api_key=api_key)

# 3. بيانات الفريق في القائمة الجانبية
st.sidebar.title("📑 Project Details")
st.sidebar.markdown("""
---
**Course:** Artificial Intelligence
**Supervised by:** Dr. Mai Ramadan Ibrahim
**University:** Horus University
**Faculty:** Faculty of Artificial Intelligence

**Team Members:**
1. **Omar Hossam** - 8251774
2. **Kareem Waleed** (Leader) - 8251536
3. **Omar Hassan** - 8241388
---
""")

st.title("⚕️ الوكيل الطبي الذكي الشامل (AI Medical Agent)")
st.write("نظام خبير متطور يعتمد على الذكاء الاصطناعي لتحليل الأعراض وترشيح الأطباء والمستشفيات في مختلف المدن المصرية.")
st.write("---")

# المدخلات الأساسية
col1, col2 = st.columns(2)
with col1:
    city = st.text_input("اسم المدينة في مصر (مثل: القاهرة، دمياط الجديدة، المنصورة):", "القاهرة")
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
    if st.checkbox("استشارة تجميل"): symptoms.append("استشارة تجميل")

user_input = st.text_area("أو اكتب وصفاً مفصلاً لشكواك (مثال: عندي وجع في بطني):")

if st.button("بدء الفحص والبحث عن الأطباء"):
    st.write("---")
    
    if not user_input and not symptoms:
        st.warning("يرجى تحديد أو كتابة الأعراض أولاً.")
    else:
        with st.spinner("جاري تحليل الأعراض والبحث بواسطة الذكاء الاصطناعي..."):
            
            # بناء التوجيه (Prompt) الذي سيتم إرساله للذكاء الاصطناعي
            prompt = f"""
            أنت وكيل طبي ذكي (AI Medical Agent) وخبير في النظام الطبي.
            بناءً على المعطيات التالية:
            - المدينة: {city}
            - درجة الحرارة: {temp}
            - الأعراض: {', '.join(symptoms)}
            - الوصف الإضافي: {user_input}

            المطلوب تقديم الآتي باللغة العربية وبشكل منسق وواضح:
            1. 🔍 تقييم وتشخيص مبدئي للحالة (مع التحذير إذا كانت درجة الحرارة مرتفعة جداً مثل 38.5 وأعلى).
            2. 🩺 التخصص الطبي الأنسب للحالة.
            3. 👨‍⚕️ ترشيح لثلاثة أطباء أو عيادات في مدينة {city} (بافتراض أطباء معروفين أو مستشفيات مشهورة في هذه المدينة لنفس التخصص).
            """
            
            try:
                # استخدام النموذج الحديث gemini-2.5-flash
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                
                st.subheader(f"🔍 تقرير الوكيل الذكي لمدينة {city}:")
                if temp >= 38.5:
                    st.error(f"⚠️ تنبيه: درجة حرارتك ({temp}) مرتفعة جداً. يرجى التوجه للطبيب أو المستشفى فوراً.")
                
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}")

st.write("---")
