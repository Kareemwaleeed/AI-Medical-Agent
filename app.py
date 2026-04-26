import streamlit as st

st.set_page_config(page_title="AI Medical Agent", page_icon="⚕️")

st.title("⚕️ المساعد الطبي الذكي - AI Agent")
st.write("هذا النظام يستخدم الذكاء الاصطناعي لتحليل الأعراض وتقديم نصائح أولية.")
st.write("---")

# مدخلات المستخدم
st.subheader("من فضلك اختر الأعراض التي تشعر بها:")
fever = st.checkbox("ارتفاع في درجة الحرارة")
cough = st.checkbox("سعال جاف")
headache = st.checkbox("صداع مستمر")
sore_throat = st.checkbox("احتقان في الحلق")

if st.button("تحليل الحالة"):
    st.write("---")
    # منطق الـ AI Agent (Decision Tree simple logic)
    if fever and cough and sore_throat:
        st.warning("التشخيص المحتمل: أعراض مشابهة للإنفلونزا.")
        st.info("النصيحة: يجب الراحة التامة وشرب سوائل دافئة، واستشارة طبيب إذا زادت الحرارة.")
    elif headache and fever:
        st.warning("التشخيص المحتمل: إجهاد عام أو بداية التهاب.")
        st.info("النصيحة: قس درجة حرارتك بانتظام وخذ قسطاً من الراحة.")
    elif cough and sore_throat:
        st.success("التشخيص المحتمل: التهاب بسيط في الحلق.")
        st.info("النصيحة: الغرغرة بماء وملح وتجنب المشروبات الباردة.")
    else:
        st.success("لا توجد أعراض خطيرة واضحة حالياً.")
        st.balloons()

st.sidebar.info("مشروع مقدم للدكتور - مادة الذكاء الاصطناعي")