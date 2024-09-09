import streamlit as st
import datetime
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder
from st_aggrid.shared import JsCode
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

st.set_page_config(layout='wide')
st.balloons()

st.title("Terpene Synthase-standard Library")

now = datetime.datetime.now()
current_hour = now.hour

if current_hour < 4 or current_hour >= 21:
    st.write("### Good morning!")
elif 4 <= current_hour < 10:
    st.write("### Good afternoon!")
elif 10 <= current_hour < 14:
    st.write("### Good evening!")
else:
    st.write("### It's late, time to rest!")

@st.cache_data
def data_create():
    file_path = 'LLLT.csv'
    data = pd.read_csv(file_path)
    return data
df = data_create()

# 定义AG-Grid的列配置
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination()
quick_filter_text = st.text_input(r"$\textsf{\Large search}$")
gb.configure_grid_options(
    quickFilterText = quick_filter_text
)

gb.configure_default_column()
gb.configure_column("ComPound No", filter="agTextColumnFilter")
gb.configure_column("Gene No", filter="agTextColumnFilter")
gb.configure_column("Compounds Name", filter="agTextColumnFilter")
gb.configure_column("Identification method", filter="agTextColumnFilter")
gb.configure_column("TPS original information", filter="agTextColumnFilter")
gb.configure_column("RT", filter="agTextColumnFilter")
gb.configure_column("Formula", filter="agTextColumnFilter")
gb.configure_column("Species", filter="agTextColumnFilter")
gb.configure_column("Resource", filter="agTextColumnFilter")
gb.configure_column("Main or By Product", filter="agTextColumnFilter")
gb.configure_column("Link", filter="agTextColumnFilter")

cell_renderer = JsCode("""
    class LinkCellRenderer {
      init(params) {
        this.eGui = document.createElement('div');
        if (params.value) { // 检查是否有值
          // 检查是否是超链接格式
          let isLink = params.value.match(/<a href="([^"]+)" target="_blank">([^<]+)<\/a>/);
          if (isLink) {
            let href = isLink[1];
            let linkText = isLink[2];
            if (!href.startsWith('http')) { // 检查是否是完整的 URL
              href = window.location.origin + '/' + href; // 转换为绝对路径
            }
            this.eGui.innerHTML = `<a href="${href}" target="_blank">${linkText}</a>`;
          } else {
            this.eGui.innerHTML = params.value; // 直接显示值
          }
        } else {
          this.eGui.innerHTML = ''; // 如果没有值，显示 'No link'
        }
        this.eGui.style.cursor = 'pointer';
      }
      getGui() {
        return this.eGui;
      }
    }
""")

# 配置列以使用自定义的cellRenderer
gb.configure_column(
    "Link",
    headerName="UniProt ID or NCBI ID",
    cellRenderer=cell_renderer
)
gb.configure_column(
    "Gene No",
    headerName="Gene No",
    cellRenderer=cell_renderer
)
gb.configure_column(
    "ComPound No",
    headerName="ComPound No",
    cellRenderer=cell_renderer
)
df['se'] = None
# 创建AG-Grid表格
AgGrid(df,
    gridOptions=gb.build(),
    updateMode=GridUpdateMode.VALUE_CHANGED,
    allow_unsafe_jscode=True,
    height=650, size=10
)

# 横向条形图
sales_by_product_line = (
    df.groupby(by=["Identification method"]).count()[["ComPound No"]]
)
color_map = {
    "Standard": "#386795",
    "Others": "#73BCD5",
    "NMR": "#FFD06E",
    "Commercial standard": "#E86254"
}
fig_product_sales = px.bar(
    sales_by_product_line,
    x="ComPound No",
    y=sales_by_product_line.index,
    orientation="h",
    color=sales_by_product_line.index,
    color_discrete_map=color_map,
    title="<b>Identification method of Compounds</b>"
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

las = df.groupby(df['Resource']).size()
las.sort_values(ascending=True,inplace=True)
layout = go.Layout(
    title = '<b>Resource of Compounds</b>',
    barmode='stack'
)
colors = ['#386795', '#73BCD5', '#FFD06E', '#E86254']
fig_price_sales = go.Figure(data=[go.Pie(labels=las.index, hole = 0.7,values=las.values,hoverinfo = "label+percent",marker=dict(colors=colors))],layout=layout)
fig_price_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)
left_column, right_column = st.columns(2)
right_column.plotly_chart(fig_price_sales, use_container_width=True)
left_column.plotly_chart(fig_product_sales, use_container_width=True)

# 隐藏streamlit默认格式信息
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
