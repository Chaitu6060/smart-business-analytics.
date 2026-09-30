
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent/"src"))
from data_preprocessing import load_and_clean_data
from analytics import kpis,monthly,category,region,products
from ml_models import train_sales_model,segment_customers,train_churn_model

st.set_page_config(page_title="Smart Business Analytics",page_icon="📊",layout="wide")
st.markdown("<h1 style='text-align:center;'>📊 Smart Business Analytics</h1>",unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Sales Intelligence • Machine Learning • Customer Analytics</p>",unsafe_allow_html=True)

uploaded=st.sidebar.file_uploader("Upload CSV",type=["csv"])
path=uploaded if uploaded else Path(__file__).parent/"data"/"sales_data.csv"
df=load_and_clean_data(path)

st.sidebar.header("Filters")
regs=st.sidebar.multiselect("Region",sorted(df.Region.unique()),default=sorted(df.Region.unique()))
cats=st.sidebar.multiselect("Category",sorted(df.Category.unique()),default=sorted(df.Category.unique()))
d=df[df.Region.isin(regs)&df.Category.isin(cats)].copy()

tabs=st.tabs(["📊 Dashboard","🤖 Sales Prediction","👥 Customer Segmentation","🚨 Churn Analysis","💡 Insights","📋 Data"])
with tabs[0]:
    a=kpis(d)
    c=st.columns(5)
    for box,(name,val) in zip(c,a.items()):
        box.metric(name, f"₹{val:,.0f}" if name in ["Revenue","Profit"] else f"{val:,.0f}")
    st.divider()
    l,r=st.columns(2)
    with l:
        st.subheader("Monthly Sales")
        st.plotly_chart(px.line(monthly(d),x="Month",y="Sales",markers=True),use_container_width=True)
    with r:
        st.subheader("Regional Sales")
        st.plotly_chart(px.bar(region(d),x="Region",y="Sales",text_auto=".2s"),use_container_width=True)
    l,r=st.columns(2)
    with l:
        st.subheader("Category Performance")
        st.plotly_chart(px.bar(category(d),x="Category",y="Sales",text_auto=".2s"),use_container_width=True)
    with r:
        st.subheader("Top Products")
        st.plotly_chart(px.bar(products(d).sort_values("Sales"),x="Sales",y="Product",orientation="h",text_auto=".2s"),use_container_width=True)

with tabs[1]:
    st.subheader("🤖 Sales Prediction Model")
    if st.button("Train / Refresh Sales Model"):
        model,metrics,result,daily,features=train_sales_model(d)
        st.session_state["sales_result"]=result
        st.session_state["sales_metrics"]=metrics
    if "sales_result" in st.session_state:
        m=st.session_state["sales_metrics"]
        c=st.columns(3)
        c[0].metric("MAE",f"₹{m['MAE']:,.0f}")
        c[1].metric("RMSE",f"₹{m['RMSE']:,.0f}")
        c[2].metric("R²",f"{m['R2']:.3f}")
        result=st.session_state["sales_result"]
        st.plotly_chart(px.line(result,x="Order_Date",y=["Sales","Predicted_Sales"],title="Actual vs Predicted Sales"),use_container_width=True)
        st.dataframe(result.tail(30),use_container_width=True)
    else:
        st.info("Click 'Train / Refresh Sales Model' to run the model.")

with tabs[2]:
    st.subheader("👥 Customer Segmentation")
    k=st.slider("Number of segments",2,6,3)
    if st.button("Run Customer Segmentation"):
        seg,_=segment_customers(d,k)
        st.session_state["segments"]=seg
    if "segments" in st.session_state:
        seg=st.session_state["segments"]
        st.dataframe(seg,use_container_width=True)
        st.plotly_chart(px.scatter(seg,x="Frequency",y="Monetary",size="Monetary",color="Segment",hover_name="Customer_ID",title="Customer Segments"),use_container_width=True)

with tabs[3]:
    st.subheader("🚨 Customer Churn Analysis")
    if st.button("Run Churn Model"):
        model,metrics,churn,features=train_churn_model(d)
        st.session_state["churn"]=churn
        st.session_state["churn_metrics"]=metrics
    if "churn" in st.session_state:
        churn=st.session_state["churn"]
        if st.session_state["churn_metrics"]:
            st.metric("Model Accuracy",f"{st.session_state['churn_metrics']['Accuracy']:.2%}")
        st.dataframe(churn.sort_values("Churn_Risk",ascending=False),use_container_width=True)
    else:
        st.info("Click 'Run Churn Model' to analyze customer inactivity risk.")

with tabs[4]:
    st.subheader("💡 Business Insights")
    a=kpis(d); ms=monthly(d); cs=category(d); rs=region(d); ps=products(d,5)
    growth=((ms.Sales.iloc[-1]/ms.Sales.iloc[-2])-1)*100 if len(ms)>1 and ms.Sales.iloc[-2] else 0
    st.success(f"📈 Latest-month sales changed by {growth:.1f}% compared with the previous month.")
    st.info(f"🏆 Highest-revenue category: {cs.iloc[0].Category}.")
    st.info(f"🌍 Highest-revenue region: {rs.iloc[0].Region}.")
    st.info(f"🥇 Top product by sales: {ps.iloc[0].Product}.")
    st.info(f"💰 Overall profit margin: {(a['Profit']/a['Revenue']*100):.1f}%.")

with tabs[5]:
    st.subheader("📋 Cleaned Dataset")
    st.write(f"Records: {len(d):,}")
    st.dataframe(d,use_container_width=True)
    st.download_button("⬇️ Download CSV",d.to_csv(index=False).encode(), "business_analytics_data.csv","text/csv")
